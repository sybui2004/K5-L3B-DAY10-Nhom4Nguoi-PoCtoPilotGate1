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

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## BuiThaiSy-2A202604002

### Phần việc phụ trách

Kỹ sư cổng 1, trưởng nhóm: lệnh eval/gate/trace, `lab10/guards.py` (`write_gate`, cổng 1–5), trace sự cố; Phiếu B mục B0–B2, B7.1; Phiếu C mục C2, C7.

### Đóng góp cụ thể

*(bạn tự viết)*

### Bằng chứng

Commit `abaffa2` (ký), `76fdeb3` (chốt vòng 1); `R-base-before-20261119-143130-bde05c`, `R-base-prepared-20261119-144513-5e2912`; Phiếu C mục C7.

### Exit ticket

*(bạn tự viết)*

## NguyenCongTu-2A202604008

### Phần việc phụ trách

Kỹ sư cổng 2: `lab10/monitors.py`, behavioral test (câu 2.8), chạy ba mốc; Phiếu B mục B7.3; Phiếu C mục C8.

### Đóng góp cụ thể

*(bạn tự viết)*

### Bằng chứng

`lab10/monitors.py` (`untrusted_directive_rate`, `customer_day_auto_refund_max_vnd`, `non_logix_payer_proposal_rate`); grade `R-S2-grade-20261119-161808-b63756` mục 6 monitor ✅.

### Exit ticket

*(bạn tự viết)*

## HoangNgocHieu-2A202603976

### Phần việc phụ trách

Sản phẩm và kinh doanh: tiêu chí chấp nhận (`config/acceptance_criteria.json`), bản đồ dữ liệu, `operating_gates.json` mục `business`, quyết định v1 (Phiếu B mục B8) và v2 (Phiếu C mục C12); Phiếu A; Phiếu C mục C5 (specification).

### Đóng góp cụ thể

*(bạn tự viết)*

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
- Điền `submission/submission.json`, chạy lệnh 7.
- Đã dùng trợ lý AI (Claude) để đọc trace, soạn nháp phiếu C và đề xuất cổng 4–5; mọi con số đã được kiểm lại bằng `lab10.eval` / `lab10.grade`.

### Bằng chứng

Phiếu C mục C3.1, C4, C10, C11; `R-S2-after-20261119-161758-b63756`, `R-base-after-20261119-161758-b63756`; grade `R-S2-grade-20261119-161808-b63756` (PASS-VISIBLE).

### Exit ticket

*(bạn tự viết)*

