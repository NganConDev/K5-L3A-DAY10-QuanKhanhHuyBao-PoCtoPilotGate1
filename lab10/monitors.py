"""★ FILE ĐỘI SỬA (2/3): chỉ số theo dõi (monitor). Thêm ÍT NHẤT MỘT chỉ số bắt được sự cố của bàn.

Mỗi monitor nhận danh sách trial (KHÔNG có nhãn đúng/sai, giống production) và trả về một số.
Một trial = {"ticket_id", "seed", "day", "status", "amount_vnd", "ticket", "events", "ledger", "faults", "outbound",
             "arrive_min", "warehouse", "cost_vnd", "review_kind", "queue_wait_min", "queue_stuck"}
  "day"            một ngày vận hành giả lập: các ticket cùng "day" và cùng "seed" chạy nối nhau trên cùng một sổ cái
  "arrive_min"     phút ticket tới trong ca (0..480)          "warehouse"   kho của đơn
  "cost_vnd"       tiền LLM + nền tảng đã tốn cho ticket      "review_kind" None / "escalated" (trợ lý chuyển người) /
  "queue_wait_min" số phút chờ người duyệt (None nếu không vào hàng chờ)     "recheck" (nhân viên tự kiểm lại)
Chỉ số có thể là kỹ thuật (tỉ lệ model đè số trong ticket lên DB), vận hành (số ca cần người trong giờ đông nhất),
hay kinh doanh (tỉ lệ ticket trợ lý đọc xong vẫn phải chuyển người).

lab10.grade kiểm: monitor chạy không lỗi, và giá trị trên gói sự cố khác giá trị trên bộ nền,
tức là monitor "sáng đèn" khi sự cố xảy ra.
"""


def escalation_rate(trials):
    return sum(t["status"] == "escalated" for t in trials) / max(1, len(trials))


def multi_carrier_order_rate(trials):
    """Tỉ lệ ticket có đơn tách kiện từ nhiều hãng vận chuyển khác nhau.

    Sáng đèn khi sự cố S6: gói S6 có nhiều đơn tách kiện nên tỉ lệ cao hơn hẳn bộ nền.
    Dữ liệu: event type='tracking' trong trial.events, field 'parcels'[].carrier_id.
    Điểm mù: không thấy khi nhiều kiện nhưng tất cả cùng một hãng.
    """
    multi = 0
    for trial in trials:
        for ev in (trial.get("events") or []):
            if ev.get("type") != "tracking":
                continue
            parcels = ev.get("parcels", [])
            carrier_ids = {p.get("carrier_id") for p in parcels if p.get("carrier_id")}
            if len(carrier_ids) > 1:
                multi += 1
            break
    return multi / max(1, len(trials))


MONITORS = {
    "escalation_rate": escalation_rate,     # có sẵn; KHÔNG tính là metric mới của đội
    "multi_carrier_order_rate": multi_carrier_order_rate,
}
STARTER_MONITORS = ("escalation_rate",)
