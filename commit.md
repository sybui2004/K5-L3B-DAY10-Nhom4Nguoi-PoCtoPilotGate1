# Kế hoạch commit · Nhom4Nguoi · LAB 10

Repo `K5-L3B-DAY10-Nhom4Nguoi-PoCtoPilotGate1`. Hạn chót (lab chiều/tối L3B): **11h59 GMT+7 ngày 20/11/2026**. Commit sau hạn không được tính.

- **`demo`**: bản tổng hợp cuối cùng, chỉ để **lấy file**. Sau bước 0 không ai commit lên `demo` nữa.
- **`main`**: nhánh team chấm đọc. Hiện chỉ có commit ký tiêu chí `abaffa2`.
- **Nhánh riêng**: mỗi người tạo từ `main`, chép phần của mình từ `demo` sang, commit, rồi merge vào `main`. Phần của ai: bảng "Phân chia công việc" trong [`TEAM.md`](TEAM.md).

## 0. Chuẩn bị

### 0a. Mỗi người, một lần, trong thư mục repo

```bash
git config user.name  "2A202604002"                  # README bước 2a: mã học viên của TRƯỞNG NHÓM, cả 4 người dùng chung
git config user.email "<MSSV của mình>@example.com"  # RULES.md: email giả, ví dụ 2A202603990@example.com
git config core.autocrlf false                       # bắt buộc trên Windows: CRLF làm hỏng hash tiêu chí và integrity
```

### 0b. Đoàn Sỹ Hưng: chốt `demo` lần cuối (làm trước mọi người)

`TEAM.md` (bảng chia việc), `commit.md` và `demo.md` mới chỉ sửa trên máy Hưng. Phải đẩy lên `demo` thì người khác mới chép được. Không add thư mục `submission/` ở bước này; nó được gom lại ở bước 4.

```bash
git checkout demo
git add TEAM.md commit.md demo.md
git commit -m "Chốt demo: chia việc trong TEAM.md, kế hoạch commit"
git push origin demo
```

## 1. Quy trình chung cho mỗi người

Làm **lần lượt**: Sỹ → Tú → Hiệu → Hưng. Người sau chỉ bắt đầu khi người trước đã merge vào `main`. Như vậy nhánh mới luôn tạo từ `main` mới nhất và không bị xung đột.

```bash
git fetch origin
git checkout -b <nhanh-rieng> origin/main
git checkout origin/demo -- <các file của mình>   # chép đúng bản trên demo, file tự được stage
git status                                         # chỉ được thấy file của mình
git commit -m "<message>"
# ... lặp lại cho từng commit ...
git push -u origin <nhanh-rieng>
```

Merge vào `main` (trên máy mình):

```bash
git checkout main
git pull origin main
git merge --no-ff <nhanh-rieng> -m "Merge <nhanh-rieng> vào main"
git push origin main
```

Có thể dùng Pull request trên GitHub thay cho lệnh trên. Khi tạo PR, chọn **base repository = repo của bàn** (`sybui2004/K5-L3B-DAY10-Nhom4Nguoi-PoCtoPilotGate1`) và base = `main`. GitHub mặc định trỏ PR về repo mẫu, mà luật cấm mở PR về repo mẫu.

Không sửa nội dung các file sau, chỉ chép nguyên từ `demo`: `config/acceptance_criteria.*`, `config/*round1*`, `config/round1.lock`, `lab10/guards_round1.py`, `incidents/`. Sửa chúng thì `integrity` hỏng và bài không được tính.

## 2. Việc của từng người

### Bước 1 · Bùi Thái Sỹ · nhánh `sy-gates`

```bash
git fetch origin
git checkout -b sy-gates origin/main

git checkout origin/demo -- lab10/guards_round1.py config/operating_gates.round1.json config/round1.lock
git commit -m "LAB 10: bản chốt cổng vòng 1 (hash 44c8d63e)"

git checkout origin/demo -- incidents/S2
git commit -m "Nhận thẻ S2"

git checkout origin/demo -- lab10/guards.py
git commit -m "guards: cổng 1-3 (vòng 1), cổng 4 phê duyệt hợp lệ và cổng 5 trần mỗi khách (vòng 2)"

git checkout origin/demo -- TEAM.md
# mở TEAM.md, viết "### Exit ticket" ở mục BuiThaiSy-2A202604002
git add TEAM.md
git commit -m "TEAM: phân chia công việc, mục cá nhân Bùi Thái Sỹ"

git push -u origin sy-gates
```

Merge `sy-gates` vào `main` theo mục 1.

**Việc thêm (không commit):** gửi file `runs/journal.jsonl` trên máy mình cho Hưng. `runs/` bị `.gitignore`, mà máy Hưng thiếu các lần chạy vòng 1 (`R-base-before-20261119-143130-bde05c`, `R-base-prepared-20261119-144513-5e2912`…). Team chấm dùng file này để kiểm "ký trước khi đo".

### Bước 2 · Nguyễn Công Tú · nhánh `tu-monitors-console`

```bash
git fetch origin
git checkout -b tu-monitors-console origin/main

git checkout origin/demo -- lab10/monitors.py
git commit -m "monitors: untrusted_directive_rate, customer_day_auto_refund_max_vnd, non_logix_payer_proposal_rate"

git checkout origin/demo -- console
git commit -m "Gate 1 Console: ba mốc base, prepared, after cho S2"

# mở TEAM.md, viết "### Exit ticket" ở mục NguyenCongTu-2A202604008
git add TEAM.md
git commit -m "TEAM: mục cá nhân Nguyễn Công Tú"

git push -u origin tu-monitors-console
```

Merge `tu-monitors-console` vào `main` theo mục 1.

### Bước 3 · Hoàng Ngọc Hiệu · nhánh `hieu-criteria-forms`

```bash
git fetch origin
git checkout -b hieu-criteria-forms origin/main

git checkout origin/demo -- templates/form-a-criteria.md workflow.md
git commit -m "Phiếu A: tiêu chí và cách đo; workflow của bàn"

git checkout origin/demo -- config/operating_gates.json templates/form-b-evaluation-gates.md
git commit -m "Phiếu B và cổng kinh doanh, vận hành, pháp lý; quyết định v1"

# mở TEAM.md, viết "### Exit ticket" ở mục HoangNgocHieu-2A202603976
git add TEAM.md
git commit -m "TEAM: mục cá nhân Hoàng Ngọc Hiệu"

git push -u origin hieu-criteria-forms
```

Merge `hieu-criteria-forms` vào `main` theo mục 1.

### Bước 4 · Đoàn Sỹ Hưng · nhánh `hung-incident-submission` (gom bài cuối)

```bash
git fetch origin
git checkout -b hung-incident-submission origin/main

git checkout origin/demo -- templates/form-c-incident.md submission/submission.json
git commit -m "Phiếu C (thẻ S2) và quyết định v2; submission.json"

git checkout origin/demo -- demo.md handoff commit.md
git commit -m "Kịch bản demo, handoff, kế hoạch commit"
```

**4a. (Khuyến nghị) Đính chính runbook trong Phiếu C.** Runbook vòng 1 (Phiếu B mục B7.5) lệch `operations.stop_conditions` trong config ở hai chỗ:

- Ngưỡng tắt `issue_refund`: config ghi "hoàn sai > 0đ"; runbook ghi "≥ 2 khoản sai hoặc ≥ 50.000đ".
- Người thu hẹp phạm vi: config ghi NV-HANH; runbook ghi NV-TUNG.

Thêm một dòng vào Runbook 4 ở Phiếu C mục C11, ghi ngưỡng nào áp dụng và ai bấm, khớp `config/operating_gates.json`. Không sửa Phiếu B.

```bash
git add templates/form-c-incident.md
git commit -m "Phiếu C: đính chính runbook cho khớp stop_conditions trong config"
```

**4b. Mục cá nhân:** viết `### Exit ticket` ở mục DoanSyHung-2A202603990.

```bash
git add TEAM.md
git commit -m "TEAM: mục cá nhân Đoàn Sỹ Hưng"
```

**4c. Gộp nhật ký.** Dùng Git Bash, không dùng PowerShell `Set-Content` vì nó thêm BOM. Các dòng của Sỹ đặt trước vì chạy sớm hơn:

```bash
cp runs/journal.jsonl runs/journal.hung.bak
cat /duong/dan/journal-cua-Sy.jsonl runs/journal.hung.bak > runs/journal.jsonl
python -c "import json;[json.loads(l) for l in open('runs/journal.jsonl',encoding='utf-8')];print('ok')"
```

Nếu hai file có dòng trùng `run_id`, xoá bớt một dòng.

**4d. Kiểm và gom bài (lệnh 7):**

```bash
python -m unittest discover -s tests          # Ran 13 tests ... OK
python -m lab10.check_submission --collect    # phải in ĐỦ THÀNH PHẦN
git add submission
git commit -m "LAB 10: bài nộp (lệnh 7 ĐỦ THÀNH PHẦN, thẻ S2, v2 Tiếp tục)"
git push -u origin hung-incident-submission
```

Nếu lệnh 7 báo "báo cáo không chạy trên đúng code và config hiện tại", chạy `python -m lab10.grade --incident S2` rồi chạy lại lệnh 7.

Merge `hung-incident-submission` vào `main` theo mục 1.

## 3. Kiểm cuối trên `main` (Hưng)

```bash
git fetch origin
git diff --stat origin/demo origin/main   # chỉ được khác: submission/, TEAM.md (exit ticket), form C (nếu đính chính)
git checkout main
git pull origin main
python -m lab10.check_submission           # vẫn in ĐỦ THÀNH PHẦN
```

Trên GitHub, nhánh `main` phải có `submission/runs/` gồm `journal.jsonl`, `grade-report.json`, `grade-report.md` và ba mốc base, prepared, after. Repo để chế độ **Public**.

## 4. Cả 4 người

Mỗi người tự nộp link `https://github.com/sybui2004/K5-L3B-DAY10-Nhom4Nguoi-PoCtoPilotGate1` trên LMS bằng tài khoản cá nhân, trước hạn chót.
