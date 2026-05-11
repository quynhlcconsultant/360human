# Chương 13: Context & Knowledge — Bộ nhớ của tổ chức

> **Nguồn gốc:** Concepts MỚI — "Bộ nhớ" là khái niệm con người có sẵn, AI phải thiết kế
> **Câu hỏi cốt lõi:** *Agent "nhớ" bằng gì? Kiến thức tổ chức được tích lũy và chia sẻ thế nào?*

---

## 1. Bài toán "bộ nhớ" trong AI-Agent Workforce

| Con người                                  | AI Agent                                                |
| ------------------------------------------ | ------------------------------------------------------- |
| Nhớ tự nhiên — kinh nghiệm tích lũy        | **Không nhớ** giữa các session — mỗi lần = "mới sinh"   |
| Tribal knowledge — "biết nhưng không viết" | Không có tribal knowledge — chỉ biết **cái đã viết ra** |
| Giao tiếp phi cấu trúc (chat, meeting)     | Giao tiếp qua **Workflow, Backlinks, Context Folders**  |
| Học từ kinh nghiệm                         | "Học" = **nạp Knowledge Items từ session trước**        |

**Hệ quả:** Trong AI-Agent Workforce, phải thiết kế **3 tầng bộ nhớ**:

```
Tầng 1: CONTEXT FOLDER — Bộ nhớ ngắn hạn (session-level)
Tầng 2: AGENT FOLDER — Bộ nhớ vai trò (role-level)
Tầng 3: KNOWLEDGE ITEMS — Bộ nhớ dài hạn (organization-level)
```

---

## 2. Tầng 1: Context Folder — Bộ nhớ ngắn hạn

### 2.1. Định nghĩa

Context Folder là thư mục chứa **tài liệu ngữ cảnh** mà Agent đọc khi bắt đầu task. Nó quyết định Agent "thấy" gì.

### 2.2. Cấu trúc chuẩn

```
.agent/ hoặc .agents/
├── workflows/           ← Quy trình khả dụng
├── skills/              ← Kiến thức chuyên môn
└── context/             ← Tài liệu ngữ cảnh
    ├── always_read/     ← Đọc MỌI LÚC (strategy, personas, rules)
    ├── on_demand/       ← Đọc KHI CẦN (technical docs, API specs)
    └── project/         ← Context riêng cho project hiện tại
```

### 2.3. Federated Context (Global + Project)

```
Agent @Writer bắt đầu task "Viết bài cho 5Balance":

  1. Load Global Context:
     ← .agents/skills/copywriting/SKILL.md         (Core Skill)
     ← .agents/context/always_read/Strategy.md      (Chiến lược chung)

  2. Load Project Context:
     ← 05_5Balance/.agent/skills/5balance-design/   (Domain Skill)
     ← 05_5Balance/.agent/context/personas/          (Persona 5Balance)
     ← 05_5Balance/.agent/context/product-info.md    (Sản phẩm 5Balance)

  3. Agent "nhìn thấy":
     → Skill copywriting + strategy + design tokens + personas + product info
     → KHÔNG nhìn thấy: Hoctap.tech context, Events context
```

### 2.4. Nguyên lý Dual-Level Briefing (Tổng quan 2 lớp)

Một Best Practice cốt lõi để giữ các AI Agent không bị lạc lối là **luôn tạo Brief tổng quan để các Agent load lại chúng vào đầu mỗi phiên làm việc**. 
Overview Context này được duy trì chặt chẽ ở hai lớp (Dual-Level):
- **Lớp Dự án (Project-level Context):** File bối cảnh toàn dự án (vd: `Product_Context.md`), load cố định ở mức độ `always_read` hoặc được ghim vào Prompts hệ thống.
- **Lớp Phiên làm việc (Sprint-level Context):** File nằm trong Sprint folder (vd: `Sprint_Plan.md`), chứa ngữ cảnh sống động của phiên làm việc hiện tại, mục tiêu ngắn hạn.

Việc thiết lập "mỏ neo" ngữ cảnh 2 lớp này giúp AI vừa có tầm nhìn xa (mục tiêu cốt lõi) vừa có tầm nhìn gần (task trong ngày) mà không bị đứt gãy.

### 2.5. Context Window Pollution — Vấn đề lớn nhất

```
❌ Nạp TẤT CẢ context cho mọi task:
  → 50 Skill files + 20 Strategy docs + 10 Persona files = NGHẼN
  → Agent "quên" instructions vì context quá dài
  → Output quality giảm vì attention bị phân tán

✅ Progressive Loading:
  → always_read: Chỉ 3-5 files tối quan trọng (< 10% context window)
  → on_demand: Nạp KHI Agent thực sự cần
  → project: Chỉ nạp project đang làm
```

---

## 3. Tầng 2: Agent Folder — Bộ nhớ vai trò

### 3.1. Định nghĩa

Agent Folder là "hồ sơ cá nhân" của mỗi Agent — chứa thông tin về vai trò, lịch sử hoạt động, và ghi chú.

### 3.2. Cấu trúc chuẩn

```
A_root_Writer/                    ← Agent Folder cho @Writer
├── JD.md                         ← Job Description (11 Elements)
├── ToDo.md                       ← Task đang làm
├── Changelog.md                  ← Lịch sử hoạt động
├── Notes.md                      ← Ghi chú, learnings
└── INDEX.md                      ← Tóm tắt nhanh

Mục đích:
  → Agent đọc JD.md → biết "mình là ai"
  → Agent đọc ToDo.md → biết "mình đang làm gì"
  → Agent đọc Notes.md → biết "mình đã học gì"
  → CEO đọc Changelog.md → biết "Agent này đã làm gì"
```

### 3.3. Agent Folder vs Context Folder

| Chiều            | Context Folder                     | Agent Folder                      |
| ---------------- | ---------------------------------- | --------------------------------- |
| **Chứa gì?**     | Tài liệu NGOÀI Agent (project)     | Tài liệu VỀ Agent (identity, log) |
| **Ai đọc?**      | Agent + CEO                        | Agent + CEO + @AI_RM              |
| **Tầm nhìn**     | Task-level (thay đổi theo project) | Role-level (cố định theo Agent)   |
| **Cập nhật bởi** | Architect/CEO                      | Agent tự cập nhật                 |

---

## 4. Tầng 3: Knowledge Items — Bộ nhớ dài hạn

### 4.1. Định nghĩa

Knowledge Items (KI) là kiến thức được **chưng cất từ kinh nghiệm làm việc**, tồn tại lâu dài qua nhiều session, phục vụ toàn bộ tổ chức.

### 4.2. Cấu trúc 1 Knowledge Item

```
knowledge/
├── topic_name/
│   ├── metadata.json      ← Summary, timestamps, references
│   └── artifacts/
│       ├── overview.md     ← Tổng quan
│       ├── detail_1.md     ← Chi tiết aspect 1
│       ├── detail_2.md     ← Chi tiết aspect 2
│       └── ...
```

### 4.3. Lifecycle

```
CREATE → INDEX → ACTIVE USE → REVIEW → UPDATE / RETIRE

Create:
  → Agent chạy /beat → chưng cất kinh nghiệm → tạo KI mới
  → Hoặc Knowledge Subagent tự động tạo sau mỗi conversation

Index:
  → KI được đánh index → xuất hiện trong KI summaries
  → Mọi Agent đầu session đều nhận KI summaries

Active Use:
  → Agent tra cứu KI khi gặp chủ đề liên quan
  → "Trước khi nghiên cứu, kiểm tra KI đã có chưa"

Review:
  → Thủ thư (@AI_RM) audit KI định kỳ
  → Kiểm tra: outdated? overlap? conflict?

Update / Retire:
  → Update: thêm insights mới vào KI hiện có
  → Retire: KI không còn relevant → archive
```

### 4.4. Backlinks — Liên kết giữa các KI

```
KI "5Balance Architecture" tham chiếu:
  → KI "SePay Integration" (payment flow)
  → KI "Content Factory" (content pipeline)
  → Conversation c65d0906... (discussion about structure)

Backlinks giúp:
  → Tra cứu nhanh — "KI này liên quan KI nào?"
  → Phát hiện knowledge gaps — "KI này thiếu liên kết?"
  → Prevent duplication — "KI mới có trùng KI cũ?"
```

### 4.5. Cảnh báo Red Team: Ảo tưởng vào sự Tự giác (Amnesia)

Trông cậy vào việc Agent tự giác gọi lệnh `/beat` sau mỗi phiên làm việc là tư duy "Human-centric". LLM rất hay quên bước cuối cùng do Context Window quá tải hoặc lỗi giữa tiến trình. Nếu quên, Knowledge sẽ bốc hơi.

**Giải pháp:** Tổ chức không dựa vào sự tự giác. Phải có **Automated State Memory (Auto-beat Hook)** ở cấp độ hạ tầng (Infrastructure). Khi một Orchestration Workflow (Tier 1) chạm cờ `[x] Hoàn thành`, hệ thống tự động trigger nền (background process) để trích xuất Knowledge mà không cần đợi Agent gõ lệnh.

---

## 5. Nguyên tắc 3 tầng bộ nhớ

```
NGUYÊN TẮC PHÂN TẦNG:

  Câu hỏi: "Thông tin này CẦN TỒN TẠI bao lâu?"

  → Chỉ trong task hiện tại     → Context Folder (Tầng 1)
  → Suốt vòng đời Agent         → Agent Folder (Tầng 2)
  → Mãi mãi, cho toàn tổ chức   → Knowledge Items (Tầng 3)

NGUYÊN TẮC TRUY CẬP:

  → Tầng 1: Agent tự đọc khi bắt đầu task
  → Tầng 2: Agent tự đọc khi cần biết "mình là ai"
  → Tầng 3: Agent tra cứu khi cần kiến thức tổ chức

NGUYÊN TẮC CẬP NHẬT:

  → Tầng 1: Architect/CEO cập nhật
  → Tầng 2: Agent tự cập nhật (Changelog, Notes)
  → Tầng 3: Mọi Agent tạo, Thủ thư quản lý chất lượng
```

---

## 6. Anti-patterns

### Anti-pattern 1: Amnesia — Không có Knowledge System

```
❌ Agent giải quyết vấn đề → session kết thúc → mọi kinh nghiệm biến mất
→ Lần sau gặp lại vấn đề → giải từ đầu
→ FIX: /beat extraction sau mỗi session quan trọng
```

### Anti-pattern 2: Context Dump — Nạp tất cả

```
❌ Agent bắt đầu task → nạp toàn bộ 100 KI + 50 Skills
→ Context window bão hòa → output quality giảm
→ FIX: Progressive Loading — always_read (ít) + on_demand (khi cần)
```

### Anti-pattern 3: Stale Knowledge — KI outdated

```
❌ KI "Deploy Process v1" vẫn active sau khi deploy process thay đổi
→ Agent làm theo KI cũ → sai
→ FIX: /stale audit + KI versioning
```

### Anti-pattern 4: Orphan Knowledge — KI không ai đọc

```
❌ 200 KI tồn tại, 150 KI không ai tra cứu
→ Lãng phí index space, gây noise
→ FIX: Audit access frequency → retire KI không ai dùng
```

---

## 7. Nguyên tắc Context & Knowledge

| #       | Nguyên tắc                                | Giải thích                                                 |
| ------- | ----------------------------------------- | ---------------------------------------------------------- |
| **CK1** | **3 tầng bộ nhớ bắt buộc**                | Context (ngắn hạn) + Agent Folder (vai trò) + KI (dài hạn) |
| **CK2** | **Progressive Loading**                   | Chỉ nạp context cần thiết — tránh pollution                |
| **CK3** | **Write First, Remember Forever**         | Chưa viết ra = chưa tồn tại. KI phải persist               |
| **CK4** | **Decentralize tạo, Centralize quản trị** | Mọi Agent tạo KI, Thủ thư giữ chất lượng                   |
| **CK5** | **Audit KI định kỳ**                      | Detect outdated, orphan, overlap → maintain quality        |
| **CK6** | **Backlinks bắt buộc**                    | KI phải liên kết với nhau → navigable knowledge graph      |

---

## 8. Liên kết với các chương khác

- **Chương 6 (Distribution of Power):** Knowledge decentralize tạo, centralize quản trị
- **Chương 8 (Processes):** Knowledge Items = cấp 1 lateral process (Shared Knowledge)
- **Chương 11 (Five Components):** Knowledge là 1 trong 5 thành phần core
- **Chương 12 (Agent Anatomy):** Context Scope (Element 6) quyết định Agent "nhìn thấy" gì
- **Chương 15 (Operational Principles):** SSOT áp dụng cho Knowledge — 1 KI per topic
