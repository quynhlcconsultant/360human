# CHƯƠNG 13-15: STANDARD DOCUMENT LIBRARY (HỆ SINH THÁI BIỂU MẪU SDL)

> *"Không có Biểu mẫu (Template) chuẩn đính kèm cho từng khâu, AI Agent sẽ tự chế ra 100 loại định dạng báo cáo khác nhau và hủy diệt hoàn toàn khả năng Parsing tự động."*

---

## 1. Sự Biến Mất Của Cuốn Từ Điển Cũ

Trước đây (ở phiên bản v1.5), toàn bộ Hệ thống Standard Document Library (SDL) — bao gồm 9 Domain và 92 kiểu loại Biểu mẫu/Văn bản kinh doanh — được liệt kê thô kệch thành một danh sách tĩnh nằm trong file `07_Standard_Document_Library.md`.

Tuy nhiên, kiến trúc **DDWA v2.0+** coi việc lưu trữ Biểu mẫu thành một kho rời rạc là Anti-pattern. Một file Template không có giá trị nếu nó không nằm sát vách với Quy trình dùng đến nó!

Vì vậy, hệ thống **ĐÃ XÓA SỔ** danh sách tĩnh này.

---

## 2. Điểm Đến Thực Sự Của Kho SDL Hiện Tại

Toàn bộ hệ sinh thái biểu mẫu SDL đã được chẻ nhỏ, đóng gói lại dưới tiền tố `TMPL_` (Template Mẫu) và `GDL_` (Guideline Hướng dẫn), sau đó **nhúng trực tiếp bằng xương bằng thịt** vào siêu mô hình Workflow Thực thi: **FW-01_AI_Workflow_Design**.

👉 **TỌA ĐỘ TRUY CẬP HIỆN TẠI:**
Toàn bộ biểu mẫu vận hành đã nằm tại: `c:\commandcenter\02_AI_Hub\05_Framework_Hub\FW-01_AI_Workflow_Design\`

**Bản đồ dải Biểu mẫu (SDL) được phân hóa theo 5 Nhịp đập:**

### 🛠️ Lõi 1: Dải Biểu mẫu Phase 1_Biz (Chiến lược)

- Nơi lưu trữ: `FW-01...\01_Phase_1_Biz\resources\`
- Các tài liệu lõi:
  - `01A_STRATEGY.md` (Tầm nhìn doanh nghiệp)
  - `01B_USER_PERSONA.md` (Chân dung khách hàng)
  - `01H_STRATEGY_BRIEF.md` (Bàn giao Chiến lược)
  - (Tổng cộng 9 Biểu mẫu Strategy Handoffs).

### 🛠️ Lõi 2: Dải Biểu mẫu Phase 2_Discovery (Sản phẩm)

- Nơi lưu trữ: `FW-01...\02_Phase_2_Discovery\resources\`
- Các tài liệu lõi:
  - `TMPL_HANDOFF_PACKAGE.md` (Túi hồ sơ Bàn giao)
  - `TMPL_PM_SIGNOFF.md` (Ấn định Nghiệm thu của PM)
  - `GDL_DEV_READING.md` (Mồi Đọc dành cho Coder)

### 🛠️ Lõi 3: Dải Biểu mẫu Phản Biện RRIT (QG0)

- Nơi lưu trữ: `FW-01...\025_Phase_25_RRIT\resources\`
- Danh mục:
  - Báo cáo phản biện tàn khốc (`GDL_RRIT.md` - Yêu cầu Đảo chiều Ảo giác).

### 🛠️ Lõi 4 & 5: Dải Biểu mẫu Delivery & Finish

- Nơi lưu trữ: `FW-01...\03_Phase_3_Delivery\` và `\04_Phase_4_Finish\`
- Danh mục: Các Biểu mẫu Tự động sinh Test Case, Code Checklist và Audit Form Môi trường.

---

## 3. Quy Tắc Kế Thừa SDL

Bất cứ khi nào bạn (Hoặc một AI Agent) cần khởi tạo một tài liệu mới (Ví dụ: Soạn PRD cho tính năng A), cấm tuyệt đối việc tạo file trống và tự vắt óc viết.
Bắt buộc phải lội vào cấu trúc `FW-01` tương ứng, Copy nội dung file `TMPL_` phù hợp ra thư mục SPRINT của mình, và **điền khuyết Data vào chỗ trống**. Đó là đỉnh cao của sự Thất truyền.
