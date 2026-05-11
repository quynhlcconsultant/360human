# Chương 9: Workflow Tiering — Phân tầng quy trình

> **Nguồn gốc:** Khái niệm MỚI — không có trong Star Model gốc
> **Câu hỏi cốt lõi:** *Không phải mọi Workflow đều ngang hàng. Cái nào điều phối? Cái nào thực thi? Cái nào hỗ trợ?*

---

## 1. Tại sao phải phân tầng?

Trong tổ chức con người, "process" là cách con người phối hợp — meeting, email, reporting. Không ai phân loại "meeting nào quan trọng hơn" vì con người tự biết.

Trong AI-Agent Workforce, **Workflow IS the process**. Và khi bạn có 100+ Workflow, câu hỏi nảy sinh:

> *Workflow /content-post (8 phase, có sub-workflows) cùng loại với /tomtat (1 bước tổng hợp chat)?*

Rõ ràng là KHÔNG. Cần **phân tầng** — xác định vai trò của mỗi Workflow trong hệ thống.

---

## 2. Bốn tầng Workflow

```
TIER 0: META
  "Workflow tạo ra Workflow"
  → /buildflow, /buildskill, /refactor, /rm
  → Thay đổi CẤU TRÚC hệ thống
  → CEO/Architect exclusive

TIER 1: ORCHESTRATION
  "Workflow điều phối nhiều Workflow con"
  → /content-post, /chain-build, /chain-plan
  → Phân công, tổng hợp, quality gate
  → Director Agent level

TIER 2: EXECUTION
  "Workflow thực thi task cụ thể"
  → /content-post-p5-writing, /code, /deploy, /test
  → Tạo output thực tế
  → Specialist Agent level

TIER 3: UTILITY
  "Workflow hỗ trợ, gọi bất cứ lúc nào"
  → /tomtat, /flog, /beat, /stale, /log
  → Không tạo output chính, phục vụ flow khác
  → Mọi Agent đều gọi được
```

### Hình dung trực quan

```
         TIER 0: META
         /buildflow  /rm
              │
              │ tạo/sửa
              ▼
         TIER 1: ORCHESTRATION
         /content-post  /chain-build  /chain-plan
              │
              │ điều phối
              ▼
         TIER 2: EXECUTION
         /code  /deploy  /test  /content-post-p5-writing
              │
              │ gọi hỗ trợ
              ▼
         TIER 3: UTILITY
         /flog  /beat  /tomtat  /stale
```

---

## 3. Đặc điểm từng Tier

### Tier 0: META — Thay đổi hệ thống

| Đặc điểm       | Giá trị                                            |
| -------------- | -------------------------------------------------- |
| **Ai sử dụng** | CEO, Architect, @AI_RM                             |
| **Output**     | Workflow mới, Skill mới, cấu trúc tổ chức thay đổi |
| **Tần suất**   | Thấp — chỉ khi hệ thống cần evolve                 |
| **Rủi ro**     | Cao — thay đổi ảnh hưởng toàn bộ tổ chức           |
| **Approval**   | CEO phải approve trước khi apply                   |
| **Ví dụ**      | `/buildflow` — tạo workflow mới từ lịch sử chat    |
|                | `/buildskill` — tạo skill mới từ nguồn tham khảo   |
|                | `/rm` — restructure tổ chức, audit workforce       |
|                | `/refactor` — đánh giá sức khỏe dự án              |

### Tier 1: ORCHESTRATION — Điều phối pipeline

| Đặc điểm          | Giá trị                                                                                                                                                                                                                                                              |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Ai sử dụng**    | Director Agents, đôi khi CEO                                                                                                                                                                                                                                         |
| **Output**        | Pipeline hoàn chỉnh (nhiều Tier 2 chạy liên tiếp)                                                                                                                                                                                                                    |
| **Tần suất**      | Trung bình — mỗi sprint / mỗi task lớn                                                                                                                                                                                                                               |
| **Rủi ro**        | Trung bình — ảnh hưởng 1 pipeline hoặc 1 BU                                                                                                                                                                                                                          |
| **Cấu trúc**      | Gọi nhiều Tier 2 theo thứ tự, có quality gate                                                                                                                                                                                                                        |
| **Bảo lưu State** | **(Red Team Warning)** Bắt buộc có **Checkpointing**. Nếu Tier 1 điều phối chuỗi bị sập ở bước 5 do đứt cáp API, hệ thống phải ghi nhớ lại State và Output của bước 4. Khi resume, tiếp tục từ bước 5 → Tránh đốt token bắt đầu lại từ đầu (State Management Decay). |
| **Ví dụ**         | `/content-post` — 8 phase viết bài viral                                                                                                                                                                                                                             |
|                   | `/chain-build` — code → test → deploy                                                                                                                                                                                                                                |
|                   | `/chain-plan` — discovery → design → spec                                                                                                                                                                                                                            |
|                   | `/discovery` — 3 stage product discovery                                                                                                                                                                                                                             |

### Tier 2: EXECUTION — Thực thi cụ thể

| Đặc điểm       | Giá trị                                          |
| -------------- | ------------------------------------------------ |
| **Ai sử dụng** | Specialist Agents                                |
| **Output**     | Sản phẩm cụ thể (bài viết, code, deploy, report) |
| **Tần suất**   | Cao — hàng ngày, hàng task                       |
| **Rủi ro**     | Thấp — ảnh hưởng 1 output cụ thể                 |
| **Cấu trúc**   | Thường tự contained, 1 Agent thực thi            |
| **Ví dụ**      | `/code` — viết code                              |
|                | `/deploy` — deploy production                    |
|                | `/content-post-p5-writing` — viết bài (phase 5)  |
|                | `/test` — chạy test suite                        |

### Tier 3: UTILITY — Hỗ trợ liên tục

| Đặc điểm       | Giá trị                                      |
| -------------- | -------------------------------------------- |
| **Ai sử dụng** | Mọi Agent, mọi lúc                           |
| **Output**     | Side-effect (log, extract, check)            |
| **Tần suất**   | Rất cao — gọi tự động hoặc thủ công liên tục |
| **Rủi ro**     | Rất thấp — không thay đổi trạng thái chính   |
| **Cấu trúc**   | Nhỏ, nhanh, stateless                        |
| **Ví dụ**      | `/flog` — track file changes                 |
|                | `/beat` — extract knowledge từ conversation  |
|                | `/tomtat` — tóm tắt chat                     |
|                | `/stale` — kiểm tra file có outdated không   |

---

## 4. Quy tắc gọi giữa các Tier

```
RULES:
  [1] Tier N chỉ gọi Tier N+1 hoặc Tier 3 (Utility)
      → Tier 0 gọi Tier 1    ✅
      → Tier 1 gọi Tier 2    ✅
      → Tier 2 gọi Tier 3    ✅
      → Bất kỳ Tier → Tier 3 ✅ (Utility = công cụ chung)

  [2] Tier N KHÔNG gọi ngược Tier N-1
      → Tier 2 gọi Tier 1    ❌ (Execution gọi Orchestration = đảo ngược chuỗi chỉ huy)
      → Tier 1 gọi Tier 0    ❌ (Orchestration tự ý thay đổi hệ thống = nguy hiểm)

  [3] Tier N có thể gọi Tier N (cùng tầng)
      → Tier 2 gọi Tier 2    ✅ (Cross-calling ngang)
      → Tier 1 gọi Tier 1    ✅ (Orchestration compose — cần kiểm soát chặt)

  [4] Tier 3 KHÔNG gọi Tier 0, 1, 2
      → Utility là tool thuần — không điều khiển flow chính
```

### Hình dung quy tắc gọi

```
    Tier 0  ──────→  Tier 1
                      │
    Tier 1  ──────→  Tier 2  ←──→  Tier 2 (ngang)
                      │
                      ▼
                    Tier 3  (utility, mọi tier đều gọi được)
```

---

## 5. Anti-patterns

### Anti-pattern 1: Flat Workflow — Không phân tầng

```
❌ 100 Workflow ngang hàng, không biết cái nào điều phối cái nào
→ CEO phải tự chọn Workflow → CEO = router thủ công
→ FIX: Gán Tier cho mỗi Workflow. Dùng /go Router ở Tier 1
```

### Anti-pattern 2: God Workflow — 1 Workflow làm tất cả

```
❌ /do-everything: tìm hiểu yêu cầu → code → test → deploy → document
→ 500+ dòng instructions, không maintain được
→ FIX: Tách thành Tier 1 Orchestration gọi 4-5 Tier 2 Execution
```

### Anti-pattern 3: Reverse Call — Tier dưới gọi Tier trên

```
❌ /code (Tier 2) tự gọi /chain-build (Tier 1)
→ Execution tự ý kích hoạt pipeline → mất kiểm soát
→ FIX: Tier 2 escalate thay vì reverse call
```

### Anti-pattern 4: Utility Creep — Utility phình to

```
❌ /flog (Tier 3) bắt đầu có logic phức tạp, gọi database, thay đổi state
→ Utility mất tính "nhẹ, nhanh, stateless"
→ FIX: Nếu Utility > 50 dòng → xem xét nâng lên Tier 2
```

---

## 6. Nguyên tắc Workflow Tiering

| #       | Nguyên tắc                                           | Giải thích                                                   |
| ------- | ---------------------------------------------------- | ------------------------------------------------------------ |
| **WT1** | **4 tầng là đủ**                                     | Meta → Orchestration → Execution → Utility. Không cần thêm   |
| **WT2** | **Tier N gọi Tier N+1 hoặc Tier 3**                  | Không gọi ngược — giữ chuỗi chỉ huy rõ                       |
| **WT3** | **Mỗi Workflow có Tier rõ ràng**                     | Ghi trong YAML frontmatter: `tier: execution`                |
| **WT4** | **Tier 1 cần quality gate**                          | Orchestration workflow phải kiểm tra output trước khi chuyển |
| **WT5** | **Tier 3 phải nhẹ và stateless**                     | Utility > 50 dòng → xem xét nâng Tier                        |
| **WT6** | **Workflow Tiering thay thế Org Hierarchy một phần** | Cách workflow gọi nhau quyết định flow thực tế của tổ chức   |

---

## 7. Liên kết với các chương khác

- **Chương 5 (Shape):** 3 tầng Agent (CEO → Director → Specialist) map với 3 Tier (1 → 2 → 3). Tier 0 là meta-level.
- **Chương 6 (Distribution of Power):** Tier càng cao → quyền thay đổi càng lớn → centralize hơn
- **Chương 8 (Processes):** Workflow Tiering là CÁC THỂ HÓA cụ thể nhất của Vertical Processes
- **Chương 10 (Cross-calling):** Cross-calling xảy ra chủ yếu ở Tier 1-2 (cùng tầng hoặc xuống)
