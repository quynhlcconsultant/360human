---
title: "Product Requirements"
id: "PRD-001"
source: "PRD.docx"
converted: "2026-03-15 13:35"
updated: "2026-03-15"
status: "active"
---

> **UPDATED 2026-03-15** — Xem [ARCH-004 Clarifications](../3.%20Architecture/ARCH-004_clarifications-log.md)

***1. Product Description:*** web-based personal intelligence platform that synthesizes five ancient and modern wisdom frameworks — Human Design (HD), Tử Vi, Numerology, Bazi, and Vedic Astrology to let people know all about themself. Better than human reader

***2. Product Strategic Approach:* Focus on 9 angles x 4 analytical lenses = 360 degree**

- *10 chủ đề phân tích chuyên sâu:*
  Overview - Mission - Identity - Love - Finance - Health - Family - Career - Growth - Social
- *4 lăng kính phân tích (diễn giải theo chủ đề tập trung vào What - How - What’s next). Diễn giải theo hệ thống*
  What - Why - How - What’s next?

***3. Product Scope:***

- Phân tích 360 độ (5 frameworks x 10 topics)
- Phân tích chuyên sâu theo hệ thống
- Time Oracle Analysis
- PDF Export (36 pages) — MAX tier only
- Not in scope: Tarot readings, Partner Compatibility (next phase)
- Trackers for reading progress
- Word limits: **FREE=2,000w (2 topics) / PRO=10,000w (10 topics) / MAX=20,000w (10 topics + PDF)**
- Payment: **VietQR (one-time purchase)** — PRO=199K VND, MAX=499K VND
- API Provider: **astrology-api.io** (All 5 systems confirmed: Tử Vi, HD, BaZi, Vedic, Numerology)

***4. Mockup (screen-by-screen):***

- Screen 1: Landing Page *- Build Trust*
- Screen 2: Onboarding *- Collect Information (Concept Display)*
- Screen 3: Lifemap 360 *- Aha Moments - Accuracy - Consistent (What - How - What’s next)*
- Screen 4: Chart Interpretation (5 charts) *- Anchor (Why)*
- Screen 5: Deep-dive & Specific problems
- Screen 6: TimeOracle *- Retention users for upsell*
- Screen 7: Payment
- Screen 8: Profile

***5. Backend Risk- Must Solve***

- *Accuracy in 3 layers (Check with users survey)****+ Compute*** (Lịch âm dương conversion, chính xác theo từng hệ thống)
  → If it wrong, collapse everythings →**Solutions: Test case**

***+ AI Hallucination***
→ If it wrong, users CSAT low - can not scale-up → Solution: RAG, Semantic, Cross-check frameworks, Framework Rules & Structured Prompt Template, Output schema validation: reject outputs containing undefined terms or hallucination markers
***+ AI synthesis***

*→ Final gate: Prompt Engineering*

***6. Timeline:*** Launch: **29/04/2026** | Team: **1 fullstack dev**

- W1 (17-23 Mar): Foundation — Docker, DB, Auth, Frontend scaffold
- W2-3 (24 Mar - 6 Apr): Core Flow — Onboarding, Dashboard, L3 AI Pipeline
- W4-5 (7-20 Apr): Monetization — VietQR, Pricing, Tier enforcement
- W6-7 (21-29 Apr): Polish & Launch — PDF, SEO, Deploy, Go-live 29/04

***6. Risks:***

- *Birthtime:* HD and Vedic require exact birth time; many users don't know theirs.
  → Solutions: Claim for users to get information
- *Overlap or conflicts:*

***7. Other Requirements:***

- Customize charts: **Recharts** (test API chart rendering trước, fallback Recharts)
- *Interpretation Tone:* Warm, intelligent, slightly poetic. Uses "bạn" naturally, growth-driven action

***8. Tuyệt đối không:***

- Anti-doom guardrail: never predict death, serious illness, divorce as certain
- Toxic positivity ("everything is perfect!"), fatalism ("you will fail")