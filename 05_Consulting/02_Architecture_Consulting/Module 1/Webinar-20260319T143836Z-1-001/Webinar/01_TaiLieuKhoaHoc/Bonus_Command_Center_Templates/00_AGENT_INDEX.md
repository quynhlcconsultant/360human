# 🧭 00_AGENT_INDEX (Bản Đồ Agent)

<!-- 
💡 HƯỚNG DẪN DÀNH CHO BẠN (Xóa sau khi đọc xong):
- File này giúp AI biết trong máy bạn đang có những "nhân viên" (Agent) nào.
- Cách dùng: Sửa thông tin trong bảng bên dưới cho phù hợp với các Agent bạn tạo ra bằng tính năng "Add Custom Agent" trên Antigravity.
-->

**Danh sách các Trợ lý AI (AI Agents) đang làm việc trong Command Center của tôi.**
*Mọi AI đọc file này để tự định vị bản thân và biết cách phân luồng công việc.*

---

## 1. Danh sách Agents hiện tại

| ID   | Tên Agent                 | Vai trò tóm tắt                       | Khi nào nên dùng?                              | Lệnh gọi     |
| ---- | ------------------------- | ------------------------------------- | ---------------------------------------------- | ------------ |
| A-01 | **Thư Ký**                | Ghi nhận task, tóm tắt họp, nhắc việc | Khi cần ghi chú hoặc tìm lại thông tin cũ      | `/secretary` |
| A-02 | **Chuyên Viên Nội Dung**  | Viết bài Facebook, Tiktok, Blog       | Viết content theo chuẩn giọng điệu thương hiệu | `/content`   |
| A-03 | **Chuyên Viên Phân Tích** | Đọc Excel, CSV, làm báo cáo           | Khi cần xử lý số liệu cuối tháng               | `/data`      |

<!-- 💡 Dòng trên là ví dụ, bạn hãy thay bằng các Agent thực tế của bạn -->

## 2. Quy tắc Phối hợp (Swarm Rules)

- **Agent Thư Ký** có quyền thu thập ToDo từ tất cả mọi thư mục.
- Nếu **Chuyên Viên Nội Dung** cần số liệu để viết bài, phải yêu cầu user cấp file báo cáo do **Chuyên Viên Phân Tích** tạo ra. Không được tự bịa số liệu.
