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
