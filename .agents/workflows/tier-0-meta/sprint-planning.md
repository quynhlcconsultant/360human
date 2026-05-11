---
description: Mở một sprint mới — tạo Sprint Plan, set scope, assign cho Directors
tier: meta
version: v1.0
owner: "@CEO-Winston"
calls:
  - /flog (Tier 3)
called_by:
  - manual (CEO gọi khi bắt đầu sprint mới)
input: "Sprint ID, tên sprint, dates, danh sách deliverables mong muốn"
output: "Sprint_Log.md cập nhật + Sprint folder trong SPRINT/ + Handoff.md cập nhật"
---

# Workflow: /sprint-planning

> **Tier 0 — META**
> Ai chạy: @CEO-Winston
> Khi nào: Đầu mỗi sprint mới

---

## Bước 1: Xác nhận context trước khi mở sprint

Đọc bắt buộc (theo thứ tự):
1. `SPRINT/Sprint_Log.md` — kiểm tra sprint hiện tại đã DONE chưa
2. `Handoff.md` — nắm trạng thái hiện tại
3. `ToDo.md` — kiểm tra backlog

**Gate:** Nếu sprint hiện tại chưa Done → KHÔNG mở sprint mới. Escalate lên CEO.

---

## Bước 2: Tạo Sprint ID và folder

Format Sprint ID: `S[##]` (ví dụ: S03, S04)
Format Sprint Folder: `SPRINT/SP-[YYMMDD]-[##]-[ShortName]/`

Tạo cấu trúc:
```
SPRINT/SP-YYMMDD-##-TenSprint/
├── Sprint_Plan.md
├── Sprint_Checklist.md
└── DOCS/
```

---

## Bước 3: Điền Sprint_Plan.md

Dùng template:

```markdown
# Sprint Plan: [Sprint ID] — [Tên Sprint]

> **Sprint ID:** S##
> **Dates:** YYYY-MM-DD → YYYY-MM-DD
> **Owner:** @CEO-Winston
> **Department:** [Dep]

## Mục tiêu Sprint (1 câu)
> ...

## Scope — Deliverables

| Task ID | Mô tả | Owner | Priority |
|---------|-------|-------|----------|
| S##-T01 | ... | @Director-Tech | P0 |
| S##-T02 | ... | @Director-Product | P1 |

## Definition of Done (DoD)
- [ ] Tiêu chí 1
- [ ] Tiêu chí 2
- [ ] QG-3 approved bởi @CEO-Winston

## Decision Log (TOL)
| # | Quyết định | Options | Chọn | Lý do |
|---|-----------|---------|------|-------|
| 1 | ... | A vs B | A | ... |

## Dependencies & Risks
| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| ... | High/Med/Low | High/Med/Low | ... |
```

---

## Bước 4: Điền Sprint_Checklist.md

```markdown
# Sprint Checklist: [Sprint ID]

## Setup ✅
- [ ] Sprint Plan viết xong
- [ ] Handoff.md cập nhật
- [ ] Sprint_Log.md cập nhật
- [ ] Directors đã nhận brief

## Progress
- [ ] S##-T01: [Tên task]
- [ ] S##-T02: [Tên task]

## Wrap-up
- [ ] Tất cả deliverables done
- [ ] QG-3 passed
- [ ] Changelog updated
- [ ] Sprint_Log.md đánh dấu Done
```

---

## Bước 5: Cập nhật Sprint_Log.md

Thêm dòng mới vào bảng trong `SPRINT/Sprint_Log.md`:

```markdown
| S## | [Tên Sprint] | YYYY-MM-DD → YYYY-MM-DD | ⬜ Pending | [Deliverables tóm tắt] | [Department] |
```

---

## Bước 6: Brief Directors

Với mỗi Director liên quan, gửi brief ngắn:

```
[TOL] Sprint Brief — S##
→ Sprint: [Tên]
→ Scope của bạn: [Task IDs liên quan]
→ Deadline: [Date]
→ Priority: [P0/P1]
→ Đọc Sprint_Plan.md để biết DoD
```

---

## Bước 7: Cập nhật Handoff.md

Sửa section **"Current State"** và **"Next Actions"** trong `Handoff.md` để phản ánh sprint mới.

---

## Bước 8: Gọi /flog

```
/flog — Sprint_Plan.md created, Sprint_Log.md updated, Handoff.md updated
```

---

## Output cam kết

- `SPRINT/SP-YYMMDD-##-TenSprint/` folder đầy đủ
- `SPRINT/Sprint_Log.md` có dòng sprint mới (status: ⬜ Pending)
- `Handoff.md` updated
- Directors đã nhận brief

```
[QG-1] Tự kiểm: Sprint folder ✓ | Sprint_Log ✓ | Handoff ✓ | Directors briefed ✓
```
