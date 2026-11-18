# Danh sách GitHub Issues cho nhóm QuanKhanhHuyBao (Khối 1 & Khối 2)

Hệ thống issues được thiết kế riêng cho nhóm **Quân - Khánh - Huy - Bảo** (Lớp L3A) thực hiện bài **LAB 10 · From PoC to Pilot (Gate 1)**.

---

## 📌 Cơ cấu 5 Issues

| File Issue | Tiêu đề Issue | Người phụ trách | Vai trò | Trọng tâm công việc |
|---|---|---|---|---|
| [`00-epic-block1-2-overview.md`](00-epic-block1-2-overview.md) | **[EPIC] Điều phối & Tiến độ Vòng 1 (Khối 1 & Khối 2)** | Cả nhóm | Điều phối | Tổng quan tiến độ, Checkpoint 1, 2, 3A, 3B, 3C |
| [`01-khanh-gate-engineer-1.md`](01-khanh-gate-engineer-1.md) | **[Member 1 - Khánh] Kỹ sư cổng 1 (Lead Gate Engineer)** | Khánh (@NganConDev) | Kỹ sư cổng 1 | Offline metric (1.3), Ký tiêu chí (A5), Base eval (2.1), Code guards (`guards.py`), Checkpoint |
| [`02-quan-gate-engineer-2.md`](02-quan-gate-engineer-2.md) | **[Member 2 - Quân] Kỹ sư cổng 2 (QA & Trace Engineer)** | Quân | Kỹ sư cổng 2 | Trace debug `T-002@55` (2.2), Tránh data leakage (2.7), Behavioral test `--adhoc` (2.8) |
| [`03-huy-product-business.md`](03-huy-product-business.md) | **[Member 3 - Huy] Sản phẩm và kinh doanh (Product & Business Lead)** | Huy | Sản phẩm & Kinh doanh | Mục tiêu hệ thống (1.1), `acceptance_criteria.json` (1.6), Data Map & Drift (2.3), Cổng kinh doanh (2.9) |
| [`04-bao-operations-legal.md`](04-bao-operations-legal.md) | **[Member 4 - Bảo] Vận hành và pháp lý (Operations & Legal Lead)** | Bảo | Vận hành & Pháp lý | Mục tiêu stakeholder (1.2), Telemetry prod (1.4), HAZOP v1 (2.4), Checklist 9 nhóm (2.4), Cổng Ops/Legal & Runbook (2.10) |

---

## 🚀 Cách đưa lên GitHub Repo

### Cách 1: Tự động qua Python Script (Khuyến nghị - Nhanh nhất)
Chạy script tự động tạo đầy đủ labels màu và 5 issues với 1 lệnh duy nhất:
```bash
python3 scripts/create_github_issues.py <GITHUB_PERSONAL_ACCESS_TOKEN>
```
*(Token chỉ cần quyền `repo` hoặc `issues`)*

### Cách 2: Tạo thủ công qua giao diện GitHub
1. Vào repo: https://github.com/NganConDev/K5-L3A-DAY10-QuanKhanhHuyBao-PoCtoPilotGate1/issues
2. Bấm **New issue**.
3. Copy tiêu đề (dòng đầu `# ...`) và nội dung từ các file trong thư mục [`docs/issues/`](file:///Users/nguyennamkhanh/Documents/AI In Action/AI20K_Lab/K5-L3A-DAY10-QuanKhanhHuyBao-PoCtoPilotGate1/docs/issues/) dán vào.
