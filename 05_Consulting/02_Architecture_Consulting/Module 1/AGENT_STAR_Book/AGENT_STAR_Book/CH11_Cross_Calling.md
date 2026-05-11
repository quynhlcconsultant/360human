# Chương 10: Cross-Calling — 5 Patterns phối hợp giữa Workflow

> **Nguồn gốc:** Concepts MỚI — mở rộng từ Galbraith's Lateral Processes
> **Câu hỏi cốt lõi:** *Khi Workflow A cần output từ Workflow B — chúng "gọi" nhau thế nào?*

---

## 1. Tại sao Cross-calling là cốt lõi?

Trong tổ chức người, "phối hợp ngang" = meeting, email, chat.
Trong AI-Agent Workforce, "phối hợp ngang" = **Workflow gọi Workflow** (cross-calling).

Cross-calling là **cơ chế duy nhất** để Agent chuyên biệt phối hợp với nhau. Không có cross-calling → mỗi Agent là ốc đảo.

---

## 2. Năm Cross-calling Patterns

### Pattern 1: Sequential Chain — Chuỗi tuần tự

```
A → B → C → D
Mỗi Workflow nhận output từ Workflow trước làm input

Ví dụ:
  /content-post-p1-idea → /content-post-p2-research → /content-post-p3-hook → ...

Khi nào dùng:
  → Pipeline có thứ tự cố định
  → Output Workflow N là input bắt buộc cho Workflow N+1

Ưu điểm: Dễ hiểu, dễ debug (biết chỗ nào fail)
Nhược điểm: Chậm — phải đợi từng bước xong
```

### Pattern 2: Router — Phân tuyến thông minh

```
        ┌→ Agent A (nếu task type = X)
CEO → Router
        ├→ Agent B (nếu task type = Y)
        └→ Agent C (nếu task type = Z)

Ví dụ:
  CEO yêu cầu → /go Router phân tích → gọi /code hoặc /content-post hoặc /deploy

Khi nào dùng:
  → CEO không muốn/không cần chọn Workflow thủ công
  → System có nhiều Workflow → cần "tổng đài" điều phối

Ưu điểm: CEO chỉ cần nói "tôi muốn X", Router tìm Workflow
Nhược điểm: Router phải hiểu context rất sâu
```

### Pattern 3: Fork-Join — Song song rồi tổng hợp

```
              ┌→ Agent B ──┐
Agent A ──┬───┤            ├───→ Agent E (tổng hợp)
              └→ Agent C ──┘
              └→ Agent D ──┘

Ví dụ:
  /chain-plan:
    Step 1: Phân tích yêu cầu
    Step 2: [Song song] Nghiên cứu thị trường + Phân tích kỹ thuật + Phân tích tài chính
    Step 3: Tổng hợp báo cáo

Khi nào dùng:
  → Nhiều mảng nghiên cứu/thực thi KHÔNG phụ thuộc nhau
  → Muốn tăng tốc bằng parallelization

Ưu điểm: Nhanh — tasks chạy song song
Nhược điểm: Join phức tạp — phải đợi tất cả xong, merge output
```

### Pattern 4: Escalation Chain — Leo thang khi thất bại

```
Agent A → thử → fail → Agent B → thử → fail → CEO

Ví dụ:
  @Writer viết bài → QA fail → @Writer rewrite → QA fail lần 2 → escalate @MktLead
  @MktLead xem xét → rewrite instructions → @Writer thử lần 3
  → Nếu fail → CEO can thiệp

Khi nào dùng:
  → Task có thể fail, cần fallback plan
  → Mỗi level cao hơn có quyền hạn/kiến thức rộng hơn

Ưu điểm: Tự động retry + escalation → ít làm phiền CEO
Nhược điểm: Chậm nếu nhiều level, có thể loop
```

### Pattern 5: Callback — Gọi ngược sau khi xong

```
Agent A → result → if success: gọi /update
                 → if fail: gọi /fix

Ví dụ:
  /deploy xong → success → callback /docs (cập nhật changelog)
  /deploy xong → fail → callback /fix (debug deployment)

Khi nào dùng:
  → Hành động "sau khi xong" phụ thuộc vào kết quả
  → Cần trigger side-effects tự động

Ưu điểm: Linh hoạt — logic if/else ở output
Nhược điểm: Phức tạp debug — phải trace callback chain
```

---

## 3. Ma trận chọn Pattern

| Tình huống                               | Pattern khuyến nghị   |
| ---------------------------------------- | --------------------- |
| Pipeline cố định, step-by-step           | **Sequential Chain**  |
| CEO giao task mơ hồ, cần phân loại       | **Router**            |
| Nhiều task độc lập có thể chạy song song | **Fork-Join**         |
| Task có thể fail, cần retry + fallback   | **Escalation Chain**  |
| Hành động tiếp theo phụ thuộc kết quả    | **Callback**          |
| Pipeline phức tạp, mix nhiều tình huống  | **Compose** (kết hợp) |

---

## 4. Interface Contract — Hợp đồng giao tiếp

Mỗi Cross-calling phải có **Interface Contract** rõ ràng — giống như API contract:

### YAML Frontmatter chuẩn

```yaml
---
description: Viết bài viral theo 8 phase
tier: orchestration
owner: "@MktLead"
calls:
  - /content-post-p1-idea
  - /content-post-p2-research
  - /content-post-p2b-factcheck
  - /content-post-p3-hook
  - /content-post-p4-structure
  - /content-post-p5-writing
  - /content-post-p6-qa
  - /content-post-p7-redteam
  - /content-post-p8-format
called_by:
  - /go
  - manual (CEO gọi trực tiếp)
input: "Yêu cầu viết bài + context BU"
output: "Bài viết hoàn chỉnh + Sprint artifacts"
---
```

### 4 thành phần bắt buộc (và 1 thành phần bảo vệ)

| Thành phần    | Mô tả                                                                                                                                                                                                                                             |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **calls**     | Danh sách Workflow mà Workflow này GỌI                                                                                                                                                                                                            |
| **called_by** | Danh sách Workflow/Agent GỌI Workflow này                                                                                                                                                                                                         |
| **input**     | Format input mong đợi                                                                                                                                                                                                                             |
| **output**    | Format output cam kết                                                                                                                                                                                                                             |
| **max_depth** | **(Red Team Warning)** Giới hạn số lần gọi đệ quy (Hop Count). Ví dụ A gọi B sửa lỗi, B lại gọi A liên tục sẽ tạo ra Vòng lặp tử thần gây cạn kiệt tài khoản API. Gắn cờ *max_depth=3*, nếu vượt quá → Tự động ngắt và báo lỗi (Circuit Breaker). |

### Tại sao Interface Contract quan trọng?

```
Không có Contract:
  /content-post gọi /extract-authority
  → /extract-authority trả về gì? Object? String? File path?
  → /content-post không biết cách parse → FAIL

Có Contract:
  /extract-authority:
    input: "URL hoặc file path"
    output: "Array of {quote, source, relevance_score}"
  → /content-post biết chính xác cách xử lý output
```

---

## 5. Dependency Graph — Bản đồ phụ thuộc

### Tại sao cần Dependency Graph?

Khi hệ thống có 100+ Workflow cross-calling nhau, câu hỏi "sửa 1 Workflow ảnh hưởng bao nhiêu Workflow khác?" trở thành **bài toán sống còn**.

### Cách vẽ Dependency Graph

```
Từ YAML frontmatter (calls/called_by):

  /go ──────→ /content-post ──→ /content-post-p1-idea
  /go ──────→ /chain-build ───→ /code
  /go ──────→ /deploy          /test
                                /deploy
  
  /content-post ──→ /extract-authority
  /content-post ──→ /sync-persona
  
  /chain-build ───→ /code ──→ /test ──→ /deploy ──→ /docs
```

### Metrics từ Dependency Graph

| Metric              | Ý nghĩa                            | Thu thập từ          |
| ------------------- | ---------------------------------- | -------------------- |
| **Fan-out**         | WF này gọi bao nhiêu WF khác?      | Đếm `calls` list     |
| **Fan-in**          | Bao nhiêu WF khác gọi WF này?      | Đếm `called_by`      |
| **Critical path**   | Chain dài nhất từ Tier 0 → Tier 3? | Graph analysis       |
| **Orphan Workflow** | WF không ai gọi và không gọi ai?   | Fan-in=0, Fan-out=0  |
| **Hub Workflow**    | WF có fan-in hoặc fan-out > 5?     | High coupling = risk |

---

## 6. Anti-patterns

### Anti-pattern 1: Spaghetti Cross-calling

```
❌ Mọi WF gọi mọi WF → dependency graph = mớ bòng bong
→ Sửa 1 WF → không biết bao nhiêu WF bị ảnh hưởng
→ FIX: Interface Contract bắt buộc + Dependency audit
```

### Anti-pattern 2: Missing Backlinks

```
❌ /content-post khai báo calls: [/extract-authority]
   /extract-authority KHÔNG khai báo called_by: [/content-post]
→ 1 chiều — không biết ai đang phụ thuộc vào mình
→ FIX: Bidirectional backlinks bắt buộc
```

### Anti-pattern 3: Implicit Cross-calling

```
❌ Workflow A "nhắc" Agent nên gọi Workflow B — nhưng không khai báo
→ "Hãy cân nhắc chạy /test nếu thấy cần" → không track được
→ FIX: Mọi cross-call phải explicit trong YAML frontmatter
```

### Anti-pattern 4: Circular Dependency

```
❌ A → B → C → A
→ Infinite loop risk
→ FIX: Dependency graph phải DAG (Directed Acyclic Graph)
```

---

## 7. Nguyên tắc Cross-calling

| #       | Nguyên tắc                       | Giải thích                                               |
| ------- | -------------------------------- | -------------------------------------------------------- |
| **CC1** | **5 Patterns là đủ**             | Sequential, Router, Fork-Join, Escalation, Callback      |
| **CC2** | **Interface Contract bắt buộc**  | Mỗi cross-call khai input, output, calls, called_by      |
| **CC3** | **Bidirectional Backlinks**      | A gọi B → B phải biết A đang gọi                         |
| **CC4** | **DAG — No Circular Dependency** | Dependency graph phải acyclic                            |
| **CC5** | **Hub Workflow cần giám sát**    | Fan-in/out > 5 → high coupling → single point of failure |
| **CC6** | **Explicit, không Implicit**     | "Cân nhắc gọi /X" ≠ cross-call. Phải khai báo rõ         |

---

## 8. Liên kết với các chương khác

- **Chương 7 (Departmentalization):** Cross-calling là cơ chế phối hợp giữa các Cluster
- **Chương 8 (Processes):** Cross-calling = hiện thực hóa 4 cấp Lateral Processes
- **Chương 9 (Workflow Tiering):** Cross-calling chủ yếu ở Tier 1 → Tier 2 (xuống) và Tier 2 ↔ Tier 2 (ngang)
- **Chương 15 (Operational Principles):** SSOT áp dụng cho Interface Contract — 1 nguồn duy nhất khai báo cross-call
