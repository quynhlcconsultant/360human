# ToDo — 360Human Project Tracker

> **Last updated:** 2026-03-22 (Session 6 — S03+S04+S05 ✅ HOÀN THÀNH. Còn S06 Polish & Launch)

---

## Sprint Hiện Tại: S06 — Polish & Launch (Sprint 3 Tech)

**Timeline:** 2026-05-11 → 2026-05-18
**Mục tiêu:** Production-ready — deploy, SEO, PDF export, monitoring
**Gate:** Live trên Vercel + Railway + domain 360human.vn

| ID | Task | Status | Owner |
| --- | --- | --- | --- |
| S06-T01 | SEO metadata (Next.js Metadata API) | ✅ Done | Winston |
| S06-T02 | PDF export (ReportLab — báo cáo 360) | ✅ Done | Winston |
| S06-T03 | Deploy Backend → Railway | ✅ Done | Winston |
| S06-T04 | Deploy Frontend → Vercel | ✅ Done | Winston |
| S06-T05 | Sentry error monitoring | ✅ Done | Winston |
| S06-T06 | CI/CD pipeline (GitHub Actions) | ✅ Done | Winston |

---

## Sprints Đã Hoàn Thành

### S03 — Foundation ✅ Done (2026-03-22)

| ID | Task | Status |
| --- | --- | --- |
| S03-T01 | Docker compose (api + db + redis + healthcheck) | ✅ Done |
| S03-T02 | PostgreSQL + Alembic migrations (001 users, 002 profiles) | ✅ Done |
| S03-T03 | Auth API — JWT HS256, bcrypt, register/login/me/refresh | ✅ Done |
| S03-T04 | Next.js 15 scaffold — App Router, Tailwind v4, Zustand, TanStack Query | ✅ Done |

### S04 — Core Flow ✅ Done (2026-03-22)

| ID | Task | Status |
| --- | --- | --- |
| S04-T01 | Profile CRUD — tạo/sửa/xóa, max 3 profiles/user | ✅ Done |
| S04-T02 | L1: astrology-api.io — 5/5 systems qua asyncio.gather | ✅ Done |
| S04-T03 | L2: Knowledge Base RAG — JSON/MD enrichment per system | ✅ Done |
| S04-T04 | L3: Claude Haiku (free) / Sonnet (pro) → prose tiếng Việt | ✅ Done |
| S04-T05 | Onboarding wizard — 5 bước nhập thông tin sinh | ✅ Done |
| S04-T06 | Dashboard — 5 SystemCards + 10 TopicCards + tier lock | ✅ Done |
| S04-T07 | System reading page — TierGate + loading skeleton | ✅ Done |
| S04-T08 | Topic reading page — TierGate + loading skeleton | ✅ Done |
| S04-T09 | TierGate component — blur/lock UI phía frontend | ✅ Done |
| S04-T10 | Redis cache 30 ngày, GET /profiles/{id}/charts | ✅ Done |

### S05 — Monetization ✅ Done (2026-03-22)

| ID | Task | Status |
| --- | --- | --- |
| S05-T01 | Migration 003 — bảng payments | ✅ Done |
| S05-T02 | Payment model + schemas | ✅ Done |
| S05-T03 | VietQR service — generate QR URL không cần gateway | ✅ Done |
| S05-T04 | POST /payments/checkout + verify + status + webhook | ✅ Done |
| S05-T05 | Pricing page — 2 gói FREE / PRO (199.000₫) | ✅ Done |
| S05-T06 | Checkout page — QR display → xác nhận → polling | ✅ Done |
| S05-T07 | Success page — invalidate cache, redirect dashboard | ✅ Done |
| S05-T08 | Profile page — thông tin tài khoản + danh sách profiles | ✅ Done |
| S05-T09 | Settings page — đổi mật khẩu + đăng xuất | ✅ Done |

---

## Backlog

| ID    | Task                                                      | Priority | Notes                                                          |
| ----- | --------------------------------------------------------- | -------- | -------------------------------------------------------------- |
| BL-04 | Tri-Framework Stress Test (SIPOC / Ishikawa / 5-WHERE)    | P2       | Monthly audit                                                  |
| BL-05 | Build Astrology Knowledge Base (KI-003 to KI-010)         | ✅ Done  | Completed 2026-03-21                                           |
| BL-06 | Prototype v2 — All 10 screens + tier system               | ✅ Done  | Completed 2026-03-21. S1-S10, modals, FREE/PRO/MAX toggle      |
| BL-07 | Provision @Specialist-Copywriter + @Specialist-Researcher | P2       | Defer S05+                                                     |
| BL-08 | Prototype v3 — Refinements & bug fixes                    | ✅ Done  | Completed 2026-03-22. Warm color palette (FE-004), 2-tier system (FREE/PRO), Vietnamese UI, detailed charts (5 hệ thống), ~500w readings, JS syntax fix, responsive fix |

---

## Completed Sprints

### S01 — Module 1 Training ✅

**Completed:** 2026-03-20

- Đọc & phân tích AGENT STAR Book (23 chương)
- Đọc & phân tích DDWA Book (18 chương)
- Đọc Orchestration & Quality materials

### S02 — Tái Cấu Trúc Tổ Chức ✅

**Completed:** 2026-03-20
**Mục tiêu:** Áp dụng DDWA + AGENT STAR để tái cấu trúc workspace và cơ chế vận hành.

| ID      | Task                                                                    | Status   |
| ------- | ----------------------------------------------------------------------- | -------- |
| S02-T01 | Phân tích GAP cấu trúc hiện tại vs DDWA                                 | ✅ Done  |
| S02-T02 | Tạo CEO-005_restructuring-plan.md                                       | ✅ Done  |
| S02-T03 | Tạo Handoff Suite (9 items at root)                                     | ✅ Done  |
| S02-T04 | Tạo SPRINT/ zone + Sprint_Log.md                                        | ✅ Done  |
| S02-T05 | Tạo 01_Governance/ + copy CEO files                                     | ✅ Done  |
| S02-T06 | Tạo 02_Production/ + copy PRD/ARCH/FE files                             | ✅ Done  |
| S02-T07 | Tạo 03_Marketing/ + copy MKT/CRE/RTM files                              | ✅ Done  |
| S02-T08 | Tạo 04_Operations/ structure                                            | ✅ Done  |
| S02-T09 | Tạo .agents/ structure                                                  | ✅ Done  |
| S02-T10 | Viết JD.md cho 3 Directors                                              | ✅ Done  |
| S02-T11 | Viết global-rules.md + quality-gates.md                                 | ✅ Done  |
| S02-T12 | Tạo 05_Consulting/ + 3 teams + 38 skills                                | ✅ Done  |
| S02-T13 | Fix prototype black-on-black bug                                        | ✅ Done  |
| S02-T14 | Thêm Checkout Flow vào prototype (VietQR + Card + Success/Fail)         | ✅ Done  |
| S02-T15 | Cải thiện responsive prototype (mobile 375px+)                          | ✅ Done  |
| S02-T16 | Viết 12 workflows T0-T3 (sprint, build, code, deploy, flog...)          | ✅ Done  |
| S02-T17 | Viết JD.md cho 6 Specialist agents                                      | ✅ Done  |
| S02-T18 | Cập nhật AGENTS-REGISTRY.md (Org Chart + Workforce layer)               | ✅ Done  |
| S02-T19 | Tạo Master_Strategy.yaml (Layer 1 SSOT)                                 | ✅ Done  |
| S02-T20 | Cập nhật Handoff.md → S03 Pending                                       | ✅ Done  |
