# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): QuanKhanhHuyBao
- Lớp: `L3A`
- Repo của bàn: `K5-L3A-DAY10-QuanKhanhHuyBao-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): S6

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Nguyễn Nam Khánh | 2A202603398 | Kỹ sư cổng 1 | Có |
|   2 | Lê Hoàng Quân | 2A202603369 | Kỹ sư cổng 2 (QA & Trace Engineer) | Không |
|   3 | Nguyễn Văn Huy | 2A20203432 | Sản phẩm và kinh doanh | Không |
|   4 | Dương Quang Bảo | 2A202603362 | Vận hành và pháp lý | Không |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## NguyenNamKhanh-2A202603398

### Phần việc phụ trách

Kỹ sư cổng 1 (Lead Gate Engineer): Phụ trách thiết kế offline metric (1.3), kiểm thử khoảng tin cậy (1.5), ký tiêu chí (A5), đo mốc base (2.1), xây dựng các cổng phòng ngừa `lab10/guards.py` (2.6), và chốt cổng vòng 1 (B8).

### Đóng góp cụ thể

- Hoàn thiện câu 1.3 và 1.5 trong Phiếu A.
- Thực hiện ký và niêm phong tiêu chí chấp nhận `acceptance_criteria.json`.

### Bằng chứng

- Commit ký tiêu chí: `Sign acceptance criteria`
- Trạng thái kiểm thử công khai: 13 tests OK.

### Exit ticket

Một điều học được: Bản tiêu chí chấp nhận phải được niêm phong bằng chữ ký hash trước khi nhìn bất kỳ con số đánh giá nào để tránh cherry-picking ngưỡng.
Một điều còn chưa chắc: Cách cân bằng giữa tỉ lệ chuyển người duyệt (escalation) và chi phí vận hành trên mỗi ticket khi gặp ca khó.
## LeHoangQuan-2A202603369

### Phần việc phụ trách

Kỹ sư cổng 2 theo issue #3. Phụ trách góp ý A2–A3, phân tích trace ở B2,
đóng góp B6 và kiểm thử hành vi ở B7.2–B7.3.

### Đóng góp cụ thể

- Kiểm tra môi trường trên Windows với Python 3.11.9, đạt 13/13 tests.
- Góp ý điểm mù của thước đo ở A2 và giải thích lựa chọn (b) ở A3.
- Dùng AI để hỗ trợ rà và diễn đạt góp ý A2–A3.

### Bằng chứng

Phiếu A, mục A2 và A3. Bổ sung mã commit hoặc mã lần chạy khi có.

### Exit ticket

Bổ sung cuối buổi.


## DuongQuangBao-2A202503362

### Phần việc phụ trách

Vận hành và pháp lý (Operations & Legal Lead), phụ trách các nội dung thuộc Issue #5 trong Khối 1 và Khối 2: mục tiêu stakeholder, telemetry production, HAZOP mở rộng, checklist Go-Live, pre-mortem, cổng vận hành/pháp lý, runbook và kế hoạch giờ cao điểm.

### Đóng góp cụ thể

- **Câu 1.2 – Mục tiêu stakeholder:** Xác định mục tiêu của chị Oanh (đối soát, không ghi nhận lỗi oan cho hãng vận chuyển) và chị Hạnh (kiểm soát năng lực duyệt, hàng chờ và thời gian xử lý).
- **Câu 1.4 – Telemetry production:** Đề xuất Re-escalation rate để theo dõi ticket khách hàng khiếu nại lại hoặc gọi tổng đài trong 24 giờ; xác định nguồn log, công thức, cửa sổ trượt 4 giờ và ngưỡng cảnh báo 5%/10%.
- **Câu 2.4 – HAZOP:** Phân tích các sai lệch khi thực hiện `issue_refund`, gồm dữ liệu ngày trễ sai, policy không hợp lệ, dữ liệu thiếu, prompt injection và lỗi ghi sổ; bổ sung rủi ro quá tải người duyệt và lộ dữ liệu cá nhân khi gửi cho bên thứ ba.
- **Câu 2.4 – Checklist Go-Live:** Xác định nội dung kiểm tra, bằng chứng và PIC cho 9 nhóm: chất lượng, dữ liệu, bảo mật, quyền hạn, hiệu năng/hạ tầng, chi phí, vận hành, con người/pháp lý và quyết định.
- **Câu 2.5 – Pre-mortem:** Đề xuất các kịch bản thất bại về quá tải hàng chờ trong Mega Sale, ghi lỗi hãng khi thiếu bằng chứng và gửi thông tin cá nhân không cần thiết cho bên thứ ba.
- **Câu 2.10 – Cổng vận hành và pháp lý:** Xây dựng đề xuất cấu hình cho `operations` và `legal` trong `config/operating_gates.json`; xác định PIC vận hành `NV-TUNG`, người duyệt `NV-HANH`, giới hạn năng lực 6 ticket/người/giờ, SLA 60 phút, điều kiện dừng, kênh cảnh báo, sampling 10%, danh sách trường PII cần chặn và yêu cầu có nguyên nhân được ghi nhận trước khi quy lỗi cho hãng.
- **Runbook 1–3:** Xác định vai trò chịu trách nhiệm, tín hiệu/ngưỡng cảnh báo, quy trình tắt switch, chuyển ticket đang chờ sang xử lý thủ công và điều kiện phê duyệt khởi động lại.
- **B7.6 – Peak Hours:** Đề xuất phương án ứng phó khung giờ 11:00–13:00 và 20:00–22:00 ngày Mega Sale với tải dự kiến 18 ticket/giờ; gọi người dự phòng khi hàng chờ vượt 6 ticket hoặc thời gian chờ đạt 45 phút; thu hẹp phạm vi tự động khi hàng chờ vượt 15 ticket.

### Bằng chứng

- Issue phân công: [Issue #5 – Operations & Legal Lead](https://github.com/NganConDev/K5-L3A-DAY10-QuanKhanhHuyBao-PoCtoPilotGate1/issues/5).
- Phiếu A: `templates/form-a-criteria.md`, mục A1/A2.
- Phiếu B: `templates/form-b-evaluation-gates.md`, mục B4–B7.6.
- Dữ liệu vận hành và nhân sự: `data/world.json`.
- Cấu hình cổng vận hành/pháp lý: `config/operating_gates.json`.
- Các nội dung trên là phần đóng góp thiết kế và tài liệu; chỉ ghi nhận cấu hình/runbook đã được áp dụng hoặc commit sau khi kiểm tra trạng thái thực tế trên repository.

### Công cụ AI và cách tự kiểm tra

- Sử dụng ChatGPT để hỗ trợ hệ thống hóa HAZOP, soạn nội dung telemetry, checklist, pre-mortem và runbook.
- Đối chiếu các ngưỡng vận hành, nhân sự và chi phí với `data/world.json`; đối chiếu tên trường cấu hình với template B7.5.
- Rà lại công thức telemetry, mẫu số và cách xử lý ticket chưa đủ 24 giờ quan sát; không tự tạo số liệu đánh giá hoặc kết quả chạy.

### Exit ticket

Một điều học được: Chỉ số production không nhất thiết phải có nhãn đúng/sai; hành vi khách hàng như mở lại ticket hoặc gọi tổng đài có thể dùng làm tín hiệu proxy để phát hiện chất lượng xử lý suy giảm.

Một điều còn chưa chắc: Cách cân bằng giữa số lượng reviewer dự phòng, chi phí vận hành và thời gian chờ trong các đợt tải tăng đột biến; cần dùng kết quả đo thực tế để xác nhận phương án.
