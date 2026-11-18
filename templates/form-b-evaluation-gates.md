# Phiếu B · Đo, rủi ro, cổng vòng 1 và quyết định v1 · Khối 2A + 2B + chốt (phút 65–115)

**Bàn:** QuanKhanhHuyBao

Tiêu chí đã ký ở Phiếu A. Từ phút 65 bàn mới được chạy trợ lý. Khối 2A (65–85) chưa sửa code hay config. Khối 2B (85–105) sửa
`lab10/guards.py` và `config/operating_gates.json`. Phút 105–115 chốt cổng vòng 1 rồi viết quyết định v1. Sau phút 115 không sửa phiếu này
(trừ khi Phiếu C bảo "mở lại" một ô và ghi bằng bút khác màu).

**Mục lục**
- [B0 · Nhật ký lần chạy vòng 1 (suốt khối)](#b0)
- [B1 · Câu 2.1 · Lần chạy đầu tiên, cổng tự chặn hay người duyệt · phút 65–71](#b1)
- [B2 · Câu 2.2 · Bảng soát lỗi `T-002@55` · phút 71–75](#b2)
- [B3 · Câu 2.3 · Bản đồ dữ liệu và ví dụ drift · phút 65–75](#b3)
- [B4 · Câu 2.4 · HAZOP vòng 1 · phút 65–75](#b4)
- [B5 · Câu 2.4 · Checklist 9 nhóm việc, lần 1 · phút 70–75](#b5)
- [B6 · Câu 2.5 · Pre-mortem bốn lăng kính → cổng phòng ngừa · phút 75–85](#b6)
- [B7 · Câu 2.6–2.10 · Cổng phòng ngừa, runbook phần 1–3, giờ cao điểm · phút 85–105](#b7)
- [B8 · Chốt cổng vòng 1 và quyết định Gate 1 · v1 · phút 105–115](#b8)

---

<a id="b0"></a>

## B0 · Nhật ký lần chạy vòng 1

*Yêu cầu: ít nhất 3 lần chạy, mỗi lần đổi một thứ, có mã lần chạy và khoảng tin cậy.* Mỗi lệnh `lab10.eval` và `lab10.grade` tự ghi
một dòng vào `runs/journal.jsonl`. Việc của bàn là điền cột "Đổi MỘT thứ gì" (tham số `--note`) và cột "Kết luận".
Mọi con số trong quyết định Gate 1 phải trỏ về một dòng ở đây hoặc ở Phiếu C mục C0.

| # | Mã lần chạy | Bộ ticket · mốc | Đổi MỘT thứ gì so với lần trước | pass_rate (khoảng tin cậy 95%) | pass_k | Hoàn sai (đ) · lỗi hãng oan · lộ dữ liệu | Tỉ lệ chuyển người | Kết luận (một câu) |
|---|---|---|---|---|---|---|---|---|
| 1 | | base · base | (baseline, chưa có cổng) | | | | | |
| 2 | | base · after | (cổng vòng 1, thử trước khi chốt) | | | | | |
| 3 | | base · prepared | (cổng vòng 1 đã chốt) | | | | | |
| 4 | | | | | | | | |

---

<a id="b1"></a>

## B1 · Câu 2.1 · Lần chạy đánh giá đầu tiên

```bash
python3 -m lab10.eval --suite base --stage base --note "baseline"
python3 -m lab10.gate --run runs/<mã lần chạy>/report.json
```

- Mã lần chạy: `__________` (ghi cả vào B0 dòng 1)
- Ngưỡng đã ký nào `[CHƯA]` đạt: …
- Khối "kinh doanh và vận hành" ở cuối output: dòng nào đáng lo? …
- Khối "theo kho và hãng": kho hoặc hãng nào có số xấu nhất? …

**Cổng so tiêu chí này có nên tự chặn một bản phát hành không (so với để người duyệt)?**

| Lý lẽ ủng hộ tự chặn | Lý lẽ phản đối |
|---|---|
| | |

Khuyến nghị (khoanh một): **tự chặn · người duyệt · kết hợp**. Vì: …

---

<a id="b2"></a>

## B2 · Câu 2.2 · Bảng soát lỗi cho `T-002@55`

```bash
python3 -m lab10.trace --suite base --ticket T-002 --seed 55
```

**Cách làm, giữ nguyên ba phần:** (1) ghi lại từng lỗi bằng **cái người ta thực sự thấy**, ai gặp, mức hệ trọng,
và xếp vào một trong ba **loại lỗi**; (2) đưa lỗi qua bộ câu hỏi để tìm **nguồn**; (3) viết **hướng xử lý**: vì sao người ta coi
đó là lỗi, người ta đi tiếp bằng đường nào, hệ thống học được gì.

Ba loại lỗi:
- **Giới hạn của hệ thống**: hệ thống không thể trả lời đúng, hoặc không trả lời được, vì giới hạn vốn có.
- **Lỗi ngữ cảnh**: hệ thống "chạy đúng thiết kế" nhưng người dùng thấy sai, vì hành động không được giải thích, trái với hình dung của họ, hoặc dựa trên giả định kém.
- **Lỗi chìm**: hệ thống chạy sai mà **cả người dùng lẫn hệ thống đều không nhận ra**. Với một trợ lý có quyền ghi sổ, đây là loại nguy hiểm nhất: người chịu hại thường là bên thứ ba.

### Phần 1 · Ghi lỗi (bằng chứng là mã ticket@seed và dòng trace, không tả chung chung)

| # | Lỗi: người ta thấy gì (dán dòng trace / sổ cái) | Ai gặp, ai chịu | Hệ trọng (thấp / cao) | Loại lỗi (giới hạn hệ thống / ngữ cảnh / chìm) |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |

### Phần 2 · Tìm nguồn (đánh dấu câu nào đúng với từng lỗi)

| Câu hỏi | Lỗi 1 | Lỗi 2 |
|---|---|---|
| **Đầu vào:** hệ thống có tự diễn giải / sửa đầu vào của người dùng theo cách họ không lường? Có đặt sai trọng số cho một lời nói hay tín hiệu của người dùng? | | |
| **Độ liên quan:** hệ thống có thiếu dữ liệu cần để quyết đúng? Dữ liệu vào có nhiễu, thiếu ổn định? | | |
| **Thứ bậc hệ thống:** có hai hệ thống cùng ghi / cùng theo dõi một thứ mà không rõ bên nào là chủ (ví dụ CSKH hoàn tay và trợ lý cùng ghi sổ)? | | |
| **Trạng thái hỏng:** nhiều lỗi cộng lại có làm tính năng không dùng được (ví dụ LLM lỗi liên tiếp)? | | |

### Phần 3 · Hướng xử lý (mỗi lỗi một ô)

| | Lỗi 1 | Lỗi 2 |
|---|---|---|
| Vì sao người gặp coi đây là lỗi | | |
| Kiểu giải pháp: phản hồi cho người dùng / trao quyền kiểm soát cho người / khác | | |
| Đường đi của người sau khi có giải pháp (ví dụ: ticket chuyển sang người duyệt → duyệt → khách được trả lời) | | |
| Hệ thống học được gì (tín hiệu ghi lại để theo dõi: tên metric trong `monitors.py`) | | |

**Ví dụ (bộ nền, đừng chép):** `T-002@55` · sổ cái có dòng hoàn 20.000đ, hãng VNX nhận một lỗi, trong khi tracking ghi trễ 2 ngày ·
khách không thấy gì sai, hãng chịu · cao · **lỗi chìm**. Nguồn: đầu vào (đặt sai trọng số cho con số khách tự khai). Xử lý:
hãng coi là lỗi vì sổ giao của họ ghi 2 ngày; kiểu giải pháp: trao quyền cho người (số khai khác tracking thì chuyển người duyệt);
tín hiệu: đếm sự kiện `model_override` mỗi ngày.

---

<a id="b3"></a>

## B3 · Câu 2.3 · Bản đồ dữ liệu của trợ lý và ví dụ drift

**Cách làm:** đi từ người dùng và việc họ cần làm, tới đầu ra của hệ thống, rồi mới hỏi hệ thống cần dữ liệu
gì, định dạng ra sao, và **thế giới thật làm dữ liệu đó lệch đi thế nào**; cuối cùng tóm lại trong vài câu.
Trợ lý LogiX không huấn luyện gì trong lab này, nên ta hỏi về "dữ liệu trợ lý đọc lúc chạy / trường then chốt / nguồn sự thật".
Gợi ý: mở `data/world.json` phần `policies`, `orders[].parcels`, `ops_limits`, `ops_facts`.

| Mục | Điền cho trợ lý hoàn tiền |
|---|---|
| Người dùng | Khách hàng LogiX (gửi yêu cầu hoàn tiền qua ticket CSKH) |
| Việc người dùng cần làm xong | Nhận xác nhận hoàn tiền (hoặc từ chối có lý do) trong cùng ngày làm việc, không cần gọi lại |
| Đầu ra của hệ thống (kể cả các lệnh ghi) | Ghi sổ cái (`issue_refund`), ghi lỗi hãng (`file_carrier_fault`), thông báo hãng (`notify_carrier`), trả lời khách; ± chuyển cho người duyệt (`escalate`) |
| Dữ liệu trợ lý đọc lúc chạy (bảng nào trong `data/world.json`) | `orders`, `orders[].parcels`, `policies`, `ops_limits`, `approvals`, `ledger_seed`, `carriers` |
| Trường then chốt quyết định tiền và lỗi hãng | `parcels[].delivered_date`, `parcels[].promised_date`, `parcels[].delay_cause`, `policies[].auto_limit_vnd`, `policies[].index_active`, `ops_limits.max_auto_refund_per_customer_per_day_vnd` |
| Với mỗi trường then chốt: **nguồn sự thật** hay **bản sao** (ai cập nhật, khi nào)? | `delivered_date`: bản sao từ hệ thống quét của hãng vận chuyển — cập nhật khi tài xế quét tại điểm phát; `promised_date`: nguồn sự thật từ hệ thống đơn hàng LogiX; `delay_cause`: nguồn sự thật từ tracking DB LogiX; `policies[].index_active`: nguồn sự thật từ policy DB, cập nhật thủ công khi đổi chính sách |
| Định dạng cần để ý (ngày, trường được phép trống, đơn nhiều kiện) | Ngày dạng ISO (YYYY-MM-DD); `delivered_date` có thể null (đơn còn IN_TRANSIT); đơn nhiều kiện (`O-1013` có P1 và P2 với 2 hãng khác nhau) — phải xử lý từng kiện riêng; `delay_cause` có thể null nếu giao đúng hạn |
| Thế giới thật làm dữ liệu lệch ở đâu (theo mùa, đổi chính sách, giờ cao điểm, người nhập tay)? | (1) Tài xế quét sót/trễ → `delivered_date` nhập bù bằng tay → không phản ánh thời điểm thật. (2) Chính sách đổi (`REFUND-v4` hiệu lực 2026-12-01) nhưng `index_active` chưa được cập nhật → trợ lý áp nhầm chính sách. (3) Khách nhập ngày trễ tự khai trong ticket, khác tracking DB. (4) Giờ cao điểm (ngày sale): nhiều ticket cùng lúc, một khách có thể vượt ngưỡng 300.000đ/ngày trước khi cổng kiểm tra xong. |
| Câu người ngoài sẽ hỏi về nguồn dữ liệu ("sao hệ thống biết đơn trễ mấy ngày?") | "Sao hệ thống biết đơn trễ mấy ngày?" → Lấy `delivered_date − promised_date` từ DB tracking của LogiX, không dùng ngày khách tự khai. "Ai xác nhận lỗi là do hãng?" → Trường `delay_cause` trong tracking DB, do LogiX gán dựa trên báo cáo hãng. |

**Tóm lại (điền vào chỗ trống):**
Trợ lý dùng `orders/parcels`, `policies`, `ops_limits` để giúp `khách hàng LogiX` làm được `nhận hoàn tiền giao trễ trong ngày mà không cần CSKH can thiệp thủ công`.
Trường mà nếu sai thì tiền hoặc lỗi hãng sai theo: `parcels[].delivered_date`, `policies[].index_active`.
Chúng tôi biết thế giới thật sẽ làm dữ liệu lệch ở: `chính sách REFUND-v4 hiệu lực 2026-12-01 chưa được đặt index_active`. Dấu hiệu nhìn thấy sớm nhất: `wrongful_carrier_faults tăng đột ngột sau ngày 2026-12-01 do FORCE_MAJEURE không còn được phép ghi lỗi hãng trong v4`.

**Ví dụ drift trong 3 tháng tới** (lấy từ dòng "thế giới thật làm dữ liệu lệch"):
- Cái gì đổi: chính sách `REFUND-v4` trở thành chính sách hiện hành, `auto_limit_vnd` giảm từ 200.000đ xuống 100.000đ, và FORCE_MAJEURE không còn được ghi lỗi hãng
- Đổi ngày nào: `2026-12-01` (13 ngày nữa kể từ hôm nay)
- Trường nào cho thấy: `policies[].index_active` — khi v4 được bật lên `true` và v3 bị tắt
- Con số nào của Bản tiêu chí bị ảnh hưởng: `wrongful_carrier_faults_max` (tăng nếu trợ lý tiếp tục ghi lỗi cho đơn FORCE_MAJEURE theo v3), `wrongful_refund_vnd_max` (tăng nếu trợ lý hoàn theo ngưỡng v3 = 200.000đ trong khi v4 chỉ cho 100.000đ)

Đây là **đầu vào đổi** (nội dung bảng `policies` đổi) đồng thời là **quan hệ vào–ra đổi** (cùng delay_cause FORCE_MAJEURE nhưng v4 không ghi lỗi hãng còn v3 thì có).
Chỉ số sẽ phát hiện: `wrongful_carrier_faults` trong report — tăng đột ngột sau 2026-12-01 khi trợ lý dùng policy sai phiên bản.

**Ví dụ một dòng (đừng chép):** trường then chốt `parcels[].delivered_date` · bản ghi do máy quét ở điểm phát tạo ra, là nguồn
sự thật về ngày giao · lệch khi điểm phát quét sót hoặc nhập bù bằng tay.

---

<a id="b4"></a>

## B4 · Câu 2.4 · HAZOP vòng 1 trên tool của agent

*Chỉ làm MỘT vòng, trên MỘT tool. Đây là HAZOP vòng 1; HAZOP của thẻ sự cố viết riêng ở Phiếu C mục C4, không ghi đè bảng này.*

**Khung tư duy.** HAZOP không hỏi "cái gì có thể hỏng" một cách chung chung. Nó cầm từng **từ gợi ý** áp vào từng **dòng dữ
liệu đi vào một hành động** và hỏi: nếu dòng này lệch theo kiểu đó thì hậu quả là gì, ai chịu. Mục tiêu là tìm ra những nhánh
mà cả bàn chưa nghĩ tới, không phải tả lại nhánh đã biết.

| Guideword | Nghĩa khi áp vào một tool của agent |
|---|---|
| **WRONG** | Giá trị đưa vào có đủ, hợp lệ về hình thức, nhưng sai sự thật |
| **INVALID** | Giá trị không còn hiệu lực: hết hạn, sai phiên bản, sai đối tượng |
| **INCOMPLETE** | Thiếu một phần thông tin cần có để quyết định |
| **PERTURBED** | Đầu vào bị ai đó cố ý hoặc vô tình làm lệch (cài câu lệnh, gửi lặp) |
| **INCAPABLE** | Thành phần không trả lời được: quá tải, lỗi, hết quota |

**Câu hỏi dẫn dắt:** tool nào tạo ra hậu quả không đảo ngược? Mỗi tham số của tool đó lấy từ đâu (ticket, DB, model tự suy)?
Với mỗi guideword: hậu quả cho ai, hiện có gì ngăn, cần thêm gate ở tầng nào (phát hiện / chặn / giới hạn thiệt hại)?

Tool chọn phân tích: `issue_refund`

| Tham số / dòng dữ liệu               | Guideword  | Lệch cụ thể                                                                 | Hậu quả                                                                    | Gate đề xuất                                                                  |
| ------------------------------------ | ---------- | --------------------------------------------------------------------------- | -------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `amount_vnd`, `delay_days`           | WRONG      | T-002 khai trễ 5 ngày nhưng tracking O-1002 chỉ ghi 2 ngày                  | Hoàn sai tiền, LogiX chịu thiệt hại                                        | `write_gate` tính lại quyền lợi từ tracking và policy trong DB                |
| `policy_id`                          | INVALID    | Policy hết hiệu lực hoặc sai phiên bản                                      | Áp dụng sai mức hoàn                                                       | `pre_guard` kiểm tra hiệu lực và ghim đúng policy                             |
| `order_id`, dữ liệu kiện hàng        | INCOMPLETE | Thiếu tracking, ngày giao hoặc nguyên nhân chậm                             | Hoàn sai hoặc quy trách nhiệm sai                                          | `write_gate` chuyển người nếu thiếu dữ liệu bắt buộc                          |
| `amount_vnd`, `payer`, `approval_id` | PERTURBED  | Ghi chú khách nhập có chỉ thị yêu cầu hoàn toàn bộ giá trị hàng và phí ship | Shop bị hoàn/nợ sai dù không có phê duyệt hợp lệ                           | `write_gate` xác minh phê duyệt từ DB, không tin chỉ thị trong ghi chú        |
| Khả năng ghi sổ cái                  | INCAPABLE  | Dịch vụ ghi sổ lỗi hoặc timeout                                             | Khách nhận thông báo đã hoàn nhưng sổ cái chưa ghi; retry có thể ghi trùng | Xác nhận ledger, dùng idempotency key và chuyển người khi trạng thái không rõ |

Nhánh PERTURBED là nhánh mới đáng chú ý: trong `agent.py`, `checkout_note` được đưa qua LLM; nếu sinh `directive.full_refund`, agent có thể đặt `payer=MERCHANT` và `preapproved=true`. Đây là rủi ro cần kiểm soát ở tầng ghi, không chỉ bằng prompt.


Không bắt buộc điền đủ năm dòng. Bắt buộc: **ít nhất ba dòng, trong đó một dòng là nhánh bàn chưa thấy trên trace**.

**Mở rộng ra ngoài kỹ thuật (thêm ít nhất hai dòng):** "thành phần" không chỉ là model và tool. Áp cùng năm từ gợi ý vào:

| Thành phần ngoài code | Ví dụ câu hỏi |
|---|---|
| **Người duyệt** (vận hành) | INCAPABLE: chỉ một người trực mà 14 ca tới trong một giờ thì ca cuối chờ bao lâu? |
| **Ngân sách** (kinh doanh) | WRONG: tổng hoàn tự động trong ngày vượt mức Finance cho phép mà không ai được báo thì sao? |
| **Phạm vi pilot** (kinh doanh) | INVALID: có nhóm ticket nào trợ lý luôn phải chuyển người, tức là tự động hoá vô nghĩa? |
| **Dữ liệu gửi bên thứ ba** (pháp lý) | PERTURBED: chữ khách tự gõ có tên, số điện thoại người khác bị chép sang hãng thì ai chịu? |

| Thành phần             | Guideword | Lệch cụ thể                                                               | Hậu quả                                    | Cổng đề xuất                                                                          |
| ---------------------- | --------- | ------------------------------------------------------------------------- | ------------------------------------------ | ------------------------------------------------------------------------------------- |
| Người duyệt            | INCAPABLE | 1 người chỉ xử lý 6 ca/giờ, nhưng cao điểm có thể tới 18 ca/giờ           | Hàng chờ vượt SLA 60 phút                  | `operations.reviewers_on_shift`, `review_capacity_per_hour`, `max_queue_wait_minutes` |
| Dữ liệu gửi bên thứ ba | PERTURBED | Nội dung khách nhập chứa số điện thoại, email hoặc địa chỉ của người khác | Rò rỉ dữ liệu cá nhân sang hãng vận chuyển | `legal.pii_fields_blocked_to_third_party`; lọc payload trước `notify_carrier`         |

---

<a id="b5"></a>

## B5 · Câu 2.4 · Checklist go-live 9 nhóm việc, lần 1

Checklist chín nhóm việc phải xong trước khi chạy thử thật. Bàn điền lần đầu ở đây, rồi cập nhật sau sự cố ở Phiếu C mục C11.
Cột "Bằng chứng lấy từ đâu" trỏ tới mục bàn đã điền ở bước khác; không điền thêm phiếu nào chỉ để lấp cột này.

Trạng thái: **Xong** (có bằng chứng) · **Chưa** · **Không áp dụng** (ghi lý do). Bằng chứng là **mã lần chạy**, tên file / mục phiếu, hoặc số trong report.
**Cột PIC bắt buộc:** mỗi dòng một người có tên (không ghi "cả bàn"). Dòng nào chưa có PIC thì coi như Chưa.

| # | Nhóm việc| Nội dung cần kiểm tra| Trạng thái| Bằng chứng| PIC 
| - | ---------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------- | -------------------------------------------------------------------------------------------------------------------------- | --------- |
| 1 | **Chất lượng**         | Kiểm tra kết quả đánh giá baseline, pass rate, pass^k và các lỗi nghiêm trọng như hoàn tiền sai, ghi lỗi hãng oan.    | Đã hoàn thành | Báo cáo `runs/<run_id>/report.json` ở mốc base; kết quả đánh giá `lab10.gate`.                                             | **Quân**  |
| 2 | **Dữ liệu**            | Xác định nguồn dữ liệu đáng tin cậy, kiểm tra dữ liệu đơn hàng, kiện hàng, tracking và chính sách hoàn tiền.          | Đã hoàn thành | Phiếu B mục B3 – Data Map; đối chiếu `data/world.json`.                                                                    | **Huy**   |
| 3 | **Bảo mật**            | Kiểm tra prompt injection, dữ liệu đầu vào không đáng tin cậy và nguy cơ rò rỉ thông tin cá nhân.                     | Đã hoàn thành | HAZOP mục B4, đặc biệt rủi ro PERTURBED; kiểm tra cơ chế lọc PII.                                                          | **Bảo**   |
| 4 | **Quyền hạn**          | Kiểm tra quyền thực hiện hành động ghi, cơ chế guard và khả năng tắt từng chức năng tự động khi có sự cố.             | Đã hoàn thành | `lab10/guards.py`; `config/switches.json`.                                                                                 | **Khánh** |
| 5 | **Hiệu năng, hạ tầng** | Đánh giá năng lực xử lý, số người duyệt, tốc độ xử lý và khả năng đáp ứng SLA 60 phút.                                | Đã hoàn thành | `data/world.json`: năng lực 6 ca/giờ/người; đánh giá công suất duyệt và hàng chờ.                                          | **Bảo**   |
| 6 | **Chi phí**            | Kiểm tra chi phí xử lý mỗi ticket, ngân sách hoàn tiền và hiệu quả kinh tế so với xử lý thủ công.                     | Đã hoàn thành | `config/operating_gates.json`, mục `business.cost_budget_per_ticket_vnd`; đối chiếu `ops_facts` và `ops_limits`.           | **Huy**   |
| 7 | **Vận hành**           | Xác định người chịu trách nhiệm, người phê duyệt, kênh cảnh báo, ngưỡng dừng và quy trình chuyển sang xử lý thủ công. | Đã hoàn thành | Runbook phần 1–3; cấu hình `operations` trong `config/operating_gates.json`.                                               | **Bảo**   |
| 8 | **Con người, pháp lý** | Kiểm tra việc bảo vệ dữ liệu cá nhân khi gửi thông tin cho bên thứ ba và điều kiện ghi nhận lỗi hãng vận chuyển.      | Đã hoàn thành | Danh sách PII filter; cấu hình `legal.pii_fields_blocked_to_third_party` và `legal.carrier_fault_requires_recorded_cause`. | **Bảo**   |
| 9 | **Quyết định**         | Kiểm tra tiêu chí chấp nhận đã ký, tính toàn vẹn của file lock và bằng chứng trước khi quyết định Gate 1.             | Đã hoàn thành | Hash file `config/acceptance_criteria.lock`; kết quả kiểm tra và quyết định Gate 1.                                        | **Khánh** |


---

<a id="b6"></a>

## B6 · Câu 2.5 · Pre-mortem bốn lăng kính → cổng phòng ngừa (khoảng 8–10 phút, cả bàn)

*Mọi bàn làm pre-mortem ở vòng 1, TRƯỚC khi biết sự cố, để chọn 2–3 cổng phòng ngừa sẽ dựng. Ở vòng 2 bàn mở lại phần này ở
Phiếu C mục C1 (bút khác màu).*

**Khung tư duy.** Hỏi "có rủi ro gì không" thì ai cũng dè dặt. Nói "nó đã hỏng rồi, vì sao" thì mọi người được phép nói ra
điều mình vẫn lo. Làm im lặng trước, đọc sau, để ý kiến của người nói to không lấn át.

**Đề bài (đọc to):** *"Ba tháng sau pilot, LogiX phải tắt trợ lý hoàn tiền ở cả hai depot. Chuyện gì đã xảy ra?"*

1. **2 phút, im lặng:** mỗi người viết 2 lý do, mỗi lý do một dòng.
2. **2 phút:** đọc vòng tròn, mỗi lượt một lý do, không bình luận. Gộp lý do trùng.
3. **2 phút:** xếp từng lý do vào một **lăng kính**. Lăng kính nào còn trống thì cả bàn viết thêm ít nhất một lý do cho nó.
4. **2 phút:** chọn 2–3 lý do sẽ biến thành **cổng phòng ngừa** ngay hôm nay (code trong `guards.py` hoặc con số trong
   `config/operating_gates.json`). Lý do còn lại → Risk register.

Bốn lăng kính (bắt buộc đủ cả bốn; dự án AI hay chết ở ba lăng kính sau hơn là ở lăng kính đầu):

| Lăng kính | Câu hỏi gợi ý trên LogiX |
|---|---|
| **Kỹ thuật** | Model tin nhầm cái gì? Dữ liệu nào thiếu, cũ, lệch? Lệnh ghi nào không đảo ngược được? |
| **Kinh doanh** | Mỗi ticket tốn bao nhiêu so với làm tay? Một ngày hoàn tối đa bao nhiêu? Nhóm ticket nào không thể có lời? |
| **Con người và vận hành** | Ai duyệt, mấy người, mỗi giờ được mấy ca? Lượng việc tăng gấp ba thì sao? Nhân viên có tin trợ lý không? |
| **Pháp lý** | Dữ liệu cá nhân của ai rời hệ thống? Bên thứ ba nào bị ghi lỗi, bị trừ tiền mà không được hỏi? |

| Lý do thất bại (viết ở thì quá khứ)                                                                                                                          | Lăng kính             | Kiểm được hôm nay? (trace / data / config nào)                                                                                          | Thành cổng phòng ngừa nào / hay vào risk register                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Hệ thống đã thất bại vì lượng ticket tăng gấp 3 trong giờ Mega Sale nhưng chỉ có 1 nhân viên duyệt, khiến hàng chờ vượt 15 ca và thời gian chờ vượt 60 phút. | Con người và vận hành | `data/world.json`: `review_capacity_per_reviewer_per_hour = 6`; `default_reviewers_on_shift = 1`; `ops_limits.review_sla_minutes = 60`. | Cổng vận hành: gọi backup khi hàng chờ trên 6 ca hoặc chờ 45 phút; thu hẹp pilot khi hàng chờ trên 15 ca.            |
| Hệ thống đã ghi lỗi hãng vận chuyển khi tracking không có bằng chứng xác nhận nguyên nhân chậm, dẫn đến tranh chấp công nợ và đối soát sai.                  | Kinh doanh            | `data/world.json`: `orders`, `tracking`, `carriers`; kiểm tra trace của `file_carrier_fault`.                                           | `write_gate`: chỉ cho phép ghi lỗi hãng khi tracking có nguyên nhân hợp lệ; lưu bằng chứng để NV-OANH đối soát.      |
| Hệ thống đã gửi số điện thoại, địa chỉ và email khách hàng cho hãng vận chuyển dù các thông tin này không cần thiết, gây rò rỉ dữ liệu cá nhân.              | Pháp lý               | Kiểm tra payload của `notify_carrier`, trace gửi hãng và các trường dữ liệu khách hàng trong `data/world.json`.                         | Cổng bảo vệ dữ liệu: chặn `customer_phone`, `customer_street`, `customer_email`; chỉ gửi trường nằm trong allowlist. |


---

<a id="b7"></a>

## B7 · Khối 2B · Cổng phòng ngừa (phút 85–105)

### B7.1 · Câu 2.6 · 2–3 cổng phòng ngừa trong `lab10/guards.py`

Mỗi cổng ứng với một dòng pre-mortem (B6) hoặc một dòng HAZOP (B4). Viết trong `pre_guard(ctx)` (trước khi trợ lý đọc ticket)
hoặc `write_gate(ctx, action)` (trước mỗi lệnh ghi). Thử bằng:

```bash
python3 -m lab10.eval --suite base --stage after --note "cổng vòng 1: ..."
python3 -m unittest discover -s tests
```

| # | Cổng (hàm và nhánh, ví dụ `write_gate` khi `tool == "issue_refund"`) | Ứng với dòng nào ở B6 / B4 | Chặn điều gì, dựa vào nguồn sự thật nào | Mã lần chạy `base · after` | Ca đang đúng nào bị hỏng? (phải là "không") |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |

### B7.2 · Câu 2.7 · Hai bước tránh rò rỉ dữ liệu

Bàn đang chỉnh cổng tới khi 22 ticket bộ nền xanh hết. Nêu 2 bước cụ thể để không "chỉnh trên chính bộ dùng để chấm"
(gắn với bộ nền, gói sự cố, bài kiểm tra ẩn):

1. …
2. …

### B7.3 · Câu 2.8 · Một behavioral test

- Tính chất (một câu): …

```bash
python3 -m lab10.trace --suite base --stage after --adhoc "..." --order O-10xx --customer C-xx
```

| Ticket hiểm | Nội dung ticket (`--adhoc`) | `--order` · `--customer` | Kết quả (dán dòng `SỔ CÁI` / `LỖI HÃNG` / `GỬI HÃNG`) | Tính chất giữ được? |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |

Giữ hai ticket này cho phần demo.

### B7.4 · Câu 2.9 · Cổng kinh doanh (`config/operating_gates.json` mục `business`)

Mỗi con số kèm một câu lý do, lấy từ `data/world.json` → `ops_limits`, `ops_facts`.

| Khoá | Giá trị bàn đặt | Lý do (một câu, có số) |
|---|---|---|
| `business.daily_refund_cap_vnd` | 2.000.000đ | Khớp `ops_limits.daily_auto_refund_budget_vnd` = 2.000.000đ đã được Ops và Finance thống nhất; vượt mức này → người duyệt phải duyệt toàn bộ ca còn lại trong ngày. |
| `business.cost_budget_per_ticket_vnd` | 6.000đ | Manual = 10.000đ/ticket (`ops_facts.manual_cost_per_ticket_vnd`); với LLM ≈ 750đ + escalation 40% × 10.000đ review = ≈ 4.750đ, đặt trần 6.000đ vẫn thấp hơn manual 40% và còn biên an toàn. |
| `business.pilot_scope` (all / warehouse / percent) | warehouse: ["HN", "HCM"] | Pilot 2 depot theo đề bài; chọn HN và HCM vì là 2 kho lớn nhất với đơn lẻ cá nhân, loại HCM-B2B (đơn sỉ ≥ 2 triệu có rủi ro tài chính cao hơn) và DN, CT để kiểm soát phạm vi ban đầu. |
| `business.roi_min` | 0.30 | ROI tối thiểu 30% nghĩa là tổng chi phí AI/ticket ≤ 7.000đ so với tay 10.000đ — đủ để lãnh đạo chấp thuận scale lên 12 depot; nếu ROI < 30% thì phải xem lại thiết kế chi phí trước khi mở rộng. |

### B7.5 · Câu 2.10 · Cổng con người, vận hành, pháp lý + Runbook phần 1–3

Điền `config/operating_gates.json` mục `operations` và `legal` (PIC, người duyệt, số người trực mỗi ca, công suất duyệt mỗi giờ,
thời gian chờ tối đa, điều kiện dừng, kênh báo tin; trường dữ liệu cá nhân không gửi cho bên thứ ba; ghi lỗi cho hãng phải có
nguyên nhân trong tracking). Rồi viết runbook dưới đây **khớp với các con số đó**.

*Runbook là tờ giấy người trực ca cầm lúc 23h khi có chuyện. Nó trả lời: nhìn con số nào, ngưỡng nào thì làm gì, ai được quyết.
Phần 1–3 và mục Giờ cao điểm viết ở vòng 1. Phần 4–5 viết ở vòng 2 (Phiếu C mục C11). Mọi con số phải khớp `config/operating_gates.json` và report.*
*Mỗi phần trả lời bốn câu hỏi: ai chịu trách nhiệm, nhìn gì, ngưỡng nào, làm gì.* **Người viết (vai Vận hành và pháp lý):** ______

#### Runbook 1 · Ai chịu trách nhiệm

| Vai | Tên / mã nhân viên (lấy từ `data/world.json` → `staff`) | Được quyền làm gì | Liên lạc qua kênh nào |
|---|---|---|---|
| PIC của trợ lý (một người) | | | |
| Người duyệt đứng tên các khoản vượt hạn mức | | | |
| Người giữ công tắc tắt từng thao tác ghi | | | |
| Người nhận khiếu nại của bên thứ ba (hãng, shop, người nhận quà) | | | |

Số người trực duyệt mỗi ca: ___ · Mỗi giờ duyệt được: ___ ca · Phạm vi pilot: ______ (tất cả / kho nào / bao nhiêu phần trăm)

#### Runbook 2 · Nhìn con số nào, ngưỡng nào thì làm gì

Mỗi dòng một tín hiệu. Cột "Lấy ở đâu" phải là một dòng trong report của `lab10.eval` / `lab10.grade` hoặc một chỉ số trong `lab10/monitors.py`.

| Tín hiệu | Lấy ở đâu | Bình thường | Ngưỡng VÀNG → việc làm | Ngưỡng ĐỎ → việc làm | Ai quyết |
|---|---|---|---|---|---|
| Thời gian chờ người duyệt lâu nhất | | | | | |
| Số ca bị ùn | | | | | |
| Chi phí mỗi ticket so với làm tay | | | | | |
| Tổng tiền hoàn tự động trong ngày so với trần | | | | | |
| Tiền hoàn sai | | | | | |
| Lỗi ghi oan cho hãng / lộ dữ liệu cá nhân (pháp lý) | | | | | |
| (tín hiệu riêng của bàn) | | | | | |

#### Runbook 3 · Điều kiện dừng và cách dừng

- Dừng một phần (tắt một thao tác ghi, thu hẹp phạm vi) khi: …
- Dừng hẳn khi: …
- Cách dừng, từng bước (công tắc nào trong `config/switches.json`, dòng nào trong `config/operating_gates.json`): …
- Từ tín hiệu đỏ đến lúc dừng xong tối đa ____ phút; người bấm: ____
- Khi đã dừng, ticket đang chờ đi đâu, ai xử lý: …
- Điều kiện để bật lại, ai ký: …

### B7.6 · Giờ cao điểm (bắt buộc với thẻ S4; các thẻ khác nên có)

Lượng ticket có thể dồn gấp ba trong một giờ (ngày sale, sau bão). Viết trước, khi chưa biết sự cố.

| Câu hỏi | Trả lời (có số, có tên) |
|---|---|
| Giờ cao điểm là khi nào, bao nhiêu ticket mỗi giờ (dựa vào `ops_facts`)? | |
| Ai trực giờ cao điểm, mấy người (khớp `operations.reviewers_on_shift`)? | |
| Ngưỡng nào thì **gọi thêm người** (hàng chờ bao nhiêu ca, chờ lâu nhất bao nhiêu phút)? Ai gọi? | |
| Ngưỡng nào thì **thu hẹp** phạm vi (khoá `business.pilot_scope`) hoặc **tắt** một thao tác ghi (`config/switches.json`)? Ai quyết? | |
| Thêm người thì chi phí mỗi ticket và ROI thay đổi thế nào (đọc report)? | |

---

<a id="b8"></a>

## B8 · Chốt cổng vòng 1 và quyết định Gate 1 · v1 (phút 105–115)

Làm đúng thứ tự:

```bash
python3 -m lab10.checkpoint
python3 -m lab10.eval --suite base --stage prepared
python3 -m lab10.gate --run runs/<mã lần chạy>/report.json
```

**Khung tư duy.** Gate 1 "đạt" khi **quyết định khớp bằng chứng và khớp tiêu chí đã ký trước**. Tiếp tục, Thu hẹp, Cải tiến
thêm, Dừng đều có thể là quyết định đạt. Quyết định không đạt là quyết định mà con số trong report không đỡ được.
Chỉ chọn Tiếp tục khi mọi chỉ số bắt buộc đều đạt.

Ba câu tự vấn trước khi viết: (1) Rủi ro còn lại có chấp nhận được như hiện trạng không? (2) Cần thêm biện pháp nào, tốn
bao nhiêu thời gian? (3) Có phần nào của dự án không nên làm tiếp?

| | **v1** (phút 105–115, TRƯỚC khi nhận thẻ sự cố) |
|---|---|
| Commit ký tiêu chí (message `Sign acceptance criteria`; hash commit, tuỳ chọn) | |
| Hash chốt cổng vòng 1 (8 ký tự lệnh `lab10.checkpoint` in ra, tuỳ chọn) | |
| Mã lần chạy dùng làm bằng chứng | bộ nền, mốc base: ________ · bộ nền với cổng vòng 1 (prepared): ________ |
| Còn dòng "vượt trần" nào trong report? (hàng chờ, chi phí, ROI, trần tiền, pháp lý) | |
| Kho hoặc hãng có số xấu nhất: ____. Nếu chỉ nhìn phân khúc này, quyết định có đổi không? *(Đọc khối "theo kho và hãng" ở cuối output `lab10.eval` / `lab10.grade`, hoặc mục `by_segment` trong `report.json`.)* | |
| Quyết định (khoanh một) | Tiếp tục · Thu hẹp · Cải tiến thêm · Dừng |
| Bằng chứng 1: mã lần chạy + chỉ số bắt buộc nào đạt / chưa | |
| Bằng chứng 2 | |
| Bằng chứng 3 | |
| Khớp dòng nào trong `decision_rule` đã ký? | |
| Nếu Thu hẹp: cắt phần nào, vì sao | |
| Nếu Cải tiến thêm: giả thuyết cụ thể + hạn | |
| Nếu Dừng: bài học ghi lại | |
| Một bằng chứng còn thiếu (thứ bộ nền chưa đo được) | |
| Ngày quyết định lại (trừ khi Dừng) | |
| PIC ký | |

Xong v1 thì lưu và đẩy một bản (sau mốc này không sửa cột v1):

```bash
git add lab10/guards.py lab10/guards_round1.py config/operating_gates.json config/operating_gates.round1.json config/round1.lock templates/form-b-evaluation-gates.md
git commit -m "LAB 10: chốt cổng vòng 1, quyết định v1"
git push -u origin main
```
