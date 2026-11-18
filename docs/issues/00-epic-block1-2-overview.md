# [EPIC] Điều phối & Tiến độ Vòng 1 (Khối 1 & Khối 2: Phút 15–115) · Gate 1 LogiX-VN

> **Repo:** `K5-L3A-DAY10-QuanKhanhHuyBao-PoCtoPilotGate1`  
> **Nhóm:** Quân - Khánh - Huy - Bảo (Lớp L3A)  
> **Mục tiêu Vòng 1:** Thống nhất tiêu chí chấp nhận -> Ký tiêu chí (chưa xem kết quả) -> Đo mốc base -> Tìm rủi ro (Pre-mortem, HAZOP, Data Map) -> Dựng cổng phòng ngừa (Code + Config + Runbook) -> Chốt cổng vòng 1 (`prepared`) -> Đưa ra Quyết định Gate 1 v1.

---

## 👥 Phân công 4 thành viên (4 vai)

| STT | Thành viên | Vai trò phụ trách | Issue chi tiết |
|:---:|---|---|---|
| 1 | **Khánh** (Trưởng nhóm) | **Kỹ sư cổng 1 (Lead Gate Engineer)**: Base eval, Guard coding (`guards.py`), Run verification, Checkpoint vòng 1 | Issue #1 |
| 2 | **Quân** | **Kỹ sư cổng 2 (QA & Trace Engineer)**: Trace debug `T-002@55`, Data leak prevention, Behavioral tests (`--adhoc`) | Issue #2 |
| 3 | **Huy** | **Sản phẩm và kinh doanh (Product & Business Lead)**: Mục tiêu hệ thống, Tiêu chí chấp nhận (`acceptance_criteria.json`), Data map & Drift, Cổng kinh doanh | Issue #3 |
| 4 | **Bảo** | **Vận hành và pháp lý (Operations & Legal Lead)**: Mục tiêu stakeholder, Telemetry production, HAZOP v1, Checklist 9 nhóm, Cổng vận hành/pháp lý, Runbook 1-3 & Giờ cao điểm | Issue #4 |

---

## 📋 Tiến độ & Mốc kiểm tra (Checkpoints)

### 🏁 Checkpoint 1: Mở đầu, cài đặt & chia vai (Phút 0–15)
- [ ] Clone repo và gắn remote upstream: `git remote add upstream https://github.com/VinUni-AI20k/K5_L3_Day10_PoC-to-Pilot_Gate1_student.git`
- [ ] Chạy bài test công khai: `python3 -m unittest discover -s tests` (kết quả `Ran 13 tests … OK`)
- [ ] Điền thông tin 4 thành viên và vai trò vào `TEAM.md`
- [ ] Mời tài khoản team chấm vào Collaborators với quyền Read

### 📝 Checkpoint 2: Khối 1 · Tiêu chí & Ký tiêu chí (Phút 15–65) · Phiếu A
- [ ] **A1 (15–20')**: Mục tiêu cấp hệ thống (Huy - Câu 1.1) & Mục tiêu chị Oanh/chị Hạnh (Bảo - Câu 1.2)
- [ ] **A2 (20–35')**: Offline metric cho 1 bước agent (Khánh - Câu 1.3) & Telemetry production (Bảo - Câu 1.4)
- [ ] **A3 (35–40')**: Thống nhất câu 1.5 đọc khoảng tin cậy (Cả bàn)
- [ ] **A4 (40–60')**: Bản tiêu chí "Nếu ... thì ...", 2 câu ranh giới đầu ra, điền `config/acceptance_criteria.json` (Huy - Câu 1.6)
- [ ] **A5 (60–65')**: **KÝ TIÊU CHÍ TRƯỚC KHI CHẠY EVAL LẦN NÀO**:
  ```bash
  python3 -m lab10.criteria sign
  git add config/acceptance_criteria.json config/acceptance_criteria.lock && git commit -m 'Sign acceptance criteria' && git push -u origin main
  ```
- [ ] Ghi mã commit và giờ ký vào Phiếu A mục A5. (Từ đây tuyệt đối không sửa `acceptance_criteria.json`)

### 🔍 Checkpoint 3A: Khối 2A · Tìm rủi ro trước khi xảy ra (Phút 65–85) · Phiếu B
- [ ] Chạy đánh giá mốc **base**:
  ```bash
  python3 -m lab10.eval --suite base --stage base --note "baseline"
  python3 -m lab10.gate --run runs/<mã lần chạy>/report.json
  ```
- [ ] **B1**: Phân tích tự chặn vs người duyệt, ghi mã run base vào B0/B1 (Khánh - Câu 2.1)
- [ ] **B2**: Dò trace `T-002@55`, điền bảng soát lỗi 3 phần (Quân - Câu 2.2)
- [ ] **B3**: Điền Bản đồ dữ liệu & 1 ví dụ Data Drift 3 tháng tới (Huy - Câu 2.3)
- [ ] **B4 & B5**: HAZOP tool ghi + checklist 9 nhóm việc có PIC (Bảo - Câu 2.4)
- [ ] **B6**: Pre-mortem 4 lăng kính (kỹ thuật, kinh doanh, vận hành, pháp lý) -> chọn 2-3 lý do dựng cổng (Cả 4 thành viên - Câu 2.5)

### 🛡️ Checkpoint 3B: Khối 2B · Cổng phòng ngừa (Phút 85–105) · Phiếu B
- [ ] **B7.1**: Code 2-3 cổng phòng ngừa trong `lab10/guards.py` (`pre_guard`, `write_gate`) (Khánh & Quân - Câu 2.6)
- [ ] **B7.2**: Viết 2 bước cụ thể tránh rò rỉ dữ liệu (Quân - Câu 2.7)
- [ ] **B7.3**: Viết Behavioral test (1 tính chất + 2 ticket adhoc) (Quân & Khánh - Câu 2.8)
- [ ] **B7.4**: Đặt cổng kinh doanh trong `config/operating_gates.json` mục `business` (Huy - Câu 2.9)
- [ ] **B7.5 & B7.6**: Đặt cổng vận hành/pháp lý trong `config/operating_gates.json`, viết Runbook 1-3 & Giờ cao điểm (Bảo - Câu 2.10)
- [ ] Chạy thử kiểm tra cổng:
  ```bash
  python3 -m lab10.eval --suite base --stage after --note "cổng vòng 1: ..."
  python3 -m unittest discover -s tests
  ```

### 🔒 Checkpoint 3C: Chốt cổng vòng 1 & Quyết định v1 (Phút 105–115) · Phiếu B mục B8
- [ ] Chốt snapshot cổng: `python3 -m lab10.checkpoint` (tạo `guards_round1.py`, `operating_gates.round1.json`, `round1.lock`)
- [ ] Chạy đo mốc prepared:
  ```bash
  python3 -m lab10.eval --suite base --stage prepared
  python3 -m lab10.gate --run runs/<mã lần chạy>/report.json
  ```
- [ ] Thống nhất Quyết định Gate 1 v1 (Tiếp tục / Thu hẹp / Cải tiến thêm / Dừng) kèm 3 bằng chứng khớp `decision_rule` đã ký
- [ ] Commit & Push kết quả vòng 1:
  ```bash
  git add lab10/guards.py lab10/guards_round1.py config/operating_gates.json config/operating_gates.round1.json config/round1.lock templates/form-b-evaluation-gates.md
  git commit -m "LAB 10: chốt cổng vòng 1, quyết định v1"
  git push -u origin main
  ```
