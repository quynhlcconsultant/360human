# 360Human - Sub-Agents Registry

> 82 skills organized into 13 sub-agents for the 360Human startup project.
> Each sub-agent folder contains specialized skills for a specific domain.
>
> **Update 2026-03-20:** Thêm AGENT STAR Workforce layer — xem section bên dưới.

## AGENT STAR Workforce (Tier Structure)

> Đây là tổ chức agent theo DDWA + AGENT STAR framework.
> Mỗi agent có JD.md đầy đủ tại `.agents/agents/@[Handle]/JD.md`

### Tier 0 (META) — CEO

| Handle       | Role                   | Autonomy |
| ------------ | ---------------------- | -------- |
| @CEO-Winston | CEO & Founder (Human)  | L5       |

### Tier 1 (ORCHESTRATION) — Directors

| Handle            | Role                     | Autonomy | Owns Workflow    |
| ----------------- | ------------------------ | -------- | ---------------- |
| @Director-Tech    | Engineering & Operations | L3       | /build-sprint    |
| @Director-Product | Product & Design         | L3       | /build-feature   |
| @Director-Growth  | Marketing, Growth & QA   | L3       | /launch-campaign |

### Tier 2 (EXECUTION) — Specialists

| Handle                  | Role                       | Autonomy | Owns Workflow       | Sprint |
| ----------------------- | -------------------------- | -------- | ------------------- | ------ |
| @Specialist-Backend     | Python/FastAPI Backend     | L2       | /code-backend       | S03+   |
| @Specialist-Frontend    | Next.js Frontend           | L2       | /code-frontend      | S03+   |
| @Specialist-AI-Pipeline | Claude AI + RAG            | L2       | /build-ai-pipeline  | S03+   |
| @Specialist-QA          | Quality Assurance          | L2       | /audit-quality      | S03+   |
| @Specialist-Designer    | UX/UI Screen Design        | L2       | /design-screen      | S04+   |
| @Specialist-Astrology   | 5 Frameworks Domain Expert | L3\*     | /validate-accuracy  | S04+   |

> \*@Specialist-Astrology có L3 (Decide & Inform) về accuracy — final say về reading correctness

### Advisory Layer (05_Consulting)

| Handle                   | Role                  |
| ------------------------ | --------------------- |
| @Consultant-Strategy     | Business Strategy     |
| @Consultant-Architecture | System Architecture   |
| @Consultant-ProductDev   | Product Development   |

### Org Chart

```
@CEO-Winston (L5)
├── @Director-Tech (L3)
│   ├── @Specialist-Backend (L2)
│   ├── @Specialist-Frontend (L2)
│   └── @Specialist-AI-Pipeline (L2)
├── @Director-Product (L3)
│   ├── @Specialist-Designer (L2)
│   └── @Specialist-Astrology (L3*)
└── @Director-Growth (L3)
    └── @Specialist-QA (L2)
         ↕ cross-call ↕
    @Specialist-Astrology (accuracy validation)
```

### Deferred (S05+)

- @Specialist-Copywriter → @Director-Growth absorb tạm thời
- @Specialist-Researcher → @Director-Growth absorb tạm thời

---

## Quick Reference: Which Agent for Which Phase?

| Phase | Timeline | Sub-Agents to Use |
|-------|----------|-------------------|
| **Phase 0: Foundation** | Week 1 | `01`, `04`, `10`, `12` |
| **Phase 1: Core Flow** | Week 2-3 | `01`, `02`, `06`, `07` |
| **Phase 2: Monetization** | Week 4-5 | `03`, `02`, `01` |
| **Phase 3: Polish & Launch** | Week 6-8 | `05`, `08`, `11`, `13` |

---

## Sub-Agent Index

### 01-backend-api (13 skills)
FastAPI + Python backend, API design, auth, database, async patterns.
```
fastapi-pro, python-pro, api-design-principles, database, postgresql,
alembic, auth-implementation-patterns, api-security-best-practices,
async-python-patterns, error-handling-patterns, fastapi-templates,
api-patterns, backend-architect
```
**Use when:** Building API endpoints, database schema, auth system, business logic layer.

### 02-frontend-ui (13 skills)
Next.js 15 + shadcn/ui + Tailwind CSS frontend development.
```
nextjs-best-practices, nextjs-shadcn, react-patterns, tailwind-patterns,
zustand-store-ts, typescript-pro, react-ui-patterns, frontend-design,
scroll-experience, form-cro, frontend-developer, react-nextjs-development,
react-state-management
```
**Use when:** Building UI components, pages, state management, onboarding wizard, dashboard.

### 03-payment-monetization (5 skills)
Payment gateway integration, billing, pricing, paywall optimization.
```
payment-integration, stripe-integration, billing-automation,
pricing-strategy, paywall-upgrade-cro
```
**Use when:** Integrating MoMo/ZaloPay, building tier system, pricing page, subscription logic.

### 04-deployment-devops (6 skills)
Docker, Vercel, CI/CD, Neon PostgreSQL, cost optimization.
```
docker-expert, vercel-deployment, github-actions-templates,
using-neon, cost-optimization, docker-best-practices
```
**Use when:** Setting up Docker, deploying to Vercel/Railway, CI/CD pipeline, infrastructure.

### 05-testing-quality (6 skills)
E2E testing, unit testing, TDD, API testing, Playwright.
```
e2e-testing, python-testing-patterns, test-driven-development,
api-testing-patterns, e2e-testing-patterns, playwright-skill
```
**Use when:** Writing tests, setting up test infrastructure, QA automation.

### 06-ai-data (7 skills)
Claude API, prompt engineering, RAG pipeline, LLM patterns.
```
prompt-engineering, rag-implementation, llm-app-patterns,
llm-evaluation, context-window-management, prompt-engineering-patterns,
rag-engineer
```
**Use when:** Building L3 AI pipeline, RAG knowledge base, prompt templates, token management.
**Note:** Also use built-in `/claude-api` skill for Claude API integration.

### 07-astrology-domain (3 skills)
Vedic, Numerology, Chinese astrology (Tu Vi, BaZi) domain knowledge.
```
project-astrology-vedic, project-astrology-numerology,
project-astrology-chinese
```
**Use when:** Implementing astrology calculations, validating framework accuracy, domain logic.

### 08-seo-marketing (8 skills)
SEO, content strategy, launch planning, conversion optimization.
```
seo-fundamentals, seo-content-writer, launch-strategy,
app-store-optimization, signup-flow-cro, seo-content-planner,
seo-meta-optimizer, geo-fundamentals
```
**Use when:** SEO setup for 360human.vn, content marketing, launch planning, signup optimization.

### 09-business-strategy (9 skills)
Startup validation, financial modeling, competitive analysis, metrics.
```
startup-idea-validation, startup-financial-modeling,
competitive-intelligence, market-sizing-analysis, buyer-personas,
product-manager-toolkit, startup-metrics-framework, startup-validator,
competitive-analyst
```
**Use when:** Business planning, investor decks, market analysis, KPI definition, user personas.

### 10-architecture-planning (7 skills)
System architecture, microservices, ADRs, implementation planning.
```
architecture, microservices-patterns, plan-writing,
architecture-decision-records, architecture-patterns,
senior-architect, software-architecture
```
**Use when:** Designing system architecture, making tech decisions, writing implementation plans.

### 11-monitoring-observability (5 skills)
Sentry, Grafana, Prometheus, monitoring setup.
```
observability-engineer, sentry-automation, grafana-dashboards,
prometheus-configuration, observability-monitoring-monitor-setup
```
**Use when:** Setting up error tracking, performance monitoring, alerts, dashboards.

### 12-security (5 skills)
Security audit, GDPR, secrets management, API security testing.
```
security-audit, gdpr-data-handling, secrets-management,
security-auditor, api-security-testing
```
**Use when:** Security review, handling birth data privacy, API key management, compliance.

### 13-pdf-export (1 skill)
PDF report generation with ReportLab.
```
pdf-official
```
**Use when:** Building the 36-page comprehensive reading report export feature.

---

## How to Use

### Invoke a skill directly:
```
/fastapi-pro          → Backend API development
/nextjs-shadcn        → Frontend with shadcn/ui
/prompt-engineering   → AI prompt design
/project-astrology-vedic → Vedic astrology domain
```

### Invoke by sub-agent context:
Tell Claude which sub-agent domain you're working in, e.g.:
- "Using 01-backend-api skills, create the auth endpoints"
- "Using 06-ai-data skills, build the RAG pipeline for Tu Vi"
- "Using 03-payment skills, integrate MoMo payment"

### Phase-based workflow:
1. Start with Phase 0 agents: `01` + `04` + `10` + `12`
2. Move to Phase 1: `01` + `02` + `06` + `07`
3. Phase 2: `03` + `02` + `01`
4. Phase 3: `05` + `08` + `11` + `13`

---

## Stats
- **Total skills:** 82
- **Sub-agents:** 13
- **Phases covered:** 4 (Foundation → Core → Monetization → Launch)
- **Generated:** 2026-03-15
