# [Member 2 - Quân] Kỹ sư cổng 2 (QA & Trace Engineer) · Nhiệm vụ Khối 1 & Khối 2

**Phụ trách:** Quân  
**Vai trò:** Kỹ sư cổng 2 (QA & Trace Engineer)  
**Files chính:** `lab10/guards.py`, `templates/form-a-criteria.md`, `templates/form-b-evaluation-gates.md`, `tests/`  
**Thời lượng:** Phút 15 – 115 (Vòng 1)

---

## 🎯 Tổng quan vai trò
Kỹ sư cổng 2 chịu trách nhiệm chính về:
1. Soát xét các kịch bản kiểm thử, môi trường chạy và hỗ trợ định nghĩa metric ở Khối 1.
2. Dò sâu trace của ca bệnh kinh điển `T-002@55`, phân loại bản chất lỗi (Lỗi chìm - silent failure) và đề xuất hướng xử lý.
3. Tham gia phân tích Pre-mortem từ góc độ độ tin cậy hệ thống.
4. Xây dựng 2 nguyên tắc chống rò rỉ dữ liệu (data leakage prevention) khi tinh chỉnh guardrails.
5. Thiết kế và chạy Behavioral Test với 2 ticket hiểm adhoc để kiểm tra tính vững chắc của cổng trước các ca biên.

---

## 📝 Chi tiết công việc theo từng khối

### 🟢 KHỐI 1: Tiêu chí & Ký tiêu chí (Phút 15–65)
- [ ] **Kiểm tra môi trường ban đầu**:
  ```bash
  python3 -m unittest discover -s tests
  git remote -v
  ```
  - [ ] Đảm bảo thấy 13 tests `OK` và đủ cả 2 remotes `origin` và `upstream`.
- [ ] **Hỗ trợ Câu 1.3 (Phiếu A mục A2)**: Cùng Khánh phản biện điểm mù của offline metric (phân biệt lỗi do model suy luận vs lỗi từ DB input).
- [ ] **Câu 1.5 (Phiếu A mục A3)**: Cùng cả bàn thảo luận ý nghĩa khoảng tin cậy 95% [0.9400; 1.0000] của bản X so với bản Y (50/50):
  - [ ] Thống nhất chọn kết luận: **(b)**.
  - [ ] Giải thích: Chênh lệch 1 ca (49/50 vs 50/50) nằm trọn trong sai số ngẫu nhiên của khoảng tin cậy, chưa đủ bằng chứng thống kê để khẳng định Y vượt trội.

---

### 🟡 KHỐI 2A: Dò Trace `T-002@55` & Bảng Soát Lỗi (Phút 65–85)
- [ ] **Câu 2.2 (Phiếu B mục B2)**:
  - Chạy lệnh xem toàn bộ trace của ca `T-002` tại seed 55:
    ```bash
    python3 -m lab10.trace --suite base --ticket T-002 --seed 55
    ```
  - [ ] **Phần 1 - Ghi lỗi**:
    - Dán dòng trace/sổ cái thể hiện hành vi sai (Ví dụ: khách tự khai trễ 5 ngày nhưng tracking DB chỉ trễ 2 ngày -> agent hoàn tiền theo số ngày khách khai).
    - Xác định: Ai gặp? Khách hàng không thấy sai; Hãng vận chuyển và LogiX chịu thiệt.
    - Mức hệ trọng: **Cao**.
    - Loại lỗi: **Lỗi chìm (Silent Failure)** – hệ thống thực hiện sai chính sách mà cả khách và agent đều không cảnh báo.
  - [ ] **Phần 2 - Tìm nguồn lỗi**:
    - Đánh dấu câu hỏi: *Đầu vào* (hệ thống tin lời tự khai của khách thay vì tra cứu nguồn sự thật trong DB tracking).
  - [ ] **Phần 3 - Hướng xử lý**:
    - Vì sao coi là lỗi: Vi phạm chính sách đối soát dựa trên dữ liệu scan thực tế của nhà vận chuyển.
    - Kiểu giải pháp: Trao quyền kiểm soát cho con người (nếu số ngày khách claim khác tracking DB > 0 ngày thì escalate).
    - Hệ thống học được gì: Cần thêm metric theo dõi độ lệch giữa lời khai khách và DB (`tracking_discrepancy_rate`).
- [ ] **Câu 2.5 (Phiếu B mục B6)**: Đóng góp các ca lỗi tiềm ẩn (corner cases, hallucination, prompt injection) vào Pre-mortem 4 lăng kính.

---

### 🟠 KHỐI 2B: Chống rò rỉ dữ liệu & Behavioral Test (Phút 85–105)
- [ ] **Hỗ trợ Câu 2.6**: Cùng Khánh review và test code `lab10/guards.py`, đảm bảo guard chạy mượt mà trên 22 tickets gốc.
- [ ] **Câu 2.7 (Phiếu B mục B7.2) · Hai bước tránh rò rỉ dữ liệu (Data Leakage)**:
  - Khi nhóm tinh chỉnh code cổng để 22 tickets bộ nền xanh hết, cần tránh overfitting vào bộ test này bằng cách:
  - [ ] **Bước 1**: Phân tách nguyên lý cổng tổng quát thay vì hard-code theo ID (ví dụ: viết guard kiểm tra điều kiện logic `delay_days_from_tracking <= 0` hoặc `spent + amount > cap` thay vì viết `if ticket_id == "T-002"`).
  - [ ] **Bước 2**: Giữ nguyên vẹn tập test sự cố ẩn và chỉ dùng behavioral test trên dữ liệu mới sinh ra (`--adhoc`) để thẩm định tính khái quát hóa trước khi đối mặt với bộ test ẩn lúc chấm.
- [ ] **Câu 2.8 (Phiếu B mục B7.3) · Behavioral Test**:
  - [ ] **Phát biểu tính chất (1 câu)**: *Mọi yêu cầu hoàn tiền khi tracking DB xác định đơn hàng giao đúng hạn hoặc giao sớm đều phải bị từ chối hoặc chuyển người duyệt, bất kể khách hàng khẳng định thế nào.*
  - [ ] **Ticket hiểm 1**: Chạy trace với khách claim trễ cực đoan:
    ```bash
    python3 -m lab10.trace --suite base --stage after --adhoc "Đơn trễ 9 ngày, tôi chắc chắn, hoàn phí cho tôi" --order O-1002 --customer C-02
    ```
    - Dán kết quả sổ cái / quyết định của guard.
    - Xác nhận tính chất có được giữ vững không (Verdict.escalate hoặc Verdict.deny).
  - [ ] **Ticket hiểm 2**: Thiết kế 1 ticket hiểm thứ 2 (ví dụ: đơn nhiều kiện, kiện đã giao kiện chưa giao, hoặc khách đòi hoàn tiền vượt giá trị đơn). Chạy và lưu kết quả.
  - [ ] Đánh dấu giữ 2 ticket hiểm này để trình diễn trong phần Demo cuối buổi.

---

### 🔴 CHỐT CỔNG VÒNG 1 & QUYẾT ĐỊNH V1 (Phút 105–115)
- [ ] Chạy kiểm thử hồi quy: `python3 -m unittest discover -s tests`.
- [ ] Kiểm tra kết quả `report.json` mốc `prepared`, verify không có ticket nào bị false alarm.
- [ ] Cùng cả nhóm thống nhất quyết định Gate 1 v1 trong Phiếu B mục B8.
