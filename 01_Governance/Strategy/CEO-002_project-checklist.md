---
title: "Project Checklist & Sprint Tracker"
id: "CEO-002"
source: "generated from ARCH-001 blueprint + CEO clarifications"
updated: "2026-03-15"
status: "active"
---

# 360Human — Sprint Tracker

> **Launch Date:** 29/04/2026 | **Team:** 1 fullstack dev
> **Total Tasks:** 105 | **Duration:** ~6.5 weeks (4 sprints)
> **Tracking:** Mark `[x]` when done, add date in `Done` column

---

## SPRINT 0 — FOUNDATION (Week 1: 17-23 Mar)

**Goal:** `docker-compose up` + frontend dev server + auth API working
**Gate:** Compose up OK + Alembic OK + Auth OK + Frontend OK

### 0.1 Infrastructure (6 tasks)

| # | Task | Priority | Done |
|---|------|----------|------|
| 0.1.1 | [ ] Create `.gitignore` (Python + Node + Docker) | P0 | |
| 0.1.2 | [ ] Create `backend/Dockerfile` (Python 3.12) | P0 | |
| 0.1.3 | [ ] Create `docker-compose.yml` (API + PG + Redis) | P0 | |
| 0.1.4 | [ ] Create `.dockerignore` | P1 | |
| 0.1.5 | [ ] CI pipeline `.github/workflows/ci.yml` | P2 | |
| 0.1.6 | [ ] **TEST:** `docker-compose up` → all services running | P0 | |

### 0.2 Database (8 tasks)

| # | Task | Priority | Done |
|---|------|----------|------|
| 0.2.1 | [ ] `alembic init` in backend/ | P0 | |
| 0.2.2 | [ ] Configure `env.py` (async + PostgreSQL) | P0 | |
| 0.2.3 | [ ] Create `User` model (UUID, email, password_hash, tier ENUM) | P0 | |
| 0.2.4 | [ ] Create `Profile` model (birth_date, birth_time, lat/lon, timezone, gender) | P0 | |
| 0.2.5 | [ ] Create `Subscription` model (tier, provider=vietqr, status) | P0 | |
| 0.2.6 | [ ] Generate migration 001 | P0 | |
| 0.2.7 | [ ] Run `alembic upgrade head` → tables created | P0 | |
| 0.2.8 | [ ] Remove `create_all()` from main.py (use Alembic only) | P1 | |

### 0.3 Auth API (8 tasks)

| # | Task | Priority | Done |
|---|------|----------|------|
| 0.3.1 | [ ] Install deps: python-jose, passlib[bcrypt], slowapi, structlog | P0 | |
| 0.3.2 | [ ] Create `core/security.py` (JWT HS256, 30d access, 30d refresh) | P0 | |
| 0.3.3 | [ ] Create `api/deps.py` (get_current_user dependency) | P0 | |
| 0.3.4 | [ ] Create `api/auth.py` (POST /register, /login, /refresh) | P0 | |
| 0.3.5 | [ ] Create `api/users.py` (GET /users/me, PUT /users/me) | P0 | |
| 0.3.6 | [ ] Add rate limiting (slowapi) | P1 | |
| 0.3.7 | [ ] Add structured logging (structlog → JSON) | P1 | |
| 0.3.8 | [ ] **TEST:** register → login → GET /me → valid response | P0 | |

### 0.4 Frontend Scaffold (9 tasks)

| # | Task | Priority | Done |
|---|------|----------|------|
| 0.4.1 | [ ] `create-next-app` (Next.js 15, App Router, TypeScript) | P0 | |
| 0.4.2 | [ ] Install deps: Axios, Zustand, TanStack Query, React Hook Form, Zod, Framer Motion | P0 | |
| 0.4.3 | [ ] `npx shadcn@latest init` + configure Tailwind v4 | P0 | |
| 0.4.4 | [ ] Add shadcn components: Button, Card, Input, Dialog, Sheet, Tabs | P0 | |
| 0.4.5 | [ ] Design tokens (CSS vars: colors, spacing, typography — warm/calm palette) | P0 | |
| 0.4.6 | [ ] App shell layout (header, main, footer) | P0 | |
| 0.4.7 | [ ] API client (Axios + JWT interceptor + auto-refresh on 401) | P0 | |
| 0.4.8 | [ ] Landing page (hero, trust-builders, CTA) | P0 | |
| 0.4.9 | [ ] **TEST:** `npm run dev` → landing page at localhost:3000 | P0 | |

**Sprint 0 Subtotal: 31 tasks**

---

## SPRINT 1 — CORE FLOW (Week 2-3: 24 Mar - 6 Apr)

**Goal:** User đăng ký → nhập birth data → xem luận giải (free tier)
**Gate:** Register → Onboard → Dashboard → Reading (free tier truncated at 2,000w)

### 1.1 Backend: Profile & Charts (5 tasks)

| # | Task | Priority | Done |
|---|------|----------|------|
| 1.1.1 | [ ] Profile CRUD endpoints (POST/GET/PUT/DELETE /profiles) | P0 | |
| 1.1.2 | [ ] Chart generation endpoint (link to profile birth data) | P0 | |
| 1.1.3 | [ ] Tier enforcement middleware (`tier_gate.py`: max_profiles, max_words) | P0 | |
| 1.1.4 | [ ] Unify all engines → astrology-api.io wrapper | P0 | |
| 1.1.5 | [ ] Remove any local computation deps (all via API) | P1 | |

### 1.2 Backend: L3 AI Pipeline (10 tasks)

| # | Task | Priority | Done |
|---|------|----------|------|
| 1.2.1 | [ ] KB loader service (`knowledge_base/loader.py`) | P0 | |
| 1.2.2 | [ ] KB JSON: `zi_wei/` (Tử Vi rules — digitize from PDF) | P0 | |
| 1.2.3 | [ ] KB JSON: `numerology/` (numerology rules) | P0 | |
| 1.2.4 | [ ] KB JSON: `human_design/`, `bazi/`, `vedic/` | P0 | |
| 1.2.5 | [ ] Interpret service: L1 (API raw) → L1.5 (enrich) → L2 (RAG) → L3 (Claude) | P0 | |
| 1.2.6 | [ ] Prompt template: system reading (1 framework → all topics) | P0 | |
| 1.2.7 | [ ] Prompt template: topic reading (1 topic → all 5 frameworks) | P0 | |
| 1.2.8 | [ ] Post-generation validator (word count, language, hallucination check) | P1 | |
| 1.2.9 | [ ] Interpret endpoints: `/interpret/system/{fw}/{pid}` + `/interpret/topic/{domain}/{pid}` | P0 | |
| 1.2.10 | [ ] Cache L3 output in Redis (TTL 30 days) | P0 | |

### 1.3 Frontend: Auth UI (5 tasks)

| # | Task | Priority | Done |
|---|------|----------|------|
| 1.3.1 | [ ] Login page (email + password) | P0 | |
| 1.3.2 | [ ] Register page (email + password + confirm) | P0 | |
| 1.3.3 | [ ] Auth store (Zustand: user, token, login/logout actions) | P0 | |
| 1.3.4 | [ ] Auth middleware (redirect unauthenticated → /login) | P0 | |
| 1.3.5 | [ ] Auth provider (wrap app, auto-refresh token) | P0 | |

### 1.4 Frontend: Onboarding Wizard (5 tasks)

| # | Task | Priority | Done |
|---|------|----------|------|
| 1.4.1 | [ ] Wizard container (5-step flow with progress bar) | P0 | |
| 1.4.2 | [ ] Birth data form (date picker, time picker, gender select) | P0 | |
| 1.4.3 | [ ] City search (autocomplete → lat/lon/timezone) | P0 | |
| 1.4.4 | [ ] Step indicator component (current step highlight) | P1 | |
| 1.4.5 | [ ] Submit → POST /profiles → navigate to dashboard | P0 | |

### 1.5 Frontend: Dashboard & Readings (9 tasks)

| # | Task | Priority | Done |
|---|------|----------|------|
| 1.5.1 | [ ] Dashboard / Home page (overview cards for 10 topics) | P0 | |
| 1.5.2 | [ ] Chart data hook (TanStack Query → GET /charts/{pid}) | P0 | |
| 1.5.3 | [ ] System Reading page (per framework, tabbed view) | P0 | |
| 1.5.4 | [ ] System card component (framework name, summary, CTA) | P0 | |
| 1.5.5 | [ ] Topic Reading page (per domain, multi-framework view) | P0 | |
| 1.5.6 | [ ] Topic card component (domain name, excerpt, status) | P0 | |
| 1.5.7 | [ ] Interpret hook (TanStack Query → GET /interpret/*) | P0 | |
| 1.5.8 | [ ] Tier gate component (blur/truncate + "Nâng cấp" CTA) | P0 | |
| 1.5.9 | [ ] Loading skeleton (shimmer effect while AI generates) | P1 | |

**Sprint 1 Subtotal: 34 tasks**

---

## SPRINT 2 — MONETIZATION (Week 4-5: 7-20 Apr)

**Goal:** User trả tiền → unlock premium content
**Gate:** VietQR payment → tier upgraded → full content unlocked

### 2.1 Backend: Payments (7 tasks)

| # | Task | Priority | Done |
|---|------|----------|------|
| 2.1.1 | [ ] VietQR service (generate QR with transaction code) | P0 | |
| 2.1.2 | [ ] Payment verification service (match bank transfer → txn code) | P0 | |
| 2.1.3 | [ ] Payment endpoints: POST /checkout, POST /verify-payment | P0 | |
| 2.1.4 | [ ] Transaction verification logic (HMAC or bank API callback) | P0 | |
| 2.1.5 | [ ] Subscription activation (update user.tier on payment success) | P0 | |
| 2.1.6 | [ ] Migration 002: `payments` + `subscriptions` tables | P0 | |
| 2.1.7 | [ ] Enforce tier check in all `/interpret/*` endpoints | P0 | |

### 2.2 Frontend: Pricing & Checkout (6 tasks)

| # | Task | Priority | Done |
|---|------|----------|------|
| 2.2.1 | [ ] Pricing page (3 tiers: FREE/PRO/MAX comparison table) | P0 | |
| 2.2.2 | [ ] Checkout page (show VietQR code, transaction instructions) | P0 | |
| 2.2.3 | [ ] Payment callback page (success/pending/fail states) | P0 | |
| 2.2.4 | [ ] Upgrade CTA component (reusable "Nâng cấp" button) | P0 | |
| 2.2.5 | [ ] Profile page (tier info, purchase date, account details) | P0 | |
| 2.2.6 | [ ] Settings page (change password, preferences, delete account) | P1 | |

**Sprint 2 Subtotal: 13 tasks**

---

## SPRINT 3 — POLISH & LAUNCH (Week 6-7: 21-29 Apr)

**Goal:** Production-ready, deploy live at 360human.vn
**Gate:** 🚀 360human.vn LIVE on 29/04/2026

### 3.1 Backend: Premium Features (7 tasks)

| # | Task | Priority | Done |
|---|------|----------|------|
| 3.1.1 | [ ] PDF export service (ReportLab — 36-page report) | P0 | |
| 3.1.2 | [ ] PDF endpoint: GET /export/pdf/{pid} (MAX tier only) | P0 | |
| 3.1.3 | [ ] Compatibility engine (partner birth data → cross-analysis) | P2 | |
| 3.1.4 | [ ] Compatibility endpoint | P2 | |
| 3.1.5 | [ ] Health check endpoint (GET /health) | P0 | |
| 3.1.6 | [ ] Sentry integration (error tracking) | P0 | |
| 3.1.7 | [ ] Rate limiting tuning (per-endpoint based on load) | P1 | |

### 3.2 Frontend: Advanced UI (6 tasks)

| # | Task | Priority | Done |
|---|------|----------|------|
| 3.2.1 | [ ] Life Map page (4x4 grid palace visualization) | P2 | |
| 3.2.2 | [ ] Palace grid component (interactive hover) | P2 | |
| 3.2.3 | [ ] Compatibility page (partner input + results) | P2 | |
| 3.2.4 | [ ] Share card component (9:16 aspect, screenshot-friendly) | P2 | |
| 3.2.5 | [ ] Domain radar chart (Recharts RadarChart for 10 topics) | P1 | |
| 3.2.6 | [ ] Timeline matrix (yearly fortune cycles) | P2 | |

### 3.3 SEO & Performance (5 tasks)

| # | Task | Priority | Done |
|---|------|----------|------|
| 3.3.1 | [ ] SEO metadata (title, description, og:image per page) | P0 | |
| 3.3.2 | [ ] Sitemap generation (next-sitemap) | P1 | |
| 3.3.3 | [ ] Mobile responsive pass (all 8 screens) | P0 | |
| 3.3.4 | [ ] Lighthouse audit → target 90+ score | P1 | |
| 3.3.5 | [ ] E2E Playwright tests (critical paths) | P2 | |

### 3.4 Deployment (9 tasks)

| # | Task | Priority | Done |
|---|------|----------|------|
| 3.4.1 | [ ] Deploy frontend → Vercel (connect GitHub repo) | P0 | |
| 3.4.2 | [ ] Deploy backend → Railway (Docker, env vars) | P0 | |
| 3.4.3 | [ ] Setup Neon PostgreSQL (production database) | P0 | |
| 3.4.4 | [ ] Setup Upstash Redis (production cache) | P0 | |
| 3.4.5 | [ ] Configure custom domain: 360human.vn | P0 | |
| 3.4.6 | [ ] SSL certificate (HTTPS) | P0 | |
| 3.4.7 | [ ] Monitoring: Sentry (errors) + UptimeRobot (uptime) | P0 | |
| 3.4.8 | [ ] DB backup config (daily, 7-day retention via Neon) | P1 | |
| 3.4.9 | [ ] CI/CD deploy pipeline (GitHub Actions → Vercel + Railway) | P1 | |

**Sprint 3 Subtotal: 27 tasks**

---

## PROGRESS DASHBOARD

| Sprint | Tasks | P0 | P1 | P2 | Status |
|--------|-------|----|----|-----|--------|
| Sprint 0 — Foundation | 31 | 25 | 5 | 1 | ⬜ Not started |
| Sprint 1 — Core Flow | 34 | 29 | 4 | 1 | ⬜ Not started |
| Sprint 2 — Monetization | 13 | 12 | 1 | 0 | ⬜ Not started |
| Sprint 3 — Polish & Launch | 27 | 14 | 6 | 7 | ⬜ Not started |
| **TOTAL** | **105** | **80** | **16** | **9** | |

### Priority Legend
- **P0 (80 tasks):** Must-have for launch — do these first
- **P1 (16 tasks):** Should-have — do if time allows
- **P2 (9 tasks):** Nice-to-have — defer to post-launch if needed

### If Time Is Tight (Cut List)
Drop these P2 tasks to save ~1 week:
- 3.1.3-3.1.4: Compatibility engine (defer post-launch)
- 3.2.1-3.2.4: Life Map + Palace grid + Compatibility page + Share card
- 3.2.6: Timeline matrix
- 3.3.5: E2E Playwright tests
→ **Minimum viable: 96 tasks (cut 9)**

---

## BLOCKERS & DEPENDENCIES

| Blocker | Impact | Owner | Status |
|---------|--------|-------|--------|
| ~~Astrology API key~~ | ~~Blocks all L1 computation~~ | ~~Winston~~ | ✅ Key saved in backend/.env |
| ~~Human Design~~ | ~~Blocks HD readings~~ | ~~Team~~ | ✅ Confirmed on API |
| ~~Tử Vi~~ | ~~Blocks Tử Vi readings~~ | ~~Team~~ | ✅ Confirmed on API |
| Knowledge Base digitization (2000+ PDF pages) | Blocks L2 RAG pipeline | Team | ⬜ See [ARCH-005](../../3.%20Architecture/ARCH-005_kb-digitization-guide.md) |
| Figma/Wireframes | Parallel track, not blocking | Winston | ⬜ See [CRE-001](../../5.%20Creative%20Team/CRE-001_design-sprint.md) |
| Domain: 360human.vn | Blocks deployment (Sprint 3) | Winston | ⬜ See [RTM-001](../../6.%20RTM%20Strategy/RTM-001_domain-registration.md) |

---

## WEEKLY MILESTONES

| Week | Dates | Milestone | Deliverable |
|------|-------|-----------|-------------|
| W1 | 17-23 Mar | Foundation complete | Docker + DB + Auth + Landing page |
| W2 | 24-30 Mar | Backend core done | Profile API + L3 pipeline working |
| W3 | 31 Mar - 6 Apr | Full reading flow | Auth UI + Onboarding + Dashboard + Readings |
| W4 | 7-13 Apr | Payment integrated | VietQR + Pricing page + Tier enforcement |
| W5 | 14-20 Apr | Monetization complete | Checkout + Profile + Settings |
| W6 | 21-27 Apr | Production ready | PDF + SEO + Deploy + Monitoring |
| W7 | 28-29 Apr | 🚀 LAUNCH | 360human.vn LIVE |
