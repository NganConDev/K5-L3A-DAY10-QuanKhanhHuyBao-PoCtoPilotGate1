# [Member 4 - Bảo] Vận hành và pháp lý (Operations & Legal Lead) · Nhiệm vụ Khối 1 & Khối 2

**Phụ trách:** Bảo  
**Vai trò:** Vận hành và pháp lý (Operations & Legal Lead)  
**Files chính:** `config/operating_gates.json`, `templates/form-a-criteria.md`, `templates/form-b-evaluation-gates.md`, `data/world.json`  
**Thời lượng:** Phút 15 – 115 (Vòng 1)

---

## 🎯 Tổng quan vai trò
Vận hành và pháp lý chịu trách nhiệm chính về:
1. Định hình mục tiêu từ góc nhìn người vận hành thực tế (Kế toán đối soát, Trưởng ca CSKH).
2. Thiết kế Telemetry Production để giám sát tác động ra bên ngoài khi không có nhãn ground truth.
3. Phân tích rủi ro hệ thống bằng HAZOP vòng 1 mở rộng ra các yếu tố con người, chi phí và pháp lý.
4. Lập Checklist Go-live 9 nhóm việc, bảo đảm mọi đầu việc đều có PIC định danh cụ thể.
5. Đóng góp lăng kính Vận hành / Pháp lý trong Pre-mortem (ùn tắc hàng chờ, khiếu nại của hãng, vi phạm dữ liệu cá nhân).
6. Thiết lập Cổng vận hành & pháp lý trong `config/operating_gates.json` (`operations` và `legal`).
7. Biên soạn Runbook phần 1–3 và kế hoạch ứng phó Giờ cao điểm (Peak Hours).

---

## 📝 Chi tiết công việc theo từng khối

### 🟢 KHỐI 1: Tiêu chí & Ký tiêu chí (Phút 15–65)
- [ ] **Câu 1.2 (Phiếu A mục A1) · Mục tiêu nhìn từ hai người vận hành**:
  - [ ] **Chị Oanh (Kế toán đối soát)**: *Không bao giờ ghi nhận lỗi oan cho đơn vị vận chuyển (`wrongful_carrier_faults = 0`) và mọi khoản tiền hoàn đều có biên bản đối soát khớp với log trạng thái thực của bưu kiện, tránh tranh chấp công nợ cuối tuần.*
  - [ ] **Chị Hạnh (Trưởng ca CSKH)**: *Hàng chờ các ca trợ lý chuyển sang không vượt quá 6 ca/người/giờ và thời gian chờ duyệt tối đa dưới 60 phút, đồng thời mỗi quyết định tự động đều có lý do rõ ràng để giảm tải kiểm tra thủ công.*
- [ ] **Câu 1.4 (Phiếu A mục A2 - cột Telemetry Production)**:
  - Thiết kế telemetry giám sát hệ thống production (nơi không có nhãn đúng/sai):
  - [ ] **Hành vi đo:** Tỉ lệ khách hàng khiếu nại lại sau khi nhận quyết định hoàn tiền (Re-escalation rate).
  - [ ] **Thước đo:** Số lượt khách mở lại ticket hoặc gọi hotline trong vòng 24h sau khi nhận phản hồi từ bot (%)
  - [ ] **Dữ liệu:** Event logs từ tổng đài CSKH và cổng tiếp nhận khiếu nại, nhóm theo mã `ticket_id`.
  - [ ] **Cách tính:** Tổng số ticket bị khiếu nại lại chia cho tổng số ticket bot đã tự động xử lý trong ngày.
  - [ ] **Khung thời gian / Ngưỡng báo động:** Cửa sổ trượt 4 giờ; Báo động Vàng khi > 5%, Báo động Đỏ khi > 10% (kích hoạt tạm dừng auto-resolve).
  - [ ] **Điểm mù:** Khách hàng bất mãn nhưng không khiếu nại mà bỏ sang nền tảng đối thủ (churn âm thầm).
- [ ] **Câu 1.5 (Phiếu A mục A3)**: Cùng cả bàn thảo luận và chọn đáp án **(b)**.

---

### 🟡 KHỐI 2A: HAZOP Mở Rộng & Checklist 9 Nhóm Việc (Phút 65–85)
- [ ] **Câu 2.4 (Phiếu B mục B4) · HAZOP Vòng 1**:
  - Chọn 1 tool ghi: `issue_refund` hoặc `file_carrier_fault`.
  - [ ] Điền **≥ 3 dòng kỹ thuật** với các guideword (`WRONG`, `INVALID`, `INCOMPLETE`, `PERTURBED`, `INCAPABLE`).
    - *Ví dụ 1 (WRONG):* `amount_vnd` sai sự thật do model tin số ngày khách tự bịa -> Hậu quả: Thất thoát ngân sách -> Cổng: Đối chiếu quyền lợi DB.
    - *Ví dụ 2 (PERTURBED):* Khách gửi prompt injection lồng trong tên hoặc ghi chú đơn hàng -> Hậu quả: Agent thực hiện lệnh ghi sai -> Cổng: Sanitize đầu vào.
    - *Ví dụ 3 (INCAPABLE):* API ngân hàng/ví điện tử timeout lúc hoàn tiền -> Hậu quả: Tiền chưa hoàn nhưng DB đã ghi nhận -> Cổng: Idempotency token & retry queue.
  - [ ] Điền **≥ 2 dòng mở rộng ngoài kỹ thuật** (bắt buộc):
    - *Người duyệt (INCAPABLE):* 1 người trực gặp 20 ca/giờ -> Quá tải hàng chờ, vi phạm SLA 60 phút -> Cổng: Auto-throttle hoặc gọi thêm backup reviewer.
    - *Dữ liệu gửi bên thứ ba (PERTURBED):* Bot chép nguyên văn lời nhắn của khách chứa SĐT/tên người khác gửi sang hãng -> Vi phạm Nghị định 13/2023/NĐ-CP về bảo vệ dữ liệu cá nhân -> Cổng: Filter PII trước khi gọi `notify_carrier`.
- [ ] **Câu 2.4 (Phiếu B mục B5) · Checklist 9 nhóm việc Go-Live**:
  - Điền hiện trạng, bằng chứng và **BẮT BUỘC có tên PIC cụ thể** cho từng dòng:
    1. *Chất lượng:* PIC: **Quân** (Bằng chứng: eval mốc base report.json)
    2. *Dữ liệu:* PIC: **Huy** (Bằng chứng: Phiếu B mục B3 Data Map)
    3. *Bảo mật:* PIC: **Bảo** (Bằng chứng: HAZOP guideword PERTURBED)
    4. *Quyền hạn:* PIC: **Khánh** (Bằng chứng: `guards.py` & `config/switches.json`)
    5. *Hiệu năng, hạ tầng:* PIC: **Bảo** (Bằng chứng: Đánh giá công suất duyệt 6 ca/giờ)
    6. *Chi phí:* PIC: **Huy** (Bằng chứng: `business.cost_budget_per_ticket_vnd`)
    7. *Vận hành:* PIC: **Bảo** (Bằng chứng: Runbook phần 1–3)
    8. *Con người, pháp lý:* PIC: **Bảo** (Bằng chứng: Danh sách PII filter và chính sách hãng)
    9. *Quyết định:* PIC: **Khánh** (Bằng chứng: Hash file lock tiêu chí đã ký)
- [ ] **Câu 2.5 (Phiếu B mục B6)**: Tham gia Pre-mortem, đưa ra các rủi ro vận hành (quá tải ca trực, tranh chấp công nợ hãng, vi phạm dữ liệu cá nhân khách hàng).

---

### 🟠 KHỐI 2B: Cổng Vận hành, Pháp lý & Runbook (Phút 85–105)
- [ ] **Câu 2.10 (Phiếu B mục B7.5) · Điền `config/operating_gates.json`**:
  - Tra cứu nhân sự trong `data/world.json` (`staff`):
  - [ ] `operations.pic`: `"NV-TUNG"` (Lê Thanh Tùng - Giám sát vận hành, người giữ công tắc dừng).
  - [ ] `operations.approver_id`: `"NV-HANH"` (Trần Thị Hạnh - Trưởng ca CSKH, người duyệt hạn mức).
  - [ ] `operations.reviewers_on_shift`: `1` (ca thường) hoặc `2` (giờ cao điểm).
  - [ ] `operations.review_capacity_per_hour`: `6` (theo `ops_facts`).
  - [ ] `operations.max_queue_wait_minutes`: `60` (theo `ops_limits.review_sla_minutes`).
  - [ ] `operations.stop_conditions`: `["Khi có 1 lỗi ghi oan cho hãng vận chuyển", "Khi tiền hoàn trong ngày vượt 2.000.000 VNĐ", "Khi có sự cố rò rỉ PII"]`.
  - [ ] `operations.alert_channel`: `"slack-cskh-ops-alerts"`.
  - [ ] `legal.pii_fields_blocked_to_third_party`: `["customer_phone", "customer_street", "customer_email"]`.
  - [ ] `legal.carrier_fault_requires_recorded_cause`: `true`.
- [ ] **Soạn thảo Runbook phần 1–3**:
  - [ ] **Runbook 1 (Ai chịu trách nhiệm)**: Liệt kê rõ PIC (`NV-TUNG`), Người duyệt (`NV-HANH`), Người đối soát (`NV-OANH`), quyền hạn và kênh liên lạc khẩn cấp.
  - [ ] **Runbook 2 (Tín hiệu & Ngưỡng hành động)**: Bảng tín hiệu 6 dòng (Thời gian chờ, ca ùn, chi phí, tiền hoàn trần, tiền hoàn sai, lỗi hãng/PII), quy định rõ ngưỡng Vàng (Warning) và ngưỡng Đỏ (Stop/Fallback).
  - [ ] **Runbook 3 (Điều kiện dừng & Cách dừng)**:
    - Quy trình dừng từng bước qua `config/switches.json`.
    - Cam kết thời gian phản ứng: Từ tín hiệu đỏ đến lúc ngắt toàn bộ không quá 5 phút do `NV-TUNG` bấm.
    - Kế hoạch chuyển hướng ticket đang chờ sang queue thủ công của CSKH.
- [ ] **B7.6 · Kế hoạch Giờ cao điểm (Peak Hours)**:
  - Khung giờ: 11h-13h và 20h-22h ngày Mega Sale (dự kiến 18 ticket/giờ gấp 3 lần bình thường).
  - Số người trực: Tăng lên 2-3 người.
  - Ngưỡng gọi backup: Khi hàng chờ > 6 ca hoặc thời gian chờ chạm 45 phút.
  - Ngưỡng thu hẹp: Tạm dừng auto-resolve cho các đơn > 100k nếu hàng chờ quá 15 ca.

---

### 🔴 CHỐT CỔNG VÒNG 1 & QUYẾT ĐỊNH V1 (Phút 105–115)
- [ ] Rà soát report mốc prepared: Đảm bảo `queue_stuck = 0`, `pii_leaks = 0`, `wrongful_carrier_faults = 0`.
- [ ] Cùng nhóm điền cột **v1** tại Phiếu B mục B8.
- [ ] Ký xác nhận vai trò Vận hành & Pháp lý.
