# [Member 3 - Huy] Sản phẩm và kinh doanh (Product & Business Lead) · Nhiệm vụ Khối 1 & Khối 2

**Phụ trách:** Huy  
**Vai trò:** Sản phẩm và kinh doanh (Product & Business Lead)  
**Files chính:** `config/acceptance_criteria.json`, `config/operating_gates.json`, `templates/form-a-criteria.md`, `templates/form-b-evaluation-gates.md`, `data/world.json`  
**Thời lượng:** Phút 15 – 115 (Vòng 1)

---

## 🎯 Tổng quan vai trò
Sản phẩm và kinh doanh chịu trách nhiệm chính về:
1. Xác lập mục tiêu cấp hệ thống gắn liền với bài toán kinh doanh của LogiX-VN.
2. Xây dựng Bản tiêu chí chấp nhận thành công ("Nếu ... thì chúng tôi sẽ ...") và thiết lập các ngưỡng chuẩn trong `config/acceptance_criteria.json`.
3. Lập Bản đồ dữ liệu (Data Map), xác định nguồn sự thật và phân tích rủi ro Data Drift trong 3 tháng tới.
4. Đóng góp lăng kính Kinh doanh trong Pre-mortem (chi phí ticket, ROI, trần ngân sách).
5. Thiết lập Cổng kinh doanh trong `config/operating_gates.json` (mục `business`) dựa trên dữ liệu thực tế từ `data/world.json`.
6. Đối chiếu kết quả đo lường mốc prepared với quy tắc quyết định (`decision_rule`) để chốt Quyết định Gate 1 v1.

---

## 📝 Chi tiết công việc theo từng khối

### 🟢 KHỐI 1: Tiêu chí & Ký tiêu chí (Phút 15–65)
- [ ] **Câu 1.1 (Phiếu A mục A1)**: Nêu **một mục tiêu cấp hệ thống** của trợ lý (dựa vào PRD v1.1 §3; không được viết chung chung "model trả lời đúng"):
  - *Ví dụ:* Giảm thời gian xử lý yêu cầu khiếu nại giao trễ từ 24h xuống dưới 5 phút cho ít nhất 70% trường hợp hợp lệ, đồng thời kiểm soát tỉ lệ hoàn sai dưới 0.5% để bảo toàn ngân sách vận hành.
- [ ] **Câu 1.5 (Phiếu A mục A3)**: Cùng nhóm chọn đáp án **(b)** và ghi câu giải thích về khoảng tin cậy.
- [ ] **Câu 1.6 (Phiếu A mục A4) · Bản tiêu chí chấp nhận**:
  - [ ] **Bước 1 - Viết câu tiêu chí dạng hành động**:
    - "Nếu **{chỉ số}** của **{trợ lý}** **{tụt dưới / vượt quá}** **{ngưỡng}** thì chúng tôi sẽ **{hành động cụ thể: Tiếp tục / Thu hẹp / Cải tiến thêm / Dừng}**."
    - Viết đủ cho 5 chỉ số bắt buộc:
      1. `pass_rate_min` (ví dụ: >= 0.85)
      2. `pass_k_min` (pass^k: đúng cả 5/5 seed, ví dụ: >= 0.75)
      3. `wrongful_refund_vnd_max` (ngưỡng an toàn: = 0 đ)
      4. `wrongful_carrier_faults_max` (ngưỡng an toàn: = 0 lỗi)
      5. `pii_leaks_max` (ngưỡng an toàn: = 0 trường hợp)
      6. Chỉ số nên có: `escalation_rate_max` (ví dụ: <= 0.35)
  - [ ] **Ranh giới đầu ra (Output boundaries - không thêm vào JSON)**:
    - Một hành động bị cấm: *Không bao giờ tự động hoàn tiền quá 300.000 VNĐ cho một khách hàng trong một ngày mà không có phê duyệt.*
    - Ngưỡng chuyển người duyệt: *Khi số tiền hoàn > 150.000 VNĐ hoặc tracking ghi nhận có yếu tố ngoại lệ thời tiết/thiên tai.*
  - [ ] **Bước 2 - Soát qua 4 câu hỏi**:
    - Có ý nghĩa với mọi bên không?
    - Ai chịu thiệt nếu ép chỉ số này?
    - Ý nghĩa ở Ngày 1 vs Ngày thứ 1.000?
  - [ ] **Bước 3 - Điền `config/acceptance_criteria.json`**:
    - `team`: `"K5-L3A-DAY10-QuanKhanhHuyBao-PoCtoPilotGate1"`
    - `signed_by`: Tên người đại diện (ví dụ: `"Nguyen Nam Khanh (Lead) & Quan, Huy, Bao"`)
    - Điền các trường `required`, `nice_to_have`.
    - Điền nhóm `business_ops`:
      - `cost_per_ticket_vnd_max`: (tham chiếu làm tay tốn 10.000đ từ `ops_facts`)
      - `roi_min`: (ví dụ >= 1.2)
      - `queue_stuck_max`: (số ca ùn tối đa, ví dụ <= 5)
    - `stop_condition`: Điều kiện dừng khẩn cấp.
    - `decision_rule`: Điền rõ điều kiện cho cả 4 nhánh: `Tiếp tục`, `Thu hẹp`, `Cải tiến thêm`, `Dừng`.
  - [ ] Hẹn ngày xem lại tiêu chí và thành phần tham gia.
- [ ] **Ký tiêu chí (Phút 60–65)**:
  - Bàn giao cho Khánh chạy `python3 -m lab10.criteria sign`, sau đó verify file `acceptance_criteria.lock` được sinh ra chính xác.

---

### 🟡 KHỐI 2A: Bản đồ dữ liệu & Phân tích Drift (Phút 65–85)
- [ ] **Câu 2.3 (Phiếu B mục B3) · Bản đồ dữ liệu (Data Map)**:
  - Tra cứu `data/world.json` các bảng `policies`, `orders[].parcels`, `ops_limits`, `ops_facts`.
  - Điền đầy đủ các mục: Người dùng, Việc cần làm xong, Đầu ra hệ thống, Dữ liệu đọc lúc chạy.
  - [ ] **Trường then chốt**: `parcels[].delivered_date`, `parcels[].carrier_id`, `orders[].total_amount_vnd`.
  - [ ] **Nguồn sự thật vs Bản sao**: `delivered_date` trong scan log của hãng là nguồn sự thật; trạng thái khách khai trên app là dữ liệu khai báo một phía (bản sao không kiểm chứng).
  - [ ] **Thế giới thật làm dữ liệu lệch ở đâu**: Điểm phát scan trễ vào mùa bão/sale, tài xế cập nhật trạng thái chậm, chính sách hoàn tiền thay đổi giữa các đợt khuyến mãi.
  - [ ] **Một ví dụ Drift cụ thể trong 3 tháng tới**:
    - *Cái gì đổi*: Chính sách giao hàng Tết chuyển thời hạn cam kết từ 3 ngày thành 5 ngày.
    - *Đổi ngày nào*: 15/01/2027.
    - *Trường nào thể hiện*: `policies[].max_delay_days`.
    - *Con số tiêu chí bị ảnh hưởng*: `wrongful_refund_vnd` sẽ tăng đột biến nếu model vẫn dùng mốc cũ.
    - *Loại drift*: Quan hệ Vào - Ra đổi (Concept Drift).
- [ ] **Câu 2.5 (Phiếu B mục B6)**: Tham gia thảo luận Pre-mortem, nêu các nguyên nhân thất bại ở Lăng kính Kinh doanh (chi phí LLM vượt trần, ROI âm do CSKH phải duyệt lại quá nhiều).

---

### 🟠 KHỐI 2B: Thiết lập Cổng kinh doanh (Phút 85–105)
- [ ] **Câu 2.9 (Phiếu B mục B7.4) · Điền `config/operating_gates.json` mục `business`**:
  - Mở `data/world.json` đối chiếu `ops_limits` và `ops_facts`:
  - [ ] `daily_refund_cap_vnd`: Đặt giá trị (ví dụ: `2000000` VNĐ theo `ops_limits.daily_auto_refund_budget_vnd`).
    - *Lý do:* Khớp với ngân sách trần Finance cho phép tự động chi trả trong 1 ngày làm việc.
  - [ ] `cost_budget_per_ticket_vnd`: Đặt giá trị (ví dụ: `3000` VNĐ).
    - *Lý do:* Thấp hơn đáng kể so với chi phí xử lý thủ công (10.000 VNĐ/ticket) để bảo đảm hiệu quả kinh tế.
  - [ ] `pilot_scope`: Cấu hình phạm vi pilot (ví dụ: `{"mode": "warehouse", "warehouses": ["HN", "HCM"], "percent": 50}`).
    - *Lý do:* Thử nghiệm giới hạn tại 2 kho lớn tập trung đơn lẻ trước khi nhân rộng toàn quốc.
  - [ ] `roi_min`: Đặt giá trị (ví dụ: `1.5`).
    - *Lý do:* Đảm bảo lợi ích tiết kiệm chi phí vượt chi phí vận hành hạ tầng và LLM tối thiểu 50%.

---

### 🔴 CHỐT CỔNG VÒNG 1 & QUYẾT ĐỊNH V1 (Phút 105–115)
- [ ] Phân tích báo cáo mốc `prepared` (`report.json`):
  - Kiểm tra dòng ROI, chi phí mỗi ticket so với làm tay, tổng tiền hoàn so với trần.
  - Đọc khối phân khúc kho/hãng (`by_segment`).
- [ ] Khớp số liệu với 4 nhánh trong `decision_rule` đã ký ở Khối 1:
  - Nếu tất cả ngưỡng đạt: Cân nhắc **Tiếp tục**.
  - Nếu có phân khúc kho/hãng quá rủi ro: Cân nhắc **Thu hẹp**.
  - Nếu chất lượng tổng thể chưa đạt nhưng có thể cải thiện: Cân nhắc **Cải tiến thêm**.
- [ ] Soạn thảo và điền nội dung cột **v1** tại Phiếu B mục B8 cùng cả nhóm.
