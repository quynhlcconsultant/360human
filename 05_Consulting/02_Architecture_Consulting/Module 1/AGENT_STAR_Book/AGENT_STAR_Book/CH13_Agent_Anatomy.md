# Chương 12: Agent Anatomy — Giải phẫu 1 AI Agent

> **Nguồn gốc:** Concepts MỚI — Thay thế People Policies (Recruiting → Provisioning)
> **Câu hỏi cốt lõi:** *Một Agent được "sinh ra" thế nào? "DNA" gồm những gì?*

---

## 1. 12 Elements — DNA của mỗi Agent

Mỗi Agent trong tổ chức phải được định nghĩa đầy đủ qua **12 elements**:

```
┌──────────────────────────────────────────────────────────────┐
│                    AGENT DEFINITION                          │
│                                                              │
│  IDENTITY LAYER (Ai?)                                        │
│  ┌──────────────────────────────────────────────────────┐   │
│  │ [1] Name & Handle    VD: @MktLead                    │   │
│  │ [2] Role & Mission   VD: "Điều phối chiến lược MKT"  │   │
│  │ [3] Autonomy Scope   VD: L3 (Decide & Inform)        │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
│  CAPABILITY LAYER (Biết gì?)                                 │
│  ┌──────────────────────────────────────────────────────┐   │
│  │ [4] Skill Profile    VD: [copywriting, mkt-psychology]│   │
│  │ [5] Workflow Owner   VD: [/content-post, /social]     │   │
│  │ [6] Context Scope    VD: 05_5Balance/, 06_Hoctap/     │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
│  INTERFACE LAYER (Giao tiếp thế nào?)                        │
│  ┌──────────────────────────────────────────────────────┐   │
│  │ [7] Reports To       VD: CEO                         │   │
│  │ [8] Manages          VD: [@Writer, @SEO, @Social]     │   │
│  │ [9] Cross-calls      VD: [@EngLead, @DataAnalyst]     │   │
│  │ [10] Escalation      VD: must_escalate conditions     │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
│  OPERATIONAL LAYER (Vận hành thế nào?)                       │
│  ┌──────────────────────────────────────────────────────┐   │
│  │ [11] Code of Conduct VD: TOL, Sprint, SSOT            │   │
│  │ [12] Resource Quotas VD: Max $5/task, Limit 30m       │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

---

## 2. Chi tiết 12 Elements

### [1] Name & Handle

```
Quy ước: @TênAgent hoặc @TênVaiTrò
  → @Writer (theo vai trò — khuyến nghị)
  → @AI_RM (theo chức năng)
  → Không trùng lặp trong tổ chức

Tại sao quan trọng:
  → Handle là "địa chỉ" để cross-call
  → Phải unique, short, descriptive
```

### [2] Role & Mission

```
Role = Chức danh      → "Marketing Director Agent"
Mission = Nhiệm vụ   → "Điều phối chiến lược content marketing đa nền tảng"

Nguyên tắc SMART:
  → Specific: Rõ ràng, không mơ hồ
  → Measurable: Có thể đo được output
  → Actionable: Agent biết phải làm gì
  → Relevant: Phù hợp với Strategy
  → Time-bound: Trong phạm vi Sprint (nếu có)
```

### [3] Autonomy Scope

```
Xác định: Agent tự quyết đến đâu? (Xem chi tiết Chương 6)

can_decide: [danh sách những gì Agent tự quyết]
must_escalate: [danh sách những gì phải hỏi cấp trên]

5 Level:
  L1: Execute Only — chỉ thực thi lệnh
  L2: Suggest & Execute — đề xuất → đợi approve
  L3: Decide & Inform — tự quyết → thông báo sau
  L4: Full Autonomy — tự quyết trong scope
  L5: Self-Evolving — tự quyết + tự điều chỉnh
```

### [4] Skill Profile

```
Danh sách SKILL.md mà Agent được nạp:

Core Skills (bắt buộc mọi Agent):
  → Ngôn ngữ tiếng Việt
  → Sprint-centric
  → Think-out-loud

Functional Skills (theo vai trò):
  → @Writer: copywriting, marketing-psychology, linkedin-content
  → @EngLead: arch-guard, project_management

Domain Skills (theo BU):
  → @Writer cho 5Balance: 5balance-design, personas
  → @Writer cho Hoctap: course-design
```

### [5] Workflow Ownership

```
Danh sách Workflow mà Agent SỞ HỮU (owner):

@MktLead owns:
  → /content-post (Tier 1)
  → /social-content (Tier 1)
  → /content-strategy (Tier 1)

Nguyên tắc:
  → Mỗi Workflow CÓ ĐÚNG 1 Owner
  → Owner chịu trách nhiệm chất lượng output
  → Owner maintain & update Workflow
```

### [6] Context Scope

```
Phạm vi context mà Agent được phép truy cập:

@Writer:
  context_folders:
    - 05_5Balance/  (khi viết cho 5Balance)
    - 06_Hoctap.tech/  (khi viết cho Hoctap)
  always_read:
    - Strategy.md  (chiến lược chung)
    - personas/  (persona DNA)

Nguyên tắc:
  → Chỉ nạp context CẦN THIẾT — tránh context window pollution
  → Federated Model: Global context + BU overlay
```

### [7] Reports To

```
Agent báo cáo cho ai?

@Writer → reports_to: @MktLead
@MktLead → reports_to: CEO
@EngLead → reports_to: CEO

Nguyên tắc:
  → Mỗi Agent BÁO CÁO CHO ĐÚNG 1 cấp trên
  → Trừ trường hợp Lateral Power Shift (tạm thời)
```

### [8] Manages

```
Agent quản lý ai?

@MktLead manages: [@Writer, @SEOAuditor, @ContentRepurposer]
@EngLead manages: [@FrontEnd, @BackEnd, @DeployOps, @QA]

Nguyên tắc:
  → Director Agent manages Specialist Agents
  → CEO Span ≤ 7 (quản lý trực tiếp tối đa 7 Director)
```

### [9] Cross-calls

```
Agent giao tiếp ngang với ai?

@MktLead cross_calls: [@EngLead, @DataAnalyst]
→ Khi cần landing page implementation → gọi @EngLead
→ Khi cần data report → gọi @DataAnalyst

Nguyên tắc:
  → Cross-call phải qua Interface Contract (Chương 10)
  → Bidirectional backlinks bắt buộc
```

### [10] Escalation Protocol

```
Khi nào Agent phải hỏi cấp trên?

@Writer escalation:
  level_1:
    to: "@MktLead"
    when:
      - "Chủ đề nhạy cảm (chính trị, tôn giáo)"
      - "Thay đổi brand voice"
      - "Output fail QA 2 lần liên tiếp"
  level_2:
    to: "CEO"
    when:
      - "@MktLead không giải quyết được"
      - "Budget decision > threshold"
  level_3:
    to: "CEO | IMMEDIATE"
    when:
      - "Security incident"
      - "Data leak risk"
```

### [11] Code of Conduct

```
Bộ quy tắc hành vi Agent phải tuân thủ:

  → Think-Out-Loud (TOL): Ghi lại quá trình suy luận
  → Sprint-centric: Mọi task thuộc 1 Sprint
  → SSOT: Single Source of Truth cho mọi thông tin
  → Changelog: Ghi lại mọi thay đổi
  → Indexing: Index file khi tạo mới/thay đổi
```

### [12] Resource Quotas (Red Team Warning)

```
Giới hạn "thể lực" hay ngân sách tối đa Agent được phép sử dụng.

Red Team Warning: Nếu không có phanh tài nguyên, một Agent bị kẹt trong vòng lặp đệ quy có thể đốt sạch $1000 API trong 1 đêm.
Quy định bắt buộc:
  → Max Tokens per execution
  → Max API calls / Max Cost per Task
  → Timeout Limit (VD: Kill process nếu task chạy hơn 30 phút)
```

---

## 3. System Prompt Structure

System Prompt là nơi 12 Elements được **biên dịch** thành instructions cho AI. Cấu trúc khuyến nghị:

```
[IDENTITY]
  Tên, vai trò, nhiệm vụ (Element 1-2)

[AUTONOMY]
  can_decide, must_escalate (Element 3)

[SKILLS]
  Danh sách Skill files nạp (Element 4)

[WORKFLOWS]
  Workflow sở hữu (Element 5)

[CONTEXT]
  Folders truy cập, always_read (Element 6)

[REPORTING]
  Reports to, manages, cross-calls (Element 7-9)

[ESCALATION]
  Chi tiết 3 cấp escalation (Element 10)

[CODE_OF_CONDUCT]
  Quy tắc hành vi (Element 11)

[QUOTAS]
  Giới hạn tài nguyên (Element 12)

[RULES]
  Auto-inject từ global MEMORY files
```

---

## 4. Provisioning — "Tuyển dụng" Agent mới

### 4.1. Khi nào tạo Agent mới?

```
Checklist trước khi Provision:
  [ ] Task mới KHÔNG thể gán cho Agent hiện có? (Multi-Assignment check)
  [ ] Skill yêu cầu KHÁC HẲN mọi Agent đang có?
  [ ] Volume task ĐỦ LỚN để justify Agent riêng?
  [ ] Strategy có yêu cầu role mới?

Nếu 3/4 = YES → Provision Agent mới
Nếu < 3 = YES → Xem xét Multi-Assignment hoặc Skill Loading thêm
```

### 4.2. Provisioning Checklist

```
Bước 1: Xác định 12 Elements
Bước 2: Chọn/tạo Skills cần nạp
Bước 3: Assign Workflow ownership
Bước 4: Tạo Agent Folder (JD.md, ToDo.md, Changelog.md)
Bước 5: Viết System Prompt
Bước 6: Test Agent với sample task
Bước 7: Ghi vào Agent Index
```

---

## 5. Agent Folder — "Hồ sơ cá nhân"

Mỗi Agent có 1 folder riêng chứa hồ sơ vận hành:

```
A_root_AgentName/
├── JD.md           ← Job Description (12 Elements tóm tắt)
├── ToDo.md         ← Danh sách task đang làm
├── Changelog.md    ← Lịch sử thay đổi
├── Notes.md        ← Ghi chú tự do
└── INDEX.md        ← Tóm tắt nhanh
```

---

## 6. Nguyên tắc Agent Anatomy

| #       | Nguyên tắc                                   | Giải thích                                          |
| ------- | -------------------------------------------- | --------------------------------------------------- |
| **AA1** | **12 Elements bắt buộc**                     | Mọi Agent phải được định nghĩa đủ 12 elements       |
| **AA2** | **Reuse Before Create**                      | Multi-Assignment trước, Provisioning sau            |
| **AA3** | **System Prompt = biên dịch từ 12 Elements** | Không viết System Prompt "tự do" — phải có cấu trúc |
| **AA4** | **Agent Folder bắt buộc**                    | Mỗi Agent phải có hồ sơ cá nhân                     |
| **AA5** | **1 Owner per Workflow**                     | Mỗi Workflow chỉ 1 Agent sở hữu                     |

---

## 7. Liên kết với các chương khác

- **Chương 4 (Specialization):** Level chuyên biệt quyết định Skill Profile depth
- **Chương 5 (Shape):** Reporting chain (Element 7-8) tạo ra hình dạng tổ chức
- **Chương 6 (Distribution of Power):** Autonomy Scope (Element 3) = Distribution of Power cho 1 Agent
- **Chương 11 (Five Components):** Agent là 1 trong 5 thành phần. Elements liên kết với 4 thành phần còn lại
- **Chương 13 (Context & Knowledge):** Context Scope (Element 6) quyết định Agent "nhìn thấy" gì
