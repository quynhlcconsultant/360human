# Handoff — 360Human Real-time Status

> **Last updated:** 2026-03-20 | **Updated by:** Claude (Architect)

---

## Current State

| Item | Status |
|------|--------|
| **Sprint hiện tại** | S03 — Foundation (Sprint 0 Tech) |
| **Phase** | Phase 2 — Build Production System |
| **Launch date** | 29/04/2026 |
| **Days to launch** | 40 ngày |

## What Just Happened (S02 — ✅ Done)

S02 hoàn thành toàn bộ tái cấu trúc tổ chức theo DDWA + AGENT STAR:

- ✅ Folder structure mới (01–05 departments + SPRINT/ + Handoff Suite)
- ✅ 7 Agent JD.md (CEO + 3 Directors + 3 Consultants)
- ✅ 6 Specialist Agent JD.md (Backend, Frontend, AI-Pipeline, QA, Designer, Astrology)
- ✅ 12 Workflows đầy đủ T0→T3
- ✅ Global Rules + Quality Gates
- ✅ Master_Strategy.yaml (Layer 1 SSOT)
- ✅ Prototype fix + Checkout Flow

## Current Blockers

| # | Blocker                                               | Impact                              | Owner                           |
|---|-------------------------------------------------------|-------------------------------------|---------------------------------|
| 1 | Figma wireframes chưa có                              | Non-blocking (có text-based FE spec) | Winston                        |
| 2 | Astrology Knowledge Base (KI-003→KI-010) chưa build   | Blocks S04 AI pipeline accuracy     | Winston / @Specialist-Astrology |

## Next Actions (S03 — bắt đầu 21/03)

1. **Docker compose setup** — `docker-compose.yml` với FastAPI + PostgreSQL + Redis
2. **PostgreSQL + Alembic** — DB schema migrations (User, Chart, Reading tables)
3. **Auth API** — JWT login/register/refresh endpoints
4. **Frontend scaffold** — Next.js 15 App Router + Tailwind + shadcn/ui base setup

## Important Decisions — Đã Chốt

- [x] **Số agent:** 13 agents (CEO + 3 Directors + 6 Specialists + 3 Consultants) — done S02
- [x] **Workflow tiering:** 4 tiers, 12 workflows — done S02
- [x] **Tech stack:** FastAPI + Next.js 15 + PostgreSQL (Neon) + Claude claude-sonnet-4-6
- [x] **Deploy:** Railway (backend) + Vercel (frontend) + Neon (DB)

## Important Decisions — Còn Pending

- [ ] Figma hi-fi mockups: làm song song trong S03 hay chờ sau S03?
- [ ] Astrology Knowledge Base: build trước S04 hay trong S04?
- [ ] Beta testers: recruit khi nào?

## Key Files to Read (Agent onboarding)

| File | Mục đích |
|------|---------|
| `INDEX.md` | Bản đồ toàn bộ workspace |
| `01_Governance/Strategy/CEO-001_business-requirements.md` | Business vision + success criteria |
| `01_Governance/Strategy/Master_Strategy.yaml` | **SSOT chiến lược — đọc trước tiên** |
| `02_Production/Architecture/ARCH-001_tech-stack.md` | Tech stack decisions |
| `02_Production/Product/PRD-001_product-requirements.md` | Product scope |
| `.agents/rules/global-rules.md` | Hiến pháp tổ chức |
| `.agents/rules/quality-gates.md` | QG-1/2/3 checklists |
| `.agents/AGENTS-REGISTRY.md` | Toàn bộ agents + org chart |
| `SPRINT/Sprint_Log.md` | Sprint history |
