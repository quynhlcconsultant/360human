# Chương 11: Hệ thống 5 thành phần — Agent, Workflow, Skill, Rules, Knowledge

> **Nguồn gốc:** Concepts MỚI — Thay thế People Policies (Recruiting, Training, Staffing)
> **Câu hỏi cốt lõi:** *"DNA" của AI Agent Workforce gồm những gì?*

---

## 1. Tại sao cần 5 thành phần?

Trong tổ chức con người, "People" có sẵn: bộ não (kiến thức), thói quen (quy trình), tính cách (identity), ký ức (kinh nghiệm), và luân lý (quy tắc).

AI Agent **không có sẵn gì**. Mọi thứ phải được **thiết kế và cấp phát**.

| Con người tự có      | AI Agent cần được cấp  | → Thành phần  |
| -------------------- | ---------------------- | ------------- |
| Identity, tính cách  | System Prompt, Mission | **Agent**     |
| Quy trình làm việc   | Workflow file (.md)    | **Workflow**  |
| Kiến thức chuyên môn | SKILL.md               | **Skill**     |
| Luân lý, kỷ luật     | MEMORY files, Rules    | **Rules**     |
| Kinh nghiệm, ký ức   | Knowledge Items (KI)   | **Knowledge** |

---

## 2. Định nghĩa 5 thành phần

### 2.1. Agent — "Nhân viên"

```
Định nghĩa: Một thực thể AI được cấu hình để thực thi vai trò cụ thể trong tổ chức.

Ẩn dụ: Agent = "Nhân viên" — có tên, chức danh, nhiệm vụ, phạm vi, giao tiếp.

Bao gồm:
  → System Prompt (não — identity + instructions)
  → Skill Profile (kiến thức chuyên môn — SKILL.md files)
  → Workflow Ownership (quy trình sở hữu)
  → Context Folder (ngữ cảnh làm việc)
  → Agent Folder (hồ sơ cá nhân)

Ví dụ: @Writer, @EngLead, @PM, @AI_RM, @DeployOps
```

### 2.2. Workflow — "Quy trình"

```
Định nghĩa: Một chuỗi bước có cấu trúc, mô tả CÁC BƯỚC để hoàn thành 1 loại task.

Ẩn dụ: Workflow = "SOP" (Standard Operating Procedure)

Bao gồm:
  → YAML Frontmatter (metadata: description, tier, owner, calls, called_by)
  → Markdown Body (các bước thực hiện chi tiết)
  → Turbo annotations (auto-run markers)
  → Slash command trigger (VD: /deploy, /content-post)

Tính chất:
  → Workflow KHÔNG PHẢI Agent. Workflow là "kịch bản". Agent là "diễn viên".
  → 1 Workflow có thể được nhiều Agent thực thi
  → 1 Agent có thể own nhiều Workflow

Ví dụ: /deploy, /content-post, /test, /fix, /buildflow
```

### 2.3. Skill — "Kiến thức chuyên môn"

```
Định nghĩa: Một gói kiến thức chuyên sâu, được đóng gói và nạp vào Agent.

Ẩn dụ: Skill = "Sách giáo khoa" — Agent đọc và áp dụng

Bao gồm:
  → SKILL.md (file chính — quy tắc, kiến thức, hướng dẫn)
  → Thư mục phụ trợ (scripts/, examples/, resources/)
  → YAML Frontmatter (name, description)

Tính chất:
  → Skill KHÔNG CHẠY. Skill là "kiến thức" nạp vào Agent.
  → Agent đọc Skill → hiểu → áp dụng vào Workflow
  → 1 Skill có thể nạp cho nhiều Agent
  → Skill phải immutable — chỉ Architect/Trainer mới sửa

3 loại Skill:
  → Core Skills: Mọi Agent bắt buộc (ngôn ngữ, quy tắc chung)
  → Functional Skills: Theo vai trò (copywriting, engineering, marketing)
  → Domain Skills: Theo BU/dự án (bazi-engine, 5balance-design)

Ví dụ: copywriting/, marketing-psychology/, arch-guard/, 5balance-design/
```

### 2.4. Rules — "Hiến pháp"

```
Định nghĩa: Các quy tắc BẮT BUỘC mà MỌI Agent phải tuân thủ, không ngoại lệ.

Ẩn dụ: Rules = "Hiến pháp" — luật tối cao, không ai sửa ngoài CEO

Bao gồm:
  → MEMORY files (global rules — áp dụng cho mọi Agent)
  → Project-level rules (áp dụng cho 1 BU cụ thể)
  → Agent-specific rules (áp dụng cho 1 Agent cụ thể)

Tính chất:
  → Rules LUÔN CENTRALIZE — chỉ CEO/Architect sửa
  → Rules inject vào System Prompt của mọi Agent
  → Agent không được diễn giải Rules theo cách riêng
  → Thay đổi Rules = thay đổi nền tảng toàn tổ chức

Ví dụ:
  → "Luôn trả lời bằng tiếng Việt"
  → "Sprint-centric: mọi task phải thuộc 1 sprint cụ thể"
  → "Think-out-loud: luôn ghi lại quá trình suy luận"
```

### 2.5. Knowledge — "Bộ nhớ tập thể"

```
Định nghĩa: Kiến thức được chưng cất từ kinh nghiệm làm việc, tích lũy theo thời gian.

Ẩn dụ: Knowledge = "Thư viện kinh nghiệm" — bất kỳ Agent nào cũng truy cập được

Bao gồm:
  → Knowledge Items (KI) — mỗi KI = 1 chủ đề
  → metadata.json (tóm tắt, timestamp, references)
  → artifacts/ (tài liệu chi tiết)

Tính chất:
  → Knowledge DO Agent TẠO — nhưng được "thủ thư" quản lý chất lượng
  → Knowledge là PERSISTENT — tồn tại qua nhiều conversation
  → Mọi Agent đều đọc được — DECENTRALIZE truy cập
  → Chất lượng được kiểm soát — CENTRALIZE quản trị

Ví dụ: "5Balance Architecture", "Content Factory Pipeline", "Deployment Standards"
```

---

## 3. Quan hệ giữa 5 thành phần

```
                    ┌─── RULES ───┐
                    │ (Hiến pháp)  │
                    │ Áp dụng cho │
                    │ MỌI Agent   │
                    └──────┬──────┘
                           │
              ┌────────────▼────────────┐
              │         AGENT           │
              │  (Nhân viên — Diễn viên) │
              │  Đọc Rules              │
              │  Nạp Skills             │
              │  Sở hữu Workflows      │
              │  Truy cập Knowledge     │
              └──┬────────┬────────┬───┘
                 │        │        │
         ┌───────▼──┐ ┌───▼────┐ ┌─▼────────┐
         │  SKILL   │ │WORKFLOW│ │KNOWLEDGE │
         │(Sách giáo│ │  (SOP) │ │(Thư viện)│
         │  khoa)   │ │        │ │          │
         └──────────┘ └────────┘ └──────────┘
```

### Ma trận quan hệ

| Từ \ Đến      | Agent       | Workflow   | Skill         | Rules    | Knowledge  |
| ------------- | ----------- | ---------- | ------------- | -------- | ---------- |
| **Agent**     | Cross-call  | Thực thi   | Nạp & áp dụng | Tuân thủ | Đọc & tạo  |
| **Workflow**  | Giao cho    | Cross-call | Tham chiếu    | Tuân thủ | Tham chiếu |
| **Skill**     | Nạp vào     | Hỗ trợ     | —             | Tuân thủ | Tham chiếu |
| **Rules**     | Áp dụng lên | Ràng buộc  | Ràng buộc     | —        | —          |
| **Knowledge** | Phục vụ     | Hỗ trợ     | Bổ sung       | —        | Liên kết   |

---

## 4. So sánh: Skill vs Workflow vs Rules vs Knowledge

| Tiêu chí         | Skill                   | Workflow                | Rules            | Knowledge            |
| ---------------- | ----------------------- | ----------------------- | ---------------- | -------------------- |
| **Bản chất**     | Kiến thức (BIẾT)        | Quy trình (LÀM)         | Ràng buộc (PHẢI) | Kinh nghiệm (NHỚ)    |
| **Format**       | SKILL.md                | workflow.md + YAML      | MEMORY file      | KI (metadata + docs) |
| **Ai tạo**       | Architect/Trainer       | Architect               | CEO              | Mọi Agent + Thủ thư  |
| **Ai sửa**       | Architect/Trainer       | Architect               | CEO              | Thủ thư              |
| **Agent đọc?**   | Có — khi được assign    | Có — khi được giao task | Có — LUÔN LUÔN   | Có — khi cần         |
| **Tần suất sửa** | Thấp (mature = ổn định) | Trung bình              | Rất thấp         | Liên tục (tích lũy)  |
| **Scope**        | Functional hoặc Domain  | Task-specific           | Global hoặc BU   | Topic-specific       |

---

## 5. Lifecycle: Vòng đời của mỗi thành phần

### Agent Lifecycle

```
Provisioning → Skill Loading → Assign Workflow → Active Duty → Audit → Re-configure / Decommission
```

### Workflow Lifecycle

```
Design → Build (/buildflow) → Test → Deploy → Monitor → Optimize / Retire
```

### Skill Lifecycle (Source Library → Adopt → Backup)

```
Stage 1: TRAINING (Skill trong AI_Hub/Skill_Hub — chưa ai dùng)
  → Skill được tạo, biên tập, version control
  → Chưa assign cho Agent nào

Stage 2: ADOPT (Skill được assign cho Agent cụ thể)
  → Copy/link vào Agent's context
  → Agent bắt đầu sử dụng

Stage 3: BACKUP (Skill cũ, vẫn giữ nhưng không active)
  → Khi Skill bị thay thế bởi phiên bản mới
  → Archive, không xóa
```

### 5.2. Cảnh báo Red Team: Skill Rot (Kỹ năng thối rữa)

Nếu môi trường thay đổi liên tục, việc quy định Skill là "Immutable" (Bất biến) đối với Agent sẽ khiến hệ thống bị trói tay (ví dụ: API đổi version).
**Giải pháp:** Bắt buộc áp dụng **Skill Evolution Protocol**. Dù Agent không được phép tự ý sửa `SKILL.md` (chỉ Architect được sửa), Agent BẮT BUỘC phải có quyền lập "Pull Request" (đề xuất nâng cấp) hoặc gửi feedback cho Architect/Trainer khi phát hiện Skill bị lỗi thời.

### Knowledge Lifecycle

```
Create (/beat) → Index → Active Use → Review → Update / Retire
```

---

## 6. Anti-patterns

### Anti-pattern 1: Agent without Skill

```
❌ Tạo Agent nhưng không gán Skill → Agent "không biết gì"
→ Output generic, không chuyên sâu
→ FIX: Mọi Agent phải có ≥ 1 Functional Skill
```

### Anti-pattern 2: Skill Explosion

```
❌ 200 Skill files không ai quản lý → overlap, conflict, outdated
→ FIX: Tri-Hub Architecture (Skill Hub + audit định kỳ)
```

### Anti-pattern 3: Workflow without Owner

```
❌ Workflow tồn tại nhưng không Agent nào own → không ai maintain
→ FIX: Mọi Workflow phải có owner: "@AgentName" trong YAML
```

### Anti-pattern 4: Rules Drift

```
❌ Rules trong MEMORY file nói "tiếng Việt" nhưng Agent vẫn trả lời tiếng Anh
→ Rules không được enforce
→ FIX: Audit compliance định kỳ
```

---

## 7. Nguyên tắc 5 thành phần

| #       | Nguyên tắc                                        | Giải thích                                           |
| ------- | ------------------------------------------------- | ---------------------------------------------------- |
| **FC1** | **Agent = Diễn viên, Workflow = Kịch bản**        | Phân tách rõ "ai" và "làm gì". Đừng trộn lẫn         |
| **FC2** | **Skill = Immutable Knowledge**                   | Chỉ Architect sửa. Agent chỉ đọc và áp dụng          |
| **FC3** | **Rules = Hiến pháp — LUÔN CENTRALIZE**           | Không ngoại lệ. CEO sửa, mọi Agent tuân thủ          |
| **FC4** | **Knowledge = Bộ nhớ tập thể — Decentralize tạo** | Mọi Agent tạo KI, thủ thư quản lý chất lượng         |
| **FC5** | **Mọi Workflow phải có Owner**                    | Workflow vô chủ = workflow sẽ chết                   |
| **FC6** | **Mọi Agent phải có ≥ 1 Skill**                   | Agent không có Skill = nhân viên không có chuyên môn |

---

## 8. Liên kết với các chương khác

- **Chương 3 (AGENT STAR):** 5 thành phần là DNA của cánh sao Capabilities
- **Chương 4 (Specialization):** Specialist Agent = Agent với Skill Profile sâu ở 1 domain
- **Chương 6 (Distribution of Power):** Rules luôn centralize. Knowledge decentralize tạo/đọc
- **Chương 9 (Workflow Tiering):** Workflow là 1 trong 5 thành phần, phân tầng theo Tier 0-3
- **Chương 12 (Agent Anatomy):** Chi tiết 11 Elements cấu thành 1 Agent
