---
description: Điều phối phát triển 1 feature — từ PRD → Design → Code handoff → Test → Ship
tier: orchestration
version: v1.0
owner: "@Director-Product"
calls:
  - /write-prd (Tier 2)
  - /design-screen (Tier 2)
  - /qg-check (Tier 3)
  - /flog (Tier 3)
called_by:
  - manual (@CEO-Winston giao feature request)
  - /build-sprint (@Director-Tech request thêm spec)
input: "Feature request (tên, mô tả, priority, user story)"
output: "PRD update + Design spec + Handoff package sẵn sàng cho @Director-Tech"
---

# Workflow: /build-feature

> **Tier 1 — ORCHESTRATION**
> Ai chạy: @Director-Product
> Khi nào: Nhận feature request từ CEO hoặc backlog

---

## Bước 1: Hiểu Feature Request

Đọc bắt buộc:
1. `02_Production/Product/PRD-001_product-requirements.md` — product scope tổng thể
2. `01_Governance/Strategy/CEO-001_business-requirements.md` — business direction
3. `02_Production/Design/FE-001_*.md` — design system hiện tại (nếu UI feature)

Xác nhận với người giao task:
- User story: "Với tư cách là [ai], tôi muốn [làm gì], để [đạt được gì]"
- Acceptance criteria: ít nhất 3 tiêu chí rõ ràng
- Priority: P0 (must-have) / P1 (should-have) / P2 (nice-to-have)
- In-scope / Out-of-scope rõ ràng

**[TOL] Decision Log:**
```
[TOL] Feature Request nhận: [Tên feature]
→ User story: ...
→ Acceptance criteria: ...
→ Priority: P#
→ Đây là NEW feature hay ENHANCE existing?
→ Ảnh hưởng đến screens nào?
→ Confidence: X%
```

---

## Bước 2: Viết/Cập nhật PRD — Gọi /write-prd

```
/write-prd
Feature: [Tên]
Scope: [User story + Acceptance criteria]
```

Output: Feature section trong PRD-001 được thêm/cập nhật.

---

## Bước 3: Design Screen Specs — Gọi /design-screen

```
/design-screen
Feature: [Tên]
PRD Section: [Link tới PRD section vừa viết]
Target Screens: [Danh sách screens bị ảnh hưởng]
```

Output: Design spec file `FE-[###]_[tên-feature]-spec.md` trong `02_Production/Design/`.

---

## Bước 4: QG-2 Review — Gọi /qg-check

Tự review hoặc nhờ Director cùng level:

```
/qg-check
Level: QG-2
Scope: Feature [Tên] — PRD + Design
```

Checklist cụ thể cho Product:
- [ ] Acceptance criteria có thể verify được không? (không mơ hồ)
- [ ] Design consistent với FE-001 design system?
- [ ] Feature không conflict với existing features?
- [ ] Vietnamese copy tự nhiên, đúng tone?
- [ ] Astrology accuracy requirements đã specify? (nếu liên quan)

**Nếu FAIL:** Sửa PRD/Design → re-check.

---

## Bước 5: Tạo Tech Handoff Package

Tạo file `SPRINT/SP-.../DOCS/handoff-[feature].md`:

```markdown
# Tech Handoff: [Feature Name]

> **From:** @Director-Product
> **To:** @Director-Tech
> **Date:** YYYY-MM-DD

## Feature Overview
[1 đoạn mô tả]

## PRD Reference
→ `02_Production/Product/PRD-001.md` — Section: [X]

## Design Specs
→ `02_Production/Design/FE-###_[tên].md`

## Acceptance Criteria (Tech perspective)
- [ ] Backend: [endpoint, data model, logic cần implement]
- [ ] Frontend: [screens, components, interactions]
- [ ] AI: [nếu có pipeline/prompt liên quan]

## API Contract (nếu biết trước)
[Mô tả expected endpoints hoặc data shape]

## Edge Cases cần handle
- Case 1: ...
- Case 2: ...

## Definition of Done
- [ ] All acceptance criteria pass
- [ ] QG-2 by @Director-Tech
- [ ] Staging demo approved by @CEO-Winston
```

---

## Bước 6: Brief @Director-Tech

```
[BUILD-FEATURE HANDOFF] [Tên feature]
→ PRD: 02_Production/Product/PRD-001.md (Section X)
→ Design: 02_Production/Design/FE-###.md
→ Handoff: SPRINT/.../DOCS/handoff-[feature].md
→ Priority: P#
→ Notes: [bất kỳ context đặc biệt nào]
```

---

## Bước 7: Cập nhật Backlog

Trong `ToDo.md` hoặc Sprint_Checklist.md, chuyển feature từ backlog → In Progress:

```
- [/] Feature: [Tên] — PRD ✅ | Design ✅ | Tech: pending
```

---

## Bước 8: Gọi /flog

```
/flog — Feature [Tên] PRD+Design done. Handoff package created for @Director-Tech.
```

---

## Output cam kết

- PRD-001 cập nhật với feature section mới
- Design spec file `FE-###_[tên].md` trong `02_Production/Design/`
- Handoff package trong `SPRINT/.../DOCS/`
- @Director-Tech đã nhận brief
- ToDo.md / Sprint_Checklist.md updated

```
[QG-1] Tự kiểm:
- [ ] PRD section rõ ràng, acceptance criteria có thể test được?
- [ ] Design spec follow FE-001 design system?
- [ ] QG-2 passed?
- [ ] Tech handoff đầy đủ (không cần @Director-Tech phải hỏi lại)?
- [ ] @Director-Tech đã acknowledge?
```
