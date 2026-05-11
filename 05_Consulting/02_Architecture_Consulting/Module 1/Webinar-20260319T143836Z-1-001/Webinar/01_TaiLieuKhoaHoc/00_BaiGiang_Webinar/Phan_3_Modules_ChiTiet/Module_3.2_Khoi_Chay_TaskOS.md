# MODULE 3.2: KHỞI CHẠY TASK OS SERVER TRÊN ANTIGRAVITY (QUÀ TẶNG)

*(Hướng dẫn thực hành Live: 10 phút)*

---

## 🧐 1. Ý Nghĩa Của Món Quà (Bộ Source Code `task_server`)

- Thay vì AI quản lý công việc ngẫu nhiên, TaskOS biến AI thành một "Quản gia" có bộ nhớ dùng chung. Các AI có thể tạo, gọi, sửa, hoàn thành danh sách công việc cùng nhau qua một cổng API (Máy chủ mini).
- TaskOS cho phép AI giao tiếp qua công nghệ `REST API` để thay đổi file JSON (`tasks.json`). Tránh tình trạng file công việc bị xung đột.

---

## 📦 2. Câu Lệnh Kích Hoạt Server (Sếp copy vào Terminal)

*Quá trình này Sếp demo từ A-Z. Giả sử Sếp đã tải File Quà tặng (TaskOS) vào thư mục tên `_task-os`.*

```bash
# Bấm phím khởi chạy Server (Localhost)
cd _task-os
python task_server.py
```

*Sau đó chép câu lệnh này vào Khung Chat cho AI:*

```text
Thư ký ơi, Sắp có dự án ra mắt sản phẩm A. Hãy liệt kê cho tôi 3 đầu mục công việc thiết yếu. Sau đó, Tự Mày gọi API của TaskOS ở địa chỉ http://localhost:8000 để tạo 3 Task đó vào hệ thống cho tôi.
```

---

> **BÀI HỌC CỐT LÕI:**
> Đây chính là tương lai. AI giờ đóng vai trò là Nút thắt Vận Hành chứ không còn là con chatbot chat linh tinh. Nó vừa tư duy (chia nhỏ công việc ra 3 task), nó vừa làm vai Coder/Thư ký đánh máy (Gửi lệnh HTTP vào máy chủ Localhost của chúng ta) để nạp công việc đó lên Bảng Điểu Khiển. Từ đây CEO chỉ việc rung đùi xem Dashboard!
