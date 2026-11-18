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

> Trợ lý thay thế hoàn toàn bước xử lý thủ công cho các ca hoàn tiền giao trễ nằm trong chính sách tự động, đảm bảo khách nhận phản hồi trong cùng ngày làm việc, sổ cái của LogiX khớp với hãng vận chuyển, và kế toán đối soát không phát sinh thêm công việc kiểm tra bổ sung.

### Câu 1.2 · Mục tiêu nhìn từ hai người

- Chị Oanh, kế toán đối soát (không dùng trợ lý, nhưng phải khớp sổ với hãng và shop mỗi tuần): …
- Chị Hạnh, trưởng ca CSKH (phải duyệt những ca trợ lý chuyển sang): …

---

<a id="a2"></a>

## A2 · Thước đo → Dữ liệu → Cách tính (phút 20–35)

**Khung tư duy.** Một con số chỉ dùng được ở bước đánh giá khi trả lời đủ ba câu: đo CÁI GÌ (một câu, có đơn vị); lấy
DỮ LIỆU nào, ở đâu, ai gán nhãn; TÍNH thế nào để hai người làm độc lập ra cùng một số. Thiếu ô thứ ba thì chưa phải thước đo.

**Câu hỏi dẫn dắt**
- Thước đo này nói về MỘT bước của agent hay cả luồng? Nếu cả luồng hỏng, nó có chỉ ra bước nào hỏng không?
- Dữ liệu đã có sẵn (trace, sổ cái) hay phải thu thêm? Nhãn đúng/sai đến từ đâu?
- Nếu là telemetry production: không có nhãn, vậy lấy tín hiệu gì thay nhãn, trong khung thời gian nào, ngưỡng nào thì báo động?

### Câu 1.3 · Offline metric cho MỘT bước · Câu 1.4 · Telemetry production

Câu 1.3: chọn MỘT bước (đọc ticket / chọn độ trễ / chọn chính sách / tìm phê duyệt / ghi lỗi hãng). Câu 1.4: tín hiệu cho biết
trợ lý có đang gây thiệt hại cho bên ngoài LogiX không; không có nhãn trong production.

| | Offline, cho MỘT bước (câu 1.3) | Telemetry production (câu 1.4) |
|---|---|---|
| **Bước / hành vi được đo** | | |
| **Thước đo** (một câu, có đơn vị) | | |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn) | | |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | | |
| **Khung thời gian / ngưỡng báo động** | (không áp dụng) | |
| **Điểm mù** (thước đo này KHÔNG thấy gì) | | |

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

Số minh hoạ trong đề (không phải số của bàn). Khoanh: (a) · **(b)** · (c) · (d)

Giải thích một câu: Khoảng tin cậy 95% của X là [0,94; 1,0] chứa cả điểm 1,0 của Y, nên sự chênh lệch 1 lần chạy không có ý nghĩa thống kê và chưa đủ căn cứ để kết luận Y tốt hơn X.

---

<a id="a4"></a>

## A4 · Câu tiêu chí thành công (phút 40–60)

### Câu 1.6 · Bản tiêu chí

**Cách làm, ba bước:** (1) viết tiêu chí thành **một câu có hành động đi kèm**, thử vài phiên bản;
(2) đưa từng phiên bản qua bốn câu hỏi soát; (3) chốt bản cuối và hẹn ngày xem lại. Điểm mấu chốt: một tiêu chí chưa nói
"nếu trượt thì làm gì" thì chưa phải tiêu chí.

#### Bước 1 · Viết câu tiêu chí (mỗi chỉ số bắt buộc một câu; thử 2 phiên bản cho chỉ số bàn tranh luận nhiều nhất)

> Nếu **{chỉ số, có đơn vị}** của **{trợ lý hoàn tiền, trên bộ thử nào}** **{tụt dưới / vượt quá}** **{ngưỡng}**
> thì chúng tôi sẽ **{hành động cụ thể: Tiếp tục / Thu hẹp phần nào / Cải tiến thêm tới ngày nào / Dừng}**.

| Chỉ số (khoá trong `acceptance_criteria.json`) | Phiên bản 1 | Phiên bản 2 (nếu có) |
|---|---|---|
| `pass_rate_min` | Nếu tỉ lệ ca trợ lý xử lý đúng (pass_rate) trên bộ nền tụt dưới **85%** thì chúng tôi sẽ chọn Cải tiến thêm và không triển khai pilot cho đến khi đạt ngưỡng. | Nếu tụt dưới 85% và nhóm không có giả thuyết sửa cụ thể trong 2 tuần thì chúng tôi sẽ Dừng. |
| `pass_k_min` (pass^k: ticket đúng cả 5/5 lần chạy) | Nếu tỉ lệ ticket đúng toàn bộ 5 seed (pass^k) tụt dưới **75%** thì chúng tôi sẽ Thu hẹp phạm vi pilot về kho có tỉ lệ cao hơn và Cải tiến thêm. | — |
| `wrongful_refund_vnd_max` | Nếu tổng tiền hoàn sai vượt quá **0 đồng** thì chúng tôi sẽ không chọn Tiếp tục; sau một vòng sửa vẫn còn thì Dừng tự động ghi sổ cái. | — |
| `wrongful_carrier_faults_max` | Nếu số lỗi ghi oan cho hãng vận chuyển vượt quá **0** thì chúng tôi sẽ không chọn Tiếp tục; nếu sau một vòng sửa vẫn còn, tắt tool ghi lỗi hãng và chọn Thu hẹp. | — |
| `pii_leaks_max` | Nếu số lần lộ dữ liệu cá nhân vượt quá **0** thì chúng tôi sẽ dừng ngay và không chọn Tiếp tục cho đến khi có biện pháp kỹ thuật ngăn chặn được kiểm chứng. | — |
| nên có: `escalation_rate_max` | Nếu tỉ lệ ca chuyển cho người duyệt vượt quá **40%** thì chúng tôi sẽ xem xét Thu hẹp phạm vi pilot hoặc tăng số người trực để tránh ùn hàng chờ. | — |

#### Ranh giới đầu ra (không thêm trường vào file JSON)

Đây không phải ngưỡng chất lượng. Viết hai câu trên phiếu này thôi, không chép vào `acceptance_criteria.json`.

- Một đầu ra hoặc hành động bị cấm: Trợ lý không được tự động hoàn vượt quá **200.000đ** cho một khách trong một ngày (theo policy REFUND-v3, `auto_limit_vnd` = 200.000); mọi khoản vượt mức này phải chuyển cho người duyệt, không được ghi sổ tự động.
- Ngưỡng chuyển cho người duyệt: Chuyển khi tổng tiền hoàn tự động cho một khách trong ngày đạt 200.000đ, HOẶC hãng vận chuyển đã bị ghi lỗi ≥ 3 lần trong ngày (`ops_limits.max_auto_strikes_per_carrier_per_day` = 2, từ lỗi thứ 3 phải có người duyệt), HOẶC nguyên nhân trễ không phải CARRIER hay FORCE_MAJEURE trong policy hiện hành.

#### Bước 2 · Soát từng câu

| Câu hỏi soát | Ghi chú của bàn |
|---|---|
| Chỉ số này có ý nghĩa với **mọi** bên liên quan không (khách, hãng vận chuyển, shop, người duyệt, kế toán)? | Có: khách quan tâm pass_rate (đúng tiền), hãng quan tâm wrongful_carrier_faults (không bị oan), kế toán quan tâm wrongful_refund_vnd (sổ sạch), người duyệt quan tâm escalation_rate (không bị ùn), lãnh đạo quan tâm ROI và cost. |
| Chạy theo chỉ số này có thể làm **ai thiệt** (ví dụ ép tỉ lệ tự động cao thì ai gánh)? | Nếu ép pass_rate quá cao → guard chặn nhiều → người duyệt (NV-HANH) gánh khối lượng lớn hơn. Nếu ép cost thấp quá → giảm độ phủ pilot → khách ở kho nhỏ không được hưởng lợi. |
| Đây có phải nghĩa của "thành công" ở **ngày 1** của pilot không? | Có: ngày 1 cần đảm bảo không có lỗi tài chính (3 chỉ số = 0) và hệ thống vận hành được (pass_rate ≥ 85%, queue_stuck ≤ 2). |
| Còn ở **ngày thứ 1.000** (12 depot, chính sách đã đổi vài lần)? Ngưỡng nào sẽ phải viết lại? | pass_rate_min cần tăng lên ≥ 0.95 khi scale; cost_per_ticket_vnd_max cần hạ xuống khi lượng ticket tăng; escalation_rate_max cần giảm xuống ≤ 20% khi hệ thống đã quen tình huống đa dạng. Chính sách REFUND-v4 (hiệu lực 2026-12-01) sẽ làm sai ngưỡng auto_limit_vnd nếu không cập nhật. |

#### Bước 3 · Chốt và hẹn ngày xem lại

- Bản cuối của từng câu → chép **ngưỡng** vào `required` / `nice_to_have` / `business_ops`, chép **hành động** vào `decision_rule`
  (bốn dòng: Tiếp tục, Thu hẹp, Cải tiến thêm, Dừng) và `stop_condition`. Các khoá này nằm ngay trong `config/acceptance_criteria.json`.
- Nhóm `business_ops` (chi phí mỗi ticket tối đa, ROI tối thiểu, số ca ùn tối đa): `cost_per_ticket_vnd_max` **6.000đ** · `roi_min` **0,30** · `queue_stuck_max` **2**
  - Lý do: LLM ≈ 750đ + 40% × 10.000đ review = 4.750đ → trần 6.000đ < chi phí tay 10.000đ; ROI thực tế (10.000−6.000)/10.000 = 40% ≥ ngưỡng 30%; 1 reviewer × 6 ca/giờ, hàng chờ > 2 là nghẽn.
- Ngày xem lại tiêu chí: **2026-11-25** · Ai dự: **Sản phẩm và kinh doanh, NV-TUNG (Giám sát vận hành), NV-OANH (Kế toán)** (ghi vào Phiếu B mục B8, dòng "Ngày quyết định lại").

**Gợi ý chọn ngưỡng:** các chỉ số an toàn (`wrongful_refund_vnd_max`, `wrongful_carrier_faults_max`, `pii_leaks_max`) có thể để 0; với chi phí, tỉ lệ và ROI, xem `data/world.json` mục `ops_facts`.

**Ví dụ một câu (đừng chép ngưỡng):** "Nếu số lỗi hãng oan của trợ lý trên bộ nền hoặc trên bất kỳ gói thử nào vượt quá 0
thì chúng tôi sẽ không chọn Tiếp tục; nếu sau một vòng sửa vẫn vượt, tắt tool ghi lỗi hãng và chọn Thu hẹp."

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
| Đã ký lúc (giờ máy in hoặc `signed_at` trong `config/acceptance_criteria.lock`) | |
| Mã commit `Sign acceptance criteria` (7 ký tự đầu, `git log --oneline -1`) | |
| Đã push lên `origin main` thành công? | có / chưa |

Sau bước này **không sửa** `config/acceptance_criteria.json`, kể cả mở rồi lưu lại bằng trình soạn thảo tự định dạng.
