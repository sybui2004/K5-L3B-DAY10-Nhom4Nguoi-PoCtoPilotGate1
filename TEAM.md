# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): Nhom4Nguoi
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-Nhom4Nguoi-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): S2

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; bàn 3 người thì để trống dòng 4. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Bùi Thái Sỹ | 2A202604002 | Kỹ sư cổng (guards.py, trace) | x |
|   2 | Nguyễn Công Tú | 2A202604008 | Kỹ sư cổng (monitors.py, behavioral test) | |
|   3 | Hoàng Ngọc Hiệu | 2A202603976 | Sản phẩm và kinh doanh | |
|   4 | Đoàn Sỹ Hưng | 2A202603990 | Vận hành và pháp lý | |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Phân chia công việc

Toàn bộ bài đã làm xong và gom trên nhánh `demo`. Mỗi người tự đưa phần của mình từ `demo` vào `main` qua nhánh riêng, theo [`commit.md`](commit.md).

| Người | Nhánh riêng | File đưa vào `main` | Mục phiếu phụ trách |
|---|---|---|---|
| Bùi Thái Sỹ | `sy-gates` | `lab10/guards_round1.py`, `config/operating_gates.round1.json`, `config/round1.lock`, `lab10/guards.py`, `incidents/S2/`, `TEAM.md` | Phiếu B mục B0–B2, B7.1–B7.2; Phiếu C mục C0, C2, C6, C7 |
| Nguyễn Công Tú | `tu-monitors-console` | `lab10/monitors.py`, `console/` (`build.py`, `template.html`, `index.html`, `data.json`) | Phiếu B mục B7.3; Phiếu C mục C8, C9 |
| Hoàng Ngọc Hiệu | `hieu-criteria-forms` | `templates/form-a-criteria.md`, `templates/form-b-evaluation-gates.md`, `config/operating_gates.json`, `workflow.md` | Phiếu A (A1–A5); Phiếu B mục B3, B6, B7.4, B8; Phiếu C mục C1, C5, C12 |
| Đoàn Sỹ Hưng | `hung-incident-submission` | `templates/form-c-incident.md`, `submission/` (`submission.json` và phần lệnh 7 gom), `demo.md`, `handoff/`, `commit.md` | Phiếu B mục B4, B5, B7.5, B7.6; Phiếu C mục C3.1, C4, C10, C11 |

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## BuiThaiSy-2A202604002

### Phần việc phụ trách

Kỹ sư cổng 1, trưởng nhóm: lệnh eval/gate/trace, `lab10/guards.py` (`write_gate`, cổng 1–5), trace sự cố, chốt vòng 1, nhận thẻ; Phiếu B mục B0–B2, B7.1–B7.2; Phiếu C mục C0, C2, C6, C7.

### Đóng góp cụ thể

- Ký tiêu chí (`python -m lab10.criteria sign`, hash `5137c9c0`, commit `abaffa2`), chạy base, gate và trace `T-002@55` (Phiếu B mục B0–B2).
- Code cổng 1–3 trong `lab10/guards.py` (hoàn theo quyền lợi tính từ DB, ghi lỗi hãng theo tracking, lọc trường gửi hãng); chạy lệnh 5 chốt vòng 1 (hash `44c8d63e`).
- Vòng 2 (thẻ S2): nhận thẻ, trace `S2-04@11`, `S2-20@11`, `S2-43@11`; code cổng 4 (phê duyệt hợp lệ trên hạn mức, `_approval_valid`) và cổng 5 (trần 300.000đ mỗi khách mỗi ngày); fault tree trước khi sửa và bảng sửa (Phiếu C mục C2, C6, C7).
- Đưa vào `main` (nhánh `sy-gates`): bản chốt vòng 1, `lab10/guards.py`, `incidents/S2/`, `TEAM.md`.

### Bằng chứng

Commit `abaffa2` (ký), `76fdeb3` (chốt vòng 1); `R-base-before-20261119-143130-bde05c`, `R-base-prepared-20261119-144513-5e2912`; Phiếu C mục C7.

### Exit ticket

- Điều tôi làm tốt nhất: trước khi sửa cổng 4 và 5 tôi dựng fault tree và chạy trace `S2-04@11`, `S2-20@11`, `S2-43@11`, nên mỗi thay đổi đều bám vào một ticket cụ thể, không sửa theo cảm tính.
- Điều tôi làm chưa tốt: tôi chốt vòng 1 (hash `44c8d63e`) khi chưa kiểm hết các ca biên của cổng 1–3, nên vòng 2 phải quay lại sửa phần đã "xong".
- Điều tôi học được: một cổng chỉ đáng tin khi nó được kiểm bằng ticket có chủ đích, còn kiểm trên bộ nền thì chưa đủ. Phê duyệt phải kiểm cả hạn mức lẫn hiệu lực, và trần chi trả mỗi khách mỗi ngày (300.000đ) cần một cổng riêng.
- Nếu làm lại: tôi sẽ viết trace cho từng cổng ngay khi code xong, thay vì gom lại cuối vòng.
- Việc tôi cần người khác giúp: đối chiếu với Sản phẩm (Hiệu) về ngưỡng trần, vì con số này do nhóm chốt trong `config/operating_gates.json`.

## NguyenCongTu-2A202604008

### Phần việc phụ trách

Kỹ sư cổng 2: `lab10/monitors.py`, behavioral test (câu 2.8), chạy ba mốc, Gate 1 Console; Phiếu B mục B7.3; Phiếu C mục C8, C9.

### Đóng góp cụ thể

- Behavioral test (Phiếu B mục B7.3): một tính chất và hai ticket hiểm chạy bằng `--adhoc` (đơn `O-1002` khách khai 9 ngày; đơn quà `O-1026` có số điện thoại người nhận), cả hai giữ tính chất.
- Ba chỉ số theo dõi mới trong `lab10/monitors.py`, đã đăng ký `MONITORS`: `untrusted_directive_rate` (0,0 trên bộ nền, 0,467 trên S2), `customer_day_auto_refund_max_vnd` (3.230.000đ ở base, 282.000đ ở after), `non_logix_payer_proposal_rate` (0,4 trên S2). Phiếu C mục C8.
- Chạy ba mốc base, prepared, after cho S2 và kiểm regression trên bộ nền; fault tree sau khi sửa (Phiếu C mục C9).
- Gate 1 Console (`console/`): dựng trang xem ba mốc từ dữ liệu engine thật (`console/build.py` sinh `index.html` từ `template.html` và `data.json`).
- Đưa vào `main` (nhánh `tu-monitors-console`): `lab10/monitors.py`, `console/`.

### Bằng chứng

`lab10/monitors.py` (`untrusted_directive_rate`, `customer_day_auto_refund_max_vnd`, `non_logix_payer_proposal_rate`); grade `R-S2-grade-20261119-161808-b63756` mục 6 monitor ✅.

### Exit ticket

- Điều tôi làm tốt nhất: ba monitor tính thẳng từ `events` và `ledger` của từng trial, không cần nhãn, nên chạy được trên cả bộ nền lẫn S2 và cho thấy rõ cổng 5 có tác dụng: tổng hoàn tự động lớn nhất mỗi khách mỗi ngày giảm từ 3.230.000đ (base) xuống 282.000đ (after), dưới trần 300.000đ.
- Điều tôi làm chưa tốt: `customer_day_auto_refund_max_vnd` khử trùng theo khoá (seed, day, ticket, order, số tiền), nên hai lần hoàn hợp lệ trùng số tiền trên cùng đơn chỉ được đếm một lần. `non_logix_payer_proposal_rate` coi đề xuất thiếu trường `payer` là LogiX trả, tức là thiếu dữ liệu lại được tính là an toàn.
- Điều tôi học được: behavioral test chặn lỗi trước khi ship, còn monitor phát hiện lỗi khi hệ thống đã chạy, nên cần cả hai. Ngưỡng của monitor phải lấy từ config đã chốt (trần 300.000đ trong `ops_limits`), không tự đặt trong code.
- Nếu làm lại: tôi sẽ viết hai ticket hiểm (`O-1002`, `O-1026`) thành test chạy lại được thay vì chỉ chạy tay bằng `--adhoc`, và báo "thiếu dữ liệu" thành một trạng thái riêng trong monitor.
- Việc tôi cần người khác giúp: Vận hành (Hưng) chốt trong runbook ai nhận cảnh báo và phải làm gì khi một monitor vượt ngưỡng.
- Phần đã dùng AI: dùng trợ lý AI (Claude) để xử lý xung đột git khi đưa nhánh `tu-monitors-console` vào `main` và soạn nháp exit ticket này; số liệu lấy từ các lần chạy `lab10.eval` / `lab10.grade` ở trên.

## HoangNgocHieu-2A202603976

### Phần việc phụ trách

Sản phẩm và kinh doanh: tiêu chí chấp nhận (`config/acceptance_criteria.json`), bản đồ dữ liệu, `operating_gates.json` mục `business`, quyết định v1 (Phiếu B mục B8) và v2 (Phiếu C mục C12); Phiếu A; Phiếu B mục B3, B6; Phiếu C mục C1, C5 (specification).

### Đóng góp cụ thể

- Phiếu A: mục tiêu hệ thống và của chị Oanh, chị Hạnh; thước đo offline cho bước ghi lỗi hãng và telemetry production; câu tiêu chí cho 6 chỉ số; ngưỡng đã ký (pass_rate 0,97, pass_k 0,93, ba chỉ số an toàn bằng 0, chi phí ≤ 7.000đ/ticket, ROI ≥ 0,3, 0 ca ùn) và 4 dòng `decision_rule`.
- Phiếu B: bản đồ dữ liệu và ví dụ drift REFUND-v3 → v4 ngày 1/12 (B3); dẫn pre-mortem 4 lăng kính (B6); cổng kinh doanh trong `config/operating_gates.json` (trần 1.000.000đ/ngày, 1.200đ/ticket, phạm vi `all`, ROI 0,3) (B7.4); quyết định v1 "Tiếp tục" (B8).
- Phiếu C: đối chiếu mốc prepared với pre-mortem (C1), specification và giả định môi trường (C5), quyết định v2 giữ "Tiếp tục" với ba dòng bắt buộc (C12).
- Đưa vào `main` (nhánh `hieu-criteria-forms`): Phiếu A, Phiếu B, `config/operating_gates.json`, `workflow.md`.

### Bằng chứng

Phiếu A mục A5 (hash `5137c9c0`); Phiếu B mục B3, B7.4, B8; Phiếu C mục C12.

### Exit ticket

*(bạn tự viết)*

## DoanSyHung-2A202603990

### Phần việc phụ trách

Vận hành và pháp lý: HAZOP, checklist 9 nhóm việc + PIC, runbook, `operating_gates.json` mục `operations` và `legal`, `submission/submission.json`, gom bài. Câu 2.4, 2.10, 3.1 (HAZOP thẻ), 3.3, 3.7; Phiếu B mục B4, B5, B7.5, B7.6; Phiếu C mục C3.1, C4, C10, C11.

### Đóng góp cụ thể

- Vòng 1: HAZOP 5 guideword trên tool ghi, checklist 9 nhóm có PIC, runbook 1–3 và giờ cao điểm khớp số trong `config/operating_gates.json` (1 người trực, 6 ca/giờ, chờ tối đa 45 phút, PIC NV-TUNG, duyệt NV-HANH).
- Vòng 2 (thẻ S2): bảng mức kiểm soát của con người (C3.1) chỉ ra 4 chỗ lệch giữa quyền NV-HANH cần và quyền hệ thống đang cho; HAZOP của thẻ (C4) có nhánh phê duyệt hết hạn chưa thấy trên trace; risk register (C10), cập nhật checklist và runbook 4–5 (C11).
- Điền `submission/submission.json`, chạy lệnh 7; kịch bản demo (`demo.md`), kế hoạch commit (`commit.md`).
- Đưa vào `main` (nhánh `hung-incident-submission`): Phiếu C, `submission/`, `demo.md`, `handoff/`, `commit.md`; gộp nhật ký vòng 1 và vòng 2, gom bài lần cuối.
- Đã dùng trợ lý AI (Claude) để đọc trace, soạn nháp phiếu C và đề xuất cổng 4–5; mọi con số đã được kiểm lại bằng `lab10.eval` / `lab10.grade`.

### Bằng chứng

Phiếu C mục C3.1, C4, C10, C11; `R-S2-after-20261119-161758-b63756`, `R-base-after-20261119-161758-b63756`; grade `R-S2-grade-20261119-161808-b63756` (PASS-VISIBLE).

### Exit ticket

*(bạn tự viết)*