---
description: Điều phối một tech sprint — từ brief → code → test → review → deploy
tier: orchestration
version: v1.0
owner: "@Director-Tech"
calls:
  - /code-backend (Tier 2)
  - /code-frontend (Tier 2)
  - /build-ai-pipeline (Tier 2)
  - /deploy (Tier 2)
  - /qg-check (Tier 3)
  - /flog (Tier 3)
called_by:
  - manual (@CEO-Winston giao sprint tech)
input: "Sprint ID + Sprint_Plan.md + danh sách task tech cần làm"
output: "Tất cả tech deliverables done + deployed + QG passed + Handoff cập nhật"
---

# Workflow: /build-sprint

> **Tier 1 — ORCHESTRATION**
> Ai chạy: @Director-Tech
> Khi nào: Nhận brief từ CEO để thực hiện 1 sprint tech

---

## Bước 1: Load Sprint Context

Đọc bắt buộc (theo thứ tự):
1. `SPRINT/Sprint_Log.md` — xác nhận Sprint ID và dates
2. `SPRINT/SP-.../Sprint_Plan.md` — scope, DoD, dependencies
3. `02_Production/INDEX.md` — hiện trạng production
4. `02_Production/Architecture/ARCH-001_*.md` — tech stack hiện tại

**[TOL] Ghi Decision Log:**
```
[TOL] Sprint Brief nhận được: S## — [Tên]
→ Tech tasks: [liệt kê]
→ Dependencies: [liệt kê]
→ Timeline: [dates]
→ Risks: [nếu có]
→ Confidence: X%
```

---

## Bước 2: Phân tích & Phân chia task

Với mỗi tech task trong Sprint_Plan.md, phân loại:

| Task | Type | Workflow | Specialist |
|------|------|----------|-----------|
| Viết API endpoint X | Backend | /code-backend | @Specialist-Backend |
| Tạo screen Y | Frontend | /code-frontend | @Specialist-Frontend |
| Build AI pipeline Z | AI | /build-ai-pipeline | @Specialist-AI-Pipeline |
| Deploy lên staging | DevOps | /deploy | @Director-Tech |

**Gate:** Nếu task không rõ scope → escalate lên @CEO-Winston trước khi bắt đầu.

---

## Bước 3: Checkpoint Setup

Tạo file checkpoint tại `SPRINT/SP-.../DOCS/checkpoint.md`:

```markdown
# Build Checkpoint — S##

| Step | Task | Status | Output |
|------|------|--------|--------|
| 1 | Backend: [task] | ⬜ | |
| 2 | Frontend: [task] | ⬜ | |
| 3 | AI Pipeline: [task] | ⬜ | |
| 4 | QG Review | ⬜ | |
| 5 | Deploy Staging | ⬜ | |
| 6 | Deploy Production | ⬜ | |
```

> **State Management:** Sau mỗi bước hoàn thành, update Status → `✅` ngay lập tức.
> Nếu pipeline bị interrupt, resume từ bước chưa done — KHÔNG làm lại từ đầu.

---

## Bước 4: Thực thi Backend Tasks

Với mỗi backend task → gọi `/code-backend`:

```
/code-backend
Input: [Task description + relevant ARCH files + existing code context]
```

Sau khi nhận output:
- Kiểm tra code follow `02_Production/Architecture/` conventions
- Update checkpoint.md → `✅`

---

## Bước 5: Thực thi Frontend Tasks

Với mỗi frontend task → gọi `/code-frontend`:

```
/code-frontend
Input: [Screen spec từ 02_Production/Design/ + component library + task description]
```

Sau khi nhận output:
- Kiểm tra follow design system (FE-001, FE-002)
- Update checkpoint.md → `✅`

---

## Bước 6: Thực thi AI Pipeline Tasks (nếu có)

Với AI pipeline tasks → gọi `/build-ai-pipeline`:

```
/build-ai-pipeline
Input: [Pipeline spec + Claude API context + accuracy requirements]
```

---

## Bước 7: Quality Gate Review — Gọi /qg-check

Sau khi tất cả code tasks done:

```
/qg-check
Level: QG-2 (Peer Review)
Scope: Sprint S## — Tech Deliverables
```

**Nếu QG-2 FAIL:** Fix issues → quay lại bước tương ứng → re-run /qg-check.
**Nếu QG-2 PASS:** Tiếp tục Bước 8.

---

## Bước 8: Deploy lên Staging

Gọi `/deploy`:

```
/deploy
Environment: staging
Sprint: S##
```

Verify sau deploy:
- [ ] All endpoints responding
- [ ] No error logs
- [ ] Core user flow functional (manual smoke test)

---

## Bước 9: CEO Sign-off (QG-3)

Báo cáo lên @CEO-Winston:

```
[BUILD-SPRINT REPORT] S## — [Tên Sprint]
✅ Done: [list tasks]
⚠️ Deferred: [list nếu có + lý do]
🔗 Staging URL: [url]
📊 QG-2: PASS
🕐 Sẵn sàng deploy production: [Y/N]
```

**Gate:** Chờ CEO approval trước khi deploy production.

---

## Bước 10: Deploy Production (nếu được approve)

```
/deploy
Environment: production
Sprint: S##
```

---

## Bước 11: Cập nhật Sprint_Checklist.md & Handoff

- Đánh dấu tất cả tech tasks ✅ trong Sprint_Checklist.md
- Update `Handoff.md` section "What Just Happened"

---

## Bước 12: Gọi /flog

```
/flog — Sprint S## tech build complete. [N] files changed. Deployed to [env].
```

---

## Output cam kết

- Tất cả tech tasks trong sprint scope đã done
- Code đã review (QG-2 passed)
- Deployed lên staging (minimum) hoặc production
- Sprint_Checklist.md updated
- Handoff.md updated
- checkpoint.md đầy đủ (traceability)

```
[QG-1] Tự kiểm:
- [ ] Tất cả tasks trong scope done hoặc có lý do defer rõ ràng?
- [ ] QG-2 passed?
- [ ] Deploy thành công (không có critical errors)?
- [ ] Checkpoint đầy đủ?
- [ ] CEO đã được báo cáo?
```
