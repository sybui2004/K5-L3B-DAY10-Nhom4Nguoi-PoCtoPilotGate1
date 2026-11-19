"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict


def _truth(ctx, order_id):
    """Sự thật từ DB (không đọc chữ khách): (order, parcel của ticket, độ trễ theo tracking, nguyên nhân, chính sách hiệu lực)."""
    order = ctx.tools.lookup_order(order_id)
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if order is None or policy is None:
        return None
    parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
    delay = H.db_delay_days(parcel, ctx.as_of)
    cause = parcel.get("delay_cause") or ("CARRIER" if delay > 0 else None)
    return order, parcel, delay, cause, policy


def pre_guard(ctx):
    return Verdict.allow()


def write_gate(ctx, action):
    # action = {"tool": "issue_refund", "ticket_id":..., "order_id":..., "amount_vnd":..., "payer":..., ...}
    tool = action.get("tool")

    # CỔNG 1 · issue_refund: tiền hoàn không được vượt quyền lợi tính từ DB (tracking + chính sách hiệu lực theo ngày),
    # trừ phần đã hoàn trước đó cho đơn này. Chặn: số ngày khách tự khai, lệnh cài trong ghi chú, ghi trùng khi retry.
    # Ứng với HAZOP B4 (issue_refund · amount_vnd · WRONG) và pre-mortem B6 (kỹ thuật, kinh doanh).
    if tool == "issue_refund":
        t = _truth(ctx, action.get("order_id"))
        if t is None:
            return Verdict.escalate("không đối chiếu được đơn hoặc chính sách hiệu lực: chuyển người")
        order, parcel, delay, cause, policy = t
        entitled = H.entitlement_vnd(policy, order, delay, cause)
        already = sum(r["amount_vnd"] for r in ctx.tools.ledger_rows(order_id=order["order_id"]))
        allowed = max(0, entitled - already)
        amount = int(action.get("amount_vnd", 0))
        ctx.log("refund_check", db_delay_days=delay, entitled=entitled, already=already, asked=amount)
        if allowed <= 0:
            return Verdict.deny("không có quyền lợi hoàn theo DB (trễ %s ngày, nguyên nhân %s, đã hoàn %s)"
                                % (delay, cause, already))
        if amount > allowed or action.get("payer", "LOGIX") != "LOGIX":
            return Verdict.modify("đưa số tiền và người trả về đúng quyền lợi theo DB", amount_vnd=min(amount, allowed),
                                  payer="LOGIX")

    # CỔNG 2 · file_carrier_fault: chỉ ghi lỗi khi DB ghi nguyên nhân thuộc lỗi hãng và đủ ngày trễ; ghi đúng kiện, đúng hãng,
    # đúng số ngày theo DB; không quá số lỗi tự động mỗi hãng mỗi ngày (ops_limits).
    # Ứng với HAZOP B4 (file_carrier_fault · INCOMPLETE/WRONG) và pre-mortem B6 (pháp lý: hãng bị ghi oan).
    if tool == "file_carrier_fault":
        t = _truth(ctx, action.get("order_id"))
        if t is None:
            return Verdict.deny("không đối chiếu được đơn hoặc chính sách hiệu lực")
        order, parcel, delay, cause, policy = t
        if not H.carrier_at_fault(policy, parcel, delay):
            return Verdict.deny("DB không ghi nguyên nhân thuộc lỗi hãng hoặc chưa đủ ngày trễ")
        limit = ctx.tools.ops_limits().get("max_auto_strikes_per_carrier_per_day")
        if limit is not None and len(ctx.tools.fault_rows(carrier_id=parcel["carrier_id"])) >= limit:
            return Verdict.deny("hãng đã đủ số lỗi tự động trong ngày: để người duyệt quyết")
        return Verdict.modify("ghi lỗi đúng kiện, đúng hãng, đúng số ngày theo DB", parcel_id=parcel["parcel_id"],
                              carrier_id=parcel["carrier_id"], driver_id=parcel.get("driver_id"), delay_days=delay)

    # CỔNG 3 · notify_carrier: chỉ gửi hãng đúng các trường chính sách cho phép; chữ khách gõ và liên hệ người nhận không rời LogiX.
    # Ứng với HAZOP B4 (dữ liệu gửi bên thứ ba · PERTURBED) và pre-mortem B6 (pháp lý: dữ liệu cá nhân).
    if tool == "notify_carrier":
        pol = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
        allowed_fields = set((pol or {}).get("carrier_notice_fields") or ["order_id", "parcel_id", "district", "delay_days"])
        payload = action.get("payload") or {}
        clean = {k: v for k, v in payload.items() if k in allowed_fields}
        if len(clean) != len(payload):
            return Verdict.modify("bỏ trường ngoài danh sách cho phép gửi hãng", payload=clean)

    return Verdict.allow()
