---
title: "360Human — Master Project Tracker"
id: "CEO-004"
updated: "2026-03-15"
status: "active"
---

# 360Human — Master Project Tracker

> **Launch:** 29/04/2026 | **Team:** Winston (CEO/Fullstack) | **Domain:** 360human.vn (purchased)
> **Updated:** 17/03/2026

---

## HIGH-LEVEL GANTT — Bird's Eye View

```mermaid
gantt
    title 360Human — High-Level Roadmap (15 Mar → 29 Apr 2026)
    dateFormat  YYYY-MM-DD
    axisFormat  %d %b
    todayMarker stroke-width:3px,stroke:#f00

    section 📋 PLANNING
    Setup & Planning              :done, hl1, 2026-03-15, 1d
    Knowledge Base (5 systems)    :active, hl2, 2026-03-15, 4d
    Reading Template & Tone       :hl3, 2026-03-24, 5d

    section 🎨 DESIGN
    Screen Specs + Design System  :done, hl4, 2026-03-16, 1d
    UX Review & Fix               :active, hl4b, 2026-03-17, 1d
    Hi-Fi Mockups & Figma         :hl5, 2026-03-18, 5d
    Prototype & Handoff           :hl6, after hl5, 2d

    section ⚙️ DEVELOPMENT
    Sprint 0 — Foundation         :hl7, 2026-03-17, 7d
    Sprint 1 — Core Flow          :crit, hl8, 2026-03-24, 14d
    Sprint 2 — Monetization       :hl9, 2026-04-07, 14d
    Sprint 3 — Polish             :hl10, 2026-04-21, 7d

    section 🚀 LAUNCH
    Deployment & QA               :crit, hl11, 2026-04-25, 4d
    GO LIVE                       :milestone, crit, launch, 2026-04-29, 0d

    section 📣 MARKETING
    Content & Social Setup        :hl12, 2026-04-01, 21d
    Beta Testing                  :hl13, 2026-04-14, 14d
    Launch Campaign               :hl14, 2026-04-25, 5d
```

---

## DETAIL GANTT — All Workstreams

```mermaid
gantt
    title 360Human — Full Project (15 Mar → 29 Apr 2026)
    dateFormat  YYYY-MM-DD
    axisFormat  %d %b
    todayMarker stroke-width:3px,stroke:#f00

    section PRE-SPRINT (Setup)
    Project Planning & Docs           :done, ps1, 2026-03-15, 1d
    Skills & Agents Setup (.agents)   :done, ps2, 2026-03-15, 1d
    Docx→MD Conversion                :done, ps3, 2026-03-15, 1d
    API Key (astrology-api.io)        :done, ps4, 2026-03-15, 1d
    Domain Registration (360human.vn) :done, ps5, 2026-03-15, 1d
    KB Schema Design                  :done, ps6, 2026-03-15, 1d

    section KNOWLEDGE BASE
    KB: Human Design (486K words)     :done, kb1, 2026-03-15, 1d
    KB: Numerology (1M words)         :done, kb2, 2026-03-15, 1d
    KB: Vedic (1.5M words)            :done, kb3, 2026-03-15, 1d
    KB: BaZi (973K words)             :done, kb4, 2026-03-15, 1d
    KB: Tu Vi (2M words)               :done, kb5, 2026-03-16, 1d
    KB: Reading Test & Tone           :done, kb6, 2026-03-15, 1d
    KB: Reading Template v6           :active, kb7, 2026-03-15, 2d

    section UX/UI DESIGN
    Screen Specs (10 screens)         :done, d1, 2026-03-16, 1d
    Design System + Components        :done, d2, 2026-03-16, 1d
    UX Review & Resolve               :active, d2b, 2026-03-17, 1d
    Hi-Fi Mockups (Figma)             :d3, 2026-03-18, 5d
    Prototype & Handoff               :d4, after d3, 2d

    section SPRINT 0 — FOUNDATION
    0.1 Infrastructure (Docker/CI)    :s01, 2026-03-17, 2d
    0.2 Database (Alembic/Models)     :s02, after s01, 2d
    0.3 Auth API (JWT/endpoints)      :s03, after s02, 2d
    0.4 Frontend Scaffold (Next.js)   :s04, after s01, 4d
    GATE 0 ✓                         :milestone, g0, after s03 s04, 0d

    section SPRINT 1 — CORE FLOW
    1.1 Profile & Charts API          :s11, 2026-03-24, 3d
    1.2 L3 AI Pipeline (RAG+Claude)   :crit, s12, 2026-03-24, 8d
    1.3 Frontend Auth UI              :s13, 2026-03-24, 3d
    1.4 Onboarding Wizard             :s14, after s13, 3d
    1.5 Dashboard & Readings UI       :s15, after s14, 4d
    GATE 1 ✓                         :milestone, g1, after s12 s15, 0d

    section SPRINT 2 — MONETIZATION
    2.1 VietQR Payment Backend        :s21, 2026-04-07, 5d
    2.2 Pricing & Checkout UI         :s22, 2026-04-09, 5d
    Tier Enforcement (BE+FE)          :s23, after s21, 3d
    GATE 2 ✓                         :milestone, g2, after s22 s23, 0d

    section SPRINT 3 — POLISH & LAUNCH
    3.1 PDF Export                    :s31, 2026-04-21, 3d
    3.2 Advanced UI                   :s32, 2026-04-21, 4d
    3.3 SEO & Performance            :s33, 2026-04-23, 3d
    3.4 Deployment                    :crit, s34, 2026-04-25, 3d
    Monitoring & Go-live              :s35, after s34, 1d
    LAUNCH 🚀                        :milestone, crit, g3, 2026-04-29, 0d
```

---

## FULL CHECKLIST — All Teams

### PRE-SPRINT: Setup & Planning (15/03/2026)

| # | Task | Owner | Status | Date |
|---|------|-------|--------|------|
| PS.1 | [x] Project structure & folder setup | Winston | ✅ Done | 15/03 |
| PS.2 | [x] Docx → MD conversion (8 files) | Claude | ✅ Done | 15/03 |
| PS.3 | [x] .archive folder + naming convention | Claude | ✅ Done | 15/03 |
| PS.4 | [x] .agents setup (88 skills, 13 sub-agents) | Claude | ✅ Done | 15/03 |
| PS.5 | [x] API key (astrology-api.io) — saved in .env | Winston | ✅ Done | 15/03 |
| PS.6 | [x] Domain registration (360human.vn) | Winston | ✅ Done | 15/03 |
| PS.7 | [x] KB schema design (5 systems) | Claude | ✅ Done | 15/03 |
| PS.8 | [x] .gitignore + .env.example | Claude | ✅ Done | 15/03 |
| PS.9 | [x] PRD clarification (18 Q&A resolved) | Winston+Claude | ✅ Done | 15/03 |
| PS.10 | [x] Brand naming (360Human) | Winston | ✅ Done | 15/03 |
| PS.11 | [x] Gantt chart + Sprint tracker | Claude | ✅ Done | 15/03 |
| PS.12 | [x] Architecture docs updated (ARCH-001→004) | Claude | ✅ Done | 15/03 |

### KNOWLEDGE BASE: Content (15-18/03/2026)

| # | Task | Words | Status | Date |
|---|------|-------|--------|------|
| KB.1 | [x] Human Design KB (5 files) | 485,870 | ✅ Done | 15/03 |
| KB.2 | [x] Numerology KB (5 files) | 1,028,107 | ✅ Done | 15/03 |
| KB.3 | [x] Vedic KB (6 files) | 1,553,404 | ✅ Done | 15/03 |
| KB.4 | [x] BaZi KB (5 files) | 972,749 | ✅ Done | 15/03 |
| KB.5 | [x] Tu Vi KB (7 files) | 2,023,735 | ✅ Done | 16/03 |
| KB.6 | [x] Reading test (HD chart: Quynh) | — | ✅ Done | 15/03 |
| KB.7 | [x] Reading tone calibration (v1→v6) | — | ✅ Done | 15/03 |
| KB.8 | [ ] Reading template finalized | — | ⬜ Deferred → Sprint 1 | |
| KB.9 | [ ] Cross-system reading template | — | ⬜ Deferred → Sprint 1 | |
| | **KB TOTAL** | **6,063,865** | **✅ 5/5 systems COMPLETE** | |

### UX/UI DESIGN (16-25/03/2026)

| # | Task | Owner | Status | Date |
|---|------|-------|--------|------|
| D.1 | [x] Screen specs: S1 Landing Page | Winston+Claude | ✅ Done | 16/03 |
| D.2 | [x] Screen specs: S2 Login/Register | Winston+Claude | ✅ Done | 16/03 |
| D.3 | [x] Screen specs: S3 Onboarding | Winston+Claude | ✅ Done | 16/03 |
| D.4 | [x] Screen specs: S4 Dashboard (2-col + accordion) | Winston+Claude | ✅ Done | 16/03 |
| D.5 | [x] Screen specs: S5 System Reading (interactive) | Winston+Claude | ✅ Done | 16/03 |
| D.6 | [x] Screen specs: S6 Topic Reading → merged into S4 | Winston+Claude | ✅ Done | 16/03 |
| D.7 | [x] Screen specs: S7 Pricing Page | Winston+Claude | ✅ Done | 16/03 |
| D.8 | [x] Screen specs: S8 Profile/Settings (+multi-profile) | Winston+Claude | ✅ Done | 16/03 |
| D.9 | [x] Screen specs: S9 Time Oracle (drill-down) | Winston+Claude | ✅ Done | 16/03 |
| D.10 | [x] Screen specs: S10 Action Items (pyramid) | Winston+Claude | ✅ Done | 16/03 |
| D.11 | [x] Design System v1 (colors, typography, texture, spacing) | Claude | ✅ Done | 16/03 |
| D.12 | [x] Component map v1 (shadcn/ui → 360Human) | Claude | ✅ Done | 16/03 |
| D.13 | [x] Vietnamese copy v1 (all screens) | Claude | ✅ Done | 16/03 |
| D.14 | [x] Figma research integrated (3 pages) | Winston+Claude | ✅ Done | 16/03 |
| D.15 | [x] UX review — 17 issues identified | Claude | ✅ Done | 16/03 |
| D.16 | [x] Review & resolve 17 UX issues (C1-C5, H1-H5, M1-M6) | Winston | ✅ Done | 17/03 |
| D.17 | [x] Fix all files based on review decisions | Claude | ✅ Done | 17/03 |
| D.18 | [x] **MAJOR: Tier collapse FREE/PRO/MAX → FREE/PRO** | Winston | ✅ Done | 17/03 |
| D.19 | [x] S4 restructure: 3-col → 2-col + accordion + inline actions | Claude | ✅ Done | 17/03 |
| D.20 | [x] S3→S4 loading merge (5-layer animation) | Claude | ✅ Done | 17/03 |
| D.21 | [x] S9 update: daily→weekly, FREE skip to Layer 3 | Claude | ✅ Done | 17/03 |
| D.22 | [x] S7 update: 2-tier pricing + checkout flow (VietQR) | Claude | ✅ Done | 17/03 |
| D.23 | [x] Navigation patterns + Error/Empty states added | Claude | ✅ Done | 17/03 |
| D.24 | [x] Design references desk research (FE-007, 12 sites) | Claude | ✅ Done | 17/03 |
| D.25 | [x] HTML wireframes built (FREE + PRO views) | Claude | ✅ Done | 17/03 |
| D.26 | [ ] Update 9 project files for tier collapse (ARCH, PRD, CEO) | Claude | 🔲 Next | |
| D.27 | [ ] Design system v2 (colors TBD after wireframe review) | Winston | 🔲 | |
| D.28 | [ ] Icon set (5 frameworks + 10 topics) | Winston | 🔲 | |
| D.29 | [ ] Hi-Fi Mockups / Figma | Winston | 🔲 | |
| D.30 | [ ] Design tokens export → CSS vars | Claude | 🔲 After D.27 | |

### SPRINT 0 — FOUNDATION (17-23/03/2026)

| # | Task | Owner | Priority | Status |
|---|------|-------|----------|--------|
| 0.1.1 | [ ] .gitignore (Python + Node + Docker) | Dev | P0 | ⬜ |
| 0.1.2 | [ ] backend/Dockerfile (Python 3.12) | Dev | P0 | ⬜ |
| 0.1.3 | [ ] docker-compose.yml (API + PG + Redis) | Dev | P0 | ⬜ |
| 0.1.4 | [ ] .dockerignore | Dev | P1 | ⬜ |
| 0.1.5 | [ ] CI pipeline (.github/workflows/ci.yml) | Dev | P2 | ⬜ |
| 0.1.6 | [ ] TEST: docker-compose up | Dev | P0 | ⬜ |
| 0.2.1 | [ ] alembic init | Dev | P0 | ⬜ |
| 0.2.2 | [ ] Configure env.py (async + PG) | Dev | P0 | ⬜ |
| 0.2.3 | [ ] User model (UUID, email, tier ENUM) | Dev | P0 | ⬜ |
| 0.2.4 | [ ] Profile model (birth data, lat/lon) | Dev | P0 | ⬜ |
| 0.2.5 | [ ] Subscription model | Dev | P0 | ⬜ |
| 0.2.6 | [ ] Generate migration 001 | Dev | P0 | ⬜ |
| 0.2.7 | [ ] alembic upgrade head | Dev | P0 | ⬜ |
| 0.2.8 | [ ] Remove create_all() from main.py | Dev | P1 | ⬜ |
| 0.3.1 | [ ] Install deps (jose, passlib, slowapi) | Dev | P0 | ⬜ |
| 0.3.2 | [ ] core/security.py (JWT HS256) | Dev | P0 | ⬜ |
| 0.3.3 | [ ] api/deps.py (get_current_user) | Dev | P0 | ⬜ |
| 0.3.4 | [ ] api/auth.py (register, login, refresh) | Dev | P0 | ⬜ |
| 0.3.5 | [ ] api/users.py (GET/PUT /users/me) | Dev | P0 | ⬜ |
| 0.3.6 | [ ] Rate limiting (slowapi) | Dev | P1 | ⬜ |
| 0.3.7 | [ ] Structured logging (structlog) | Dev | P1 | ⬜ |
| 0.3.8 | [ ] TEST: register → login → GET /me | Dev | P0 | ⬜ |
| 0.4.1 | [ ] create-next-app (Next.js 15, App Router) | Dev | P0 | ⬜ |
| 0.4.2 | [ ] Install deps (Axios, Zustand, TanStack) | Dev | P0 | ⬜ |
| 0.4.3 | [ ] shadcn init + Tailwind v4 | Dev | P0 | ⬜ |
| 0.4.4 | [ ] Add shadcn components | Dev | P0 | ⬜ |
| 0.4.5 | [ ] Design tokens (CSS vars) | Dev | P0 | ⬜ |
| 0.4.6 | [ ] App shell layout | Dev | P0 | ⬜ |
| 0.4.7 | [ ] API client (Axios + JWT interceptor) | Dev | P0 | ⬜ |
| 0.4.8 | [ ] Landing page | Dev | P0 | ⬜ |
| 0.4.9 | [ ] TEST: localhost:3000 OK | Dev | P0 | ⬜ |

### SPRINT 1 — CORE FLOW (24/03 - 06/04/2026)

| # | Task | Owner | Priority | Status |
|---|------|-------|----------|--------|
| 1.1.1 | [ ] Profile CRUD endpoints | Dev | P0 | ⬜ |
| 1.1.2 | [ ] Chart generation endpoint | Dev | P0 | ⬜ |
| 1.1.3 | [ ] Tier enforcement middleware | Dev | P0 | ⬜ |
| 1.1.4 | [ ] Unify engines → astrology-api.io | Dev | P0 | ⬜ |
| 1.2.1 | [ ] KB loader service | Dev | P0 | ⬜ |
| 1.2.2 | [ ] KB integration (all 5 systems) | Dev | P0 | ⬜ |
| 1.2.5 | [ ] Interpret service (L1→L1.5→L2→L3) | Dev | P0 | ⬜ |
| 1.2.6 | [ ] Prompt: system reading | Dev | P0 | ⬜ |
| 1.2.7 | [ ] Prompt: topic reading | Dev | P0 | ⬜ |
| 1.2.8 | [ ] Post-gen validator | Dev | P1 | ⬜ |
| 1.2.9 | [ ] Interpret endpoints | Dev | P0 | ⬜ |
| 1.2.10 | [ ] Cache L3 output (Redis 30d) | Dev | P0 | ⬜ |
| 1.3.1 | [ ] Login page | Dev | P0 | ⬜ |
| 1.3.2 | [ ] Register page | Dev | P0 | ⬜ |
| 1.3.3 | [ ] Auth store (Zustand) | Dev | P0 | ⬜ |
| 1.3.4 | [ ] Auth middleware | Dev | P0 | ⬜ |
| 1.4.1 | [ ] Wizard container (5-step) | Dev | P0 | ⬜ |
| 1.4.2 | [ ] Birth data form | Dev | P0 | ⬜ |
| 1.4.3 | [ ] City search (autocomplete) | Dev | P0 | ⬜ |
| 1.4.5 | [ ] Submit → create profile | Dev | P0 | ⬜ |
| 1.5.1 | [ ] Dashboard / Home page | Dev | P0 | ⬜ |
| 1.5.3 | [ ] System Reading page | Dev | P0 | ⬜ |
| 1.5.5 | [ ] Topic Reading page | Dev | P0 | ⬜ |
| 1.5.7 | [ ] Interpret hook (TanStack Query) | Dev | P0 | ⬜ |
| 1.5.8 | [ ] Tier gate component (blur + CTA) | Dev | P0 | ⬜ |
| 1.5.9 | [ ] Loading skeleton (shimmer) | Dev | P1 | ⬜ |

### SPRINT 2 — MONETIZATION (07-20/04/2026)

| # | Task | Owner | Priority | Status |
|---|------|-------|----------|--------|
| 2.1.1 | [ ] VietQR service (QR + txn code) | Dev | P0 | ⬜ |
| 2.1.2 | [ ] Payment verification service | Dev | P0 | ⬜ |
| 2.1.3 | [ ] Payment endpoints | Dev | P0 | ⬜ |
| 2.1.5 | [ ] Subscription activation | Dev | P0 | ⬜ |
| 2.1.6 | [ ] Migration 002 (payments table) | Dev | P0 | ⬜ |
| 2.1.7 | [ ] Tier check in /interpret/* | Dev | P0 | ⬜ |
| 2.2.1 | [ ] Pricing page (FREE/PRO) | Dev | P0 | ⬜ |
| 2.2.2 | [ ] Checkout page (VietQR) | Dev | P0 | ⬜ |
| 2.2.3 | [ ] Payment callback (success/fail) | Dev | P0 | ⬜ |
| 2.2.5 | [ ] Profile page (tier info) | Dev | P0 | ⬜ |
| 2.2.6 | [ ] Settings page | Dev | P1 | ⬜ |

### SPRINT 3 — POLISH & LAUNCH (21-29/04/2026)

| # | Task | Owner | Priority | Status |
|---|------|-------|----------|--------|
| 3.1.1 | [ ] PDF export service (ReportLab) | Dev | P0 | ⬜ |
| 3.1.2 | [ ] PDF endpoint (PRO tier) | Dev | P0 | ⬜ |
| 3.1.5 | [ ] Health check endpoint | Dev | P0 | ⬜ |
| 3.1.6 | [ ] Sentry integration | Dev | P0 | ⬜ |
| 3.2.5 | [ ] Domain radar chart (Recharts) | Dev | P1 | ⬜ |
| 3.3.1 | [ ] SEO metadata (per page) | Dev | P0 | ⬜ |
| 3.3.2 | [ ] Sitemap (next-sitemap) | Dev | P1 | ⬜ |
| 3.3.3 | [ ] Mobile responsive pass | Dev | P0 | ⬜ |
| 3.3.4 | [ ] Lighthouse 90+ | Dev | P1 | ⬜ |
| 3.4.1 | [ ] Deploy frontend → Vercel | Dev | P0 | ⬜ |
| 3.4.2 | [ ] Deploy backend → Railway | Dev | P0 | ⬜ |
| 3.4.3 | [ ] Setup Neon PostgreSQL (prod) | Dev | P0 | ⬜ |
| 3.4.4 | [ ] Setup Upstash Redis (prod) | Dev | P0 | ⬜ |
| 3.4.5 | [ ] Configure domain: 360human.vn | Dev | P0 | ⬜ |
| 3.4.6 | [ ] SSL certificate | Dev | P0 | ⬜ |
| 3.4.7 | [ ] Monitoring (Sentry + UptimeRobot) | Dev | P0 | ⬜ |
| 3.4.9 | [ ] CI/CD pipeline | Dev | P1 | ⬜ |

### MARKETING & LAUNCH (Parallel)

| # | Task | Owner | Status |
|---|------|-------|--------|
| M.1 | [ ] UX Writing finalized (Vietnamese tone) | Winston | ⬜ |
| M.2 | [ ] Landing page copy | Winston | ⬜ |
| M.3 | [ ] Nano/Atomic influencer outreach | Winston | ⬜ |
| M.4 | [ ] Social media accounts setup | Winston | ⬜ |
| M.5 | [ ] Beta testers recruitment (10-20 people) | Winston | ⬜ |
| M.6 | [ ] Launch announcement content | Winston | ⬜ |

---

## PROGRESS DASHBOARD

```mermaid
pie title Task Completion (17/03/2026)
    "Done" : 35
    "In Progress" : 1
    "Remaining" : 99
```

| Workstream | Total | Done | In Progress | Remaining |
|-----------|-------|------|-------------|-----------|
| Pre-Sprint Setup | 12 | 12 | 0 | 0 |
| Knowledge Base | 9 | 7 | 1 | 1 |
| UX/UI Design | 23 | 18 | 0 | 5 |
| Sprint 0 (Foundation) | 31 | 0 | 0 | 31 |
| Sprint 1 (Core Flow) | 26 | 0 | 0 | 26 |
| Sprint 2 (Monetization) | 11 | 0 | 0 | 11 |
| Sprint 3 (Launch) | 17 | 0 | 0 | 17 |
| Marketing | 6 | 0 | 0 | 6 |
| **TOTAL** | **135** | **37** | **1** | **97** |

---

## WEEKLY MILESTONES

| Week | Dates | Focus | Deliverable | Status |
|------|-------|-------|-------------|--------|
| W0 | 15-16 Mar | Setup + KB | Planning, KB 5/5, Domain | ✅ Done |
| W1 | 17-23 Mar | Foundation + Design | Docker + DB + Auth + Wireframes | 🟡 17/03: UX done, wireframes done, tier collapse done |
| W2 | 24-30 Mar | Core Backend + Auth UI | L3 Pipeline + Onboarding | ⬜ |
| W3 | 31 Mar-6 Apr | Core Frontend | Dashboard + Readings | ⬜ |
| W4 | 7-13 Apr | Payment | VietQR + Pricing | ⬜ |
| W5 | 14-20 Apr | Monetization | Checkout + Tier enforcement | ⬜ |
| W6 | 21-27 Apr | Polish + Deploy | PDF + SEO + Vercel/Railway | ⬜ |
| W7 | 28-29 Apr | 🚀 LAUNCH | 360human.vn LIVE | ⬜ |

---

## BLOCKERS

| Blocker | Impact | Status |
|---------|--------|--------|
| ~~API Key~~ | ~~All L1 computation~~ | ✅ Done |
| ~~Domain~~ | ~~Deployment~~ | ✅ 360human.vn purchased |
| ~~HD KB~~ | ~~HD readings~~ | ✅ 486K words |
| ~~Numerology KB~~ | ~~Num readings~~ | ✅ 1M words |
| ~~Vedic KB~~ | ~~Vedic readings~~ | ✅ 1.5M words |
| ~~BaZi KB~~ | ~~BaZi readings~~ | ✅ 973K words |
| ~~Tu Vi KB~~ | ~~Tu Vi readings~~ | ✅ 2M words |
| ~~Wireframes~~ | ~~Frontend implementation~~ | ✅ HTML wireframes (FREE + PRO) |
| Tier collapse update | 9 project files still reference MAX | 🔲 Next session |
| Design system v2 | Colors TBD (current wireframe = B&W) | 🔲 After wireframe review |
| Reading template | L3 prompt quality | 🔲 Sprint 1 |

---

## TODAY DONE (17/03/2026)

| # | Task | Impact |
|---|------|--------|
| 1 | UX Review 17 issues → all resolved | S4 2-col, accordion, inline actions |
| 2 | **Tier collapse: 3→2 tiers (FREE/PRO)** | PRO = everything, no MAX |
| 3 | FE-003, FE-004, FE-005 fully updated | All screens, design system, components |
| 4 | FE-007 Design References created | 12 sites researched, categorized |
| 5 | HTML wireframes (FREE + PRO views) | Clickable prototype in browser |
| 6 | Navigation patterns + Error states added | 3 layouts, 8 error states defined |

## NEXT SESSION — Plan

| Priority | Task | Notes |
|----------|------|-------|
| P0 | Update 9 project files for tier collapse | ARCH-001, ARCH-002, ARCH-004, PRD-001, CEO-002, etc. |
| P0 | Design system v2 — finalize colors | Wireframe hiện tại B&W, cần decide palette |
| P1 | Sprint 0 kickoff — Docker + DB | If design decisions settled |

---

## DETAIL GANTT — Per Workstream

### Knowledge Base Detail

```mermaid
gantt
    title KB Build Timeline
    dateFormat  YYYY-MM-DD
    axisFormat  %d %b

    section Human Design
    Schema design           :done, hd1, 2026-03-15, 1d
    Source files (10 books)  :done, hd2, 2026-03-15, 1d
    Types (40K words)        :done, hd3, 2026-03-15, 1d
    Centers (35K words)      :done, hd4, 2026-03-15, 1d
    Profiles (15K words)     :done, hd5, 2026-03-15, 1d
    Authorities (12K words)  :done, hd6, 2026-03-15, 1d
    Gates+Channels (383K)    :done, hd7, 2026-03-15, 1d

    section Numerology
    Source files (11 books)  :done, nm1, 2026-03-15, 1d
    Life Path (281K)         :done, nm2, 2026-03-15, 1d
    Expression (226K)        :done, nm3, 2026-03-15, 1d
    Soul Urge (344K)         :done, nm4, 2026-03-15, 1d
    Personal Year (128K)     :done, nm5, 2026-03-15, 1d
    Karmic Debt (49K)        :done, nm6, 2026-03-15, 1d

    section Vedic
    Source files (14 books)  :done, vd1, 2026-03-15, 1d
    Rashis (262K)            :done, vd2, 2026-03-15, 1d
    Nakshatras (489K)        :done, vd3, 2026-03-15, 1d
    Planets (182K)           :done, vd4, 2026-03-15, 1d
    Houses (215K)            :done, vd5, 2026-03-15, 1d
    Dashas (145K)            :done, vd6, 2026-03-15, 1d
    Yogas (260K)             :done, vd7, 2026-03-15, 1d

    section BaZi
    Source files (11 books)  :done, bz1, 2026-03-15, 1d
    Heavenly Stems (183K)    :done, bz2, 2026-03-15, 1d
    Earthly Branches (317K)  :done, bz3, 2026-03-15, 1d
    Ten Gods (171K)          :done, bz4, 2026-03-15, 1d
    Day Master (222K)        :done, bz5, 2026-03-15, 1d
    Luck Pillars (80K)       :done, bz6, 2026-03-15, 1d

    section Tu Vi
    Source files             :active, tv1, 2026-03-16, 1d
    Schema + Structure       :tv2, after tv1, 1d
    Content extraction       :tv3, after tv2, 2d
```

### UX/UI Design Detail

```mermaid
gantt
    title UX/UI Design Timeline
    dateFormat  YYYY-MM-DD
    axisFormat  %d %b

    section D1 Wireframes
    Landing Page             :d11, 2026-03-16, 1d
    Login/Register           :d12, 2026-03-16, 1d
    Onboarding Wizard        :d13, 2026-03-17, 1d
    Dashboard/Home           :d14, 2026-03-17, 1d
    System Reading           :d15, 2026-03-18, 1d
    Topic Reading            :d16, 2026-03-18, 1d
    Pricing Page             :d17, 2026-03-19, 1d
    Profile/Settings         :d18, 2026-03-19, 1d

    section D2 Design System
    Color palette            :d21, 2026-03-20, 1d
    Typography scale         :d22, 2026-03-20, 1d
    Spacing & grid           :d23, 2026-03-21, 1d
    Component library        :d24, 2026-03-21, 1d
    Icon set (5fw + 10topic) :d25, 2026-03-22, 1d

    section D3 Hi-Fi
    Landing (desktop+mobile) :d31, 2026-03-23, 1d
    Onboarding flow          :d32, 2026-03-23, 1d
    Dashboard + Reading      :d33, 2026-03-24, 1d
    Pricing + Checkout       :d34, 2026-03-24, 1d
    Chart visualizations     :d35, 2026-03-25, 1d

    section D4 Handoff
    Clickable prototype      :d41, 2026-03-26, 1d
    Design tokens export     :d42, 2026-03-26, 1d
    Component specs          :d43, 2026-03-27, 1d
```

### Development Sprint Detail

```mermaid
gantt
    title Development Sprints Detail
    dateFormat  YYYY-MM-DD
    axisFormat  %d %b

    section Sprint 0 — Foundation
    .gitignore + Dockerfile      :s001, 2026-03-17, 1d
    docker-compose.yml           :s002, 2026-03-17, 1d
    TEST compose up              :s003, 2026-03-18, 1d
    Alembic init + env.py        :s004, 2026-03-18, 1d
    User + Profile + Sub models  :s005, 2026-03-19, 1d
    Migration 001 + upgrade      :s006, 2026-03-19, 1d
    JWT security + deps.py       :s007, 2026-03-20, 1d
    Auth endpoints (register/login) :s008, 2026-03-20, 1d
    Users endpoints + rate limit :s009, 2026-03-21, 1d
    TEST auth flow               :s010, 2026-03-21, 1d
    create-next-app + deps       :s011, 2026-03-17, 1d
    shadcn init + components     :s012, 2026-03-18, 1d
    Design tokens + app shell    :s013, 2026-03-19, 1d
    API client (Axios+JWT)       :s014, 2026-03-20, 1d
    Landing page                 :s015, 2026-03-21, 1d
    TEST frontend dev OK         :s016, 2026-03-22, 1d
    GATE 0                       :milestone, g0, 2026-03-23, 0d

    section Sprint 1 — Core Flow
    Profile CRUD + Charts API    :s101, 2026-03-24, 2d
    Tier enforcement middleware  :s102, 2026-03-26, 1d
    Unify engines → API          :s103, 2026-03-24, 2d
    KB loader service            :s104, 2026-03-24, 1d
    Interpret service (L1→L3)    :crit, s105, 2026-03-25, 4d
    Prompt templates (sys+topic) :s106, 2026-03-27, 2d
    Post-gen validator           :s107, 2026-03-29, 1d
    Interpret endpoints          :s108, 2026-03-29, 2d
    Cache L3 (Redis 30d)         :s109, 2026-03-31, 1d
    Login + Register pages       :s110, 2026-03-24, 2d
    Auth store (Zustand)         :s111, 2026-03-26, 1d
    Auth middleware + provider   :s112, 2026-03-27, 1d
    Onboarding wizard (5 steps)  :s113, 2026-03-28, 3d
    Dashboard / Home             :s114, 2026-03-31, 2d
    System Reading page          :s115, 2026-04-02, 2d
    Topic Reading page           :s116, 2026-04-04, 2d
    Tier gate + Loading skeleton :s117, 2026-04-05, 1d
    GATE 1                       :milestone, g1, 2026-04-06, 0d

    section Sprint 2 — Monetization
    VietQR service               :s201, 2026-04-07, 2d
    Payment verification         :s202, 2026-04-09, 2d
    Payment endpoints            :s203, 2026-04-11, 1d
    Subscription activation      :s204, 2026-04-12, 1d
    Migration 002 (payments)     :s205, 2026-04-07, 1d
    Tier check in /interpret/*   :s206, 2026-04-13, 1d
    Pricing page (3 tiers)       :s207, 2026-04-09, 2d
    Checkout page (VietQR)       :s208, 2026-04-11, 2d
    Payment callback             :s209, 2026-04-13, 1d
    Profile page (tier info)     :s210, 2026-04-14, 1d
    Settings page                :s211, 2026-04-15, 1d
    GATE 2                       :milestone, g2, 2026-04-20, 0d

    section Sprint 3 — Polish & Launch
    PDF export service           :s301, 2026-04-21, 2d
    PDF endpoint (MAX)           :s302, 2026-04-23, 1d
    Health check + Sentry        :s303, 2026-04-21, 1d
    Domain radar chart           :s304, 2026-04-22, 2d
    SEO metadata + sitemap       :s305, 2026-04-23, 1d
    Mobile responsive            :s306, 2026-04-24, 1d
    Lighthouse 90+               :s307, 2026-04-24, 1d
    Deploy Vercel + Railway      :crit, s308, 2026-04-25, 1d
    Neon PG + Upstash Redis      :s309, 2026-04-25, 1d
    Domain + SSL                 :s310, 2026-04-26, 1d
    Monitoring (Sentry+Uptime)   :s311, 2026-04-27, 1d
    CI/CD pipeline               :s312, 2026-04-27, 1d
    Final QA                     :s313, 2026-04-28, 1d
    LAUNCH 🚀                   :milestone, crit, launch, 2026-04-29, 0d
```

### Marketing & Launch Detail

```mermaid
gantt
    title Marketing Timeline
    dateFormat  YYYY-MM-DD
    axisFormat  %d %b

    section Content
    UX Writing (Vietnamese tone) :m1, 2026-04-01, 5d
    Landing page copy            :m2, 2026-04-01, 3d
    Social media accounts        :m3, 2026-04-05, 2d
    Launch announcement content  :m4, 2026-04-20, 5d

    section Outreach
    Nano/Atomic influencer list  :m5, 2026-04-07, 3d
    Influencer outreach          :m6, 2026-04-10, 10d
    Beta testers recruit (10-20) :m7, 2026-04-14, 5d
    Beta testing period          :m8, 2026-04-19, 10d

    section Launch
    Pre-launch buzz              :m9, 2026-04-25, 3d
    Launch day campaign          :crit, m10, 2026-04-29, 1d
    Post-launch monitoring       :m11, 2026-04-29, 7d
```
