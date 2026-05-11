---
title: "Design Sprint — Wireframe & Prototype"
id: "CRE-001"
updated: "2026-03-15"
status: "active"
---

# Design Sprint — 360Human UI/UX

> Parallel track, không block dev sprints.
> Tool: **Figma** (Free plan đủ dùng cho 1 người)
> Style: Co-Star vibe — sạch, typography rõ, whitespace cao, KHÔNG cải lương phương Đông

---

## Sprint D1 — Wireframes (3 days)

Mục tiêu: Low-fidelity wireframes cho 8 screens cốt lõi

| # | Screen | Wireframe Content | Priority | Done |
|---|--------|-------------------|----------|------|
| D1.1 | [ ] Landing Page | Hero + value props + 5 frameworks icons + CTA "Bắt đầu" | P0 | |
| D1.2 | [ ] Register / Login | Simple form, email+password, social proof | P0 | |
| D1.3 | [ ] Onboarding Wizard | 5-step: date → time → city → gender → name, progress bar | P0 | |
| D1.4 | [ ] Dashboard / Home | 10 topic cards grid, tier badge, profile summary | P0 | |
| D1.5 | [ ] System Reading | Tab view (5 frameworks), reading content area, chart placeholder | P0 | |
| D1.6 | [ ] Topic Reading | Multi-framework synthesis, What→How→What's Next structure | P0 | |
| D1.7 | [ ] Pricing Page | 3-tier comparison table (FREE/PRO/MAX), CTA buttons | P0 | |
| D1.8 | [ ] Profile + Settings | Tier info, account details, change password, delete account | P1 | |

## Sprint D2 — Design System (2 days)

Mục tiêu: Foundation cho consistent UI

| # | Task | Detail | Done |
|---|------|--------|------|
| D2.1 | [ ] Color palette | Warm, calming tones — reference Co-Star (cream, soft black, muted gold) |  |
| D2.2 | [ ] Typography scale | 1 serif heading font + 1 sans body font, Vietnamese support | |
| D2.3 | [ ] Spacing & grid | 8px base grid, responsive breakpoints (mobile-first) | |
| D2.4 | [ ] Component library | Button, Card, Input, Tab, Badge, Modal, Skeleton — map to shadcn/ui | |
| D2.5 | [ ] Icon set | 5 framework icons (Tử Vi, HD, Numerology, BaZi, Vedic) + 10 topic icons | |

## Sprint D3 — Hi-Fi Mockups (3 days)

Mục tiêu: Pixel-ready designs cho dev handoff

| # | Screen | Focus | Done |
|---|--------|-------|------|
| D3.1 | [ ] Landing Page (desktop + mobile) | Trust-building, conversion-optimized | |
| D3.2 | [ ] Onboarding flow (mobile-first) | Step-by-step, smooth transitions | |
| D3.3 | [ ] Dashboard + Reading pages | Data-dense but clean, tier-gate blur effect | |
| D3.4 | [ ] Pricing page | Clear tier comparison, VietQR checkout preview | |
| D3.5 | [ ] Chart visualizations | Radar chart, palace grid (Tử Vi), body graph (HD) concept | |

## Sprint D4 — Prototype & Handoff (2 days)

| # | Task | Done |
|---|------|------|
| D4.1 | [ ] Link screens into clickable prototype (Figma) | |
| D4.2 | [ ] Export design tokens (colors, fonts → CSS variables) | |
| D4.3 | [ ] Component specs → map to shadcn/ui components | |
| D4.4 | [ ] Share Figma link with dev | |

---

## Design Principles (from CEO)

1. **"Personal identity card"** — Chart screen beautiful enough to screenshot & share
2. **"Wise elder" tone** — Reading feels like guidance, not fortune-telling
3. **Growth-oriented** — Even negative readings end with actionable hope
4. **Warm, calming colors** — NOT anxiety-inducing dark themes
5. **Clean, minimal** — High whitespace, clear typography, no visual clutter
6. **NO cải lương** — Professional, modern, not mystical/superstitious aesthetic

## Quick Start: Figma Setup

1. Go to figma.com → Sign up (Free plan)
2. Create project: "360Human"
3. Create pages: `Wireframes` | `Design System` | `Hi-Fi` | `Prototype`
4. Use Figma Community template for speed:
   - Search "shadcn/ui Figma" → clone component library
   - Search "Mobile wireframe kit" → clone for quick wireframing

## Suggested Timeline

```
Can run parallel with dev sprints:
├─ D1 Wireframes:     During Sprint 0 (W1)
├─ D2 Design System:  During Sprint 0-1 (W1-2)
├─ D3 Hi-Fi Mockups:  During Sprint 1 (W2-3)
└─ D4 Handoff:        Before Sprint 2 starts (W3)
```
