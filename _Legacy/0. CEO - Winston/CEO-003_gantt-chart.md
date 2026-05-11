---
title: "Gantt Chart — 360Human Development"
id: "CEO-003"
source: "generated from CEO-002 sprint tracker"
updated: "2026-03-15"
status: "active"
---

# 360Human — Gantt Chart

> Launch: **29/04/2026** | Team: **1 fullstack dev (Winston)** | Total: **105 tasks**
> Render: Paste into any Mermaid-compatible viewer (GitHub, VSCode Mermaid Preview, mermaid.live)

## Master Gantt

```mermaid
gantt
    title 360Human — Development Timeline (17 Mar → 29 Apr 2026)
    dateFormat  YYYY-MM-DD
    axisFormat  %d %b
    todayMarker stroke-width:3px,stroke:#f00

    section SPRINT 0 — FOUNDATION
    0.1 Infrastructure (Docker/CI)        :s01, 2026-03-17, 2d
    0.2 Database (Alembic/Models)          :s02, after s01, 2d
    0.3 Auth API (JWT/endpoints)           :s03, after s02, 2d
    0.4 Frontend Scaffold (Next.js/shadcn) :s04, after s01, 4d
    GATE 0 ✓ Compose+Auth+Frontend        :milestone, g0, after s03 s04, 0d

    section SPRINT 1 — CORE FLOW
    1.1 Profile & Charts API               :s11, 2026-03-24, 3d
    1.2 L3 AI Pipeline (KB+RAG+Claude)     :crit, s12, 2026-03-24, 8d
    1.3 Frontend Auth UI                   :s13, 2026-03-24, 3d
    1.4 Frontend Onboarding Wizard         :s14, after s13, 3d
    1.5 Dashboard & Readings UI            :s15, after s14, 4d
    KB Digitization (PDF→JSON)             :crit, kb, 2026-03-24, 10d
    GATE 1 ✓ Full Reading Flow             :milestone, g1, after s12 s15, 0d

    section SPRINT 2 — MONETIZATION
    2.1 VietQR Payment Backend             :s21, 2026-04-07, 5d
    2.2 Pricing & Checkout UI              :s22, 2026-04-09, 5d
    Tier Enforcement (BE+FE)               :s23, after s21, 3d
    GATE 2 ✓ Payment Working               :milestone, g2, after s22 s23, 0d

    section SPRINT 3 — POLISH & LAUNCH
    3.1 PDF Export (ReportLab)             :s31, 2026-04-21, 3d
    3.2 Advanced UI (Life Map/Charts)      :s32, 2026-04-21, 4d
    3.3 SEO & Performance                  :s33, 2026-04-23, 3d
    3.4 Deployment (Vercel/Railway/Neon)   :crit, s34, 2026-04-25, 3d
    Sentry + Monitoring                    :s35, after s34, 1d
    GATE 3 🚀 LAUNCH                      :milestone, crit, g3, 2026-04-29, 0d
```

## Dependency Map

```mermaid
graph LR
    subgraph "SPRINT 0 — Week 1"
        A[0.1 Docker+PG+Redis] --> B[0.2 Alembic+Models]
        B --> C[0.3 Auth API]
        A --> D[0.4 Frontend Scaffold]
    end

    subgraph "SPRINT 1 — Week 2-3"
        C --> E[1.1 Profile CRUD]
        E --> F[1.2 L3 AI Pipeline]
        C --> G[1.3 Auth UI]
        G --> H[1.4 Onboarding]
        H --> I[1.5 Dashboard+Readings]
        F --> I
        KB[KB Digitize PDF→JSON] --> F
    end

    subgraph "SPRINT 2 — Week 4-5"
        I --> J[2.1 VietQR Backend]
        J --> K[2.2 Pricing+Checkout]
        J --> L[Tier Enforcement]
    end

    subgraph "SPRINT 3 — Week 6-7"
        L --> M[3.1 PDF Export]
        K --> N[3.2 Advanced UI]
        K --> O[3.3 SEO+Perf]
        O --> P[3.4 Deploy]
        P --> Q[🚀 LAUNCH 29/04]
    end

    style F fill:#ff6b6b,color:#fff
    style KB fill:#ff6b6b,color:#fff
    style P fill:#ff6b6b,color:#fff
    style Q fill:#51cf66,color:#fff
```

## Critical Path (Red = Blocker)

```
Docker → Alembic → Auth API → Profile CRUD → L3 AI Pipeline → Dashboard → Payment → Deploy → 🚀
                                                    ↑
                                            KB Digitization (PDF→JSON)
```

**Longest chain: 38 days** (17 Mar → 29 Apr) — zero slack on critical path.

## Task Breakdown by Week

```mermaid
gantt
    title Weekly Task Distribution
    dateFormat  YYYY-MM-DD
    axisFormat  %d %b

    section Backend
    Docker + DB + Auth          :2026-03-17, 6d
    Profile + Charts API        :2026-03-24, 3d
    L3 AI Pipeline              :crit, 2026-03-24, 8d
    VietQR Payment              :2026-04-07, 5d
    Tier Enforcement            :2026-04-12, 3d
    PDF Export                  :2026-04-21, 3d
    Health + Sentry             :2026-04-25, 3d

    section Frontend
    Next.js Scaffold + Landing  :2026-03-17, 4d
    Auth UI (Login/Register)    :2026-03-24, 3d
    Onboarding Wizard           :2026-03-27, 3d
    Dashboard + Readings        :2026-03-30, 4d
    Pricing + Checkout          :2026-04-09, 5d
    Advanced UI + Charts        :2026-04-21, 4d
    SEO + Mobile                :2026-04-23, 3d

    section Data/AI
    KB Digitization (PDF→JSON)  :crit, 2026-03-24, 10d
    Prompt Templates            :2026-03-28, 4d
    Post-gen Validator          :2026-04-01, 2d

    section DevOps
    CI Pipeline                 :2026-03-19, 1d
    Deploy Vercel+Railway+Neon  :crit, 2026-04-25, 3d
    Domain + SSL + Monitoring   :2026-04-27, 2d
```

## Resource Allocation (1 Fullstack Dev)

| Week | Dates | Focus | Hours/day |
|------|-------|-------|-----------|
| W1 | 17-23 Mar | **Backend heavy:** Docker, DB, Auth API + Frontend scaffold | BE 70% / FE 30% |
| W2 | 24-30 Mar | **Parallel:** L3 Pipeline + Auth UI + Onboarding | BE 50% / FE 40% / AI 10% |
| W3 | 31 Mar - 6 Apr | **Frontend heavy:** Dashboard + Readings + KB digitize | FE 50% / AI 40% / BE 10% |
| W4 | 7-13 Apr | **Backend heavy:** VietQR payment + Tier enforcement | BE 60% / FE 40% |
| W5 | 14-20 Apr | **Frontend:** Pricing + Checkout + Profile + Settings | FE 70% / BE 30% |
| W6 | 21-27 Apr | **Polish:** PDF + Advanced UI + SEO + Deploy | FE 40% / BE 30% / Ops 30% |
| W7 | 28-29 Apr | **Launch:** Final QA + Go-live | Ops 80% / Fix 20% |

## Risk Heatmap

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| KB digitization takes >10 days | 🔴 High | 🔴 Critical | Start Day 1 of Sprint 1. Prioritize Tử Vi + Numerology first (highest user demand) |
| API rate limits hit during dev | 🟡 Medium | 🟡 Medium | Cache aggressively (Redis permanent TTL for L1 data) |
| VietQR verification edge cases | 🟡 Medium | 🟡 Medium | Manual verification fallback + admin panel |
| Single dev burnout (7 weeks straight) | 🔴 High | 🔴 Critical | Strict P0-only in Weeks 1-4. Cut P2 tasks if behind |
| Claude API output quality inconsistent | 🟡 Medium | 🔴 Critical | Post-gen validator + structured prompts + few-shot examples |

## Milestones & Deliverables

```mermaid
timeline
    title 360Human Key Milestones
    17 Mar : Sprint 0 Start
           : Docker + DB running
    23 Mar : GATE 0 ✓
           : Auth API + Frontend OK
    30 Mar : Backend L3 Pipeline MVP
           : Auth UI + Onboarding done
    06 Apr : GATE 1 ✓
           : Full reading flow working
    14 Apr : VietQR payment integrated
    20 Apr : GATE 2 ✓
           : Monetization complete
    27 Apr : Production deployed
           : SEO + monitoring live
    29 Apr : 🚀 GATE 3 — LAUNCH
           : 360human.vn LIVE
```

## How to View These Charts

1. **VSCode:** Install "Markdown Preview Mermaid Support" extension → Open Preview (Ctrl+Shift+V)
2. **GitHub:** Push to repo → GitHub renders Mermaid natively in `.md` files
3. **Online:** Paste Mermaid blocks at [mermaid.live](https://mermaid.live)
4. **Notion:** Use `/mermaid` block and paste chart code
