# Chương 5: Processes — Luồng vận hành trong AI-Agent Workforce

> **Nguồn gốc:** Process Policy — Star Model™ (Jay R. Galbraith)
> **Câu hỏi cốt lõi:** *Thông tin và công việc "chảy" thế nào trong tổ chức AI Agent?*

---

## 1. Lý thuyết gốc: Processes — "Sinh lý học" của tổ chức

Galbraith phân biệt 2 thứ:

- **Structure** = "Giải phẫu học" (anatomy) — xương, cơ, nội tạng → VỊ TRÍ các bộ phận
- **Processes** = "Sinh lý học" (physiology) — máu chảy, thần kinh truyền tín hiệu → CÁCH vận hành

> *"Structure chỉ là khung xương. Chính Processes mới tạo ra máu chảy — quyết định tổ chức vận hành tốt hay không."*
> — Jay R. Galbraith

### 2 loại Process:

```
VERTICAL PROCESSES (Luồng dọc):
  ┌─── CEO ───┐
  │ Chiến lược │ ← Top-down: giao mục tiêu, phân bổ ngân sách
  │ Mục tiêu   │
  └─────┬─────┘
        │
  ┌─────▼─────┐
  │ Managers  │
  │ Teams     │
  │ ICs       │ → Bottom-up: báo cáo, escalation, đề xuất
  └───────────┘

LATERAL PROCESSES (Luồng ngang):
  Engineering ←──────────────→ Marketing
        ↑                         ↑
        └──── Product ────────────┘
  Phối hợp liên chức năng — cắt ngang các phòng ban
```

### 4 cấp độ Lateral Processes (Galbraith)

| Cấp | Tên                        | Cơ chế                               | Mức phức tạp | Ví dụ                         |
| --- | -------------------------- | ------------------------------------ | ------------ | ----------------------------- |
| 1   | **Voluntary/Informal**     | Giao tiếp tự nhiên, không cấu trúc   | Thấp         | Hỏi đáp giữa 2 phòng ban      |
| 2   | **Cross-functional Teams** | Nhóm chính thức, meeting định kỳ     | Trung bình   | Sprint team đa chức năng      |
| 3   | **Integrator Roles**       | 1 người chuyên điều phối luồng ngang | Cao          | Product Manager, Scrum Master |
| 4   | **Matrix Organization**    | Dual reporting — mỗi người 2 boss    | Rất cao      | Dot-matrix, BU × Function     |

> **Nguyên tắc Galbraith:** *Chọn cấp độ lateral process **vừa đủ** cho mức complexity. Đừng dùng Matrix khi Cross-functional Teams đã đủ.*

---

## 2. Chuyển đổi: Processes trong AI-Agent Workforce

### 2.1. Vertical Processes → Workflow Tiering

Trong AI-Agent Workforce, luồng dọc **CHÍNH LÀ** Workflow Tiering:

```
TOP-DOWN (Tier 0 → Tier 3):
  CEO (con người)
    → Ra chiến lược, giao mục tiêu
    → Kích hoạt Tier 0 Meta-Workflow (/buildflow, /refactor)
    → Meta-Workflow tạo/cải tiến Tier 1+2+3
    → Tier 1 Orchestration (/content-post) phân công Tier 2
    → Tier 2 Execution (/content-post-p5-writing) thực thi
    → Tier 3 Utility (/flog, /beat) hỗ trợ

BOTTOM-UP (Tier 3 → Tier 0):
  Tier 2 Agent thực thi → phát hiện vấn đề
    → Escalation lên Tier 1 Director
    → Director không giải quyết được → Escalation lên CEO
    → CEO ra quyết định → Tier 0 Meta cập nhật hệ thống

LUỒNG THÔNG TIN DỌC:
  Top-down: Strategy ──→ Workflow Design ──→ Task Assignment ──→ Execution
  Bottom-up: Output ◄── Quality Report ◄── Escalation ◄── Sprint Log
```

**Ma trận luồng dọc:**

| Hướng         | Nội dung truyền tải           | Cơ chế trong AI-Agent                     |
| ------------- | ----------------------------- | ----------------------------------------- |
| **Top-down**  | Chiến lược, mục tiêu, ưu tiên | Sprint assignment, ToDo.md, Workflow call |
| **Top-down**  | Chuẩn hóa quy trình           | Skill file update, Workflow update        |
| **Top-down**  | Phân bổ nguồn lực             | Agent Provisioning, Skill Loading         |
| **Bottom-up** | Báo cáo kết quả               | Sprint artifacts, Changelog, Walkthrough  |
| **Bottom-up** | Escalation vấn đề             | `must_escalate` triggers                  |
| **Bottom-up** | Đề xuất cải tiến              | Knowledge Items, /learn output            |

### 2.2. Lateral Processes → Cross-calling + Backlinks

Lateral Processes trong AI-Agent dịch sang **4 cấp tương đương**, nhưng với cơ chế AI-native:

```
Cấp 1 (Galbraith): Voluntary/Informal
Cấp 1 (AI): SHARED KNOWLEDGE
  → Agent tự tra cứu Knowledge Items từ Cluster khác
  → Không cần "hỏi" — đọc KI index là đủ
  → Ví dụ: @Writer đọc KI "5Balance Architecture" trước khi viết
  → Mức phối hợp: Thấp — chỉ đọc, không tương tác
  → Khi nào đủ: Task cần info từ Cluster khác nhưng không cần output

Cấp 2 (Galbraith): Cross-functional Teams
Cấp 2 (AI): CROSS-CALLING
  → Agent Cluster A gọi Agent Cluster B qua Workflow interface
  → VD: /content-post gọi /extract-authority (Content → Research)
  → Mức phối hợp: Trung bình — tương tác 1 chiều
  → Khi nào đủ: Task cần output cụ thể từ Cluster khác

Cấp 3 (Galbraith): Integrator Roles
Cấp 3 (AI): ORCHESTRATION WORKFLOW
  → Tier 1 Workflow điều phối nhiều Agent từ nhiều Cluster
  → VD: /chain-build gọi /code (Eng) → /test (QA) → /deploy (Ops)
  → Mức phối hợp: Cao — quản lý luồng liên Cluster
  → Khi nào đủ: Pipeline cần output từ 3+ Cluster phối hợp

Cấp 4 (Galbraith): Matrix Organization
Cấp 4 (AI): FEDERATED MODEL + DYNAMIC CONTEXT
  → 1 Agent phục vụ nhiều BU đồng thời
  → VD: @Writer global, nạp context 5Balance KHI làm 5Balance
  → Mức phối hợp: Rất cao — Agent "sống" ở intersection
  → Khi nào dùng: Agent có skill universal + cần context multi-BU
```

---

## 3. Thiết kế Vertical Processes cho AI-Agent

### 3.1. Top-down: Cách CEO truyền chiến lược xuống Agent

```
CEO Decision
  │
  ├── [1] STRATEGY DOCUMENT
  │   Viết/cập nhật file chiến lược (Strategy.md)
  │   → Agent đọc khi bắt đầu task mới
  │   → Location: Context Folder > always_read
  │
  ├── [2] SPRINT ASSIGNMENT
  │   Tạo Sprint → giao nhiệm vụ cụ thể
  │   → Agent đọc Sprint_Plan.md, ToDo.md
  │   → Mỗi task có DoD (Definition of Done) rõ ràng
  │
  ├── [3] WORKFLOW UPDATE
  │   Sửa Workflow.md → thay đổi quy trình
  │   → Mọi Agent Owner tự động "được đào tạo lại"
  │   → Zero deployment — file update = process update
  │
  └── [4] SKILL UPDATE
      Sửa SKILL.md → thay đổi kiến thức
      → Agent nạp Skill mới ngay lần chạy tiếp
      → Đào tạo tức thì — không cần workshop
```

### 3.2. Bottom-up: Cách Agent báo cáo và escalation

```
Agent Execution
  │
  ├── [1] SPRINT ARTIFACTS
  │   Output lưu trong Sprint Folder
  │   → CEO review bất kỳ lúc nào
  │   → Bao gồm: Plan, TOL, Walkthrough
  │
  ├── [2] CHANGELOG UPDATE
  │   Agent tự cập nhật Changelog.md
  │   → CEO đọc Changelog = biết đã làm gì
  │   → Format: Date + Action + Result
  │
  ├── [3] ESCALATION TRIGGER
  │   Khi gặp điều kiện trong must_escalate:
  │   → Agent DỪNG → thông báo CEO
  │   → Kèm context: vấn đề gì, đã thử gì, cần quyết gì
  │   → CEO quyết → Agent tiếp tục
  │
  └── [4] KNOWLEDGE CREATION
      Sau task → /beat chưng cất kiến thức
      → KI mới hoặc cập nhật KI cũ
      → Index KI → Agent khác hưởng lợi
```

### 3.3. Escalation Protocol — Luồng dọc quan trọng nhất

**3 mức Escalation:**

```
Level 1: ROUTINE ESCALATION
  Trigger: Task nằm ngoài can_decide
  Action: Agent hỏi Director Agent
  Response time: Trong cùng session
  Ví dụ: @Writer muốn viết chủ đề mới → hỏi @MktLead

Level 2: CRITICAL ESCALATION
  Trigger: Director không giải quyết được
  Action: Director hỏi CEO (con người)
  Response time: Trong ngày
  Ví dụ: @MktLead phát hiện brand crisis → hỏi CEO

Level 3: EMERGENCY ESCALATION
  Trigger: Vấn đề ảnh hưởng production/security
  Action: Agent bất kỳ → CEO NGAY LẬP TỨC
  Response time: Tức thì — bypass mọi tầng
  Ví dụ: @DeployOps phát hiện security breach → CEO ngay
```

**Cấu hình Escalation trong Agent Definition:**

```yaml
interface:
  escalation:
    level_1:
      to: "@MktLead"
      conditions:
        - "Task ngoài can_decide scope"
        - "Output chất lượng thấp sau 2 lần thử"
    level_2:
      to: "CEO"
      conditions:
        - "@MktLead không giải quyết được"
        - "Quyết định ảnh hưởng > 1 BU"
    level_3:
      to: "CEO | IMMEDIATE"
      conditions:
        - "Security incident"
        - "Data loss risk"
        - "Brand damage risk"
```

### 3.4. Cảnh báo Red Team: Hố đen Escalation (Escalation Black Hole)

Nếu Agent gửi yêu cầu escalate lên cấp trên nhưng gặp lỗi hệ thống (Timeout, sập API, CEO không phản hồi), luồng xử lý sẽ bị treo vĩnh viễn và khóa cứng tài nguyên của tổ chức.

**Giải pháp:** Bắt buộc áp dụng **Timeout & Default Action**. Mỗi cơ chế escalation phải có thời gian chờ (Vd: "Đợi 15 phút"). Nếu quá hạn, Process bị cưỡng ép kết thúc và chuyển về trạng thái (Fallback) an toàn nhất — ví dụ: `abort_with_error_log` hoặc `skip_non_critical_step`.

---

## 4. Thiết kế Lateral Processes cho AI-Agent

### 4.1. Cấp 1: Shared Knowledge — Phối hợp thụ động

```
Cơ chế:
  Agent tự tra cứu Knowledge Items từ domain khác
  → Không cần tương tác trực tiếp
  → Chỉ cần KI được index tốt

Ưu điểm:
  → Không overhead phối hợp
  → Agent tự serve — không phụ thuộc Agent khác online

Nhược điểm:
  → KI có thể outdated
  → Thiếu nuance — KI không trả lời câu hỏi cụ thể

Khi nào dùng:
  → Task cần BỐI CẢNH từ domain khác
  → Không cần OUTPUT cụ thể từ Agent khác
  → VD: @Writer cần hiểu architecture 5Balance → đọc KI
```

### 4.2. Cấp 2: Cross-calling — Phối hợp 1 chiều

```
Cơ chế:
  Workflow A gọi Workflow B → nhận output → tiếp tục
  → Tương tác rõ ràng qua Interface Contract

Ưu điểm:
  → Output cụ thể, real-time
  → Interface Contract đảm bảo input/output rõ ràng

Nhược điểm:
  → Coupling — A phụ thuộc B
  → Nếu B fail → A bị block

Khi nào dùng:
  → Task cần OUTPUT CỤ THỂ từ Agent khác
  → VD: /content-post gọi /extract-authority → nhận trích dẫn

5 Cross-calling Patterns (tóm tắt từ Framework v2):
  [1] Sequential Chain: A → B → C → D
  [2] Router: /go → phân tích → gọi Agent phù hợp
  [3] Fork-Join: A → [B, C, D song song] → tổng hợp
  [4] Escalation Chain: A → thử → fail → B → fail → C
  [5] Callback: A → result → if ok: /update. if fail: /fix
```

### 4.3. Cấp 3: Orchestration Workflow — Phối hợp đa chiều

```
Cơ chế:
  Tier 1 Workflow điều phối nhiều Agent từ nhiều Cluster
  → Quản lý luồng, dependencies, quality gates
  → Tổng hợp output từ nhiều nguồn

Ưu điểm:
  → Phối hợp phức tạp được tự động hóa
  → 1 Orchestration Workflow = 1 "Project Manager ảo"

Nhược điểm:
  → Workflow phức tạp — khó debug khi fail
  → Dependency chain dài = rủi ro cascade

Khi nào dùng:
  → Task cần OUTPUT TỪ 3+ AGENT phối hợp
  → Output cuối cần tổng hợp/merge từ nhiều nguồn
  → VD: /chain-build: /code → /test → /deploy → /docs

Ví dụ chi tiết:
  /content-post (Tier 1 Orchestration):
    Step 1: /content-post-p1-idea         (MARKETING cluster)
    Step 2: /content-post-p2-research      (MARKETING cluster)
    Step 2b: /content-post-p2b-factcheck   (MARKETING → RESEARCH cross)
    Step 3: /content-post-p3-hook          (MARKETING cluster)
    Step 4: /content-post-p4-structure     (MARKETING cluster)
    Step 5: /content-post-p5-writing       (MARKETING cluster)
    Step 6: /content-post-p6-qa            (MARKETING → QA cross)
    Step 7: /content-post-p7-redteam       (MARKETING → EXTERNAL review)
    Step 8: /content-post-p8-format        (MARKETING cluster)
```

### 4.4. Cấp 4: Federated Model — Phối hợp cấu trúc

```
Cơ chế:
  1 Agent hoạt động xuyên suốt nhiều BU/Cluster
  → Global identity + Dynamic context loading
  → File system: Global (.agents/) + Override (.agent/)

Ưu điểm:
  → Tái sử dụng Agent cao nhất
  → Consistency — cùng methodology, khác context
  → Scale — thêm BU không cần thêm Agent

Nhược điểm:
  → Context switching overhead
  → Context window pollution nếu load quá nhiều BU context

Khi nào dùng:
  → Agent có SKILL UNIVERSAL
  → Nhiều BU đều cần Agent đó với cùng methodology
  → VD: @Writer viết cho 5Balance, Hoctap, Events → cùng skill, khác context

Cơ chế hoạt động:
  @Writer nhận task "Viết bài cho 5Balance":
    1. Load Global Profile → A_root_Writer/ (identity, core skills)
    2. Load BU Context → 05_5Balance/ (personas, product info)
    3. Load Project Skill → .agent/skills/ (5balance-design)
    4. Execute → output trong Sprint Folder
    5. Unload BU Context → sẵn sàng cho task BU khác
```

---

## 5. Ma trận chọn cấp Lateral Process

| Mức complexity task       | # Cluster liên quan | Cấp lateral khuyến nghị  |
| ------------------------- | ------------------- | ------------------------ |
| Thấp — 1 domain           | 1                   | Cấp 1 (Shared Knowledge) |
| Trung bình — cần 1 output | 2                   | Cấp 2 (Cross-calling)    |
| Cao — pipeline đa bước    | 3+                  | Cấp 3 (Orchestration)    |
| Rất cao — xuyên BU        | All                 | Cấp 4 (Federated Model)  |

> **Nguyên tắc Galbraith áp dụng cho AI:**
> *Chọn cấp lateral process VỪA ĐỦ. Đừng dùng Orchestration Workflow khi Cross-calling đã đủ. Đừng dùng Federated Model khi Orchestration đã đủ.*

---

## 6. Process Debt — Nợ quy trình

### 6.1. Khái niệm

Tương tự **Technical Debt**, Process Debt là tình trạng hệ thống Processes phát triển **nhanh hơn khả năng quản lý** — tạo ra shortcuts, gaps, và inconsistencies.

### 6.2. Dấu hiệu Process Debt

```
[ ] Workflow gọi Workflow khác nhưng KHÔNG khai báo calls/called_by
[ ] Agent cross-call Agent khác mà không qua Interface Contract rõ ràng
[ ] Escalation "ad-hoc" — Agent tự quyết khi nào hỏi CEO, khi nào không
[ ] Output từ Cluster A đến Cluster B nhưng không ai kiểm tra chất lượng trung gian
[ ] Knowledge Items outdated — Cấp 1 lateral process bị méo
[ ] Workflow Tier không rõ ràng — không biết đâu là Orchestration, đâu là Execution
[ ] Cross-calling circular: A → B → C → A (infinite loop)
[ ] "God Workflow" — 1 Orchestration Workflow gọi 20+ sub-workflows
```

### 6.3. Trả Process Debt

| Loại debt                | Cách trả                                   | Workflow hỗ trợ   |
| ------------------------ | ------------------------------------------ | ----------------- |
| Missing Interface        | Khai báo calls/called_by trong frontmatter | /doccheck, /stale |
| Circular dependency      | Vẽ dependency graph, cut loops             | /refactor         |
| Escalation inconsistency | Chuẩn hóa Autonomy Scope cho mọi Agent     | /rm /assess       |
| Knowledge outdated       | Chạy /beat extraction, retire KI cũ        | /beat, /learn     |
| Workflow proliferation   | Audit, merge, consolidate                  | /rm /audit        |
| Missing Quality Gate     | Thêm QA step vào mọi Tier 2 Workflow       | /test, /code      |

---

## 7. Anti-patterns Processes

### Anti-pattern 1: CEO as Router

```
❌ Mọi cross-cluster request đều qua CEO
→ CEO = bottleneck luồng ngang
→ FIX: Tạo Tier 1 Orchestration Workflows + Router (/go)
```

### Anti-pattern 2: Cross-calling Spaghetti

```
❌ Mọi Agent gọi mọi Agent khác — không có pattern
→ Không ai biết dependency graph
→ 1 Agent fail → cascade unpredictable
→ FIX: Interface Contract bắt buộc + Dependency Map
```

### Anti-pattern 3: Escalation Avoidance

```
❌ Agent không bao giờ escalate — tự xử lý mọi thứ (kể cả ngoài scope)
→ Agent hallucinate câu trả lời cho domain Agent không biết
→ CEO không bao giờ biết Agent đang gặp khó
→ FIX: Escalation Protocol rõ ràng + audit compliance
```

### Anti-pattern 4: Pipeline Overkill

```
❌ Task đơn giản (VD: sửa typo) phải chạy qua pipeline 8 bước
→ Overhead > giá trị
→ FIX: Dynamic Shape — task đơn giản = CEO → Specialist trực tiếp
```

---

## 8. Nguyên tắc Processes cho AI-Agent Workforce

| #       | Nguyên tắc                                     | Giải thích                                                    |
| ------- | ---------------------------------------------- | ------------------------------------------------------------- |
| **PR1** | **Vertical = Workflow Tiering**                | Luồng dọc chính là cách Workflow tầng trên gọi tầng dưới      |
| **PR2** | **Lateral = Cross-calling + Shared Knowledge** | Luồng ngang chính là cơ chế phối hợp liên Cluster             |
| **PR3** | **Vừa đủ — không quá mức**                     | Dùng cấp lateral thấp nhất đủ cho task. Đừng over-engineer    |
| **PR4** | **Interface Contract bắt buộc**                | Mọi cross-calling phải khai báo input/output/called_by        |
| **PR5** | **Escalation Protocol lập trình sẵn**          | Mỗi Agent biết chính xác KHI NÀO hỏi AI, KHI NÀO hỏi CEO      |
| **PR6** | **Trả Process Debt định kỳ**                   | Audit Workflow, dependency graph, KI freshness mỗi sprint     |
| **PR7** | **Bottom-up feedback loop**                    | Agent tạo KI, Sprint artifacts, Changelog → CEO nắm tình hình |
| **PR8** | **Dynamic routing, không cố định**             | /go router phân tích context → chọn Agent phù hợp nhất        |

---

## 9. Tổng kết: Bản đồ Processes toàn tổ chức

```
┌─────────────────────────────────────────────────────────────────┐
│                        CEO (Con người)                           │
│  ┌──────────────┐  ┌──────────────┐  ┌────────────────────┐   │
│  │ Giao chiến   │  │ Approve      │  │ Audit & Govern     │   │
│  │ lược/Sprint  │  │ escalation   │  │ /rm /refactor      │   │
│  └──────┬───────┘  └──────┬───────┘  └────────┬───────────┘   │
│         │ top-down         │ bottom-up          │ meta          │
├─────────┼──────────────────┼────────────────────┼───────────────┤
│         │                  │                    │               │
│  ┌──────▼──────────────────▼────────────────────▼─────────┐   │
│  │              TIER 1: ORCHESTRATION LAYER                │   │
│  │  /go (router) → /chain-build → /content-post → ...     │   │
│  │  Cross-cluster coordination                             │   │
│  └─────────────────────────┬───────────────────────────────┘   │
│                            │ cross-calling                      │
│  ┌─────────────────────────▼───────────────────────────────┐   │
│  │              TIER 2: EXECUTION LAYER                     │   │
│  │  @Writer  @FrontEnd  @SEO  @DeployOps  @PM  ...         │   │
│  │  Intra-cluster execution + Quality Gate                  │   │
│  └─────────────────────────┬───────────────────────────────┘   │
│                            │ utility calls                      │
│  ┌─────────────────────────▼───────────────────────────────┐   │
│  │              TIER 3: UTILITY LAYER                       │   │
│  │  /flog  /beat  /tomtat  /stale  /log                     │   │
│  │  Support services + Knowledge extraction                 │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                  │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │              SHARED SUBSTRATE                              │  │
│  │  Knowledge Items | Global Skills | Rules | Context Folders │  │
│  └───────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 10. Liên kết với các chương khác

- **Chương 1 (Specialization):** Specialist Agent cần lateral processes mạnh — vì mỗi output thường cần nhiều Specialist phối hợp
- **Chương 2 (Shape):** Tổ chức flat cần lateral processes mạnh hơn (không có tầng trung gian). Tổ chức tall có thể dùng vertical processes nhiều hơn
- **Chương 3 (Distribution of Power):** Vertical processes = cơ chế centralize (escalation). Lateral processes = cơ chế decentralize (cross-calling tự động)
- **Chương 4 (Departmentalization):** Intra-cluster dùng vertical processes chủ yếu. Cross-cluster dùng lateral processes
