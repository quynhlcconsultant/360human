# CEO-005: Kế Hoạch Tái Cấu Trúc Tổ Chức 360Human

> **Áp dụng:** DDWA (Data-Driven Workspace Architecture) + AGENT STAR™ Model
> **Ngày tạo:** 2026-03-20
> **Trạng thái:** DRAFT — Chờ CEO phê duyệt
> **Sprint:** S02 — Tái Cấu Trúc Tổ Chức

---

## 1. TÓM TẮT VẤN ĐỀ (GAP ANALYSIS)

### 1.1 Cấu Trúc Hiện Tại — Các Vi Phạm

| # | Vi phạm | Nguyên lý bị vi phạm | Mức độ |
|---|---------|----------------------|--------|
| 1 | Folder root đặt tên theo team thay vì **chức năng phổ quát** | DDWA Law #1: Universal Functions | 🔴 Critical |
| 2 | Không có **Handoff Suite** (9 file bắt buộc tại root) | DDWA Ch07: Handoff Suite | 🔴 Critical |
| 3 | Không phân tách **WIP vs SSOT** (không có SPRINT/) | DDWA Ch05: WIP/SSOT Separation | 🔴 Critical |
| 4 | Không có **Sprint_Log.md** | DDWA Ch05: Sprint Log mandatory | 🔴 Critical |
| 5 | Đánh số trùng (hai folder "2.") | DDWA Ch09: Naming Conventions | 🟡 Medium |
| 6 | Không có định nghĩa **Agent Anatomy** (JD.md) | AGENT STAR Ch13: 12 Elements | 🟡 Medium |
| 7 | Không có **Workflow Tiering** (Tier 0-3) | AGENT STAR Ch10: Workflow Tiering | 🟡 Medium |
| 8 | Không có **Quality Gates** | AGENT STAR Ch16: Measurement | 🟡 Medium |
| 9 | Folder `Module 1/` nằm ngang hàng production folders | DDWA Law #5: WIP vs SSOT | 🟢 Low |
| 10 | Folder `backend/` nằm lẫn với org folders | DDWA Law #1: Isomorphism | 🟢 Low |

### 1.2 Ánh Xạ Hiện Tại → Chức Năng Phổ Quát (DDWA Ch02)

| Cấu trúc cũ | Chức năng DDWA | Code |
|-------------|----------------|------|
| `0. CEO - Winston` | Strategy & Governance | GOV |
| `1. Product Strategy` | Production / R&D | PRD |
| `2. Design` | Production / R&D | PRD |
| `3. Architecture` | Production / R&D | PRD |
| `4. Frontend Team` | Production / R&D | PRD |
| `backend/` | Production / R&D | PRD |
| `2. Market Research` | Marketing & Growth | MKT |
| `5. Creative Team` | Marketing & Growth | MKT |
| `6. RTM Strategy` | Marketing & Growth + Sales | MKT+SAL |
| *(không tồn tại)* | Operations & Support | OPS |
| *(không tồn tại)* | Finance & Accounting | FIN |

**Kết luận:** Tier M startup (1-2 người + AI agents) → Gộp FIN vào GOV, SAL vào MKT, OPS tách riêng (theo DDWA Ch03: Merge/Split Rules).

---

## 2. THIẾT KẾ CẤU TRÚC MỚI

### 2.1 Folder Tree Mới (DDWA Tier M Baseline)

```
360Human/
│
│── INDEX.md                          # Handoff Suite #1: Bản đồ workspace
│── Guideline.md                      # Handoff Suite #2: Quy tắc, naming conventions
│── Onboarding.md                     # Handoff Suite #3: Hướng dẫn cho agent/người mới
│── Handoff.md                        # Handoff Suite #4: Trạng thái bàn giao real-time
│── Changelog.md                      # Handoff Suite #5: Lịch sử thay đổi cấu trúc
│── ToDo.md                           # Handoff Suite #6: Sprint + Backlog tracking
│── Notes/                            # Handoff Suite #7: Scratch pad, ideas
│── Archive/                          # Handoff Suite #8: Tài liệu cũ (never delete)
│── Temporary/                        # Handoff Suite #9: File tạm (can delete)
│
│── SPRINT/                           # ═══ WIP ZONE (Construction Site) ═══
│   │── Sprint_Log.md                 # ★ MANDATORY: Master sprint tracker
│   │── SP-260317-01-Foundation/      # Sprint 0: Docker, DB, Auth
│   │── SP-260324-02-CoreFlow/        # Sprint 1: Profile, L3 Pipeline, UI
│   │── SP-260407-03-Monetization/    # Sprint 2: VietQR, Tier unlock
│   └── SP-260421-04-Polish-Launch/   # Sprint 3: PDF, SEO, Deploy
│
│── 01_Governance/                    # ═══ GOV: Strategy & Finance ═══
│   │── INDEX.md
│   │── Strategy/                     # CEO vision, BMC, SWOT, OKR
│   │   │── Master_Strategy.yaml      # SSOT Layer 1 (structured data)
│   │   │── CEO-001_business-requirements.md
│   │   │── CEO-002_project-checklist.md
│   │   │── CEO-003_gantt-chart.md
│   │   └── CEO-004_master-project-tracker.md
│   │── Finance/                      # Pricing, P&L, Unit economics
│   │   └── Pricing_Model.yaml
│   └── Decisions/                    # Decision logs (Think-Out-Loud)
│       └── Decision_Log.md
│
│── 02_Production/                    # ═══ PRD: Product, Design, Tech ═══
│   │── INDEX.md
│   │── Product/                      # PRD, Feature specs
│   │   │── PRD-001_product-requirements.md
│   │   └── Feature_Backlog.md
│   │── Design/                       # UX/UI, Design System
│   │   │── FE-003_screen-specs.md
│   │   │── FE-004_design-system.md
│   │   └── Wireframes/
│   │── Architecture/                 # Technical blueprint
│   │   │── ARCH-001_project-blueprint.md
│   │   │── ARCH-002_api-integration.md
│   │   │── ARCH-003_ai-interpretation.md
│   │   └── ARCH-004_deployment.md
│   │── Backend/                      # Source code (symlink/reference)
│   │   └── → ../backend/            # Actual code lives separately
│   │── Frontend/                     # Component mapping, UI specs
│   │   │── FE-001_component-mapping.md
│   │   └── FE-002_ui-audit.md
│   └── Knowledge_Base/              # 6M+ words astrology KB
│       │── Human_Design/
│       │── Numerology/
│       │── Vedic/
│       │── BaZi/
│       └── TuVi/
│
│── 03_Marketing/                     # ═══ MKT + SAL: Growth & Conversion ═══
│   │── INDEX.md
│   │── Market_Research/              # Competitor analysis, personas
│   │   │── MR-001_market-insights.md
│   │   └── MR-002_competitor-map.md
│   │── Creative/                     # Brand, content, campaigns
│   │   └── Brand_Guidelines.md
│   │── RTM_Strategy/                 # Route-to-market, distribution
│   │   │── RTM-001_strategy.md
│   │   └── Domain_Registration.md
│   └── Sales/                        # Conversion optimization
│       └── Conversion_Funnel.md
│
│── 04_Operations/                    # ═══ OPS: Deploy, Monitor, Support ═══
│   │── INDEX.md
│   │── DevOps/                       # CI/CD, Docker, Infra
│   │   │── docker-compose.yaml
│   │   └── Deployment_Checklist.md
│   │── Monitoring/                   # Logs, Alerts, SLOs
│   │   └── SLO_Dashboard.md
│   └── Support/                      # User support, feedback
│       └── FAQ.md
│
│── .agents/                          # ═══ AGENT STAR: AI Workforce ═══
│   │── rules/                        # Global rules (constitution)
│   │   │── global-rules.md           # 5 Operating Principles
│   │   └── quality-gates.md          # QG-1, QG-2, QG-3
│   │── skills/                       # Shared skill libraries
│   │   │── vietnamese-professional-writing/
│   │   └── first-principles-thinking/
│   │── workflows/                    # Workflow definitions (Tier 0-3)
│   │   │── tier-0-meta/
│   │   │── tier-1-orchestration/
│   │   │── tier-2-execution/
│   │   └── tier-3-utility/
│   │── agents/                       # Agent definitions (JD.md per agent)
│   │   │── @CEO-Winston/             # Human (Architect + Governor)
│   │   │── @Director-Product/        # Tier 1: Product Director
│   │   │── @Director-Tech/           # Tier 1: Tech Director
│   │   │── @Director-Growth/         # Tier 1: Growth Director
│   │   │── @Specialist-Designer/     # Tier 2: UX/UI
│   │   │── @Specialist-Frontend/     # Tier 2: Frontend Dev
│   │   │── @Specialist-Backend/      # Tier 2: Backend Dev
│   │   │── @Specialist-AI-Pipeline/  # Tier 2: AI/LLM Engineer
│   │   │── @Specialist-Copywriter/   # Tier 2: Content & Copy
│   │   │── @Specialist-Researcher/   # Tier 2: Market Research
│   │   └── @Specialist-QA/           # Tier 2: Quality Assurance
│   └── knowledge/                    # Organizational memory (KIs)
│       └── KI_Index.md
│
│── backend/                          # ═══ SOURCE CODE (Git-managed) ═══
│   └── (FastAPI project - unchanged)
│
└── Module_1/                         # ═══ TRAINING ARCHIVE ═══
    │── AGENT_STAR_Book/
    │── DDWA_Book/
    └── (training materials)
```

### 2.2 Ánh Xạ Cấu Trúc Cũ → Mới

| Cấu trúc cũ | Di chuyển đến | Ghi chú |
|-------------|--------------|---------|
| `0. CEO - Winston/CEO-001_*.md` | `01_Governance/Strategy/` | SSOT zone |
| `0. CEO - Winston/CEO-002_*.md` | `01_Governance/Strategy/` | SSOT zone |
| `0. CEO - Winston/CEO-003_*.md` | `01_Governance/Strategy/` | SSOT zone |
| `0. CEO - Winston/CEO-004_*.md` | `01_Governance/Strategy/` | SSOT zone |
| `1. Product Strategy/*` | `02_Production/Product/` | SSOT zone |
| `2. Design/*` | `02_Production/Design/` | SSOT zone |
| `2. Market Research/*` | `03_Marketing/Market_Research/` | SSOT zone |
| `3. Architecture/*` | `02_Production/Architecture/` | SSOT zone |
| `4. Frontend Team/*` | `02_Production/Frontend/` + `02_Production/Design/` | Split theo nội dung |
| `5. Creative Team/*` | `03_Marketing/Creative/` | SSOT zone |
| `6. RTM Strategy/*` | `03_Marketing/RTM_Strategy/` | SSOT zone |
| `backend/` | `backend/` | Giữ nguyên (source code) |
| `Module 1/` | `Module_1/` (rename, move to Archive sau khi học xong) | Training materials |

---

## 3. AGENT STAR — CƠ CHẾ VẬN HÀNH

### 3.1 Cánh Sao 1: STRATEGY (Chiến Lược)

**6 Strategy Domains cho 360Human:**

| Domain | File SSOT | Nội dung |
|--------|----------|---------|
| Biz Strategy | `Master_Strategy.yaml` | Vision: "Giúp khai mở bản thân"; USP: 5 frameworks × 10 topics; BMC |
| Product Strategy | `PRD-001_product-requirements.md` | Freemium → PRO → MAX; 10 screens; Feature backlog |
| Market & Sales | `MR-001_market-insights.md` | Urban Vietnam → Asia → Global; Digital youth → Mass |
| Ops Strategy | `ARCH-001_project-blueprint.md` | FastAPI + Next.js + Claude AI; 4 Sprint delivery |
| Financial Model | `Pricing_Model.yaml` | FREE/PRO(199K)/MAX(499K); VietQR payment |
| MBO Tracking | `CEO-004_master-project-tracker.md` | North Star: Accuracy 99%; Launch 29/04/2026 |

### 3.2 Cánh Sao 2: ARCHITECTURE (Kiến Trúc Tổ Chức)

**Mô hình 3 Tầng (AGENT STAR Ch06):**

```
┌─────────────────────────────────────────────┐
│            TẦNG 0: CEO (Human)              │
│         Winston — Architect + Governor      │
│            Span: 3 Directors                │
└──────────────┬──────────────────────────────┘
               │
    ┌──────────┼──────────────┐
    ▼          ▼              ▼
┌────────┐ ┌────────┐  ┌──────────┐
│Director│ │Director│  │ Director │
│Product │ │ Tech   │  │ Growth   │
│Span: 3 │ │Span: 3 │  │ Span: 3  │
└───┬────┘ └───┬────┘  └────┬─────┘
    │          │             │
    ▼          ▼             ▼
┌────────────────────────────────────────────┐
│         TẦNG 2: SPECIALIST AGENTS          │
│                                            │
│ Product:  @Designer, @Copywriter           │
│ Tech:     @Frontend, @Backend, @AI-Pipeline│
│ Growth:   @Researcher, @QA                 │
└────────────────────────────────────────────┘
```

**Autonomy Scope (AGENT STAR Ch07):**

| Agent | Level | Quyền |
|-------|-------|-------|
| @CEO-Winston | L5 | Full authority, self-evolving |
| @Director-Product | L3 | Decide & Inform (within product scope) |
| @Director-Tech | L3 | Decide & Inform (within tech scope) |
| @Director-Growth | L3 | Decide & Inform (within marketing scope) |
| @Specialist-* | L2 | Suggest & Execute (wait approval for non-trivial) |

**Escalation Protocol:**
- **L1 → Director:** Routine issues (naming, formatting, minor bugs)
- **L2 → CEO:** Critical decisions (architecture change, feature scope, budget)
- **L3 → CEO IMMEDIATE:** Security breach, data loss, brand damage

### 3.3 Cánh Sao 3: ORCHESTRATION (Quy Trình)

**Workflow Tiering (AGENT STAR Ch10):**

| Tier | Tên | Ví dụ cho 360Human | Ai chạy | Tần suất |
|------|-----|---------------------|---------|----------|
| **0: META** | Tạo/sửa workflow | `/buildflow`, `/provision-agent`, `/restructure` | CEO | Hiếm |
| **1: ORCH** | Điều phối pipeline | `/build-feature` (PRD→Design→Code→Test→Deploy) | Director | Trung bình |
| **2: EXEC** | Thực thi task | `/code-backend`, `/design-screen`, `/write-copy` | Specialist | Cao |
| **3: UTIL** | Hỗ trợ | `/flog`, `/beat`, `/tomtat`, `/quality-check` | Any | Rất cao |

**Golden Rule:** Tier N chỉ gọi Tier N+1 hoặc Tier 3 (không gọi ngược).

**Cross-Calling Patterns cho 360Human:**

```
/build-feature (Tier 1 — @Director-Product)
  ├── /write-prd (Tier 2 — @Director-Product)
  ├── /design-screen (Tier 2 — @Specialist-Designer)
  ├── /code-frontend (Tier 2 — @Specialist-Frontend)
  ├── /code-backend (Tier 2 — @Specialist-Backend)
  ├── /build-ai-pipeline (Tier 2 — @Specialist-AI-Pipeline)
  ├── /quality-check (Tier 3 — @Specialist-QA)
  └── /flog (Tier 3 — Any)
```

### 3.4 Cánh Sao 4: CAPABILITIES (Năng Lực)

**5 Thành Phần Cốt Lõi (AGENT STAR Ch12):**

| Thành phần | Vị trí | Mô tả |
|-----------|--------|-------|
| **Agent** | `.agents/agents/@Name/JD.md` | Định danh, scope, interface (12 elements) |
| **Workflow** | `.agents/workflows/tier-N/` | SOP cho từng quy trình |
| **Skill** | `.agents/skills/` | Knowledge base immutable (textbook) |
| **Rules** | `.agents/rules/` | Hiến pháp — mọi agent phải đọc |
| **Knowledge** | `.agents/knowledge/` | Bộ nhớ tổ chức (KIs learned over time) |

**T-Shaped Agent Model (AGENT STAR Ch05):**

```
Mỗi Agent = Core (Horizontal) + Functional (Vertical) + Domain (Arrow)

Core (mọi agent):     Vietnamese, Sprint-centric, Think-Out-Loud, SSOT
Functional:           Theo vai trò (design, code, research, copy...)
Domain:               Theo lĩnh vực (astrology, 360Human product, VietQR...)
```

### 3.5 Cánh Sao 5: MEASUREMENT & ALIGNMENT (Đo Lường)

**Quality Gates (AGENT STAR Ch16):**

| Gate | Tên | Ai thực hiện | Khi nào |
|------|-----|-------------|---------|
| QG-1 | Self-check | Agent tự đánh giá vs DoD | Sau mỗi task |
| QG-2 | Peer review | QA agent kiểm tra chéo | Sau mỗi feature |
| QG-3 | CEO approval | Winston review | Trước merge vào SSOT |

**Configuration Feedback Loop:**
- Excellent → Mở rộng scope (L2 → L3)
- Good → Duy trì, thêm BU
- Average → Audit skill, tối ưu prompt
- Poor → Giảm autonomy, re-skill
- Failure → Decommission + provision mới

**Alignment Check Matrix (9 cặp):**

| Cặp | Câu hỏi kiểm tra | Trạng thái |
|-----|-------------------|-----------|
| Strategy ↔ Architecture | Agent roles có match với product scope? | ⬜ Check |
| Strategy ↔ Orchestration | Feature ưu tiên có workflow tốt hơn? | ⬜ Check |
| Architecture ↔ Orchestration | Mọi agent đều nằm trong workflow? | ⬜ Check |
| Architecture ↔ Capabilities | Mọi agent có đủ skill? | ⬜ Check |
| Architecture ↔ Measurement | Mọi tier có metrics? | ⬜ Check |
| Orchestration ↔ Capabilities | Cross-calling match interface contracts? | ⬜ Check |
| Orchestration ↔ Measurement | Mọi process có quality gate? | ⬜ Check |
| Capabilities ↔ Measurement | Feedback loop → skill updates? | ⬜ Check |
| Measurement ↔ Strategy | Metrics phục vụ strategy (Accuracy 99%)? | ⬜ Check |

---

## 4. CƠ CHẾ VẬN HÀNH HÀNG NGÀY

### 4.1 Năm Nguyên Tắc Vận Hành (AGENT STAR Ch17)

| # | Nguyên tắc | Cách áp dụng cho 360Human |
|---|-----------|--------------------------|
| 1 | **Think-Out-Loud (TOL)** | Mọi agent ghi log reasoning vào `Decisions/Decision_Log.md` |
| 2 | **Sprint-Centric** | Mọi task thuộc 1 sprint. Format: `SP-YYMMDD-##-Name` |
| 3 | **Changelog** | Mọi thay đổi ghi vào `Changelog.md` (root + per folder) |
| 4 | **SSOT** | Mỗi thông tin chỉ ở 1 nơi. Reference bằng backlink |
| 5 | **Indexing** | Mọi file mới phải có trong INDEX.md tương ứng |

### 4.2 Bốn Vai Trò Con Người (AGENT STAR Ch18)

Winston đảm nhiệm cả 4 vai trò (1-person team):

| Vai trò | % Thời gian | Trách nhiệm chính |
|---------|------------|-------------------|
| **Architect** | 30% | Thiết kế org structure, provision/decommission agents |
| **Trainer** | 25% | Viết SKILL.md, configure agent definition |
| **Governor** | 20% | QG-3 approval, strategic decisions, escalation |
| **Documentarian** | 15% | Maintain KIs, update INDEX, enforce SSOT |
| *Executor* | 10% | Code trực tiếp khi cần |

### 4.3 Chu Kỳ Vận Hành

**Hàng ngày:**
1. Update `Handoff.md` (status, blockers, next actions)
2. Agent ghi TOL vào Decision_Log
3. Sprint tasks tracked trong `ToDo.md`

**Cuối Sprint:**
1. QG-3: CEO review deliverables
2. Merge WIP → SSOT (cherry-pick từ SPRINT/ vào department folders)
3. Lock sprint folder (move to Archive/)
4. Update Sprint_Log.md
5. `/beat` — Extract Knowledge Items

**Hàng tháng:**
1. Audit Handoff Suite (9 items complete?)
2. Scan God Folders, Orphan Files, Dead Handoffs
3. Tri-Framework Stress Test (SIPOC → Ishikawa → 5-WHERE)
4. Agent performance review → Configuration Feedback

---

## 5. SIPOC CHO 360Human (DDWA Stress Test)

```
┌──────────┐    ┌──────────┐    ┌──────────────┐    ┌────────────┐    ┌──────────┐
│ SUPPLIER │    │  INPUT   │    │   PROCESS    │    │   OUTPUT   │    │ CUSTOMER │
├──────────┤    ├──────────┤    ├──────────────┤    ├────────────┤    ├──────────┤
│CEO       │───▶│Strategy  │───▶│01_Governance │───▶│BMC, OKR    │───▶│All Agents│
│          │    │Vision    │    │Strategy Def  │    │Pricing     │    │          │
├──────────┤    ├──────────┤    ├──────────────┤    ├────────────┤    ├──────────┤
│CEO +     │───▶│PRD, KB   │───▶│02_Production │───▶│Working App │───▶│End Users │
│Astro API │    │API Keys  │    │Build Feature │    │AI Readings │    │(360human │
│          │    │6M words  │    │Pipeline      │    │Dashboard   │    │ .vn)     │
├──────────┤    ├──────────┤    ├──────────────┤    ├────────────┤    ├──────────┤
│Market    │───▶│Research  │───▶│03_Marketing  │───▶│Content     │───▶│Prospects │
│Data      │    │Personas  │    │Growth Engine │    │Campaigns   │    │Customers │
├──────────┤    ├──────────┤    ├──────────────┤    ├────────────┤    ├──────────┤
│Tech Team │───▶│Code      │───▶│04_Operations │───▶│Live System │───▶│End Users │
│          │    │Infra     │    │Deploy+Monitor│    │Uptime SLOs │    │          │
└──────────┘    └──────────┘    └──────────────┘    └────────────┘    └──────────┘
```

---

## 6. KẾ HOẠCH TRIỂN KHAI

### Phase 1: Tạo Cấu Trúc Mới (Ngay lập tức)
1. Tạo 9 file Handoff Suite tại root
2. Tạo SPRINT/ với Sprint_Log.md
3. Tạo 01_Governance/, 02_Production/, 03_Marketing/, 04_Operations/
4. Di chuyển file từ cấu trúc cũ sang mới (theo bảng ánh xạ 2.2)
5. Archive cấu trúc cũ

### Phase 2: Provision Agents (Tuần 1)
1. Tạo `.agents/` structure
2. Viết JD.md cho 3 Director agents
3. Viết JD.md cho 7 Specialist agents
4. Viết global-rules.md (5 Operating Principles)
5. Viết quality-gates.md

### Phase 3: Workflow Tiering (Tuần 2)
1. Định nghĩa Tier 0 workflows (meta)
2. Định nghĩa Tier 1 workflows (orchestration)
3. Định nghĩa Tier 2 workflows (execution)
4. Định nghĩa Tier 3 workflows (utility)
5. Viết Interface Contracts cho cross-calling

---

## 7. QUYẾT ĐỊNH CẦN CEO PHÊ DUYỆT

| # | Quyết định | Options | Recommendation |
|---|-----------|---------|----------------|
| 1 | Có di chuyển file vật lý hay chỉ tạo cấu trúc mới? | A: Move files, B: Copy + Archive old | **B**: An toàn hơn, rollback dễ |
| 2 | Bắt đầu với bao nhiêu agents? | A: 3 (Directors only), B: 10 (Full) | **A**: Bắt đầu nhỏ, mở rộng dần |
| 3 | Module_1/ giữ hay archive? | A: Giữ nguyên, B: Move to Archive/ | **A**: Vẫn cần reference |
| 4 | backend/ code giữ nguyên vị trí? | A: Giữ, B: Move vào 02_Production/ | **A**: Git history intact |
| 5 | Triển khai ngay Phase 1 hay chờ review? | A: Ngay, B: Review trước | **Tuỳ CEO** |

---

*Tài liệu này được tạo dựa trên nguyên lý từ:*
- *DDWA Book (Data-Driven Workspace Architecture) — 18 chapters*
- *AGENT STAR™ Book — 23 chapters*
- *Áp dụng cho 360Human — Tier M Startup*
