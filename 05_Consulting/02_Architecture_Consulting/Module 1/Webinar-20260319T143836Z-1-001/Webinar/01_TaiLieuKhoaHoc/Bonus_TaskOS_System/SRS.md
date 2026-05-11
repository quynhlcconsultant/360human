# SRS — Đặc tả Yêu cầu Phần mềm

**Product:** Antigravity Task OS  
**Document Type:** Software Requirements Specification (SRS) / Functional Requirements Specification (FRS)  
**Version:** v1.0  
**Date:** 2026-03-09

---

## 1. Kiến trúc Tổng thể

```
┌─────────────────────────────────────────────────────────┐
│                  WORKSPACE (Command Center)              │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │
│  │ Project A   │  │ Project B   │  │ Project N   │     │
│  │ ToDo.md     │  │ ToDo.md     │  │ ToDo.md     │     │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘     │
│         │                │                │             │
│         └────────┬────────┘                │             │
│                  │        ┌─────────────────┘             │
│                  ▼        ▼                               │
│         ┌────────────────────────┐                        │
│         │    task_server.py      │  ← Python Aggregator   │
│         │  (HTTP Server :8000)   │                        │
│         └───────────┬────────────┘                        │
│                     │ generates                           │
│                     ▼                                     │
│             ┌───────────────┐                             │
│             │  todos.json   │  ← Centralized Data Store   │
│             └───────┬───────┘                             │
│                     │ serves                              │
│                     ▼                                     │
│           ┌─────────────────────┐                         │
│           │    dashboard.html   │  ← Master View (SPA)    │
│           │  http://localhost   │                         │
│           │  :8000/dashboard   │                         │
│           └─────────────────────┘                         │
└─────────────────────────────────────────────────────────┘
```

---

## 2. Mô tả Thành phần

### 2.1 `task_server.py` — Core Engine

**Trách nhiệm:**
- Quét toàn bộ thư mục `Workspace Root` theo chiều sâu tối đa `MAX_DEPTH = 5`.
- Phân loại từng file `ToDo.md` vào đúng Project Taxonomy (Cấp 1 = Dự án Cha, Cấp 2+ = Module).
- Trích xuất task theo cú pháp Markdown Checkbox.
- Serialize dữ liệu ra file `todos.json`.
- Chạy HTTP Server tại `localhost:8000` để phục vụ Dashboard và nhận lệnh Re-scan.

**Endpoints:**
| Method | Path          | Mô tả                               |
| ------ | ------------- | ----------------------------------- |
| `GET`  | `/`           | Serve static files (HTML, JSON)     |
| `GET`  | `/todos.json` | Trả về file JSON data               |
| `POST` | `/update`     | Kích hoạt re-scan toàn bộ workspace |

### 2.2 `dashboard.html` — Master View SPA

**Trách nhiệm:**
- Fetch `todos.json` từ local server.
- Render giao diện Kanban 3 cột (Critical / In Progress / Completed).
- Hỗ trợ Project Filter dropdown (tự động sinh từ data).
- Trigger re-scan bằng nút **SYNC** qua HTTP POST.
- Render cơ bản Markdown (Bold, Italic, Code Inline) trong nội dung task.

### 2.3 `todos.json` — Centralized Data Store

File JSON trung gian. Auto-generated bởi `task_server.py`. **KHÔNG chỉnh sửa thủ công.**

**Schema:**
```json
[
  {
    "project": "PROJECT_A",       // Tên project cha (folder cấp 1)
    "module": "Sub-Team / Feature", // Module con (folder cấp 2+)
    "file_path": "PROJECT_A\\ToDo.md",  // Đường dẫn tương đối
    "line": 3,                    // Số dòng trong file gốc
    "text": "Setup API endpoint #urgent",  // Nội dung task
    "tags": ["#urgent"],          // Danh sách hashtag
    "done": false                 // Trạng thái hoàn thành
  }
]
```

---

## 3. Chuẩn hóa File `ToDo.md` (Metadata Standard)

### 3.1 Định vị File
- Tên file bắt buộc: `ToDo.md` (case-insensitive: `todo.md`, `TODO.md` đều được nhận diện).
- Vị trí: Bất kỳ thư mục con nào trong Workspace Root (trừ `.git`, `.gemini`, `node_modules`, `__pycache__`, `.vscode`, `.agent`, `.claude`).
- Hệ thống tự xác định Project/Module dựa trên **vị trí thư mục**.

### 3.2 Cú pháp Task (BẮTBUỘC)

```markdown
- [ ] Nội dung task #tag1 #tag2
- [x] Task đã hoàn thành #done
- [/] Task đang thực hiện (tùy chọn)
```

**Quy tắc:**
| Ký tự                      | Ý nghĩa                                 |
| -------------------------- | --------------------------------------- |
| `- [ ]`                    | Task chưa làm (pending)                 |
| `- [x]` hoặc `- [X]`       | Task đã xong (done)                     |
| `#urgent` hoặc `#critical` | Task khẩn cấp → hiển thị cột CRITICAL   |
| `#tag_bất_kỳ`              | Tag phân loại (hiển thị trên Dashboard) |

**Hợp lệ:**
```markdown
- [ ] Viết API đăng nhập #urgent #dev
- [x] Update README
- [ ] **Bold task title** với `code` inline
```

**Không hợp lệ:**
```markdown
* [ ] Task (dấu *)
-[ ] Task (thiếu khoảng trắng)
• [ ] Task (dấu chấm tròn)
```

### 3.3 Nội dung Bổ trợ (Tùy chọn)
Các dòng mô tả bên dưới task (thụt lề) hiện tại không được đưa lên Dashboard (chỉ hiển thị trên file gốc). Đây là nội dung dự kiến cho v1.5+.

---

## 4. Yêu cầu Phi Chức năng

| Yêu cầu                   | Giá trị                                                                          |
| ------------------------- | -------------------------------------------------------------------------------- |
| **Nền tảng**              | Python 3.8+, không cần cài thêm package                                          |
| **Trình duyệt**           | Chrome, Edge, Firefox (latest)                                                   |
| **Giới hạn quét**         | MAX_DEPTH = 5 (configurable trong code)                                          |
| **Folder bị bỏ qua**      | `.git`, `.gemini`, `node_modules`, `__pycache__`, `.vscode`, `.agent`, `.claude` |
| **Cổng mặc định**         | `8000` (configurable)                                                            |
| **Dung lượng todos.json** | < 1MB cho workspace với 1000 task                                                |

---

## 5. Giới hạn & Rủi ro Hiện tại (v1.0)

| Hạn chế               | Mô tả                              | Kế hoạch giải quyết       |
| --------------------- | ---------------------------------- | ------------------------- |
| Read-only Dashboard   | Không thể check/uncheck task từ UI | v1.5: Two-way sync        |
| Không có File Watcher | Phải nhấn Sync thủ công            | v2.5: watchdog library    |
| Single-server         | Chỉ 1 instance tại localhost:8000  | v3.0: Multi-workspace     |
| Race condition        | Nếu Agent và User cùng sửa file    | v1.5: File lock mechanism |
