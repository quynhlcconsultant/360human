# Chương 20: Templates — Mẫu triển khai thực tế

> **Mục đích:** Copy-paste templates để triển khai ngay các khái niệm trong cuốn sách

---

## Template 1: Agent Definition Card

```yaml
# Agent Definition Card
# Copy template này cho mỗi Agent mới

agent:
  # IDENTITY LAYER
  name: "@TênAgent"
  role: "Chức danh"
  mission: "Nhiệm vụ 1 câu"
  autonomy_level: "L3"  # L1-L5

  # CAPABILITY LAYER
  skill_profile:
    core: [viet-chuyen-nghiep, sprint-centric, think-out-loud]
    functional: [skill-1, skill-2]
    domain: [domain-skill-1]
  workflow_ownership:
    - /workflow-1 (Tier 2)
    - /workflow-2 (Tier 2)
  context_scope:
    always_read: [Strategy.md, personas/]
    project: [05_5Balance/]

  # INTERFACE LAYER
  reports_to: "@DirectorAgent"
  manages: ["@Agent1", "@Agent2"]
  cross_calls: ["@Agent3", "@Agent4"]
  escalation:
    level_1:
      to: "@DirectorAgent"
      when: ["Ngoài can_decide", "Fail QA 2 lần"]
    level_2:
      to: "CEO"
      when: ["Cross-BU impact", "Budget > threshold"]
    level_3:
      to: "CEO | IMMEDIATE"
      when: ["Security", "Data loss", "Brand damage"]

  # OPERATIONAL LAYER
  code_of_conduct: [TOL, Sprint-centric, Changelog, SSOT, Indexing]

  # AUTONOMY DETAIL
  can_decide:
    - "Chọn approach/methodology"
    - "Quyết định trình tự thực thi"
    - "Tạo/sửa file trong phạm vi BU"
  must_escalate:
    - "Thay đổi strategy"
    - "Chủ đề nhạy cảm"
    - "Budget > 1M VND"
```

---

## Template 2: Workflow YAML Frontmatter

```yaml
---
description: Mô tả ngắn workflow này làm gì
tier: execution  # meta | orchestration | execution | utility
owner: "@AgentName"
calls:
  - /workflow-it-calls-1
  - /workflow-it-calls-2
called_by:
  - /workflow-that-calls-it
  - manual (CEO gọi trực tiếp)
input: "Mô tả input mong đợi"
output: "Mô tả output cam kết"
---

# Tên Workflow

## Bước 1: ...
## Bước 2: ...
## Bước 3: ...
```

---

## Template 3: Sprint Folder

```
SPRINTS/
└── SP-YYMMDD-NN-TenSprint/
    ├── Sprint_Plan.md          ← Kế hoạch, TOL, Decision Log
    ├── Sprint_Checklist.md     ← Tracking progress [/] [x] [ ]
    └── DOCS/
        ├── output_1.md         ← Deliverable 1
        ├── output_2.md         ← Deliverable 2
        └── ...

Sprint_Plan.md template:
---
# Sprint Plan: SP-YYMMDD-NN-TenSprint

## Mục tiêu Sprint
> 1 câu mô tả mục tiêu

## Phạm vi (Scope)
- Task 1: ...
- Task 2: ...

## Definition of Done (DoD)
- [ ] Tiêu chí 1
- [ ] Tiêu chí 2

## Decision Log (TOL)
| #   | Quyết định | Lựa chọn | Lý do |
| --- | ---------- | -------- | ----- |
| 1   | ...        | A vs B   | ...   |

## Notes
- ...
---
```

---

## Template 4: Agent Folder

```
A_root_AgentName/
├── JD.md           ← Job Description
├── ToDo.md         ← Task đang làm
├── Changelog.md    ← Lịch sử
├── Notes.md        ← Ghi chú
└── INDEX.md        ← Tóm tắt

JD.md template:
---
# @AgentName — Job Description

## Identity
- **Name:** @AgentName
- **Role:** Chức danh
- **Mission:** Nhiệm vụ
- **Autonomy:** L3

## Skill Profile
- Core: [...]
- Functional: [...]
- Domain: [...]

## Workflow Ownership
| Workflow | Tier      | Mô tả |
| -------- | --------- | ----- |
| /wf-1    | execution | ...   |

## Reporting
- Reports to: @DirectorAgent
- Manages: [@Agent1, @Agent2]
- Cross-calls: [@Agent3]

## Escalation
| Level | To            | When        |
| ----- | ------------- | ----------- |
| 1     | @Director     | Ngoài scope |
| 2     | CEO           | Cross-BU    |
| 3     | CEO IMMEDIATE | Security    |
---
```

---

## Template 5: Alignment Check

```markdown
# Alignment Check — [Date]

## ⭐ Strategy ↔ 📐 Architecture
- [ ] Số Agent Role match số BU?
- [ ] BU ưu tiên có nhiều Agent hơn?

## ⭐ Strategy ↔ 🔄 Orchestration
- [ ] BU ưu tiên có Tier 1 Workflow mạnh hơn?
- [ ] Cross-calling hỗ trợ strategy execution?

## 📐 Architecture ↔ 🔄 Orchestration
- [ ] Mỗi Agent có ≥ 1 Workflow?
- [ ] Workflow Tiering đúng?

## 📐 Architecture ↔ 🔧 Capabilities
- [ ] Mỗi Agent có SKILL.md?
- [ ] Mỗi Agent có Agent Folder?

## 🔄 Orchestration ↔ 📏 Measurement
- [ ] Mỗi Tier 1 Workflow có quality gate?
- [ ] Mỗi Agent có ≥ 1 metric?

## 📏 Measurement ↔ 🔧 Capabilities
- [ ] Feedback loop kết nối metric → skill update?
- [ ] Configuration changes logged trong Changelog?

## 🔧 Capabilities ↔ ⭐ Strategy
- [ ] Skills phục vụ competitive advantage?
- [ ] Knowledge Items align với direction?

## Verdict
- Misalignment detected: _______________
- Action needed: _______________
```

---

## Template 6: Lateral Power Shift Protocol

```yaml
lateral_power_shift:
  trigger: "Mô tả tình huống kích hoạt"  # VD: production_incident_p0
  activated_agent: "@AgentName"
  temporary_powers:
    - "Quyền tạm thời 1"   # VD: freeze_all_deployments
    - "Quyền tạm thời 2"   # VD: bypass_chain_to_specialist
    - "Quyền tạm thời 3"   # VD: rollback_without_ceo_approval
  duration: "until_incident_resolved"
  notification: ["CEO", "@Agent1", "@Agent2"]
  post_resolution:
    - return_to_normal_power
    - write_postmortem_to_knowledge
    - update_agent_folder_changelog
```

---

## Template 7: Knowledge Item Structure

```
knowledge/
└── topic_name/
    ├── metadata.json
    │   {
    │     "title": "Tên KI",
    │     "summary": "Tóm tắt 2-3 câu",
    │     "created": "2026-03-09",
    │     "last_updated": "2026-03-09",
    │     "owner": "@AgentName",
    │     "version": "v1.2", // Bổ sung versioning
    │     "references": ["conversation_id_1", "sprint_id_1"],
    │     "tags": ["architecture", "deployment"],
    │     "status": "active"  // active | archived | draft
    │   }
    └── artifacts/
        ├── overview.md      ← Tổng quan (bắt buộc)
        ├── detail_1.md      ← Chi tiết aspect 1
        └── detail_2.md      ← Chi tiết aspect 2
```

### Cảnh báo Red Team: Template Drift (Lệch chuẩn Biểu mẫu)

**Lỗ hổng:** Việc dùng tĩnh các biểu mẫu theo thời gian sẽ nảy sinh rủi ro khi Org Scale (Scale-up) thêm các tham số mới, nhưng các Agent thế hệ cũ vẫn dùng template hệ số cũ, gây crash parser ở phía hệ thống.
**Giải pháp:** Bắt buộc áp dụng **Template Versioning**. Mọi file YAML frontmatter trong hệ thống (Workflow, Agent Definition, Skills) phải chèn trường `version: vX.X`. Các Workflow Orchestration luôn check schema version trước khi dùng. Nếu phát hiện version out-of-date, nó sẽ trigger hàm gọi '/update-template'.

---

## Tổng kết cuốn sách

```
AGENT STAR™ — Tóm tắt 1 trang:

⭐ STRATEGY       CEO quyết chiến lược. Agent thực thi.
📐 ARCHITECTURE   Specialize Agent → 3 tầng → Hybrid Cluster → Centralize cấu hình
🔄 ORCHESTRATION  Workflow Tiering → Cross-calling → Progressive lateral processes
🔧 CAPABILITIES   5 Components → 11 Elements → 3 tầng bộ nhớ → Source Library Lifecycle
📏 MEASUREMENT    Metrics + Quality Gates + Configuration Feedback Loop

5 Nguyên tắc vận hành: TOL · Sprint · Changelog · SSOT · Indexing
4 Vai trò con người: Architect · Trainer · Governor · Documentarian
4 Phase triển khai: Foundation → Structure → Scale → Optimize
```
