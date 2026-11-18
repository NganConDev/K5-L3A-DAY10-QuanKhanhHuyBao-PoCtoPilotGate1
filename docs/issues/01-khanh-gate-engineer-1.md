# [Member 1 - Khánh] Kỹ sư cổng 1 (Lead Gate Engineer) · Nhiệm vụ Khối 1 & Khối 2

**Phụ trách:** Khánh (@NganConDev)  
**Vai trò:** Kỹ sư cổng 1 (Lead Gate Engineer)  
**Files chính:** `lab10/guards.py`, `templates/form-a-criteria.md`, `templates/form-b-evaluation-gates.md`, `config/acceptance_criteria.json`  
**Thời lượng:** Phút 15 – 115 (Vòng 1)

---

## 🎯 Tổng quan vai trò
Kỹ sư cổng 1 chịu trách nhiệm chính về:
1. Thiết kế Offline metric cho 1 bước của trợ lý.
2. Thực thi lệnh ký tiêu chí và kiểm tra tính toàn vẹn git commit.
3. Chạy đánh giá mốc **base** đầu tiên, đọc báo cáo `lab10.gate`, phân tích cơ chế Tự chặn vs Người duyệt.
4. Triển khai code các cổng phòng ngừa trong `lab10/guards.py` (`pre_guard` và `write_gate`).
5. Thực thi chốt cổng vòng 1 (`lab10.checkpoint`) và chạy mốc **prepared** để phục vụ quyết định v1.

---

## 📝 Chi tiết công việc theo từng khối

### 🟢 KHỐI 1: Tiêu chí & Ký tiêu chí (Phút 15–65) [ĐÃ HOÀN THÀNH ĐẾN ĐIỂM CHẶN 1]
- [x] **Câu 1.3 (Phiếu A mục A2 - cột Offline)**: Chọn **MỘT bước** của agent (`chọn độ trễ`).
  - [x] **Thước đo:** Tỉ lệ lần chạy mà số ngày trễ trợ lý dùng để tính bồi thường sai lệch so với dữ liệu tracking DB (%).
  - [x] **Dữ liệu:** Dữ liệu trace `proposal.delay_days_used` và `tracking.db_delay_days` trong `runs/<mã>/traces/`, tập 22 tickets × 5 seeds = 110 lượt chạy. Ground truth từ log scan vận chuyển trong `data/world.json`.
  - [x] **Cách tính:** `(Số lần proposal.delay_days_used != tracking.db_delay_days) / (Tổng số lần có sinh proposal) * 100%`.
  - [x] **Điểm mù:** Không phát hiện được trường hợp lỗi nằm ngay ở thiết bị quét của bưu tá/depot (quét thiếu hoặc cập nhật trễ).
- [x] **Câu 1.5 (Phiếu A mục A3)**: Cùng cả bàn đọc kết quả bootstrap confidence interval:
  - Bản X: pass_rate = 0.9800 [0.9400; 1.0]. Bản Y: pass_rate = 1.0 (50/50).
  - Chọn đáp án: **(b)** Chưa đủ căn cứ nói Y tốt hơn X (vì chênh lệch 1 run nằm trọn trong khoảng tin cậy 95% của X).
- [x] **Ký tiêu chí (Phút 60–65 - Phiếu A mục A5)**:
  - Đã hoàn tất và kiểm tra `config/acceptance_criteria.json`.
  - Đã chạy lệnh ký thành công:
  ```bash
  python3 -m lab10.criteria sign
  git add config/acceptance_criteria.json config/acceptance_criteria.lock && git commit -m 'Sign acceptance criteria'
  ```
  - [x] Đã ký lúc: `2026-11-18 15:57:10` (SHA256: `f309c912880d38d7240dc8cb82e47072e940ba40298b0e71f21d761fa66bc2b7`)
  - [x] Mã commit: `68f6d96`
  - [x] Đã điền bảng mục A5 trong `templates/form-a-criteria.md`.
  - ⚠️ *Tiêu chí đã ký và niêm phong an toàn. Đã sẵn sàng sang Khối 2A (Đo mốc base).*

---

### 🟡 KHỐI 2A: Đo mốc Base & Phân tích rủi ro (Phút 65–85)
- [ ] **Câu 2.1 (Phiếu B mục B1 & B0 dòng 1)**:
  - Chạy lệnh eval baseline:
    ```bash
    python3 -m lab10.eval --suite base --stage base --note "baseline"
    python3 -m lab10.gate --run runs/<mã lần chạy>/report.json
    ```
  - [ ] Ghi mã lần chạy baseline vào B0 (dòng 1) và B1.
  - [ ] Liệt kê các chỉ số bị `[CHƯA]` đạt so với tiêu chí đã ký.
  - [ ] Đọc khối "kinh doanh và vận hành": dòng nào đáng lo (tỉ lệ chuyển người, chi phí/ticket, ca bị ùn)?
  - [ ] Đọc khối "theo kho và hãng": kho nào (HN/HCM/DN) hoặc hãng nào (VNX/DHT/FAST) có số xấu nhất?
  - [ ] Điền bảng so sánh **Tự chặn vs Người duyệt**:
    - Lý lẽ ủng hộ tự chặn (bảo vệ tức thì, không phụ thuộc ca trực con người).
    - Lý lẽ phản đối (nguy cơ false positive làm tê liệt hệ thống, gián đoạn CSKH).
    - Khoanh khuyến nghị (thường là *Kết hợp* theo tầng mức độ rủi ro).
- [ ] **Câu 2.5 (Phiếu B mục B6)**: Tham gia Pre-mortem 4 lăng kính cùng cả nhóm (đóng góp góc nhìn rủi ro kỹ thuật và lỗi ghi đè dữ liệu).

---

### 🟠 KHỐI 2B: Dựng cổng phòng ngừa bằng Code (Phút 85–105)
- [ ] **Câu 2.6 (Phiếu B mục B7.1)**: Hiện thực hóa 2–3 cổng trong `lab10/guards.py`:
  - [ ] **Cổng 1 (Pre-guard hoặc Write-gate hoàn tiền)**:
    - Chặn hoặc chuyển người duyệt nếu đơn chưa giao thành công hoặc số ngày trễ < 0.
    - Chặn hoặc chuyển duyệt nếu số tiền hoàn `amount_vnd` vượt quá trần ngày trong config `(ctx.gates.get("business", {}).get("daily_refund_cap_vnd"))`.
  - [ ] **Cổng 2 (Write-gate ghi lỗi hãng)**:
    - Khi `tool == "file_carrier_fault"`: Kiểm tra tracking DB xem lỗi có thực sự do hãng không trước khi cho phép ghi.
  - [ ] **Cổng 3 (Write-gate chống rò rỉ PII)**:
    - Khi gửi thông tin cho hãng vận chuyển (`notify_carrier`), loại bỏ các trường PII nhạy cảm nếu có trong `legal.pii_fields_blocked_to_third_party`.
- [ ] **Kiểm thử cổng**:
  ```bash
  python3 -m lab10.eval --suite base --stage after --note "cổng vòng 1: ..."
  python3 -m unittest discover -s tests
  ```
  - [ ] Đảm bảo 13 public tests vẫn `OK`.
  - [ ] Đảm bảo không làm hỏng thêm bất kỳ ticket nào đang đúng của bộ nền.
  - [ ] Điền bảng B7.1 với mã lần chạy `base · after`.

---

### 🔴 CHỐT CỔNG VÒNG 1 & QUYẾT ĐỊNH V1 (Phút 105–115)
- [ ] Chạy lệnh chốt snapshot cổng vòng 1:
  ```bash
  python3 -m lab10.checkpoint
  ```
  - Kiểm tra thông báo: `ĐÃ CHỐT cổng vòng 1 (mốc prepared). 8 ký tự đầu: ...`
- [ ] Chạy đo mốc prepared:
  ```bash
  python3 -m lab10.eval --suite base --stage prepared
  python3 -m lab10.gate --run runs/<mã lần chạy>/report.json
  ```
- [ ] Cùng nhóm điền cột **v1** tại Phiếu B mục B8 (Quyết định, 3 bằng chứng, rule tương ứng).
- [ ] Commit và push kết quả vòng 1:
  ```bash
  git add lab10/guards.py lab10/guards_round1.py config/operating_gates.json config/operating_gates.round1.json config/round1.lock templates/form-b-evaluation-gates.md
  git commit -m "LAB 10: chốt cổng vòng 1, quyết định v1"
  git push -u origin main
  ```
