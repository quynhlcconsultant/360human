# INDEX — 05_Consulting (Advisory Layer)

> **Chức năng:** Tư vấn trực tiếp cho CEO trước khi triển khai xuống execution teams
> **Vị trí tổ chức:** Nằm giữa CEO và Directors (01-04)
> **Owner:** @CEO-Winston (direct collaboration)
> **Last updated:** 2026-03-20

---

## Mô Hình Vận Hành

```
                    ┌─────────────┐
                    │ CEO Winston │
                    └──────┬──────┘
                           │ Advisory (trước mỗi quyết định lớn)
              ┌────────────┼────────────┐
              ▼            ▼            ▼
     ┌──────────────┐ ┌──────────┐ ┌──────────────┐
     │  Strategy    │ │  Arch    │ │ Product/Dev  │
     │  Consulting  │ │Consulting│ │ Consulting   │
     │  (MBB+Start) │ │(DDWA+AS) │ │ (Solution)   │
     └──────────────┘ └──────────┘ └──────────────┘
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
         @Director-   @Director-   @Director-
          Product       Tech        Growth
              │            │            │
              ▼            ▼            ▼
         Specialists  Specialists  Specialists
```

**Flow:** CEO có câu hỏi chiến lược → Consulting phân tích + recommend → CEO quyết định → Directors triển khai

---

## Teams

### 01_Strategy_Consulting — MBB + Startup Consulting
| Item | Chi tiết |
|------|---------|
| **Agent:** | @Consultant-Strategy |
| **Focus:** | Chiến lược kinh doanh, competitive intel, market sizing, financial modeling, pricing |
| **Skills:** | 11 skills imported (competitive-analyst, market-sizing, financial-modeling, startup-validator, pricing-strategy, launch-strategy...) |
| **When to call:** | Trước quyết định về market positioning, pricing, go-to-market, pivot, fundraising |

### 02_Architecture_Consulting — Org + System Architecture
| Item | Chi tiết |
|------|---------|
| **Agent:** | @Consultant-Architecture |
| **Focus:** | DDWA compliance, AGENT STAR alignment, software architecture, tech decisions |
| **Skills:** | 12 skills imported + Module 1 knowledge (DDWA Book + AGENT STAR Book) |
| **When to call:** | Trước quyết định về org restructure, tech stack, database design, deployment strategy, agent provisioning |
| **Knowledge:** | `Module 1/` — DDWA (18 chương) + AGENT STAR (23 chương) + Orchestration |

### 03_Product_Dev_Consulting — Product/Dev/Solution/Critical
| Item | Chi tiết |
|------|---------|
| **Agent:** | @Consultant-ProductDev |
| **Focus:** | Product review, code quality, security audit, LLM evaluation, red team, cost optimization |
| **Skills:** | 15 skills imported (fastapi, react, TDD, security-audit, llm-evaluation, prompt-engineering, cost-optimization...) |
| **When to call:** | Trước sprint mới (pre-sprint review), sau feature build (code audit), trước launch (security + LLM eval) |

---

## Skill Inventory

| Team | Skills Count | Key Skills |
|------|-------------|-----------|
| Strategy | 11 | competitive-analyst, market-sizing, financial-modeling, startup-validator, buyer-personas, pricing-strategy, launch-strategy |
| Architecture | 12 + Module 1 | architecture, ADR, architecture-patterns, senior-architect, software-architecture, backend-architect, database, docker-expert |
| Product/Dev | 15 | fastapi-pro, python-pro, react-patterns, TDD, e2e-testing, security-audit, llm-evaluation, prompt-engineering, cost-optimization |
| **Total** | **38 + Module 1** | |

---

## Cách Sử Dụng

1. **CEO có câu hỏi chiến lược** → Tag @Consultant-Strategy
2. **CEO cần quyết định kiến trúc** → Tag @Consultant-Architecture
3. **CEO cần review solution/code** → Tag @Consultant-ProductDev
4. **Quyết định phức tạp** → Gọi cả 3 consultants cùng lúc (multi-perspective)

**Output format:** Mọi recommendation phải có:
- Reasoning chain (TOL)
- Options matrix (≥2 alternatives)
- Recommendation + confidence score
- Risks + mitigations
