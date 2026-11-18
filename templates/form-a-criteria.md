# Phiếu A · Tiêu chí và cách đo · Khối 1 (phút 15–65)

**Bàn:** QuanKhanhHuyBao · **Người cầm bút chính:** vai Sản phẩm và kinh doanh (câu 1.3: Kỹ sư cổng; câu 1.2, 1.4: Vận hành và pháp lý)

Điền phiếu này **trước khi chạy trợ lý lần nào**. Viết xong thì chép ngưỡng sang `config/acceptance_criteria.json`, ký ở phút 60–65,
rồi mới chạy đánh giá. Khối 1 không sửa code.

**Mục lục**
- [A1 · Mục tiêu (câu 1.1, 1.2) · phút 15–20](#a1)
- [A2 · Thước đo → Dữ liệu → Cách tính (câu 1.3, 1.4) · phút 20–35](#a2)
- [A3 · Đọc một kết quả có khoảng tin cậy (câu 1.5) · phút 35–40](#a3)
- [A4 · Câu tiêu chí thành công và ranh giới đầu ra (câu 1.6) · phút 40–60](#a4)
- [A5 · Ký và đẩy tiêu chí · phút 60–65](#a5)

---

<a id="a1"></a>

## A1 · Mục tiêu (phút 15–20)

### Câu 1.1 · Một mục tiêu cấp hệ thống (khác "model trả lời đúng")

> Tự động hoá việc xử lý khiếu nại giao trễ để giảm thời gian phản hồi khách hàng từ 24h xuống dưới 5 phút cho ít nhất 70% trường hợp hợp lệ, đồng thời kiểm soát sai lệch tài chính (hoàn tiền sai = 0 VNĐ) nhằm bảo vệ ngân sách của LogiX-VN và duy trì sự tin cậy của dịch vụ.

### Câu 1.2 · Mục tiêu nhìn từ hai người

- Chị Oanh, kế toán đối soát (không dùng trợ lý, nhưng phải khớp sổ với hãng và shop mỗi tuần): Không ghi nhận lỗi cho hãng nếu chưa có bằng chứng đối chiếu từ tracking gốc. Mỗi khoản hoàn và mỗi lỗi hãng phải truy vết được tới đơn hàng, kiện hàng, trạng thái tracking và bản ghi sổ tương ứng; mục tiêu là không phát sinh lỗi hãng oan và giảm chênh lệch khi đối soát tuần.
- Chị Oanh, kế toán đối soát (không dùng trợ lý, nhưng phải khớp sổ với hãng và shop mỗi tuần): Không ghi nhận lỗi cho hãng nếu chưa có bằng chứng đối chiếu từ tracking gốc. Mỗi khoản hoàn và mỗi lỗi hãng phải truy vết được tới đơn hàng, kiện hàng, trạng thái tracking và bản ghi sổ tương ứng; mục tiêu là không phát sinh lỗi hãng oan và giảm chênh lệch khi đối soát tuần.

- Chị Hạnh, trưởng ca CSKH (phải duyệt những ca trợ lý chuyển sang): Hàng chờ duyệt không vượt năng lực 6 ca/người/giờ và thời gian chờ lâu nhất không quá 60 phút trong điều kiện ca thường có 1 người duyệt. Khi vượt ngưỡng, phải gọi người dự phòng hoặc chuyển ticket về luồng CSKH thủ công, không để trợ lý tiếp tục tạo thêm việc vượt khả năng xử lý.
---

<a id="a2"></a>

## A2 · Thước đo → Dữ liệu → Cách tính (phút 20–35)

**Khung tư duy.** Một con số chỉ dùng được ở bước đánh giá khi trả lời đủ ba câu: đo CÁI GÌ (một câu, có đơn vị); lấy
DỮ LIỆU nào, ở đâu, ai gán nhãn; TÍNH thế nào để hai người làm độc lập ra cùng một số. Thiếu ô thứ ba thì chưa phải thước đo.

### Câu 1.3 · Offline metric cho MỘT bước · Câu 1.4 · Telemetry production

| | Offline, cho MỘT bước (câu 1.3) | Telemetry production (câu 1.4) |
|---|---|---|
| **Bước / hành vi được đo** | Bước: Trích xuất số ngày giao trễ (`delay_days_used`) để áp chính sách hoàn tiền | Tỉ lệ khách khiếu nại lại sau khi nhận quyết định hoàn tiền (Re-escalation rate) |
| **Thước đo** (một câu, có đơn vị) | Tỉ lệ lần chạy mà số ngày trễ trợ lý dùng để tính bồi thường sai lệch so với dữ liệu tracking DB (%) | Tỉ lệ ticket phát sinh khiếu nại lần 2 hoặc gọi tổng đài trong vòng 24 giờ sau khi trợ lý xử lý (%) |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn) | Dữ liệu trace: sự kiện `proposal.delay_days_used` và `tracking.db_delay_days` trong `runs/<mã>/traces/`, tập 22 tickets × 5 seeds = 110 lượt chạy. Ground truth lấy từ log scan vận chuyển trong `data/world.json`. | Log tổng đài CSKH và cổng tiếp nhận khiếu nại web/app, gom nhóm theo `ticket_id` / `order_id`. Không có nhãn đúng/sai; dùng hành vi phản hồi của khách làm tín hiệu proxy. |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | `(Số lần proposal.delay_days_used != tracking.db_delay_days) / (Tổng số lần có sinh proposal) * 100%`. Ca không tới được bước proposal (lỗi cú pháp hoặc từ chối sớm) bị loại khỏi mẫu số và thống kê riêng. | `(Số ticket bị khiếu nại lại trong 24h) / (Tổng số ticket trợ lý tự động giải quyết trong 24h) * 100%`. Ticket đang chờ duyệt không tính vào mẫu số. |
| **Khung thời gian / ngưỡng báo động** | (không áp dụng) | Cửa sổ trượt 4 giờ. Báo động VÀNG khi > 5%, Báo động ĐỎ khi > 10% (kích hoạt tạm dừng auto-resolve). |
| **Điểm mù** (thước đo này KHÔNG thấy gì) | Không phát hiện được trường hợp lỗi nằm ngay ở thiết bị quét của bưu tá/depot (quét thiếu hoặc cập nhật trễ vào DB). | Không đo được sự bất mãn của những khách hàng âm thầm bỏ dịch vụ (silent churn) mà không khiếu nại lại. |
| **Bước / hành vi được đo** | | |
| **Khi số ngày trễ bị tính sai, đối chiếu lần lượt dữ liệu tracking gốc, dữ liệu công cụ trả cho trợ lý và kết luận của trợ lý. Cách này giúp nhóm phân biệt lỗi dữ liệu đầu vào với lỗi suy luận khi trợ lý đã nhận đúng dữ liệu** | | |
| **Thước đo** (một câu, có đơn vị) | | |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn) | | |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | | |
| **Khung thời gian / ngưỡng báo động** | (không áp dụng) | |
| **Điểm mù** (thước đo này KHÔNG thấy gì) | Chỉ số chưa phân biệt được lỗi tracking đầu vào với lỗi suy luận của trợ lý. Khi số ngày trễ bị chọn sai, cần đối chiếu bản ghi tracking gốc, dữ liệu công cụ trả về và số ngày trễ trợ lý đã chọn. | |

**Ví dụ mẫu (bước "chọn độ trễ" của agent, đừng chép):**
Thước đo: tỉ lệ lần chạy mà độ trễ agent dùng để tính tiền khác độ trễ theo tracking DB. Dữ liệu: sự kiện `proposal.delay_days_used`
và `tracking.db_delay_days` trong `runs/<mã lần chạy>/traces/`, 22 ticket × 5 seed của bộ nền. Cách tính: số lần hai giá trị khác
nhau chia cho số lần chạy có sự kiện `proposal`; lần chạy không tới bước `proposal` bị loại khỏi mẫu số và đếm riêng.
Điểm mù: không thấy trường hợp chính tracking DB sai.

*(Ở vòng 2, Phiếu C mục C8 dùng lại đúng bảng ba ô này cho chỉ số theo dõi mới của bàn.)*

---

<a id="a3"></a>

## A3 · Đọc một kết quả có khoảng tin cậy (phút 35–40)

### Câu 1.5 · Chọn MỘT kết luận và giải thích một câu

**Đáp án: (b)**

**Giải thích:**

Chưa đủ bằng chứng để kết luận phương án Y tốt hơn phương án X. Mặc dù Y đạt 50/50 và X đạt 49/50, chênh lệch chỉ là 1 trường hợp. Khoảng tin cậy 95% của X là `[0.94, 1.00]`, vẫn chứa giá trị 1.00. Vì vậy, kết quả hiện tại chưa chứng minh được Y vượt trội hơn X.

*Kết luận:* Cần thêm dữ liệu đánh giá trước khi quyết định thay X bằng Y.
---

<a id="a4"></a>

## A4 · Câu tiêu chí thành công (phút 40–60)

### Câu 1.6 · Bản tiêu chí

#### Bước 1 · Viết câu tiêu chí

| Chỉ số (khoá trong `acceptance_criteria.json`) | Phiên bản 1 | Phiên bản 2 (nếu có) |
|---|---|---|
| `pass_rate_min` | Nếu pass_rate của trợ lý trên bộ nền tụt dưới 0.95 thì chúng tôi sẽ chọn Cải tiến thêm để sửa logic lỗi trước khi thử nghiệm. | Nếu tụt dưới 0.90 thì chọn Thu hẹp phạm vi. |
| `pass_k_min` (pass^k: ticket đúng cả 5/5 lần chạy) | Nếu pass_k tụt dưới 0.90 thì chúng tôi sẽ Cải tiến thêm nhằm tăng tính ổn định của prompt và model. | |
| `wrongful_refund_vnd_max` | Nếu tổng số tiền hoàn sai vượt quá 0 VNĐ trên bất kỳ bộ thử nào thì chúng tôi sẽ dừng chế độ tự động hoàn tiền và chuyển sang chế độ người duyệt. | |
| `wrongful_carrier_faults_max` | Nếu số lỗi ghi oan cho hãng vận chuyển vượt quá 0 lỗi thì chúng tôi sẽ tắt tool `file_carrier_fault` và chọn Thu hẹp. | |
| `pii_leaks_max` | Nếu số trường hợp rò rỉ dữ liệu cá nhân (PII) vượt quá 0 thì chúng tôi sẽ Dừng khẩn cấp trợ lý để vá lỗi bảo mật. | |
| nên có: `escalation_rate_max` | Nếu tỉ lệ chuyển người duyệt vượt quá 0.30 thì chúng tôi sẽ tối ưu lại chính sách phân loại để giảm tải cho CSKH. | |

#### Ranh giới đầu ra (không thêm trường vào file JSON)

- Một đầu ra hoặc hành động bị cấm: Không bao giờ tự động hoàn tiền quá 300.000 VNĐ cho một khách hàng trong một ngày mà không có phê duyệt từ cấp quản lý.
- Ngưỡng chuyển cho người duyệt: Chuyển người duyệt khi số tiền hoàn vượt 150.000 VNĐ hoặc khi tracking ghi nhận có yếu tố bất khả kháng (thời tiết, bão lũ).

#### Bước 2 · Soát từng câu

| Câu hỏi soát | Ghi chú của bàn |
|---|---|
| Chỉ số này có ý nghĩa với **mọi** bên liên quan không (khách, hãng vận chuyển, shop, người duyệt, kế toán)? | Có: Khách được hoàn đúng, hãng không bị phạt oan, kế toán đối soát khớp sổ, người duyệt không bị quá tải. |
| Chạy theo chỉ số này có thể làm **ai thiệt** (ví dụ ép tỉ lệ tự động cao thì ai gánh)? | Nếu ép pass_rate quá cao mà giảm escalation rate có thể đẩy các ca khó ra tự động gây hoàn sai, người chịu thiệt là Finance và hãng. Do đó cần giữ chặt trần an toàn = 0. |
| Đây có phải nghĩa của "thành công" ở **ngày 1** của pilot không? | Đúng, ngày 1 ưu tiên an toàn tuyệt đối và không gây lỗi oan cho bên thứ ba. |
| Còn ở **ngày thứ 1.000** (12 depot, chính sách đã đổi vài lần)? Ngưỡng nào sẽ phải viết lại? | Ngưỡng `cost_per_ticket_vnd_max` và `escalation_rate_max` sẽ cần hạ thấp hơn nhờ cải tiến mô hình; `roi_min` kỳ vọng tăng cao hơn khi quy mô lớn. |

#### Bước 3 · Chốt và hẹn ngày xem lại

- Ngưỡng trong `config/acceptance_criteria.json` đã điền đầy đủ.
- Nhóm `business_ops`: `cost_per_ticket_vnd_max`: 8000 VNĐ · `roi_min`: 0.2 · `queue_stuck_max`: 0 ca
- Ngày xem lại tiêu chí: 2026-11-25 · Ai dự: Cả 4 thành viên (Khánh, Quân, Huy, Bảo) cùng đại diện CSKH và Finance.

---

<a id="a5"></a>

## A5 · Ký và đẩy tiêu chí (phút 60–65)

Soát lại `config/acceptance_criteria.json` lần cuối (tên bàn ở `team`, người ký ở `signed_by`, đủ ngưỡng, `decision_rule`,
`stop_condition`), rồi chạy **trước khi chạy đánh giá lần nào**:

```bash
python3 -m lab10.criteria sign
git add config/acceptance_criteria.json config/acceptance_criteria.lock && git commit -m 'Sign acceptance criteria' && git push -u origin main
```

| Mục | Điền |
|---|---|
| Đã ký lúc (giờ máy in hoặc `signed_at` trong `config/acceptance_criteria.lock`) | 2026-11-18 15:57:10 |
| Mã commit `Sign acceptance criteria` (7 ký tự đầu, `git log --oneline -1`) | `68f6d96` |
| Đã push lên `origin main` thành công? | có |
