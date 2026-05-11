# CHƯƠNG 4: CẤU TRÚC BÊN TRONG MỖI PHÒNG BAN (INTERNAL ANATOMY)

---

Mỗi folder (phòng ban) không phải là nơi chứa "văn bản", mà là một **Schema (Cấu trúc dữ liệu)**.

> 💡 **Quan trọng:** Workspace Design bản chất chính là **Database Design & ERP Design**. Chúng ta không thiết kế "Mục lục văn bản", chúng ta đang thiết kế **Data Object Model**.

## 4.1 Bốn Tầng Dữ liệu (4-Layer Data Model)

### Tầng 1: Strategy & Master Data (YAML SSOT)
- **Bản chất:** Các file `YAML` hoặc `JSON` chứa các trường dữ liệu (fields) cấu trúc.
- **Ví dụ:** `Master_Strategy.yaml` có các key: `vision:`, `mission:`, `target_audience:`.
- **Vai trò:** Đây là **SSOT (Single Source of Truth) duy nhất**. Con người KHÔNG đọc file này. Các Agent dùng cấu trúc này để parse data bằng code chuẩn xác 100%.

### Tầng 2: Operations Layer (CSV/Database)
- **Bản chất:** Dữ liệu dạng chuỗi giao dịch liên tục (hàng cột).
- **Medium:** `CSV` cho dự án nhỏ, `Google Sheet` cho cộng tác, `Supabase` cho dự án lớn.
- **Ví dụ:** Revenue_Tracker.csv, Member_Registry (Supabase table), Campaign_Log.csv.

### Tầng 3: Report & View Layer (Markdown)
- **Bản chất:** Các file `.md` hoặc `.html`.
- **Vai trò:** Là **View (Báo cáo hiển thị)** do AI auto-generate từ YAML/CSV. Giúp con người đọc dễ hiểu.
- **Quy trình sửa:** Nếu con người muốn sửa "Markdown" này → nói vào Chat → AI sửa file `YAML` (tầng 1) → Render lại file `Markdown` (tầng 3).

### Tầng 4: Agent Layer
- Agent chuyên trách, đọc YAML, ghi CSV, và giao tiếp CEO.
- Mỗi Zone có assigned Agent (VD: A-07 cho Zone 02_Production).

## 4.2 Bảng Ánh xạ Cụ thể

| Phòng ban | Strategy Layer (YAML/MD) | Operations Layer (CSV/DB) | Agent Layer |
| :--- | :--- | :--- | :--- |
| **01_Governance** | Master_Strategy.yaml, Org_Chart.md, Staffing_Plan.md | Finance/Tracker (CSV/Sheet), Daily_Operations.md | A-05 BizStrat |
| **02_Production** | Product_Roadmap.md, SIPOC.md | Content_Library/, Published_Content (DB/CSV) | A-07 Producer |
| **03_Marketing** | Content_Strategy.md, Marketing_Plan.md | Campaign_Result.md, Data ở nền tảng | A-06 Growth |
| **04_Sales** | Sales_Playbook.md, Pricing.md | Deal_Pipeline (DB/CRM), Revenue_Tracker (CSV) | (Tuỳ) |
| **05_Operations** | Onboarding_Flow.md, SLA.md | Member_Registry (DB/CSV), Ticket_Log (CSV) | A-08 Bot |

> 💡 **Quy tắc Medium:** Tầng Operations chứa dữ liệu sinh ra liên tục. Nếu là bảng phức tạp/nhiều row: lưu thành `CSV`, `Google Sheet`, hoặc Database (`Supabase`). File Markdown `.md` ở Operations Layer CHỈ DÙNG để lưu báo cáo phân tích tổng hợp. Đừng ép dữ liệu Data-lake vào file văn bản.
