---
description: Chạy Quality Gate checklist — QG-1 self-check hoặc QG-2 peer review
tier: utility
version: v1.0
owner: "Any Agent"
calls: []
called_by:
  - Any Tier 1-2 workflow (trước khi wrap up)
  - manual
input: "QG Level (1 hoặc 2) + Scope mô tả + Files cần check"
output: "[QG-N] PASS/FAIL — [Agent] — [Scope] — [Notes]"
---

# Workflow: /qg-check

> **Tier 3 — UTILITY**
> Ai chạy: Bất kỳ agent nào
> Khi nào: Cuối mỗi task (QG-1) hoặc cuối mỗi feature (QG-2)

---

## Bước 1: Xác định Level

| Level | Ai chạy | Khi nào |
|-------|---------|---------|
| QG-1 | Agent vừa làm task | Sau mỗi task hoàn thành |
| QG-2 | Agent khác (peer) hoặc Director | Sau mỗi feature hoàn thành |
| QG-3 | @CEO-Winston | Trước merge vào SSOT — KHÔNG chạy qua workflow này |

---

## Bước 2: QG-1 Checklist (Universal)

Áp dụng cho MỌI output:

```
QG-1 Universal Checklist — [Task/Output name]

Core Operating Principles:
[ ] TOL: Đã ghi reasoning/decision log trong quá trình làm?
[ ] Sprint-centric: Task này thuộc sprint nào? Sprint ID gắn chưa?
[ ] SSOT: Output ở đúng location chưa? (SSOT zone hay WIP zone?)
[ ] Changelog: Thay đổi cấu trúc đã log vào Changelog.md chưa?
[ ] Indexing: File mới đã thêm vào INDEX.md tương ứng chưa?

Quality:
[ ] Output đúng format yêu cầu?
[ ] Đã đọc đủ context trước khi làm?
[ ] Confidence ≥ 80%? (Nếu không → flag uncertainty rõ ràng)

Anti-patterns Check:
[ ] KHÔNG tạo God File/Folder? (max 30 files/folder, max 10 skills/agent)
[ ] KHÔNG tạo Orphan File? (mọi file đều thuộc 1 zone)
[ ] KHÔNG tạo Duplicate SSOT? (chỉ 1 bản truth, còn lại là backlink)
[ ] KHÔNG để WIP trong SSOT zone?
```

---

## Bước 3: QG-2 Checklist (nếu Level = 2)

Thêm vào QG-1, check cross-agent consistency:

```
QG-2 Peer Review Checklist — [Feature/Deliverable]

Consistency:
[ ] QG-1 đã pass trước?
[ ] Output consistent với PRD/specs hiện tại?
[ ] Không conflict với SSOT files đã có?
[ ] Cross-references (backlinks) valid? (files tham chiếu có tồn tại không?)
[ ] Naming conventions đúng theo Guideline.md?

Type-specific checks:
→ Code: Tests pass? Security OK? Performance OK? No hardcoded secrets?
→ Content: Tone đúng? Facts accurate? Vietnamese natural? Astrology claims validated?
→ Design: Follow FE-001 design system? All states covered? Mobile-first?
→ PRD: ACs testable? No ambiguity? Tech can implement without asking?
```

---

## Bước 4: Output Result

Format output bắt buộc:

```
[QG-1] PASS — @AgentHandle — [Task/Feature] — [Date]
Notes: [nếu có gì đặc biệt]
```

Hoặc nếu FAIL:

```
[QG-1] FAIL — @AgentHandle — [Task/Feature] — [Date]
Issues:
  🔴 Critical: [mô tả issue + file + cách fix]
  🟡 Major: [mô tả]
Required actions before proceeding:
  1. [Action cụ thể]
  2. [Action cụ thể]
```

---

## Quy tắc khi FAIL

- **QG-1 FAIL:** Agent tự fix → re-run /qg-check → chỉ report lên Director sau khi PASS
- **QG-2 FAIL:** Director gửi issues list cho agent gốc → agent fix → re-submit → QG-2 lại

**KHÔNG** tiếp tục pipeline nếu có Critical issue chưa resolve.

---

## Output cam kết

- Kết quả PASS/FAIL rõ ràng
- Nếu FAIL: issues cụ thể, actionable
- Stateless: không thay đổi file nào (chỉ report)

```
[/qg-check complete]
```
