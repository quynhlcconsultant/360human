# MODULE 2.2: KIẾN TRÚC KHÔNG GIAN SỐ - MÔ HÌNH IPO FACTORY (TỪ CHƯƠNG 22)
*(Hướng dẫn thực hành Live: 10 phút)*

---

## 🧐 1. Lý Thuyết: Tổ chức thư mục như một Nhà Máy Sản Xuất
- Một thiết kế tổ chức xuất sắc trên giấy sẽ thất bại nếu không gian làm việc số (folder, file) là một mớ hỗn độn. Nếu để file nháp và chiến lược chung một chỗ, AI sẽ đọc chéo dữ liệu, học sai ngữ cảnh và "bịa chuyện".
- Rút tỉa từ **Chương 22 - Sách AI OrgDesign**, chúng tôi áp dụng mô hình **IPO Factory (Input - Process - Output)**. Không gian dự án được chia làm 2 phân khu độc lập hoàn toàn:

  1. **Khu Vực Sản Xuất (WORKSPACE_SPRINTS):** Đại diện cho "Process". Là xưởng làm việc thực tế nơi các Task đang chạy (WIP). Cấu trúc cực kỳ phẳng, file nháp, code tạm vứt hết vào đây.
  2. **Kho Lưu Trữ Thành Phẩm (WAREHOUSE_STORAGE):** Chia theo phòng ban (Marketing, Product, Finance). Nơi chứa nguyên liệu đầu vào (Input) và thành phẩm cuối cùng (Output). Cấu trúc tĩnh, sạch sẽ.

---

## 🛠️ 2. Vòng Đời Chuyển Giao (The Handoff Lifecycle)

**Mục tiêu:** Mở Terminal và diễn giải dòng chảy của một tài liệu.

1. **Khởi tạo Sprint (Process):** Tạo thư mục dạng `SP-260310-ContentPlan` trong `WORKSPACE_SPRINTS`. Giao việc cho Agent.
2. **Lấy Input:** Agent tự động vào `WAREHOUSE_STORAGE/Marketing/00_Inputs` để lấy File Định Lượng Personas.
3. **Giao Hàng (Output):** Sau khi Sprint chạy xong, "chiết xuất" file Content Plan sạch nhất, **MOVE** sang `WAREHOUSE_STORAGE/Marketing/01_Finished_Outputs`.
4. **Dọn dẹp:** Xóa thư mục nháp ở Sprint đi.

---

## 📦 3. Framework Chia Folder Thực Chiến (Sếp show trên màn hình)

*Sử dụng mô hình bên dưới làm Slide/Hình ảnh minh họa trực quan.*

```text
📁 COMMAND CENTER (Root Kiến trúc chuẩn)
│
├── 🤖 00_AGENT_HQ/                     (Phòng ngủ của AI)
│   └── A_root_Marketer/               👉 Cấu hình, Job Description, Prompt
│
├── ⚙️ 01_WORKSPACE_SPRINTS/            (Phân Xưởng Sản Xuất)
│   ├── SprintLog.md                   👉 Sổ cái Tracking tiến độ nhà máy
│   └── SP-260310-01-BizModel/         👉 Task đang chạy (File nháp, Think-out-loud)
│
└── 🏛️ 02_WAREHOUSE_STORAGE/           (Kho Lưu Trữ Thành Phẩm - SSOT)
    ├── A_Strategy_and_Market/         👉 Kho Đầu Não
    ├── B_Product_and_Tech/            👉 Kho Sản Phẩm
    │   ├── 00_Inputs_References/      (Đầu vào nhận từ Strategy)
    │   └── 01_Finished_Outputs/       (Đầu ra: PRD, Architecture đã chốt)
    └── C_Marketing_and_Sales/         👉 Kho Branding & Tăng trưởng
```

---
> **BÀI HỌC CỐT LÕI:** 
> Tại sao AI của anh em lại hay cầm râu ông nọ cắm cằm bà kia? Vì anh em cho nó đọc cả file nháp lẫn file chốt! Ở mô hình IPO Factory, AI đi làm ở Phân xưởng Sprint. Nó lấy nguyên liệu Input từ Kho B, xử lý xong nó cất thành phẩm sang Kho C. Nó không thể đọc nhầm, không thể ghi đè file gốc. Gọn gàng, truy vết sắc lẹm, và bảo vệ 100% ngữ cảnh tri thức của doanh nghiệp (Single Source of Truth)!
