# PRD — Antigravity Task OS

**Product Name:** Antigravity Task OS  
**Version:** v1.0  
**Date:** 2026-03-09  
**Author:** Antigravity AI Workspace  
**Status:** Production-Ready PoC

---

## 1. Overview

Antigravity Task OS là một hệ thống quản lý task cục bộ (local-native), được thiết kế đặc biệt cho các workspace AI-Agent như Antigravity. Hệ thống cho phép các AI Agent và người dùng con người theo dõi, quản lý và tổng hợp tất cả các task phân tán từ nhiều dự án con khác nhau mà không cần phụ thuộc vào bất kỳ dịch vụ SaaS nào.

**Định vị sản phẩm:** *"Jira meets the terminal — built for AI-native teams."*

---

## 2. Problem Statement

### 2.1 Bối cảnh
Trong môi trường phát triển dự án phức tạp (đặc biệt khi workspace có nhiều dự án con), các file `ToDo.md` thường bị phân tán rải rác ở hàng chục thư mục khác nhau. Kết quả là:

- Không có "View tổng" (Master View) để xem tất cả task cùng lúc.
- AI Agent không biết task nào đang pending, cái nào đã done khi context bị giới hạn.
- Người dùng phải mở từng file để kiểm tra tiến độ — cực kỳ tốn thời gian.

### 2.2 Hạn chế của giải pháp hiện có
| Giải pháp              | Vấn đề                                           |
| ---------------------- | ------------------------------------------------ |
| Jira / Linear / Notion | Yêu cầu API Key, có độ trễ mạng, tốn phí         |
| Supabase Database      | Cần thiết kế schema, không "Native" với Markdown |
| Obsidian Dataview      | Chỉ đọc được, không có server-side logic         |
| Spreadsheet            | Không kết nối được với AI Agent workflow         |

---

## 3. Goals & Non-Goals

### Goals ✅
- **G1:** Tổng hợp tất cả task từ mọi file `ToDo.md` vào một Master Dashboard duy nhất.
- **G2:** Phân loại task tự động theo dự án (Project Taxonomy) mà không cần cấu hình thủ công.
- **G3:** Hỗ trợ lọc task theo từng dự án con real-time.
- **G4:** Hoạt động hoàn toàn offline, không cần internet hay API bên ngoài.
- **G5:** Tốc độ quét và tải dữ liệu < 3 giây cho workspace 1000+ files.
- **G6:** AI Agent có thể tạo/cập nhật task bằng cách ghi vào file `.md` theo chuẩn.

### Non-Goals ❌
- Không thay thế Git (không quản lý code).
- Không có tính năng Real-time Collaboration (multi-user cùng lúc).
- Không có Mobile App.
- Không sync lên Cloud.

---

## 4. Target Users

### User Persona 1: AI Agent (Primary)
- **Là ai:** Agent RM, Agent ở các dự án 5Balance, Hoctap.tech, v.v.
- **Nhu cầu:** Đọc danh sách task pending → Thực thi → Đánh dấu hoàn thành.
- **Cách dùng:** Đọc/ghi file `ToDo.md` theo đúng chuẩn cú pháp.

### User Persona 2: Project Lead / CEO (Secondary)
- **Là ai:** Người quản lý workspace, có nhiều dự án con đang chạy song song.
- **Nhu cầu:** Xem nhanh tất cả task đang pending, ưu tiên task khẩn cấp.
- **Cách dùng:** Mở Dashboard trên trình duyệt, bấm nút Sync khi cần cập nhật.

---

## 5. User Stories

| ID    | As a...      | I want to...                                 | So that...                                  |
| ----- | ------------ | -------------------------------------------- | ------------------------------------------- |
| US-01 | AI Agent     | Ghi task vào file ToDo.md theo chuẩn         | Dashboard tự gom vào Master View            |
| US-02 | Project Lead | Xem tất cả task từ mọi dự án trên 1 màn hình | Không phải mở từng file                     |
| US-03 | Project Lead | Lọc task theo tên dự án                      | Tập trung review từng team                  |
| US-04 | Project Lead | Nhấn nút Sync bất kỳ lúc nào                 | Dashboard luôn phản ánh trạng thái mới nhất |
| US-05 | Project Lead | Phân biệt task khẩn cấp ngay lập tức         | Ưu tiên xử lý đúng thứ tự                   |
| US-06 | AI Agent     | Đọc được nội dung file todos.json            | Context-aware khi nhận nhiệm vụ mới         |

---

## 6. Success Metrics

| Metric                              | Target                         |
| ----------------------------------- | ------------------------------ |
| Thời gian Scan workspace            | < 3 giây cho 200 file ToDo.md  |
| Thời gian Load Dashboard            | < 1 giây                       |
| Tỷ lệ task được nhận diện đúng      | > 99% (tuân thủ cú pháp chuẩn) |
| Số lần click để xem full task board | 0 (tự mở khi chạy script)      |

---

## 7. Roadmap

| Phase          | Tính năng                                         | Status    |
| -------------- | ------------------------------------------------- | --------- |
| **v1.0 (Now)** | Aggregator + JSON + Read-only Dashboard           | ✅ Done    |
| **v1.5**       | Two-way sync (Click checkbox → update file)       | 🔵 Planned |
| **v2.0**       | Block-based ToDo (Task ID + context phụ)          | 🔵 Planned |
| **v2.5**       | File Watcher (Auto-sync khi file thay đổi)        | 🔵 Planned |
| **v3.0**       | Agent-native API (AI truy vấn trực tiếp qua HTTP) | 🔵 Planned |
