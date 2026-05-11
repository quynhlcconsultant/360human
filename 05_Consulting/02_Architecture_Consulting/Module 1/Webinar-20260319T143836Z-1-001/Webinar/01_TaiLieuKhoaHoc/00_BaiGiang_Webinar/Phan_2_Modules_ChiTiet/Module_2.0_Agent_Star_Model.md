# MODULE 2.0: TỔNG QUAN MÔ HÌNH AGENT STAR™ (5 CÁNH SAO)

*(Hướng dẫn lý thuyết nền tảng: 5 phút)*

---

## 🌟 1. Sự Dịch Chuyển Từ Hierarchy Sang Star Model

Rút tỉa từ **Sách AI OrgDesign**, thiết kế tổ chức doanh nghiệp truyền thống dựa trên sơ đồ phân cấp (Hierarchy) từ trên xuống dưới đã trở nên lỗi thời khi áp dụng với AI. Thay vì thiết lập các phòng ban "cứng", chúng ta cần một hệ thống linh hoạt có khả năng tự vận hành và tự điều chỉnh.

Giải pháp của chúng ta là mô hình **AGENT STAR™** — một bản nâng cấp từ mô hình Star Model của Jay R. Galbraith, được tối ưu hóa đặc biệt cho AI-Agent Workforce (Lực lượng lao động AI).

Mô hình này giúp tổ chức xoay quanh 5 cánh sao cốt lõi, làm nền tảng cho mọi thiết lập từ chiến lược đến thực thi.

---

## 🧩 2. Khám Phá 5 Cánh Sao (The 5 Stars)

### 2.1. Strategy (Chiến lược)

- **Nhiệm vụ:** Định vị và thiết lập ngữ cảnh "SSOT" (Single Source of Truth).
- **Ý nghĩa:** AI không thể tự nghĩ ra hướng đi nếu không có Strategy. Cánh sao này đảm bảo mọi quy trình và Agent đều bám sát mô hình kinh doanh cốt lõi (6 Strategy Domains) để tạo ra giá trị.
- **Thực tiễn áp dụng:** Module 2.1 (Biz Model Setup) - Tạo các thư mục SSOT.

### 2.2. Architecture (Kiến trúc)

- **Nhiệm vụ:** Thiết kế hạ tầng và môi trường làm việc số.
- **Ý nghĩa:** Tránh "Context Pollution" (ô nhiễm ngữ cảnh) cho AI bằng cách phân định rõ ràng giữa Khu vực Sản xuất (Workspace/Sprints) và Khu vực Lưu trữ (Warehouse/Knowledge).
- **Thực tiễn áp dụng:** Module 2.2 (Workspace Best Practices) - Khởi tạo mô hình thư mục IPO Factory.

### 2.3. Orchestration (Điều phối)

- **Nhiệm vụ:** Cơ chế giao tiếp và luân chuyển công việc giữa các Agent.
- **Ý nghĩa:** Chuyển từ "Người điều khiển máy" sang "Hệ thống tự gọi nhau" (Cross-calling). Phân tầng các AI Agent thành Node định tuyến (Tier 1) và Node thực thi (Tier 2/3).
- **Thực tiễn áp dụng:** Module 2.3 (Workflow Tiering) - Quản trị chuỗi quy trình Agent nối tiếp nhau.

### 2.4. Capabilities (Năng lực / Giải phẫu Agent)

- **Nhiệm vụ:** Cấu trúc nên một "Nhân sự số" hoàn chỉnh.
- **Ý nghĩa:** Không dùng Prompt chat ngớ ngẩn. Biến AI thành một chuyên gia thực thụ nhờ Giải phẫu 11 thành tố (Anatomy) và nạp Kỹ năng (Skill Loading).
- **Thực tiễn áp dụng:** Module 2.4 (Agentic Org Design - Anatomy) và Module 2.5 (Skill Loading).

### 2.5. Measurement (Đo lường & Kiểm soát chất lượng)

- **Nhiệm vụ:** Đảm bảo tính an toàn và chất lượng đầu ra.
- **Ý nghĩa:** Xây dựng các Quality Gates, Red Team Safeguards, và Circuit Breakers để ngăn chặn AI "ảo giác" hoặc tiêu hao tài nguyên không kiểm soát. Cánh sao này giữ cho hệ thống luôn trong vòng kiểm soát (Blast Radius).
- **Thực tiễn áp dụng:** Tích hợp ngầm vào các bộ Rules Binding và Code of Conduct của Agent.

---
