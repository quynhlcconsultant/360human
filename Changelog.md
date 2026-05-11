# Changelog — 360Human Workspace

> **Format:** `[YYYY-MM-DD] [TYPE] Description`
> **Types:** `[STRUCTURE]` `[FILE]` `[AGENT]` `[WORKFLOW]` `[DECISION]`

---

## 2026-03-20 (Session 2)

- `[WORKFLOW]` Tạo 12 workflows đầy đủ cho 4 tiers: /sprint-planning, /sprint-review, /buildflow (T0) | /build-sprint, /build-feature, /launch-campaign (T1) | /code-backend, /code-frontend, /deploy, /write-prd, /design-screen, /audit-quality (T2) | /flog, /beat, /qg-check (T3)
- `[AGENT]` Tạo JD.md cho 6 Specialist agents: @Specialist-Backend, @Specialist-Frontend, @Specialist-AI-Pipeline, @Specialist-QA, @Specialist-Designer, @Specialist-Astrology
- `[DECISION]` Thêm @Specialist-Astrology (không có trong kế hoạch gốc) — critical cho accuracy KPI 60% weight
- `[DECISION]` Defer @Specialist-Copywriter và @Specialist-Researcher sang S05+ — Director-Growth absorb trong giai đoạn đầu
- `[FILE]` Tạo Master_Strategy.yaml — Layer 1 SSOT chiến lược tại 01_Governance/Strategy/
- `[FILE]` Cập nhật Handoff.md — S02 Done, S03 Pending, decisions chốt
- `[FILE]` Cập nhật ToDo.md — S02 hoàn thành 20 tasks, S03 ready

## 2026-03-20 (Session 1)

- `[STRUCTURE]` Tạo cấu trúc DDWA mới: 01_Governance/, 02_Production/, 03_Marketing/, 04_Operations/
- `[STRUCTURE]` Tạo SPRINT/ zone với Sprint_Log.md
- `[STRUCTURE]` Tạo Handoff Suite (9 items tại root): INDEX, Guideline, Onboarding, Handoff, Changelog, ToDo, Notes/, Archive/, Temporary/
- `[STRUCTURE]` Tạo .agents/ structure: rules/, skills/, workflows/, agents/, knowledge/
- `[FILE]` Copy CEO-001→005 từ `0. CEO - Winston/` sang `01_Governance/Strategy/`
- `[FILE]` Copy PRD-001 từ `1. Product Strategy/` sang `02_Production/Product/`
- `[FILE]` Copy ARCH-001→005 từ `3. Architecture/` sang `02_Production/Architecture/`
- `[FILE]` Copy FE-001→007 từ `4. Frontend Team/` sang `02_Production/Design/` + `02_Production/Frontend/`
- `[FILE]` Copy MKT-001 từ `2. Market Research/` sang `03_Marketing/Market_Research/`
- `[FILE]` Copy CRE-001 từ `5. Creative Team/` sang `03_Marketing/Creative/`
- `[FILE]` Copy RTM-001 từ `6. RTM Strategy/` sang `03_Marketing/RTM_Strategy/`
- `[DECISION]` Giữ nguyên toàn bộ folder cũ (0-6, backend, Module 1) — không xóa
- `[DECISION]` Folder cũ đánh dấu Legacy trong INDEX.md
- `[STRUCTURE]` Gom toàn bộ folder cũ (0-6) vào `_Legacy/` — không xóa file nào
- `[STRUCTURE]` Tạo `05_Consulting/` — Advisory Layer với 3 teams (Strategy, Architecture, Product/Dev)
- `[FILE]` Move `Module 1/` vào `05_Consulting/02_Architecture_Consulting/`
- `[AGENT]` Tạo JD.md cho @Consultant-Strategy, @Consultant-Architecture, @Consultant-ProductDev
- `[FILE]` Import 38 skills vào 3 consulting teams (11 + 12 + 15)
- `[AGENT]` Tạo JD.md cho @Director-Product, @Director-Tech, @Director-Growth
- `[AGENT]` Tạo global-rules.md và quality-gates.md
- `[FILE]` Upgrade prototype index.html — fix CSS bug (--sage-bg/--ember-bg/--error-bg đều là #141414 = black-on-black), thêm Checkout Flow modal (VietQR + Card + Success/Failure), cải thiện responsive
- `[FILE]` Upgrade prototype index-pro.html — fix CSS bug, cải thiện responsive, thêm @keyframes copulse
