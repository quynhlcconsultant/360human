# 🗺️ GUIDELINE — Hướng dẫn Triển khai Antigravity Task OS

> Tài liệu này dành cho **Khách hàng / Đội nhóm** muốn áp dụng Antigravity Task OS vào dự án thực tế của mình.

---

## Phần 1: Triết lý Thiết kế

Antigravity Task OS được xây dựng trên 3 nguyên tắc cốt lõi:

### 1. Markdown là Nguồn Sự thật Duy nhất (SSOT)
Tất cả task **phải sống trong file `.md`**, không phải trong database hay app riêng. Khi bạn mở file `ToDo.md` bằng bất kỳ text editor nào, bạn thấy ngay dữ liệu thô. Hệ thống chỉ *tổng hợp và hiển thị* — không bao giờ thay thế file gốc.

### 2. Zero Dependency — Không phụ thuộc
Script Python không dùng bất kỳ thư viện bên ngoài nào (`pip install`). Chỉ cần Python 3.8+ là chạy ngay. Điều này giúp hệ thống hoạt động ổn định vĩnh viễn mà không lo breaking changes.

### 3. AI-Native First
Cú pháp Markdown Checkbox là cú pháp mà mọi LLM (ChatGPT, Claude, Gemini...) đều hiểu và có thể tạo ra ngay. AI Agent của bạn có thể tự động tạo task, đánh dấu hoàn thành chỉ bằng cách ghi vào file — không cần API keys, không cần webhook.

---

## Phần 2: Cấu trúc Thư mục Khuyên dùng

### Workspace đơn giản (1 dự án)
```
My-Project/
├── _task-os/               ← Chứa hệ thống Task OS
│   ├── task_server.py
│   ├── dashboard.html
│   └── todos.json (auto)
├── docs/
│   └── ToDo.md             ← Task của toàn dự án
├── src/
│   └── feature-A/
│       └── ToDo.md         ← Task riêng của feature A
└── marketing/
    └── ToDo.md             ← Task marketing
```

### Workspace đa dự án (Workspace tổng)
```
Command-Center/             ← workspace_root
├── _task-os/               ← Task OS ở mức tổng
├── 01_Project-Alpha/
│   ├── ToDo.md
│   └── Sub-Module/
│       └── ToDo.md
├── 02_Project-Beta/
│   └── ToDo.md
└── 03_Marketing/
    └── ToDo.md
```

> ⚠️ **Lưu ý:** `workspace_root` trong `task_server.py` phải trỏ đến thư mục **cha** của tất cả các dự án (trong ví dụ trên là `Command-Center/`).

---

## Phần 3: Quy ước Viết Task theo Nhóm

Để cả team (bao gồm AI Agent) hiểu task của nhau, hãy dùng bộ quy ước sau:

### Convention 1: Tiêu đề rõ ràng, có Động từ
```markdown
✅ ĐÚNG: - [ ] Viết API endpoint thanh toán #dev
❌ SAI:  - [ ] Thanh toán
```

### Convention 2: Tag theo Domain
Chọn 1 domain tag cho mỗi task để dễ phân loại:

| Tag          | Domain                 |
| ------------ | ---------------------- |
| `#dev`       | Kỹ thuật, code         |
| `#design`    | Thiết kế UI/UX         |
| `#marketing` | Marketing, nội dung    |
| `#ops`       | Vận hành, hành chính   |
| `#research`  | Nghiên cứu, phân tích  |
| `#agent`     | Task giao cho AI Agent |

### Convention 3: Tag theo Mức độ ưu tiên
Chỉ dùng `#urgent` hoặc `#critical` cho task **thực sự** khẩn cấp để tránh lạm dụng.

```markdown
- [ ] Fix lỗi thanh toán production #urgent #dev
- [ ] Viết report tháng #ops  ← Không urgent, không cần tag
```

### Convention 4: Grouping bằng Heading

```markdown
# ToDo - Project Alpha

## 🔴 Sprint 3 (Current)
- [ ] Task A #urgent
- [ ] Task B #dev

## 📝 Backlog
- [ ] Task C (cho Sprint 4)
- [ ] Task D (idea)

## ✅ Archived (Done)
- [x] Task E
```

> **Lưu ý:** Hệ thống chỉ đọc checkboxes, không đọc headings. Headings chỉ giúp bạn đọc file `.md` dễ hơn.

---

## Phần 4: Tích hợp với AI Agent

### Hướng dẫn cho AI Agent (System Prompt Snippet)

Copy đoạn sau vào System Prompt của Agent:

```
TASK MANAGEMENT PROTOCOL:
- Khi được giao nhiệm vụ, hãy kiểm tra file ToDo.md trong thư mục dự án hiện tại.
- Tạo task mới theo cú pháp: - [ ] [Mô tả rõ ràng] #[domain-tag]
- Khi hoàn thành task, đổi [ ] thành [x]: - [x] [Mô tả]
- Gắn tag phù hợp: #urgent cho nhiệm vụ khẩn, #agent cho task do AI thực hiện.
- Bắt buộc dùng dấu gạch ngang (-), khoảng trắng, ngoặc vuông theo đúng cú pháp.
```

### Workflow tối ưu với AI Agent

```
1. User giao nhiệm vụ cho Agent
2. Agent đọc file ToDo.md để hiểu context
3. Agent thực hiện nhiệm vụ
4. Agent cập nhật task: đổi [ ] ➜ [x]
5. Agent (hoặc User) gọi SYNC trên Dashboard
6. Dashboard cập nhật ngay lập tức
```

---

## Phần 5: Vận hành Hàng ngày

### Routine sáng (Team Lead)
1. Mở Dashboard: `python task_server.py`
2. Nhìn qua cột **CRITICAL** — xử lý task đỏ trước.
3. Filter theo từng dự án để review tiến độ.

### Routine kết thúc ngày (AI Agent / Member)
1. Cập nhật các task đã hoàn thành: đổi `[ ]` → `[x]`
2. Thêm task mới phát sinh vào đúng file `ToDo.md` của dự án.
3. Bấm Sync hoặc thông báo cho Team Lead biết.

### Routine tuần (Project Manager)
1. Archive (xóa hoặc comment) các task `[x]` đã làm xong từ lâu để file gọn.
2. Review Backlog — thêm tag `#urgent` nếu task nào trở nên cấp bách.
3. Kiểm tra xem có dự án mới nào chưa có `ToDo.md` không.

---

## Phần 6: Checklist Triển khai

Sử dụng checklist này khi setup hệ thống lần đầu:

- [ ] Python 3.8+ đã cài đặt (`python --version`)
- [ ] Sao chép thư mục `antigravity-task-os` vào workspace
- [ ] Cập nhật `workspace_root` trong `task_server.py`
- [ ] Chạy `python task_server.py` lần đầu — không có lỗi
- [ ] Dashboard mở trên trình duyệt, hiển thị đúng
- [ ] Tạo file `ToDo.md` thử nghiệm với 2-3 task
- [ ] Nhấn SYNC — task xuất hiện trên Dashboard
- [ ] Thử bộ lọc Project Filter
- [ ] Thông báo cho team về quy ước viết task
- [ ] (Tùy chọn) Thêm script vào Agent System Prompt
