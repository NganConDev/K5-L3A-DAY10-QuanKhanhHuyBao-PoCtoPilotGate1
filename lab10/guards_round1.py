"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict


def pre_guard(ctx):
    # Ghim phiên bản chính sách đang hiệu lực để model không tự chọn nhầm phiên bản
    policies = ctx.tools.lookup_policies()
    policy = H.effective_policy(policies, ctx.as_of)
    if policy:
        return Verdict.allow(policy_id=policy["policy_id"])
    return Verdict.allow()


def write_gate(ctx, action):
    # action = {"tool": "issue_refund", "ticket_id":..., "order_id":..., "amount_vnd":..., "payer":..., ...}
    tool = action["tool"]

    # CỔNG 1: Xác minh số tiền hoàn dựa vào DB tracking, không dựa vào số ngày khách tự khai
    if tool == "issue_refund":
        order = ctx.tools.lookup_order(action["order_id"])
        if order is None:
            return Verdict.escalate("không tìm thấy đơn hàng trong DB")
        policies = ctx.tools.lookup_policies()
        policy = H.effective_policy(policies, ctx.as_of)
        if policy is None:
            return Verdict.escalate("không xác định được phiên bản chính sách hiệu lực")
        parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
        db_delay = H.db_delay_days(parcel, ctx.as_of)
        db_amount = H.entitlement_vnd(policy, order, db_delay, parcel.get("delay_cause"))
        if action["amount_vnd"] != db_amount:
            if db_amount == 0:
                return Verdict.escalate(
                    f"model đề xuất hoàn {action['amount_vnd']}đ nhưng DB cho thấy không đủ điều kiện: "
                    f"trễ {db_delay} ngày theo tracking, ngưỡng tối thiểu {policy['late']['min_days_fee']} ngày"
                )
            return Verdict.modify(
                f"sửa số tiền hoàn theo DB: {action['amount_vnd']}đ → {db_amount}đ "
                f"(DB trễ {db_delay} ngày, không phải số khách khai)",
                amount_vnd=db_amount,
            )

    # CỔNG 2: Chỉ ghi lỗi hãng khi DB tracking xác nhận đủ điều kiện (trễ đủ ngày và đúng nguyên nhân)
    if tool == "file_carrier_fault":
        order = ctx.tools.lookup_order(action["order_id"])
        if order is None:
            return Verdict.escalate("không tìm thấy đơn hàng khi kiểm tra lỗi hãng")
        policies = ctx.tools.lookup_policies()
        policy = H.effective_policy(policies, ctx.as_of)
        if policy is None:
            return Verdict.escalate("không xác định được phiên bản chính sách hiệu lực")
        parcel_id = action.get("parcel_id")
        parcel = next((p for p in order["parcels"] if p["parcel_id"] == parcel_id), None)
        if parcel is None:
            parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
        db_delay = H.db_delay_days(parcel, ctx.as_of)
        if not H.carrier_at_fault(policy, parcel, db_delay):
            return Verdict.deny(
                f"DB không xác nhận lỗi hãng: trễ {db_delay} ngày (ngưỡng {policy['late']['min_days_fee']} ngày), "
                f"nguyên nhân={parcel.get('delay_cause')}"
            )

    # CỔNG 3: Xóa customer_note khỏi thông báo gửi hãng để không rò rỉ chữ khách viết (có thể chứa PII)
    if tool == "notify_carrier":
        payload = dict(action.get("payload") or {})
        if "customer_note" in payload:
            payload.pop("customer_note")
            return Verdict.modify(
                "xóa customer_note khỏi payload gửi hãng: chữ khách viết tự do có thể chứa tên/số điện thoại bên thứ ba",
                payload=payload,
            )

    return Verdict.allow()
