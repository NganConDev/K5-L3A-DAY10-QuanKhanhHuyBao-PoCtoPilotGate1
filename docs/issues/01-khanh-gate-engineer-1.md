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

### 🟡 KHỐI 2A: Đo mốc Base & Phân tích rủi ro (Phút 65–85) [ĐÃ HOÀN THÀNH]
- [x] **Câu 2.1 (Phiếu B mục B1 & B0 dòng 1)**:
  - Chạy lệnh eval baseline:
    ```bash
    python3 -m lab10.eval --suite base --stage base --note "baseline"
    python3 -m lab10.gate --run runs/<mã lần chạy>/report.json
    ```
  - [x] Ghi mã lần chạy baseline: `R-base-before-20261118-171200-96d40b` (pass_rate: 0.9909 [0.9727, 1.0], pass_k: 0.9545, hoàn sai: 20000đ, lỗi hãng oan: 1, pii_leaks: 0, escalation: 0.2273).
  - [x] Liệt kê các chỉ số bị `[CHƯA]` đạt so với tiêu chí đã ký: `wrongful_refund_vnd` (20.000đ > 0) và `wrongful_carrier_faults` (1 > 0).
  - [x] Đọc khối "kinh doanh và vận hành": Hoàn sai ngày tệ nhất 20.000đ (dù tổng hoàn tự động 155.000đ còn xa ngân sách nhưng tạo rủi ro tranh chấp công nợ đối soát).
  - [x] Đọc khối "theo kho và hãng": Kho HCM pass_rate 0.96 (thấp nhất); Hãng VNX pass_rate 0.9714 với 20.000đ hoàn sai và 1 lỗi hãng oan.
  - [x] Điền bảng so sánh **Tự chặn vs Người duyệt**:
    - Lý lẽ ủng hộ tự chặn: Lỗi chìm (hãng bị ghi oan không biết) xảy ra ngay từ bộ nền; tiêu chí an toàn zero-tolerance; người duyệt dễ bỏ sót khi tải lớn; tiền xuất quỹ không hoàn lại ngay được.
    - Lý lẽ phản đối: Một số trường hợp model_override hợp lý khi hãng nhập trễ vào DB; tự chặn 100% làm gián đoạn bồi thường đúng cho khách; chi phí escalation (10.000đ/ca) ngang làm tay.
    - Khuyến nghị: **Kết hợp** (Tự chặn khi phát hiện claim của khách mâu thuẫn DB tracking; chuyển người duyệt khi số tiền lớn hoặc ca ngoại lệ thời tiết/thiên tai).
- [x] **Câu 2.5 (Phiếu B mục B6)**: Tham gia Pre-mortem 4 lăng kính cùng cả nhóm: Đóng góp góc nhìn kỹ thuật về rủi ro model override số ngày từ DB bằng số ngày khách tự khai (`trust_claim=true`) và nguy cơ ghi sai sổ cái / phạt oan hãng VNX.

---

### 🟠 KHỐI 2B: Dựng cổng phòng ngừa bằng Code (Phút 85–105) [ĐÃ HOÀN THÀNH]
- [x] **Câu 2.6 (Phiếu B mục B7.1)**: Hiện thực hóa 3 cổng phòng ngừa trong `lab10/guards.py`:
  - [x] **Cổng 1 (Write-gate hoàn tiền `issue_refund`)**:
    - Cross-check số tiền đề xuất với DB tracking qua `H.db_delay_days` và `H.entitlement_vnd`.
    - Nếu `db_amount == 0`: Escalate ("model đề xuất hoàn nhưng DB cho thấy không đủ điều kiện").
    - Nếu `db_amount > 0` và khác `action['amount_vnd']`: Modify về đúng số tiền theo DB entitlement (`amount_vnd=db_amount`).
  - [x] **Cổng 2 (Write-gate ghi lỗi hãng `file_carrier_fault`)**:
    - Xác thực qua DB tracking xem lỗi có thực sự do hãng không bằng hàm `H.carrier_at_fault(policy, parcel, db_delay)`.
    - Nếu không thỏa mãn điều kiện lỗi hãng: Deny lệnh ghi lỗi để bảo vệ hãng vận chuyển khỏi phạt oan 100.000đ/lần.
  - [x] **Cổng 3 (Write-gate chống rò rỉ PII `notify_carrier`)**:
    - Khi gọi `notify_carrier`: Tự động loại bỏ `customer_note` khỏi payload gửi bên thứ ba để tránh rò rỉ dữ liệu cá nhân theo Nghị định 13/2023/NĐ-CP.
- [x] **Kiểm thử cổng**:
  ```bash
  python3 -m lab10.eval --suite base --stage after --note "cổng vòng 1: ..."
  python3 -m unittest discover -s tests
  ```
  - [x] Mã lần chạy `base · after`: `R-base-after-20261118-171308-710696`.
  - [x] Kết quả: pass_rate: 1.0 [1.0, 1.0], pass_k: 1.0, hoàn sai: 0đ, lỗi hãng oan: 0, rò rỉ PII: 0, escalation: 0.2462.
  - [x] Đảm bảo 13 public tests vẫn `OK` (13 tests in ~1.5s).
  - [x] Đảm bảo không làm hỏng thêm bất kỳ ticket nào đang đúng của bộ nền.

---

### 🔴 CHỐT CỔNG VÒNG 1 & QUYẾT ĐỊNH V1 (Phút 105–115) [ĐÃ HOÀN THÀNH]
- [x] Chạy lệnh chốt snapshot cổng vòng 1:
  ```bash
  python3 -m lab10.checkpoint
  ```
  - [x] Đã tạo snapshot: `lab10/guards_round1.py`, `config/operating_gates.round1.json`, `config/round1.lock`.
  - [x] Hash chốt vòng 1: `b8695640c180a85417b91ec8903288c7584b5117ab85f20ca9cc6da53e90103c`.
- [x] Chạy đo mốc prepared:
  ```bash
  python3 -m lab10.eval --suite base --stage prepared
  python3 -m lab10.gate --run runs/R-base-prepared-20261118-171319-710696/report.json
  ```
  - [x] Mã lần chạy: `R-base-prepared-20261118-171319-710696` (pass_rate: 1.0, pass_k: 1.0, hoàn sai: 0đ, lỗi oan: 0, PII: 0).
- [x] Cùng nhóm điền cột **v1** tại Phiếu B mục B8:
  - Quyết định: **Tiếp tục**.
  - Bằng chứng: (1) Mọi chỉ số bắt buộc đạt (pass_rate=1.0, pass_k=1.0, 3 chỉ số an toàn = 0); (2) Ngưỡng business_ops đạt (cost=5641đ < 8000đ, ROI=0.77 > 0.20, queue_stuck=0); (3) Cổng phòng ngừa khóa cố định với hash `b8695640`.
- [x] Commit và push kết quả vòng 1:
  - Commit: `394c25a` ("LAB 10: chốt cổng vòng 1, quyết định v1").

---

### 🟣 VÒNG 2: XỬ LÝ SỰ CỐ S6 & QUYẾT ĐỊNH V2 (Phút 125–200) [ĐÃ HOÀN THÀNH]
- [x] **Nhận diện sự cố S6**: Đơn hàng tách kiện (multi-carrier), khách khiếu nại chung không ghi rõ parcel_id khiến agent chọn nhầm kiện hoặc quy lỗi oan cho hãng giao đúng.
- [x] **Cổng S6 bổ sung trong `lab10/guards.py`**:
  - CỔNG 1 (trước `issue_refund`): Escalate khi đơn có nhiều kiện do nhiều hãng khác nhau giao mà có hơn 1 hãng bị xác định at_fault.
  - CỔNG 2a (trước `file_carrier_fault`): Escalate khi có nhiều hãng at_fault để người duyệt phân định trách nhiệm.
  - CỔNG 2b: Modify về đúng `parcel_id` khi ticket ghi rõ mã kiện nhưng agent đề xuất kiện khác.
- [x] **Bổ sung chỉ số giám sát**: Thêm `multi_carrier_order_rate` trong `lab10/monitors.py`.
- [x] **Đánh giá mốc After**:
  - Mã lần chạy after: `R-S6-after-20261118-174326-b47231` (visible pass_rate: 1.0, wrongful_carrier_faults: 0, wrongful_refund_vnd: 0).
  - Không gây regression trên bộ nền: `R-S6-after-20261118-181933-b47231` (base pass_rate: 1.0).
- [x] **Quyết định Gate 1 v2**: **Thu hẹp** (Scope pilot cắt đơn tách kiện hoặc chỉ pilot tại kho HN/HCM; chi phí visible 7.462đ > trần 6.000đ do tỉ lệ escalation cao).
