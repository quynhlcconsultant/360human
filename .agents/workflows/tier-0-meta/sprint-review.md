---
description: Đóng một sprint — review deliverables, đánh dấu Done, extract lessons learned
tier: meta
version: v1.0
owner: "@CEO-Winston"
calls:
  - /beat (Tier 3)
  - /flog (Tier 3)
called_by:
  - manual (CEO gọi khi sprint kết thúc)
input: "Sprint ID cần đóng"
output: "Sprint_Log.md cập nhật Done + KI mới trong knowledge/ + Handoff.md cập nhật"
---

# Workflow: /sprint-review

> **Tier 0 — META**
> Ai chạy: @CEO-Winston
> Khi nào: Cuối mỗi sprint

---

## Bước 1: Load context sprint

Đọc:
1. `SPRINT/Sprint_Log.md` — tìm sprint cần review
2. `SPRINT/SP-YYMMDD-##-TenSprint/Sprint_Checklist.md` — kiểm tra DoD
3. `SPRINT/SP-YYMMDD-##-TenSprint/Sprint_Plan.md` — đối chiếu scope gốc

---

## Bước 2: Đánh giá DoD (Definition of Done)

Với mỗi item trong checklist:

| Status | Hành động |
|--------|----------|
| ✅ Done | Ghi nhận — OK |
| ❌ Không done | Ghi lý do, chuyển vào backlog sprint sau hoặc Archive |
| ⚠️ Partial | Ghi rõ phần nào done, phần nào defer |

**Gate:** Nếu < 70% DoD đạt → Sprint INCOMPLETE → ghi rõ trong Sprint_Log + tạo recovery tasks.

---

## Bước 3: Đánh giá từng Director (Agent Performance)

Dùng Configuration Feedback Loop từ quality-gates.md:

| Director | Tasks | Done | Score | Action |
|----------|-------|------|-------|--------|
| @Director-Tech | # tasks | # done | Excellent/Good/Avg/Poor | ... |
| @Director-Product | # tasks | # done | ... | ... |
| @Director-Growth | # tasks | # done | ... | ... |

Ghi vào Sprint_Plan.md section "Retrospective".

---

## Bước 4: Gọi /beat — Extract Knowledge Items

Với mỗi insight quan trọng từ sprint này:

```
/beat — [Tên insight]
```

Ưu tiên extract KI khi:
- Phát hiện anti-pattern mới
- Quyết định kiến trúc quan trọng
- Giải pháp cho blocker khó
- Bài học từ failure

---

## Bước 5: Cập nhật Sprint_Log.md

Đổi status sprint từ `🔄 In Progress` → `✅ Done`:

```markdown
| S## | [Tên Sprint] | [Dates] | ✅ Done | [Deliverables thực tế] | [Department] |
```

Nếu Incomplete: `⚠️ Partial`

---

## Bước 6: Di chuyển deliverables vào SSOT

Với mỗi output đã hoàn thành trong `SPRINT/SP-.../DOCS/`:
- Copy (hoặc move) vào department folder tương ứng (01-04)
- Cần QG-3 approval trước khi merge vào SSOT

```
[QG-3] Checklist trước merge:
- [ ] QG-1 + QG-2 đã pass?
- [ ] Aligned với strategy (CEO-001)?
- [ ] Không conflict với existing decisions?
- [ ] Resource cost acceptable?
```

---

## Bước 7: Cập nhật Handoff.md

```markdown
## What Just Happened
- Sprint S## [Tên] → ✅ Done / ⚠️ Partial
- Deliverables: [list]
- Lessons: [tóm tắt]

## Next Actions
1. Bắt đầu Sprint S[##+1]...
```

---

## Bước 8: Gọi /flog

```
/flog — Sprint S## closed, KIs extracted, SSOT updated, Handoff updated
```

---

## Output cam kết

- Sprint_Log.md: status ✅ Done
- KI mới trong `.agents/knowledge/` (nếu có insight)
- Deliverables merged vào SSOT (nếu QG-3 pass)
- Handoff.md phản ánh trạng thái mới
- Retrospective notes trong Sprint_Plan.md

```
[QG-1] Tự kiểm: DoD evaluated ✓ | Sprint_Log Done ✓ | KIs extracted ✓ | Handoff updated ✓
```
