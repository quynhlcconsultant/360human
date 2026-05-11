# Chương 22: Kiến Trúc Không Gian Làm Việc Số (Digital Workspace) - Mô Hình IPO Factory

> "Một thiết kế tổ chức xuất sắc trên giấy sẽ thất bại nếu không gian làm việc số (thư mục, file, hệ thống lưu trữ) là một mớ hỗn độn. Kiến trúc file/folder cũng chính là kiến trúc tổ chức (Conway's Law)."

Trong quá trình tổ chức lực lượng lao động AI (AI Workforce) kết hợp với con người, cách chúng ta thiết kế bộ rễ thư mục (Directory Tree) quyết định tốc độ luân chuyển thông tin. Nếu thư mục chỉ được sắp xếp theo cảm tính hoặc "lưu trữ tĩnh", các AI Agent sẽ không thể tự động hóa việc tìm kiếm Input hay lưu trữ Output.

Do đó, Antigravity áp dụng **Mô hình IPO (Input - Process - Output) Factory** để kiến trúc không gian làm việc số nội bộ.

---

## 22.1. Tư duy Nhà Máy (The Factory Mindset)

Trong mô hình này, mỗi phòng ban (ví dụ: Marketing, Product, Finance, HR) không phải là một "thư mục chứa tài liệu", mà là một **Đơn vị Sản xuất (Production Unit)**. 

Hệ thống được vận hành bởi 3 yếu tố cốt lõi:
1. **Con người / Agent (Role / Who)**: Là công nhân hoặc quản đốc thực thi trên dây chuyền sản xuất (Ví dụ: `A-5B-Marketer`, CPO, CMO).
2. **Process (Sprints / Workspace)**: Là phiên làm việc thực tế, nơi các Role xử lý nguyên liệu thô (Input) thành thành phẩm (Output).
3. **Storage (Kho Hàng Hóa)**: Nơi chứa nguyên liệu đầu vào (Ví dụ: Insights, Market Research) và nơi cất trữ thành phẩm cuối cùng (Cột mốc, PRD, Ads Copy).

Việc thiết kế folder cần đảm bảo chúng dễ dàng được quản lý, chuyển giao (Handoff) và tìm thấy khi cần thiết giống như quản trị các dây chuyền sản xuất thật.

---

## 22.2. Kiến Trúc 2 Cụm Lớn: Workspace và Warehouse

Để khắc phục tình trạng file nháp, file kịch bản chạy (scripts), và file chiến lược chốt lưu lẫn lộn, toàn bộ không gian dự án được chia làm 2 phân khu độc lập:

### Khu 1: Khối Sản Xuất (01_WORKSPACE_SPRINTS)
Đây là "công xưởng" diễn ra các hoạt động thực thi hàng ngày.
- **Đặc điểm**: Vì team vận hành (Human) thường rất mỏng (1 CEO hoặc vai người), các folder Sprint ở đây phải **rất phẳng (Flat)** để cực kỳ dễ theo dõi.
- **Cách đánh tên**: Đánh ID duy nhất theo thời gian và tên task (Ví dụ: `SP-260310-01-MKT_Plan/`).
- **Nội dung**: File nháp, Think-out-loud của AI, script code tạm, file data raw. Mọi thứ trong này đều mang tính "đang xử lý" (WIP).
- **Hệ thống Tracking**: Một file `SprintLog.md` làm sổ cái trung tâm (Master Ledger) để log trạng thái tất cả các Sprints.

### Khu 2: Kho Lưu Trữ Thành Phẩm (02_WAREHOUSE_STORAGE)
Đây là các kho lưu trữ có cấu trúc tĩnh, chia theo Phòng ban (Departmentalization) đúng như sơ đồ tổ chức.
- **Đặc điểm**: Chỉ chứa "Hàng hóa" đã hoàn thiện, sạch sẽ, chuẩn chỉ.
- **Cấu trúc**: Phân rã thành 5-6 khối như: *A_Strategy_and_Market, B_Product_and_Tech, C_Marketing_and_Sales, D_Operations, E_Finance_HR*.
- **Phân luồng trong mỗi Kho**: Mỗi phòng ban lại chia thành 2 khu vực:
  - `00_Inputs_References/`: Chứa các bản thiết kế, Handoff document nhận từ phòng ban khác.
  - `01_Finished_Outputs/`: Chứa sản phẩm đã đóng gói của chính phòng ban đó (đã gắn tag ID của Sprint tạo ra nó).

---

## 22.3. Dòng Chảy Giá Trị Kép (Value Chain Flow) và Sự Chuyển Giao (Handoffs)

Thiết kế này hỗ trợ hoàn hảo cho dòng chảy từ Abstract (Tư duy) đến Concrete (Thực thi). Ví dụ về luồng giá trị khép kín:

1. **Giai đoạn Strategy**: 
   - *Input*: Market Research, User Feedback. 
   - *Process (Sprint)*: CEO & Strategist Agent phân tích. 
   - *Output*: Business Strategy, Product Vision (lưu vào Kho Strategy).
2. **Giai đoạn Tỏa Nhánh**:
   - Master Strategy này được làm thành **Handoff Document** và gửi vào nhánh Đầu vào (Input) của Kho Product, Kho Marketing, và Kho Finance. Điều này châm ngòi cho các dự án con.
3. **Giai đoạn MKT/Sales**:
   - *Input*: Cầm Master Strategy.
   - *Process (Sprint)*: Lên Content Strategy, Ads Copy.
   - *Output*: Leads, Landing Page Copy (lưu vào Kho MKT).

---

## 22.4. Lợi Ích Của Mô Hình IPO Workspace

- **Tính Định Vị (Traceability)**: Bất kỳ một tài liệu thành phẩm nào trong Kho (Warehouse) cũng đều có thể truy vết ngược lại Sprint nào đã tạo ra nó (thông qua YAML ID).
- **Tránh Ô Nhiễm Ngữ Cảnh (Context Pollution)**: AI Agent khi thực thi nhiệm vụ sẽ không bị quét nhầm vào các file nháp hay quá trình tư duy ngổn ngang của các Sprint cũ. Giao thức chỉ cho phép Agent lấy Input từ phân vùng Warehouse.
- **Hỗ Trợ Ráp Nối Agile**: Khi có Agent mới được bổ nhiệm, Agent đó chỉ cần được trỏ vào đúng Khu vực 00_Inputs_References của phòng ban mình phụ trách là có đủ bộ ngữ cảnh sản xuất mà không cần hỏi lại Human.

Mô hình IPO Folder Architecture khép lại khoảng cách giữa Lập quy hoạch chiến lược (Org Design Theory) và Quản trị vận hành thực tế (Execution & DevOps).
