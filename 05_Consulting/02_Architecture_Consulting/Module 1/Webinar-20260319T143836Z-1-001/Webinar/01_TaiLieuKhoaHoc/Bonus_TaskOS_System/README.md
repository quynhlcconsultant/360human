# 📖 README — Antigravity Task OS

> **Quản lý task phân tán — Không cần SaaS, Không cần Internet.**  
> *Local-native, AI-friendly, Pixel-aesthetics.*

---

## 🎯 Hệ thống này làm gì?

**Antigravity Task OS** là một giải pháp quản lý task siêu nhẹ, chạy hoàn toàn trên máy local của bạn. Nó quét tất cả các file `ToDo.md` trong workspace của bạn, tổng hợp chúng lại và hiển thị lên một **Master Dashboard đẹp** trên trình duyệt.

**Luồng hoạt động:**
```
File ToDo.md (của bạn) ──► task_server.py (quét) ──► todos.json ──► dashboard.html (hiển thị)
```

---

## 🚀 Bắt đầu nhanh (Quick Start)

### Yêu cầu
- Python 3.8 trở lên (không cần cài thêm package)
- Trình duyệt Chrome / Edge / Firefox

### Bước 1: Chép thư mục vào workspace của bạn

Chép toàn bộ thư mục `antigravity-task-os` vào bất kỳ đâu trong workspace của bạn (ví dụ: `_tools/task-os/`).

### Bước 2: Cấu hình đường dẫn workspace

Mở file `task_server.py` và tìm dòng:

```python
workspace_root = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
```

Thay bằng đường dẫn thực tế đến thư mục gốc workspace của bạn:

```python
workspace_root = r"C:\Users\YourName\Desktop\YourWorkspace"
```

### Bước 3: Chạy server

```bash
python task_server.py
```

Trình duyệt sẽ **tự mở** Dashboard tại `http://localhost:8000/dashboard.html`.

### Bước 4: Thêm task vào dự án của bạn

Tạo file `ToDo.md` trong bất kỳ thư mục dự án nào. Viết task theo cú pháp:

```markdown
- [ ] Tên task của tôi #urgent
- [ ] Một task khác #dev
- [x] Task đã hoàn thành
```

Nhấn nút **↺ SYNC** trên Dashboard để cập nhật.

---

## 📋 Hướng dẫn viết file `ToDo.md`

### ✅ Cú pháp đúng

```markdown
# ToDo - Tên Dự án

- [ ] Task chưa làm
- [x] Task đã xong
- [ ] **Task in đậm** có `inline code`
- [ ] Task khẩn cấp cần làm ngay #urgent
- [ ] Task thuộc nhóm marketing #marketing #content
```

### ❌ Cú pháp sai (sẽ bị bỏ qua)

```markdown
* [ ] Task dùng dấu sao — KHÔNG ĐƯỢC
-[ ] Task thiếu khoảng trắng — KHÔNG ĐƯỢC  
• [ ] Task dấu chấm — KHÔNG ĐƯỢC
```

### 🏷️ Hệ thống Hashtag

| Tag          | Ý nghĩa           | Hiệu ứng trên Dashboard     |
| ------------ | ----------------- | --------------------------- |
| `#urgent`    | Khẩn cấp          | Đẩy vào cột 🔥 CRITICAL (đỏ) |
| `#critical`  | Nghiêm trọng      | Đẩy vào cột 🔥 CRITICAL (đỏ) |
| `#dev`       | Kỹ thuật          | Hiển thị tag màu tím        |
| `#marketing` | Marketing         | Hiển thị tag màu tím        |
| `#agent`     | Giao cho AI Agent | Hiển thị tag màu tím        |
| `#bất_kỳ`    | Tuỳ bạn đặt       | Hiển thị tag màu tím        |

---

## 📁 Cấu trúc thư mục

```
antigravity-task-os/
├── task_server.py      ← Core Engine (Python HTTP Server + Aggregator)
├── dashboard.html      ← Master Dashboard UI (Pixel-art RPG theme)
├── todos.json          ← Auto-generated data (ĐỪNG chỉnh tay)
├── README.md           ← Tài liệu này
├── PRD.md              ← Product Requirements Document
└── SRS.md              ← Software Requirements Specification
```

---

## ⚙️ Cấu hình Nâng cao

### Thay đổi Port

Mở `task_server.py`, tìm và sửa:
```python
start_http_server(8000)  # Đổi 8000 thành port bạn muốn
```
Nhớ đổi luôn trong URL của `webbrowser.open(...)`.

### Thay đổi giới hạn độ sâu quét

```python
MAX_DEPTH = 5  # Tăng nếu workspace của bạn có cấu trúc sâu hơn
```

### Thêm thư mục bị bỏ qua

Tìm dòng kiểm tra trong hàm `parse_todos`:
```python
if any(x in root for x in ['.gemini', '.agent', '.git', ...]):
```
Thêm tên thư mục cần bỏ qua vào danh sách.

---

## 🔧 Troubleshooting

| Triệu chứng                          | Nguyên nhân      | Cách xử lý                          |
| ------------------------------------ | ---------------- | ----------------------------------- |
| Dashboard trắng tinh                 | Server chưa chạy | Chạy `python task_server.py`        |
| Không thấy task                      | File tên sai     | Chắc chắn tên là `ToDo.md`          |
| Nút Sync không phản hồi              | Port bị chiếm    | Đổi port hoặc tắt process cũ        |
| Task không hiển thị mặc dù file đúng | Cú pháp sai      | Kiểm tra lại `- [ ]` có đúng format |
| Python không tìm thấy                | Chưa cài Python  | Cài Python 3.8+ từ python.org       |

---

## 🛣️ Roadmap

- **v1.0** (hiện tại) — Read-only Dashboard + Project Filter + Sync
- **v1.5** — Click checkbox trên Dashboard tự update file `.md`
- **v2.0** — Task Block với ID duy nhất và context mô tả
- **v2.5** — File Watcher tự động (không cần bấm Sync)
- **v3.0** — REST API cho AI Agent truy vấn trực tiếp

---

## 📄 License

MIT — Tự do sử dụng, chỉnh sửa và phân phối.  
*Built with ❤️ by Antigravity AI Workspace.*
