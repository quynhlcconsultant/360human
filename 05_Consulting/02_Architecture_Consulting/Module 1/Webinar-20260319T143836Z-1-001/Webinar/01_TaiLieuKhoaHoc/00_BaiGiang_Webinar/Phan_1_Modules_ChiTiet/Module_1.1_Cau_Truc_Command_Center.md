# MODULE 1.1: CẤU TRÚC THƯ MỤC COMMAND CENTER

*(Hướng dẫn thực hành Live: 10 phút)*

---

## 🧐 1. Lý Thuyết: Tổ chức file là Tổ chức "Bộ Não" cho AI

- Bất cứ ai làm việc với AI sâu đều nhận ra: **Quản trị Prompt là sai lầm.** Quản trị **Dữ liệu Context (Ngữ cảnh)** mới là chân lý.
- Command Center không chỉ là nơi lưu file, nó là **Sơ đồ tổ chức nhân sự (Org Chart)** của doanh nghiệp phiên bản AI. Để AI làm việc như một nhân sự cao cấp, kiến trúc cần phải rõ ràng:

### 3 Trụ Cột + 3 Không Gian Đặc Biệt

1. **Root Folder (Sảnh Chờ Công Ty):** Nơi chứa các file chỉ dẫn tổng quan dùng chung cho toàn bộ phòng ban mà không phụ thuộc vào dự án nào. Bao gồm: **Cơ cấu tổ chức (Org Structure), Chiến lược chung (General Strategy), Bối cảnh kinh doanh (Biz Context)** và các file Định danh AI (`00_AGENT_INDEX`, `01_ONBOARDING_ASSISTANTS`). Đây là tài liệu "nhập môn" để bất cứ Agent nào bật lên cũng hiểu: Tôi là ai, công ty bán gì, và đồng nghiệp của tôi nằm ở đâu.
2. **02_AI_HUB (Trường Đào Tạo Đại Học):** Nơi chứa thư viện Workflows, Skills, và Profile của các Agent. Agents được "huấn luyện" ở đây.
3. **01_OPERATION (Phòng Làm Việc/Vận Hành):** Nơi làm việc hàng ngày của các phòng ban AI (Marketing, Code, Sale). Chứa Job Description (JD), CV, Tech Notes, và To-do list cá nhân của Agent.
4. **03_MY_PROJECTS (Cấu Trúc Ma Trận):** Nơi quản lý các dự án. Ở đây áp dụng cấu trúc Matrix (Dự án có nhiều phòng ban, hoặc phòng ban có nhiều dự án). AI sẽ dùng **Mapping File (Sơ đồ liên kết)** để biết cần gọi Agent nào từ phòng ban nào vào giải quyết dự án này.
5. **Sprint Folder (Bãi Đáp Thực Thi):** Mỗi khi giao 1 nhiệm vụ cho AI, hãy tạo 1 thư mục `Sprint`. Đây là "chiếc hộp cách ly" để AI thực thi công việc (nghiên cứu, viết nháp, code). Sau khi hoàn thành, Hàng hóa (kết quả) mới được mang đi "Merge/Setup" vào đúng vị trí dự án. Xong xuôi, Sprint này có thể lưu trữ (Archive) và dọn dẹp sạch sẽ.
6. **Không Gian Lõi - Task OS (Trung Tâm Điều Hành):** Nơi chứa hệ thống Code (`Python`) để tự động quét toàn bộ file `ToDo.md` từ tất cả dự án và phòng ban, sau đó đồng bộ hóa (sync) và ném lên một `Dashboard HTML` trực quan. Giúp Sếp giám sát và điều phối bầy đàn AI thời gian thực mà không cần mở từng thư mục!

---

## 🛠️ 2. Kịch Bản Demo Live

**Mục tiêu:** Mở rộng (Expand) các thư mục mẫu để học viên thấy được hình hài của một Tổ chức Nhân sự AI.

**Bước 1:** Khởi động từ **Root**. Mở nhanh các file Onboarding mẫu để học viên thấy sức mạnh của việc "AI tự đọc tài liệu công ty".
**Bước 2:** Lướt qua **AI HUB** (Trường Đào Tạo) và **OPERATION** (Phòng Làm Việc). Giải thích sự khác biệt giữa nơi đào tạo năng lực và nơi thực thi tác vụ.
**Bước 3:** Bẻ lái sang **PROJECTS** & **SPRINT FOLDER**. Giải thích mô hình Ma trận và cách dùng Sprint để "Nhốt AI vào một cái hộp" - giúp AI tập trung 100% vào task hiện tại mà không làm rối bộ máy.
**Bước 4 (Trùm Cuối):** Mở thư mục **`_task-os`** và bấm chạy file `Python`, sau đó mở trang `HTML Dashboard`. Cho học viên thấy tất cả các file `ToDo.md` rải rác khắp gốc rễ công ty giờ đây hội tụ lại thành một Bảng Điều Khiển Tổng siêu cấp!

---

## 📦 3. Khung Giao Diện Demo (Sếp dùng để chiếu)

*Đây là cấu trúc thư mục giả định để sếp giải thích. Sếp trỏ chuột vào đâu thì đọc lời việt sub ở đó.*

```text
Demo_Taskflow_Enterprise/
├── _task-os/                    👉 [TRÙM CUỐI] Hệ thống Python tự quét Todo.md hiển thị lên Dashboard HTML!
├── 00_AGENT_INDEX.md            👉 Sơ đồ tổ chức phòng ban AI toàn công ty
├── 01_ONBOARDING_ASSISTANTS.md  👉 Chào sân mọi Agent (Văn hóa, Cách xưng hô)
├── 02_BIZ_CONTEXT_STRATEGY.md   👉 Bối cảnh Kinh doanh & Chiến lược chung (Dùng chung cho mọi ban)
├── 03_ORG_STRUCTURE.md          👉 Cơ cấu tổ chức nhân sự toàn doanh nghiệp
├── 01_OPERATION/                👉 Phòng làm việc
│   ├── Phong_Marketing/         👉 JD, Todo list của Team MKT AI
│   └── Phong_Dev/               👉 Tech Notes của Team Code AI
├── 02_AI_HUB/                   👉 Trường Đào Tạo
│   ├── Workflows/               👉 Các kịch bản có thứ tự (Vd: Tuyển Dụng)
│   └── Skills/                  👉 Kỹ năng cụ thể (Viết báo cáo, Gọi API)
├── 03_My_Projects/              👉 Dự án Thực Tế (Cấu trúc Ma Trận)
│   ├── Du_an_CRM/             
│   │   ├── Mapping_File.md      👉 Sơ đồ gọi AI từ các phòng ban vào làm dự án
│   │   ├── ToDo.md              👉 Bắt buộc phải có để Task OS quét lên Dashboard
│   │   └── SP-260310-Moi/       👉 SPRINT FOLDER: Cái Hộp để AI thực thi task này
│   └── Du_an_App/             
```

---

### 💡 Bài Học Rút Ra Từ Cấu Trúc Này:

1. **Tổ chức như một "Tòa Nhà Văn Phòng":** Ở sảnh lớn (Root) có Sơ đồ tổ chức, bất kỳ con AI nào bước vào là biết công ty đang làm gì. `AI HUB` là trường đại học để huấn luyện. `OPERATION` là văn phòng làm việc tập trung.
2. **Quyền năng của MAPPING FILE:** Trong dự án CRM, có thể cần AI từ ban MKT và AI từ ban Dev. Chúng ta không copy paste dữ liệu lộn xộn, mà dùng Mapping File để "triệu hồi" đúng người, đúng việc.
3. **Cái Hộp Sprint:** Khi giao task, hãy 'nhốt' con AI vào `Sprint Folder`. Nó sẽ lấy thông tin, nghiên cứu, brainstorm và code trong đúng ranh giới đó. Xong việc, kết quả được Merge vào dự án chính, còn Sprint rác sẽ bị dẹp đi.
4. **Hệ Điều Hành Tác Vụ (Task OS):** Chúng ta không đi tìm việc trong từng dự án nữa. Với Script Python và một Dashboard HTML, Sếp chỉ việc ngồi nhìn dòng chảy công việc (từ mọi `ToDo.md` rải rác) tự động chạy ngược về bộ điều khiển trung tâm! **Kết quả:** Quản trị bầy đàn AI (AI Workforce) hoàn hảo!
