---
title: "Project Blueprint"
id: "ARCH-001"
source: "project-blueprint.md.docx"
converted: "2026-03-15 13:35"
status: "active"
---

# 360Human — Project Blueprint (Master Map)

**Cập nhật:** 2026-03-15 **Mục đích:** Bản đồ tổng thể — nhìn 1 lần hiểu toàn bộ project
> **UPDATED 2026-03-15** — API: astrology-api.io | Tiers: FREE/PRO/MAX | Launch: 29/04/2026 | Team: 1 fullstack
> Xem [ARCH-004 Clarifications](ARCH-004_clarifications-log.md) cho chi tiết changes.

## 1. MASTER TIMELINE

Week 1 Week 2 Week 3 Week 4 Week 5 Week 6 Week 7 Week 8

┌──────────┐ ┌──────────────────────────┐ ┌──────────────────────────┐ ┌──────────────────────────────────────────┐

│ PHASE 0 │ │ PHASE 1 │ │ PHASE 2 │ │ PHASE 3 │

│Foundation│ │ Core Flow │ │ Monetization │ │ Polish & Launch │

│ 24 tasks │ │ 29 tasks │ │ 13 tasks │ │ 22 tasks │

│ │ │ │ │ │ │ │

│ GATE: ✓ │──▶│ GATE: ✓ │──▶│ GATE: ✓ │──▶│ GATE: 🚀 LAUNCH │

└──────────┘ └──────────────────────────┘ └──────────────────────────┘ └──────────────────────────────────────────┘

## 2. ARCHITECTURE OVERVIEW (What We're Building)

┌─────────────────────────────────────────────────────────────────────────────────┐

│ │

│ 👤 USER (Browser / Mobile) │

│ │ │

│ ▼ │

│ ┌─────────────────────────────────────┐ │

│ │ FRONTEND — Next.js 15 (Vercel) │ │

│ │ ┌───────┬──────┬───────┬─────────┐ │ │

│ │ │Landing│Auth │Onboard│Dashboard│ │ Pages: │

│ │ │Page │Pages │Wizard │& Reads │ │ 11 screens total │

│ │ └───────┴──────┴───────┴─────────┘ │ │

│ │ Tailwind + shadcn/ui + Zustand │ │

│ └──────────────┬──────────────────────┘ │

│ │ HTTPS (JWT Bearer) │

│ ▼ │

│ ┌─────────────────────────────────────┐ ┌──────────────────────────────┐ │

│ │ BACKEND — FastAPI (Railway) │ │ EXTERNAL APIs │ │

│ │ ┌───────────────────────────────┐ │ │ ┌────────────────────────┐ │ │

│ │ │ API Layer │ │ │ │ AstroVisor API │ │ │

│ │ │ /auth /profiles /charts │ │────▶│ │ • /zi-wei/chart │ │ │

│ │ │ /interpret /payments │ │ │ │ • /human-design/chart │ │ │

│ │ └───────────────────────────────┘ │ │ │ • /bazi/chart │ │ │

│ │ ┌───────────────────────────────┐ │ │ │ • /vedic/natal │ │ │

│ │ │ Service Layer │ │ │ └────────────────────────┘ │ │

│ │ │ 3-Layer Pipeline (L1→L2→L3) │ │ │ ┌────────────────────────┐ │ │

│ │ │ Payment (MoMo/ZaloPay) │ │────▶│ │ Claude API (L3 AI) │ │ │

│ │ │ PDF Export │ │ │ └────────────────────────┘ │ │

│ │ └───────────────────────────────┘ │ │ ┌────────────────────────┐ │ │

│ │ ┌───────────────────────────────┐ │ │ │ MoMo / ZaloPay │ │ │

│ │ │ Data Layer │ │────▶│ │ Payment Gateways │ │ │

│ │ │ PostgreSQL + Redis + Cache │ │ │ └────────────────────────┘ │ │

│ │ └───────────────────────────────┘ │ └──────────────────────────────┘ │

│ └─────────────────────────────────────┘ │

│ │

└─────────────────────────────────────────────────────────────────────────────────┘

## 3. PHASE → TASK MAPPING (Detail)

### PHASE 0 — FOUNDATION (24 tasks, Week 1)

PHASE 0: "Chạy được docker-compose up + frontend dev"

═══════════════════════════════════════════════════════

┌─ 0.1 INFRASTRUCTURE (6 tasks) ──────────────────────────────────────────────┐

│ │

│ 0.1.1 .gitignore ─┐ │

│ 0.1.2 Dockerfile ├─▶ 0.1.3 docker-compose.yml ─▶ 0.1.6 TEST: compose up │

│ 0.1.4 .dockerignore┘ │

│ 0.1.5 CI pipeline (.github/workflows/ci.yml) │

│ │

│ Output: docker-compose up → API + PG + Redis running │

└─────────────────────────────────────────────────────────────────────────────┘

│

▼

┌─ 0.2 DATABASE (8 tasks) ───────────────────────────────────────────────────┐

│ │

│ 0.2.1 alembic init ──▶ 0.2.2 env.py config │

│ │ │

│ 0.2.3 User model ─────┐ │ │

│ 0.2.4 Profile model ──┼────▶ 0.2.6 migration 001 ──▶ 0.2.7 upgrade head │

│ 0.2.5 Subscription ───┘ │

│ │

│ 0.2.8 Remove create\_all() from main.py │

│ │

│ Output: users, profiles, subscriptions, chart\_cache tables │

└────────────────────────────────────────────────────────────────────────────┘

│

▼

┌─ 0.3 AUTH API (8 tasks) ──────────────────────────────────────────────────┐

│ │

│ 0.3.1 Install deps (jose, passlib) ──▶ 0.3.2 core/security.py │

│ │ │

│ 0.3.3 api/deps.py (get\_user) │

│ │ │

│ ┌────────────────────┴────────────────┐ │

│ ▼ ▼ │

│ 0.3.4 auth.py 0.3.5 users.py │

│ POST /register GET /users/me │

│ POST /login PUT /users/me │

│ POST /refresh │

│ │ │

│ 0.3.6 Rate limiting (slowapi) │

│ 0.3.7 Structured logging (structlog) │

│ │ │

│ 0.3.8 TEST: register → login → me │

│ │

│ Output: Working JWT auth endpoints │

└───────────────────────────────────────────────────────────────────────────┘

│

▼ (parallel with 0.3)

┌─ 0.4 FRONTEND SCAFFOLD (9 tasks) ────────────────────────────────────────┐

│ │

│ 0.4.1 create-next-app ──▶ 0.4.2 Install deps ──▶ 0.4.3 shadcn init │

│ │ │

│ 0.4.4 Add components │

│ │ │

│ 0.4.5 Design tokens (CSS vars) ──┐ │ │

│ 0.4.6 App shell layout ──────────┼──▶ 0.4.8 Landing page │ │

│ 0.4.7 API client (ky + JWT) ─────┘ │ │ │

│ 0.4.9 TEST: dev ok │ │

│ │

│ Output: Landing page at localhost:3000 │

└───────────────────────────────────────────────────────────────────────────┘

GATE 0 ✓ = compose up OK + alembic OK + auth OK + frontend OK

### PHASE 1 — CORE FLOW (29 tasks, Week 2-3)

PHASE 1: "User đăng ký → nhập birth data → xem luận giải"

═══════════════════════════════════════════════════════════

┌─ 1.1 BACKEND: Profile & Charts (5 tasks) ──────────────────────────┐

│ │

│ 1.1.1 Profile CRUD ──▶ 1.1.2 Chart gen (link profile) │

│ │ │

│ 1.1.4 Unify engines ──▶ 1.1.5 Remove local deps │

│ (all 5 → AstroVisor) │ │

│ 1.1.3 Tier enforcement middleware │

│ │

└─────────────────────────────────────────────────────────────────────┘

│

▼

┌─ 1.2 BACKEND: L3 AI Pipeline (10 tasks) ──────────────────────────┐

│ │

│ ┌──────────────┐ ┌──────────────┐ ┌──────────────────────┐ │

│ │ 1.2.1 KB │ │ 1.2.2-4 JSON │ │ 1.2.5 Interpret svc │ │

│ │ Loader │──▶│ zi-wei/ │──▶│ L1 → L2 → L3 │ │

│ │ │ │ numerology/ │ │ Claude API call │ │

│ └──────────────┘ │ human-design/│ └──────────┬───────────┘ │

│ └──────────────┘ │ │

│ ▼ │

│ 1.2.6 Prompt: system reading ──┐ 1.2.8 Post-gen validator │

│ 1.2.7 Prompt: topic reading ──┘ │ │

│ 1.2.9 Interpret endpoints│

│ 1.2.10 Cache L3 output │

│ │

│ Output: /interpret/system/:fw/:pid + /interpret/topic/:dom/:pid │

└─────────────────────────────────────────────────────────────────────┘

│

▼ (parallel)

┌─ 1.3 FRONTEND: Auth (5 tasks) ─┐ ┌─ 1.4 FRONTEND: Onboarding (5 tasks) ─┐

│ │ │ │

│ 1.3.1 Login page │ │ 1.4.1 Wizard (5 steps) │

│ 1.3.2 Register page │ │ 1.4.2 Birth data form │

│ 1.3.3 Auth store (Zustand) │ │ 1.4.3 City search │

│ 1.3.4 Auth middleware │ │ 1.4.4 Step indicator │

│ 1.3.5 Auth provider │ │ 1.4.5 Submit → create profile │

│ │ │ │

└─────────────────────────────────┘ └────────────────────────────────────────┘

│ │

└────────────────┬───────────────────────┘

▼

┌─ 1.5 FRONTEND: Dashboard & Readings (9 tasks) ────────────────────┐

│ │

│ 1.5.1 Dashboard / Home ──▶ 1.5.2 Chart data hook │

│ │ │

│ ┌──────────────────────────┼──────────────────┐ │

│ ▼ ▼ ▼ │

│ 1.5.3 System Reading 1.5.5 Topic Reading 1.5.7 Interpret │

│ (per framework) (per domain) hook │

│ │ │ │

│ 1.5.4 System card 1.5.6 Topic card │

│ │

│ 1.5.8 Tier gate component ("Unlock" CTA) │

│ 1.5.9 Loading skeleton (shimmer) │

│ │

│ Output: Full reading flow with AI interpretation │

└─────────────────────────────────────────────────────────────────────┘

GATE 1 ✓ = register → onboard → dashboard → reading (free tier truncated)

### PHASE 2 — MONETIZATION (13 tasks, Week 4-5)

PHASE 2: "User trả tiền → unlock premium"

══════════════════════════════════════════

┌─ 2.1 BACKEND: Payments (7 tasks) ─────────────────────────────────┐

│ │

│ 2.1.1 MoMo service ────┐ │

│ 2.1.2 ZaloPay service ─┤ │

│ ▼ │

│ 2.1.3 Payment endpoints (/checkout, /webhook) │

│ │ │

│ 2.1.4 Webhook HMAC verification │

│ │ │

│ 2.1.5 Subscription activation │

│ │ │

│ 2.1.6 Migration 002 ───┘ │

│ (payments table) │

│ │

│ 2.1.7 Tier check in all /interpret/\* endpoints │

│ │

└─────────────────────────────────────────────────────────────────────┘

│

▼

┌─ 2.2 FRONTEND: Pricing & Checkout (6 tasks) ──────────────────────┐

│ │

│ 2.2.1 Pricing page ──▶ 2.2.2 Checkout page ──▶ 2.2.3 Callback │

│ (3 tiers) (MoMo/ZaloPay) (success/fail) │

│ │

│ 2.2.4 Upgrade CTA (reusable "Nâng cấp" button) │

│ 2.2.5 Profile page (tier info, subscription expiry) │

│ 2.2.6 Settings page (password, prefs, delete account) │

│ │

└─────────────────────────────────────────────────────────────────────┘

┌─ PRICING MODEL ───────────────────────────────────────────────┐

│ FREE │ 0 VND │ 5 systems (blur)│ 2,000w │ 2/10 topics │

│ PRO │ 199,000 (1 lần)│ 5 systems full │10,000w │ 10/10 topics │

│ MAX │ 499,000 (1 lần)│ 5 systems full │20,000w │ Full + PDF │

└───────────────────────────────────────────────────────────────┘

GATE 2 ✓ = pay via MoMo → tier upgraded → full content unlocked

### PHASE 3 — POLISH & LAUNCH (22 tasks, Week 6-8)

PHASE 3: "Production-ready, deploy live"

════════════════════════════════════════

┌─ 3.1 BACKEND: Premium (7) ──┐ ┌─ 3.2 FRONTEND: Advanced (6) ─────────┐

│ │ │ │

│ 3.1.1 PDF export service │ │ 3.2.1 Life Map page (4x4 grid) │

│ 3.1.2 PDF endpoint │ │ 3.2.2 Palace grid component │

│ 3.1.3 Compatibility engine │ │ 3.2.3 Compatibility page │

│ 3.1.4 Compatibility endpoint │ │ 3.2.4 Share card (9:16) │

│ 3.1.5 Full health check │ │ 3.2.5 Domain radar chart │

│ 3.1.6 Sentry integration │ │ 3.2.6 Timeline matrix │

│ 3.1.7 Rate limiting tuning │ │ │

└───────────────────────────────┘ └───────────────────────────────────────┘

│ │

└──────────────┬───────────────────────┘

▼

┌─ 3.3 SEO & PERFORMANCE (5) ──────────────────────────────────────┐

│ 3.3.1 SEO metadata │ 3.3.2 Sitemap │ 3.3.3 Mobile responsive│

│ 3.3.4 Lighthouse 90+ │ 3.3.5 E2E Playwright tests │

└───────────────────────────────────────────────────────────────────┘

│

▼

┌─ 3.4 DEPLOYMENT (9 tasks) ───────────────────────────────────────┐

│ │

│ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ │

│ │ Frontend │ │ Backend │ │ Database │ │ Redis │ │

│ │ Vercel │ │ Railway │ │ Neon │ │ Upstash │ │

│ │ 3.4.1 │ │ 3.4.2 │ │ 3.4.3 │ │ 3.4.4 │ │

│ └──────────┘ └──────────┘ └──────────┘ └──────────┘ │

│ │

│ 3.4.5 Custom domain (360human.vn) │

│ 3.4.6 SSL certificate │

│ 3.4.7 Monitoring (Sentry + UptimeRobot) │

│ 3.4.8 DB backup (daily, 7-day retention) │

│ 3.4.9 CI/CD deploy pipeline │

│ │

└───────────────────────────────────────────────────────────────────┘

GATE 3 ✓ = 360human.vn LIVE 🚀

## 4. DATA FLOW (How a Reading Works)

User nhấn "Xem Tử Vi"

│

▼

┌─ FRONTEND ──────────────────────────────────┐

│ TanStack Query → GET /interpret/system/ │

│ tu\_vi/{profile\_id} │

└──────────────────┬──────────────────────────┘

│

┌──────────▼──────────┐

│ CHECK CACHE (Redis) │

│ Key: tu\_vi:{pid} │

└──┬──────────────┬───┘

│ │

HIT │ MISS │

▼ ▼

Return cached ┌───────────────────────────────────────────────┐

│ L1: RAW DATA │

│ ┌─────────────────────────────────────────┐ │

│ │ asyncio.gather( │ │

│ │ AstroVisor.zi\_wei(birth\_data), │ │

│ │ AstroVisor.human\_design(birth\_data), │ │

│ │ AstroVisor.bazi(birth\_data), │ │

│ │ AstroVisor.vedic(birth\_data), │ │

│ │ ) │ │

│ │ + local\_numerology(birth\_data) │ │

│ └─────────────────────────────────────────┘ │

│ ~2-3s (4 API calls parallel) │

└─────────────────┬─────────────────────────────┘

│

┌─────────────────▼─────────────────────────────┐

│ L2: KB RAG LOOKUP │

│ Match L1 data → ground\_truth/\*.json │

│ "Thất Sát ở Cung Mệnh" → kb\_rule\_that\_sat │

│ "Life Path 2" → kb\_rule\_lp2 │

└─────────────────┬─────────────────────────────┘

│

┌─────────────────▼─────────────────────────────┐

│ L3: CLAUDE AI INTERPRETATION │

│ System prompt + L1 data + L2 rules │

│ → Claude API → Vietnamese prose │

│ Token budget: FREE 2,000w / PRO 10,000w / MAX 20,000w│

│ ~3-5s │

└─────────────────┬─────────────────────────────┘

│

┌─────────────────▼──────────┐

│ CACHE + RETURN │

│ Redis SET (TTL 30 days) │

│ → JSON response to frontend │

└──────────────────────────────┘

## 5. SCREEN MAP (11 Screens across Phases)

┌─────────────────────────────────────────────────────────────────────────────┐

│ SCREEN MAP │

│ │

│ PUBLIC (no auth) APP (auth required) PREMIUM (paid) │

│ ═══════════════ ══════════════════ ══════════════ │

│ │

│ ┌─────────┐ ┌─────────────┐ ┌──────────┐ │

│ │ Landing │──▶ Register ──▶ │ Dashboard │ │ Life Map │ │

│ │ Page │ /Login │ (Home) │ │ (4x4) │ │

│ └─────────┘ └──────┬──────┘ └──────────┘ │

│ Phase 0 │ Phase 3 │

│ │ │

│ ┌─────────┐ ┌─────────▼────────┐ ┌──────────┐ │

│ │ Pricing │ │ Onboarding │ │ Compat │ │

│ │ Page │ │ (5 steps) │ │ Page │ │

│ └─────────┘ └─────────┬────────┘ └──────────┘ │

│ Phase 2 │ Phase 3 │

│ ▼ │

│ ┌────────────────┐ │

│ │ System Reading │──▶ 5 tabs (Tu Vi, Than So, │

│ │ Page │ HD, BaZi, Vedic) │

│ └────────┬───────┘ │

│ │ │

│ ┌────────▼───────┐ │

│ │ Topic Reading │──▶ 6 domains (Career, │

│ │ Page │ Love, Health, ...) │

│ └────────────────┘ │

│ Phase 1 │

│ │

│ ┌────────────────┐ ┌────────────────┐ │

│ │ Profile Page │ │ Settings │ │

│ │ (tier, expiry) │ │ (pwd, prefs) │ │

│ └────────────────┘ └────────────────┘ │

│ Phase 2 Phase 2 │

│ │

│ Phase 0: Landing + Auth (3 screens) │

│ Phase 1: Onboarding + Dashboard + Readings (4 screens) │

│ Phase 2: Pricing + Profile + Settings + Checkout (4 screens) │

│ Phase 3: Life Map + Compatibility + Share (3 screens) │

└─────────────────────────────────────────────────────────────────────────────┘

## 6. DEPENDENCY CHAIN (What Blocks What)

┌─────────────────────────────────────────┐

│ CRITICAL PATH │

│ (mỗi bước phải xong trước bước sau) │

└─────────────────────────────────────────┘

Phase 0 Phase 1 Phase 2 Phase 3

─────── ─────── ─────── ───────

Docker + PG ──────▶ Alembic migrations OK

│

▼

Auth API ─────────▶ Auth UI (Login/Register) ──▶ All protected pages

│

▼

Frontend scaffold ─▶ Onboarding wizard ─────────▶ Dashboard ──▶ Readings

│

▼

Profile CRUD ──────▶ Chart generation ──▶ L3 AI interpret

│

▼

AstroVisor OK ──▶ All 5 systems

│

▼

Claude API OK ──▶ L3 prose output

│

▼

┌────────────────────────────┐

│ MONETIZATION CAN START │

│ (Phase 2: Payments + Tiers)│

└────────────────────────────┘

│

▼

Phase 3: PDF,

Compat, Deploy

PARALLEL TRACKS (không block nhau):

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

• Backend Auth (0.3) ∥ Frontend Scaffold (0.4)

• Auth UI (1.3) ∥ Onboarding (1.4)

• Backend L3 (1.2) ∥ Frontend Auth+Onboard (1.3+1.4)

• MoMo service (2.1) ∥ ZaloPay service (2.1) ∥ Frontend Pricing (2.2)

• PDF export (3.1) ∥ Life Map (3.2) ∥ SEO (3.3)

## 7. TECH STACK QUICK REFERENCE

┌──────────────────────────────────────────────────────────────────────────┐

│ LAYER TECHNOLOGY WHY │

│ ═════ ══════════ ═══ │

│ │

│ Frontend Next.js 15 App Router SSR + SEO + React Server Comp │

│ UI Tailwind + shadcn/ui Rapid, consistent UI │

│ State Zustand Simple, no boilerplate │

│ Data Fetch TanStack Query Cache, retry, dedup │

│ Forms React Hook Form + Zod Type-safe validation │

│ Animation Framer Motion Smooth transitions │

│ HTTP Axios JWT interceptor, auto-refresh │

│ │

│ Backend FastAPI (Python 3.12) Async, type hints, auto-docs │

│ ORM SQLAlchemy 2.0 async Mature, async support │

│ Migration Alembic SQLAlchemy integration │

│ Auth python-jose + passlib JWT + bcrypt │

│ Rate Limit slowapi Per-endpoint control │

│ Logging structlog JSON structured logs │

│ AI anthropic SDK Claude API for L3 │

│ │

│ Database PostgreSQL 16 Reliable, full-featured │

│ Cache Redis 7 Fast KV, TTL support │

│ │

│ External astrology-api.io All 5 systems (confirmed) │

│ Claude API L3 AI interpretation │

│ MoMo + ZaloPay Vietnamese payments │

│ │

│ Deploy Vercel (frontend) Free tier, edge network │

│ Railway (backend) Docker, easy setup │

│ Neon (PostgreSQL) Serverless PG, free tier │

│ Upstash (Redis) Serverless Redis │

│ │

│ DevOps Docker + Compose Local dev parity │

│ GitHub Actions CI/CD pipeline │

│ Sentry Error monitoring │

│ UptimeRobot Uptime monitoring │

│ │

│ Cost ~$85-150/month MVP │

└──────────────────────────────────────────────────────────────────────────┘

## 8. TASK COUNT SUMMARY

┌──────────┬──────────────────────┬───────┬────────────────────────────┐

│ PHASE │ SECTION │ TASKS │ KEY OUTPUT │

├──────────┼──────────────────────┼───────┼────────────────────────────┤

│ 0 │ 0.1 Infrastructure │ 6 │ Docker running │

│ │ 0.2 Database │ 8 │ Schema created │

│ │ 0.3 Auth API │ 8 │ JWT auth working │

│ │ 0.4 Frontend │ 9 │ Landing page OK │

│ │ │ ──────│ │

│ │ SUBTOTAL │ 31 │ │

├──────────┼──────────────────────┼───────┼────────────────────────────┤

│ 1 │ 1.1 Profile/Charts │ 5 │ API-based engines │

│ │ 1.2 L3 AI Pipeline │ 10 │ Claude interpretation │

│ │ 1.3 Auth UI │ 5 │ Login/Register pages │

│ │ 1.4 Onboarding │ 5 │ 5-step wizard │

│ │ 1.5 Dashboard/Read │ 9 │ Reading pages │

│ │ │ ──────│ │

│ │ SUBTOTAL │ 34 │ │

├──────────┼──────────────────────┼───────┼────────────────────────────┤

│ 2 │ 2.1 Payments │ 7 │ MoMo/ZaloPay working │

│ │ 2.2 Pricing/Checkout │ 6 │ Purchase flow │

│ │ │ ──────│ │

│ │ SUBTOTAL │ 13 │ │

├──────────┼──────────────────────┼───────┼────────────────────────────┤

│ 3 │ 3.1 Premium Backend │ 7 │ PDF + Compatibility │

│ │ 3.2 Advanced UI │ 6 │ Life Map + Charts │

│ │ 3.3 SEO/Performance │ 5 │ Lighthouse 90+ │

│ │ 3.4 Deployment │ 9 │ 360human.vn LIVE │

│ │ │ ──────│ │

│ │ SUBTOTAL │ 27 │ │

├──────────┼──────────────────────┼───────┼────────────────────────────┤

│ │ GRAND TOTAL │ 105 │ 🚀 Full launch │

└──────────┴──────────────────────┴───────┴────────────────────────────┘

*Blueprint này là bản đồ tổng thể. Chi tiết từng task xem tại action-plan-phases.md.* *Kiến trúc kỹ thuật chi tiết xem tại techstack-development-guide.md.*