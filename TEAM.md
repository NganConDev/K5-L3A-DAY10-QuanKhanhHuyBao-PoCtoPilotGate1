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

Kỹ sư cổng 1 (Lead Gate Engineer) & Trưởng nhóm, phụ trách Issue #1 / Issue #2: Thiết kế offline metric (1.3), kiểm thử khoảng tin cậy (1.5), ký tiêu chí (A5), đo mốc base (2.1), xây dựng các cổng phòng ngừa code `lab10/guards.py` (2.6, B7.1), chốt cổng vòng 1 (B8), hỗ trợ xử lý sự cố S6 và quyết định Gate 1 v2.

### Đóng góp cụ thể

- **Khối 1 · Tiêu chí & Ký tiêu chí (1.3, 1.5, A5)**: Thiết kế offline metric đo bước trích xuất số ngày trễ (`proposal.delay_days_used` vs `tracking.db_delay_days`, phân tích điểm mù do scan chậm ở depot); cùng bàn phân tích khoảng tin cậy bootstrap [0.9400; 1.0000] chọn đáp án (b); thực hiện ký tiêu chí niêm phong `acceptance_criteria.json` với commit `68f6d96`.
- **Khối 2A · Đo mốc Base & Phân tích rủi ro (2.1, 2.5)**: Chạy đo mốc base `R-base-before-20261118-171200-96d40b`; phân tích kết quả chưa đạt ở 2 chỉ số an toàn (`wrongful_refund_vnd` = 20.000đ, `wrongful_carrier_faults` = 1) do lỗi chìm `T-002@55`; phân tích so sánh cơ chế Tự chặn vs Người duyệt đưa ra khuyến nghị Kết hợp; tham gia Pre-mortem góc nhìn kỹ thuật về model override dữ liệu DB.
- **Khối 2B · Cổng phòng ngừa (2.6, B7.1)**: Lập trình 3 cổng phòng ngừa cấp hệ thống trong `lab10/guards.py`:
  - Cổng 1 (Write-gate hoàn tiền): Cross-check với DB entitlement (modify về đúng số tiền DB nếu hợp lệ, escalate nếu DB không đủ điều kiện).
  - Cổng 2 (Write-gate ghi lỗi hãng): Xác minh điều kiện lỗi hãng qua `carrier_at_fault` trước khi gọi `file_carrier_fault` (deny nếu không đủ điều kiện để tránh phạt oan hãng 100.000đ/lần).
  - Cổng 3 (Write-gate chống rò rỉ PII): Xóa `customer_note` khỏi payload của `notify_carrier` để ngăn chặn rò rỉ dữ liệu cá nhân theo Nghị định 13/2023/NĐ-CP.
  - Kiểm thử mốc after đạt 100% tiêu chí trên bộ nền (`R-base-after-20261118-171308-710696`).
- **Chốt cổng vòng 1 & Quyết định v1 (B8)**: Thực thi lệnh chốt snapshot `lab10.checkpoint` niêm phong vòng 1 với mã hash `b8695640c180a85417b91ec8903288c7584b5117ab85f20ca9cc6da53e90103c`; đo mốc prepared `R-base-prepared-20261118-171319-710696` đạt 100% tiêu chí bắt buộc; thống nhất quyết định Gate 1 v1: "Tiếp tục".
- **Khối 3 · Sự cố S6 & Quyết định v2**: Tham gia phân tích sự cố đơn tách kiện S6; hỗ trợ cập nhật guard escalate cho đơn tách kiện nhiều hãng at fault và modify đúng parcel_id; đo mốc after và grade kiểm tra regression; thống nhất quyết định Gate 1 v2: "Thu hẹp".

### Bằng chứng

- Commit ký tiêu chí: `68f6d96` ("Sign acceptance criteria")
- Mã lần chạy base: `R-base-before-20261118-171200-96d40b`
- Mã lần chạy after vòng 1: `R-base-after-20261118-171308-710696`
- Mã lần chạy prepared: `R-base-prepared-20261118-171319-710696`
- Mã lần chạy sự cố S6 after: `R-S6-after-20261118-174326-b47231`
- Commit chốt vòng 1: `394c25a` ("LAB 10: chốt cổng vòng 1, quyết định v1")
- Hash chốt vòng 1: `b8695640c180a85417b91ec8903288c7584b5117ab85f20ca9cc6da53e90103c`
- Trạng thái kiểm thử công khai: `Ran 13 tests … OK`

### Công cụ AI và cách tự kiểm tra

- Sử dụng trợ lý AI (ChatGPT / Claude / Antigravity) để hỗ trợ rà soát cấu trúc hook guard, kiểm tra regex PII và phân tích trace logs của các ca biên `T-002@55`.
- Tự kiểm chứng bằng cách chạy `python3 -m unittest discover -s tests`, `python3 -m lab10.checkpoint verify`, `python3 -m lab10.criteria verify`, `python3 -m lab10.grade --incident S6`, và `python3 -m lab10.check_submission --collect`.

### Exit ticket

Một điều học được: Bản tiêu chí chấp nhận phải được niêm phong bằng chữ ký hash trước khi nhìn bất kỳ con số đánh giá nào để tránh cherry-picking ngưỡng; đồng thời các cổng cấp hệ thống (guards) ngoài model là phòng tuyến quyết định bảo vệ ngân sách và pháp lý khi model có xu hướng tin vào lời khai người dùng (trust_claim).
Một điều còn chưa chắc: Cách tối ưu hóa cân bằng giữa tỉ lệ chuyển người duyệt (escalation) và chi phí vận hành trên mỗi ticket trong các ca phức tạp (như đơn tách kiện nhiều hãng) để vừa đảm bảo an toàn vừa giữ được ROI kinh doanh.

## LeHoangQuan-2A202603369

### Phần việc phụ trách

Kỹ sư cổng 2 theo issue #3. Phụ trách góp ý A2–A3, phân tích trace ở B2,
đóng góp B6 và kiểm thử hành vi ở B7.2–B7.3.

### Đóng góp cụ thể

- Kiểm tra môi trường trên Windows với Python 3.11.9, đạt 13/13 tests.
- Góp ý điểm mù của thước đo ở A2 và giải thích lựa chọn (b) ở A3.
- Dò trace `T-002@55`, lập bảng soát lỗi 3 phần phân loại lỗi chìm (silent failure).
- Thiết kế 2 bước cụ thể chống rò rỉ dữ liệu cá nhân (B7.2).
- Viết Behavioral tests kiểm thử tính chất và các ca biên (B7.3).
- Dùng AI để hỗ trợ rà và diễn đạt góp ý A2–A3, B2.

### Bằng chứng

- Phiếu A, mục A2 và A3.
- Phiếu B, mục B2, B6, B7.2, B7.3.
- Mã lần chạy trace: `python3 -m lab10.trace --suite base --ticket T-002 --seed 55`.
- Trạng thái kiểm thử: 13 tests OK.

### Exit ticket

Một điều học được: Lỗi chìm (silent failure) như việc ghi nhận sai ngày trễ khiến bồi thường sai và phạt oan hãng là loại lỗi nguy hiểm nhất vì cả model và khách hàng đều không nhận biết được, chỉ lộ ra khi đối soát sổ sách.
Một điều còn chưa chắc: Cách xây dựng bộ behavioral tests tự động hóa bao phủ hết các trường hợp prompt injection tinh vi trong trường ghi chú của khách.

## DuongQuangBao-2A202603362

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

## NguyenVanHuy-2A20203432

### Phần việc phụ trách

Sản phẩm và kinh doanh (Product & Business Lead), phụ trách Issue #4: Mục tiêu hệ thống (1.1), tiêu chí chấp nhận (1.6), bản đồ dữ liệu và data drift (2.3), cổng kinh doanh (2.9), chủ trì xử lý sự cố S6 và quyết định Gate 1 v2 (Phiếu C).

### Đóng góp cụ thể

- **Câu 1.1 – Mục tiêu cấp hệ thống:** Thiết lập mục tiêu trợ lý thay thế bước xử lý thủ công cho các ca hoàn tiền giao trễ nằm trong chính sách tự động, đảm bảo phản hồi trong ngày và khớp sổ cái.
- **Câu 1.6 & A4 – Bản tiêu chí chấp nhận:** Soạn thảo bản tiêu chí "Nếu ... thì ..." cho 5 chỉ số bắt buộc và ngưỡng kinh doanh/vận hành, cấu hình `config/acceptance_criteria.json`.
- **Câu 2.3 – Bản đồ dữ liệu & Data Drift:** Lập bản đồ dữ liệu các trường thông tin và phân tích ví dụ rủi ro Data Drift trong 3 tháng tới.
- **Câu 2.9 – Cổng kinh doanh:** Cấu hình nhóm `business` trong `config/operating_gates.json` (daily_refund_cap_vnd: 2.000.000đ, cost_budget: 6.000đ, roi_min: 0.30).
- **Khối 3 – Xử lý sự cố S6 & Quyết định v2:** Chủ trì phân tích nguyên nhân lỗi đơn tách kiện multi-carrier, bổ sung chỉ số giám sát `multi_carrier_order_rate` trong `lab10/monitors.py`, hoàn thiện toàn bộ Phiếu C (C0–C12), fault tree, risk register, runbook 4–5, và đưa ra quyết định Gate 1 v2 "Thu hẹp".

### Bằng chứng

- Issue phân công: [Issue #4 – Product & Business Lead](https://github.com/NganConDev/K5-L3A-DAY10-QuanKhanhHuyBao-PoCtoPilotGate1/issues/4).
- Phiếu A: `templates/form-a-criteria.md`, mục A1, A4, A5.
- Phiếu B: `templates/form-b-evaluation-gates.md`, mục B3, B7.4.
- Phiếu C: `templates/form-c-incident.md`, mục C0–C12.
- Commit xử lý sự cố S6: `c368a37` ("LAB 10: hoàn thành phần C, sự cố S6, quyết định v2 Thu hẹp").
- Cấu hình kinh doanh: `config/operating_gates.json`.
- Monitor bổ sung: `lab10/monitors.py`.

### Công cụ AI và cách tự kiểm tra

- Sử dụng Claude để hỗ trợ soạn thảo fault tree, phân tích cây nguyên nhân và diễn đạt runbook phần 4–5.
- Tự kiểm chứng bằng cách chạy `python3 -m lab10.grade --incident S6` và đối chiếu các ngưỡng tài chính trong `data/world.json`.

### Exit ticket

Một điều học được: Tự động hóa không thể giải quyết mọi trường hợp biên; khi chi phí xử lý trên mỗi ticket vượt trần kinh doanh (7.462đ > 6.000đ) do ca khó phát sinh nhiều chi phí escalation, quyết định "Thu hẹp" phạm vi pilot là lựa chọn bảo toàn tính bền vững kinh doanh.
Một điều còn chưa chắc: Cơ chế phân bổ chi phí và trách nhiệm đối soát giữa các hãng vận chuyển khi cùng phục vụ một đơn hàng tách kiện trong thực tế.
