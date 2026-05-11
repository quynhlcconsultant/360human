---
doc_id: DOC-PRJ-EVENT01-BONUS-TEMPLATE
template_version: 2.0.0
---

# 🎁 Tặng phẩm: Template Xây Dựng Không Gian Làm Việc Số (Digital Workspace)

Đây là khung cấu trúc (Framework) tiêu chuẩn giúp bạn quản trị **Hệ thống AI Agent cá nhân** theo mô hình Command Center chuyên nghiệp nhất, đúc kết từ hệ thống thực chiến của Hoàng Đức Minh.

## 📁 1. Cấu Trúc Thư Mục Tiêu Chuẩn (Folder Hierarchy)
Sức mạnh của AI nằm ở **ngữ cảnh** (Context). Việc có một cấu trúc thư mục rõ ràng giúp bạn (và cả AI) dễ dàng tìm kiếm và nạp đúng thông tin. Mô hình Command Center v2 được chia làm 6 phân khu lõi:

```text
My_Command_Center/
├── _task-os/                    👉 [TRÙM CUỐI] Hệ thống Task OS quét Todo.md hiển thị Board
├── 00_AGENT_INDEX.md            👉 Sơ đồ tổ chức phòng ban AI toàn công ty (Org Chart)
├── 01_ONBOARDING_ASSISTANTS.md  👉 Hồ sơ Onboarding, Cách xưng hô, Văn hóa
├── 02_BIZ_CONTEXT_STRATEGY.md   👉 Bối cảnh Kinh doanh & Chiến lược chung 
├── 03_ORG_STRUCTURE.md          👉 Cơ cấu tổ chức nhân sự toàn doanh nghiệp
├── 01_OPERATION/                👉 ĐỊA ĐIỂM 1: Phòng Làm Việc / Vận Hành (Chứa JD, Todo list cá nhân)
├── 02_AI_HUB/                   👉 ĐỊA ĐIỂM 2: Trường Đào Tạo AI (Chứa Skills, Workflows)
└── 03_My_Projects/              👉 ĐỊA ĐIỂM 3: Kho Dự Án Thực Tế (Thiết kế Ma trận)
```

## 🧠 2. Hệ Thống 6 Phân Khu Quản Trị Tối Thượng

1. **Root Folder (Sảnh Chờ Công Ty):** Nơi chứa `00_AGENT_INDEX.md`, `01_ONBOARDING_ASSISTANTS.md`, `02_BIZ_CONTEXT_STRATEGY.md`, `03_ORG_STRUCTURE.md`. Bất cứ Agent nào làm việc đều phải đọc thư mục này để hiểu "Linh hồn doanh nghiệp".
2. **`02_AI_HUB` (Trường Đào Tạo Đại Học):** Nơi chứa thư viện Workflows (Kịch bản hành động từ 1 -> 5) và Skills (Tư duy, framework). Agents được "huấn luyện" ở đây.
3. **`01_OPERATION` (Phòng Làm Việc/Vận Hành):** Nơi làm việc hàng ngày của các ban bệ AI (Marketing, Code, Sale). Chế độ công tác của tác Agent.
4. **`03_MY_PROJECTS` (Cấu Trúc Ma Trận):** Nơi quản lý dự án. Dùng **Mapping File** để triệu hồi AI từ các phòng ban khác nhau vào chung một dự án.
5. **Sprint Folder (Bãi Đáp Thực Thi):** Bên trong mỗi Dự án, hãy tạo 1 thư mục `Sprint`. Đây là "chiếc hộp cách ly" để AI thực thi task. Xong việc thì Merge, sau đó dọn dẹp sạch sẽ để tránh ô nhiễm context.
6. **Không Gian Lõi - Task OS (`_task-os`):** Hệ thống Python tự quét toàn bộ file `ToDo.md` rải rác và đồng bộ hóa lên 1 Dashboard duy nhất. Giám sát bầy đàn AI thời gian thực!

## ⚙️ 3. Phân Biệt Sức Mạnh (Agents vs Workflows vs Skills)
Khi setup, đừng biến 1 con AI thành "God Mode" (biết tuốt). Hãy chia nhỏ:
- **🕵️ AI Agent (Người điều phối):** Nằm ở Root/Operation. (VD: Thư ký, GĐ Marketing).
- **🚀 Workflow (Kịch bản/Quy trình):** Trình tự các bước 1-2-3 để hoàn thành 1 task. Lưu ở `AI_HUB`.
- **🛠️ Skill (Kỹ năng, Công cụ):** Khả năng thực thi 1 nhiệm vụ hẹp, tư duy phân tích. Lưu ở `AI_HUB`.

---
> **⚡ Bắt đầu thực hành ngay:** Hãy tạo 1 thư mục trống trên máy tính và copy bộ `Bonus_Command_Center_Templates` vào. Tùy chỉnh file `01_ONBOARDING_ASSISTANTS.md` đầu tiên để mô tả công ty bạn nhé!
