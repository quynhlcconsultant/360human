---
title: "Design System — Colors, Typography, Spacing, Texture"
id: "FE-004"
updated: "2026-03-16"
status: "ready-for-review"
stack: "Tailwind v4 / CSS Custom Properties / shadcn/ui"
source: "Figma research board — Competitors + My Reference + Typography notes"
---

# Design System — 360Human

> **Vision**: Premium, warm, textured. Like opening a personal journal that knows you —
> not a cold SaaS dashboard, not a fortune-telling app.
>
> **What we take from competitors**:
> - Co-Star: Information hierarchy, one action/screen, daily ritual UX — BUT NOT their coldness, B&W, emotional distance
> - Horos: Unique UI, fresh colors — BUT NOT their text overload
> - Linear: Typography hierarchy, motion restraint, dark mode warmth
> - Notion: Warm cream backgrounds, clean typography, restraint
>
> **Texture**: "Cảm giác giấy nhám" — rough, organic paper feel. NOT smooth parchment, NOT glossy.
> **Tone**: Wise elder, premium, personal — KHÔNG cải lương phương Đông.

---

## 1. Color Palette

### Philosophy

Warm cream base — like rough-textured paper, not digital white. Gold as primary accent — premium, not gaudy.
Background should feel physical, tangible ("nhám"). Cards float slightly above with subtle warmth.

NOT Co-Star's cold B&W. NOT Horos' neon-on-dark. NOT generic SaaS neutral gray.

### Palette Definitions

#### Base Colors

| Name | Hex | CSS var | Usage |
|------|-----|---------|-------|
| `cream` | `#F7F3ED` | `--color-cream` | Page background — slightly warmer than pure white |
| `warm-white` | `#FFFDF9` | `--color-warm-white` | Card surfaces, elevated elements |
| `sand` | `#EDE6DA` | `--color-sand` | Section backgrounds, subtle depth layers |
| `ink` | `#1C1917` | `--color-ink` | Primary text — warm black, not pure #000 |
| `charcoal` | `#44403C` | `--color-charcoal` | Secondary text, body text variant |
| `stone` | `#78716C` | `--color-stone` | Muted text, metadata, footnotes |
| `border` | `#E7E0D6` | `--color-border` | Card borders, dividers |

#### Accent Colors

| Name | Hex | CSS var | Usage |
|------|-----|---------|-------|
| `gold` | `#B8860B` | `--color-gold` | Primary CTA, active states, MAX tier, links |
| `gold-soft` | `#D4A843` | `--color-gold-soft` | Hover states, secondary gold |
| `gold-bg` | `#F5ECD4` | `--color-gold-bg` | Gold tinted backgrounds, MAX badge |
| `sage` | `#6B8F71` | `--color-sage` | PRO tier, success, growth topics |
| `sage-bg` | `#DCE8DD` | `--color-sage-bg` | PRO badge bg, success bg |
| `ember` | `#B85C38` | `--color-ember` | Warnings, shadow/challenge readings |
| `ember-bg` | `#F2DDD3` | `--color-ember-bg` | Warning backgrounds |
| `error` | `#C53030` | `--color-error` | Form errors, danger zone |
| `error-bg` | `#FEE2E2` | `--color-error-bg` | Error backgrounds |

#### Tier Colors

| Tier | Accent | Badge bg | Badge border |
|------|--------|----------|-------------|
| FREE | `charcoal` | `sand` | `border` |
| PRO | `sage` | `sage-bg` | `sage` |
| MAX | `gold` | `gold-bg` | `gold` |

### CSS Variables (globals.css)

```css
@layer base {
  :root {
    /* Base */
    --color-cream: #F7F3ED;
    --color-warm-white: #FFFDF9;
    --color-sand: #EDE6DA;
    --color-ink: #1C1917;
    --color-charcoal: #44403C;
    --color-stone: #78716C;
    --color-border: #E7E0D6;

    /* Accent */
    --color-gold: #B8860B;
    --color-gold-soft: #D4A843;
    --color-gold-bg: #F5ECD4;
    --color-sage: #6B8F71;
    --color-sage-bg: #DCE8DD;
    --color-ember: #B85C38;
    --color-ember-bg: #F2DDD3;
    --color-error: #C53030;
    --color-error-bg: #FEE2E2;

    /* shadcn/ui semantic mapping */
    --background: var(--color-cream);
    --foreground: var(--color-ink);
    --card: var(--color-warm-white);
    --card-foreground: var(--color-ink);
    --border: var(--color-border);
    --input: var(--color-border);
    --ring: var(--color-gold);
    --primary: var(--color-gold);
    --primary-foreground: var(--color-warm-white);
    --secondary: var(--color-sand);
    --secondary-foreground: var(--color-charcoal);
    --muted: var(--color-sand);
    --muted-foreground: var(--color-stone);
    --destructive: var(--color-error);
    --destructive-foreground: var(--color-warm-white);
    --accent: var(--color-gold-bg);
    --accent-foreground: var(--color-gold);
    --radius: 0.5rem;
  }
}
```

---

## 2. Typography

### Font Stack (from Figma research)

| Role | Font | Weight | Google Fonts | Usage |
|------|------|--------|-------------|-------|
| Heading | **Playfair Display** | 400–700 | `Playfair+Display:wght@400;500;600;700` | H1–H3, hero, section titles |
| UI Body | **Inter** | 400, 500 | `Inter:wght@400;500;600` | Forms, buttons, nav, labels, metadata |
| Reading Body | **Lora** | 400 | `Lora:wght@400;500;600;700&display=swap` | Long-form reading content (Topic Reading) |
| Meta / Code | **JetBrains Mono** | 400 | `JetBrains+Mono:wght@400` | Source footnotes, chart labels, technical metadata |

> All 4 fonts support Vietnamese diacritics (ắ ộ ừ ổ ữ ể ạ).
> Playfair Display → editorial gravitas, timeless.
> Inter → maximally legible UI text.
> Lora → warm serif for long reading — friendlier than Playfair at body sizes.
> JetBrains Mono → clean monospace for technical labels, system source tags.

### Vietnamese Typography Rules (CRITICAL)

```
1. NEVER use text-transform: uppercase on Vietnamese text
   — Uppercase Vietnamese diacritics are broken/ugly in most fonts
   — Exception: brand name "360HUMAN" in logo only (no diacritics)

2. Minimum font size: 15px for body text and interactive elements
   — Vietnamese diacritics become illegible below 15px
   — Use 15px where you would normally use 14px
   — Exception: source footnotes (mono) and captions may use 13px

3. Line-height: minimum 1.7 for body text (16px-18px)
   — Vietnamese stacking diacritics (ệ, ộ, ẫ) need extra vertical room
   — Reading content: 1.8 or higher
   — Headings (20px+): may use tighter line-height (1.2-1.5) — diacritics visible at larger sizes

4. Maximum line width: 68 characters (~600px at 16px, ~680px at 18px)
   — Vietnamese words average shorter than English, but diacritics add visual density
   — Tighter line width improves readability significantly
```

### Type Scale

| Token | Size | Line height | Weight | Font | Usage |
|-------|------|-------------|--------|------|-------|
| `display` | 40px | 1.2 (48px) | 700 | Playfair | Landing hero H1 only |
| `h1` | 32px | 1.3 (42px) | 600 | Playfair | Page titles |
| `h2` | 24px | 1.4 (34px) | 600 | Playfair | Section headings |
| `h3` | 20px | 1.5 (30px) | 500 | Playfair | Card titles, subsections |
| `h4` | 16px | 1.7 (27px) | 600 | Inter | Subsection labels |
| `reading` | 18px | 1.8 (32px) | 400 | Lora | Long-form reading content |
| `body` | 16px | 1.7 (27px) | 400 | Inter | Standard UI body text |
| `body-sm` | 15px | 1.7 (26px) | 400 | Inter | Secondary text (NOT 14px) |
| `caption` | 13px | 1.7 (22px) | 400 | Inter | Captions only — use sparingly |
| `mono` | 13px | 1.5 (20px) | 400 | JetBrains Mono | Source footnotes, chart labels |
| `label` | 13px | 1.7 (22px) | 500 | Inter | Form labels, badge text |

### CSS Variables

```css
:root {
  --font-heading: "Playfair Display", Georgia, "Times New Roman", serif;
  --font-body: "Inter", system-ui, -apple-system, sans-serif;
  --font-reading: "Lora", Georgia, serif;
  --font-mono: "JetBrains Mono", "Fira Code", monospace;
}
```

### Reading Content Typography

```css
.reading-content {
  font-family: var(--font-reading);
  font-size: 1.125rem;        /* 18px */
  line-height: 1.8;           /* Vietnamese-optimized */
  color: var(--color-ink);
  max-width: 42.5rem;         /* ~680px ≈ 68 chars at 18px */
  margin: 0 auto;
  letter-spacing: 0.01em;     /* Slightly open for Lora readability */
}

.reading-content h2 {
  font-family: var(--font-heading);
  font-size: 1.5rem;
  line-height: 1.4;
  margin-top: 3rem;
  margin-bottom: 1rem;
  color: var(--color-ink);
}

.reading-content p {
  margin-bottom: 1.5rem;
}

/* Source footnotes — technical metadata style */
.reading-source {
  font-family: var(--font-mono);
  font-size: 0.8125rem;       /* 13px */
  color: var(--color-stone);
  font-style: normal;         /* Mono, not italic */
  opacity: 0.8;
}
```

---

## 3. Texture & Surface

### Philosophy: "Cảm giác giấy nhám" (rough paper feel)

The background should NOT feel like a flat digital screen. It should feel like rough, uncoated paper — warm, tactile, slightly imperfect. This is the single biggest differentiator from competitors.

NOT smooth parchment. NOT glossy. NOT flat white. Nhám = rough, grainy, organic.

### Implementation: CSS Noise Grain

```css
/* Apply to body or main wrapper */
.grain-texture {
  position: relative;
}

.grain-texture::before {
  content: "";
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 0;
  opacity: 0.03;                /* Very subtle — barely visible */
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)'/%3E%3C/svg%3E");
  mix-blend-mode: multiply;
  isolation: isolate;
}
```

Alternative: use a subtle noise PNG tile (3KB) for better cross-browser support:
```css
.grain-texture::before {
  background: url("/textures/grain-light.png") repeat;
  opacity: 0.04;
}
```

### Card Surfaces

Cards should feel slightly raised from the textured background:
```css
.card-surface {
  background: var(--color-warm-white);
  border: 1px solid var(--color-border);
  border-radius: 0.75rem;     /* 12px */
  /* NO heavy shadow — just a very subtle lift */
  box-shadow: 0 1px 4px rgba(28, 25, 23, 0.06);
}
```

---

## 4. Spacing System

### Base Unit: 8px

| Token | Value | Tailwind | Usage |
|-------|-------|---------|-------|
| `xs` | 4px | `gap-1` | Inline gaps, icon padding |
| `sm` | 8px | `gap-2` | Close-together elements |
| `md` | 16px | `gap-4` | Standard component padding |
| `lg` | 24px | `gap-6` | Section padding |
| `xl` | 32px | `gap-8` | Between major sections |
| `2xl` | 48px | `gap-12` | Page section gaps |
| `3xl` | 64px | `gap-16` | Hero vertical padding |
| `4xl` | 96px | `gap-24` | Landing page section separators |

### Layout Grid (Web-Based Responsive)

| Breakpoint | Width | Columns | Gutter | Side margin |
|-----------|-------|---------|--------|-------------|
| Mobile | < 768px | 4 col | 16px | 20px |
| Tablet | 768–1024px | 8 col | 24px | 40px |
| Desktop | 1024–1280px | 12 col | 24px | 48px |
| Wide | > 1280px | 12 col | 24px | auto (centered, max 1280px) |

### Container Max Widths

```css
:root {
  --container-form: 480px;      /* Auth forms (S2), onboarding (S3) */
  --container-reading: 680px;   /* Reading content max-width inside Col 1 (68 chars at 18px) */
  --container-content: 960px;   /* Pricing (S7), profile (S8) */
  --container-full: 1280px;     /* Dashboard 3-col (S4), system reading (S5) */
}
```

### Component Spacing

| Component | Padding |
|-----------|---------|
| Page wrapper | `px-5 py-8` (mobile) / `px-12 py-12` (desktop) |
| Card | `p-5` (mobile) / `p-6` (desktop) |
| Button (md) | `px-6 py-3` (height: 48px) |
| Input | `px-4 py-3` (height: 48px) |
| Reading section gap | `mt-12` (between reading sections) |
| Topic card grid | `gap-4` (mobile) / `gap-6` (desktop) |

---

## 5. Border Radius & Shadow

### Border Radius

| Token | Value | Usage |
|-------|-------|-------|
| `sm` | 6px | Inputs, small tags |
| `md` | 8px | Buttons |
| `lg` | 12px | Cards, topic cards, modals |
| `xl` | 16px | Large cards, reading cards |
| `full` | 9999px | Badges, avatars, pills, tier badges |

### Shadows (warm-tinted, very subtle)

```css
:root {
  --shadow-sm: 0 1px 3px rgba(28, 25, 23, 0.06);
  --shadow-md: 0 4px 12px rgba(28, 25, 23, 0.08);
  --shadow-lg: 0 8px 24px rgba(28, 25, 23, 0.10);
  --shadow-glow: 0 0 20px rgba(184, 134, 11, 0.08);  /* Gold glow for CTAs */
}
```

Shadow philosophy: less is more. Cards use `shadow-sm` + border. Only modals and floating elements use `shadow-lg`. Gold glow for primary CTA hover states.

---

## 6. Iconography

### System Icons
**Lucide React** (included with shadcn/ui)
- Default size: 20px
- In-text size: 16px
- Navigation: 24px
- Stroke width: **1.5** (lighter = more elegant, less SaaS-y)

### 5 System Framework Icons (custom — Sprint 1)

| System | Icon concept | Aesthetic |
|--------|-------------|-----------|
| Tử Vi | 12-palace circular chart | Gold line art, geometric |
| BaZi | 4-pillar vertical bars | Structured, balanced |
| Human Design | Body graph diamond | Angular, connected nodes |
| Số học | Sacred geometry / numbers | Clean number glyph |
| Vedic | 12-house wheel | Circular, precise |

Style: Single-weight line art, warm gold or ink color. NOT filled, NOT colorful.
Sprint 0 placeholder: use Lucide geometric icons (Hexagon, Square, Diamond, Hash, Star).

---

## 7. Motion / Animation

**Principle: Restraint.** (From Linear.app reference — "motion restraint")

Every animation must have a purpose. No decoration, no delight-for-delight's-sake.

| Type | Duration | Easing | Usage |
|------|----------|--------|-------|
| Page transition | 200ms | ease-out | Fade between routes |
| Card hover | 150ms | ease | Subtle lift: translateY(-2px), shadow-md |
| Button press | 100ms | ease-in | Scale 0.98 |
| Modal/Dialog | 250ms | cubic-bezier(0.16, 1, 0.3, 1) | Fade + scale from 0.96 |
| Skeleton shimmer | 1.5s loop | ease-in-out | Loading states |
| Tab switch | 150ms | ease | Underline slide |

```css
/* Reduced motion respect */
@media (prefers-reduced-motion: reduce) {
  * {
    animation: none !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

## 8. UX Principles (from competitor analysis)

These are NOT just aesthetic choices — they are UX rules extracted from the Figma research.

### 8.1 — Primary Action Hierarchy

Learned from Co-Star's best pattern. Each screen has ONE primary action (gold CTA) + secondary actions (ghost/text).

- Landing: "Khám phá bản thân"
- Register: "Tạo tài khoản"
- Onboarding: "Bắt đầu khám phá"
- Reading: read (no competing CTAs inside reading content)
- Pricing: choose a plan

**Exception — Workspace screens**: S4 Dashboard and S5 System Reading are "workspace" screens, not "action" screens. Workspace screens allow multiple interactions but maintain visual hierarchy: reading content (dominant) > actions (supportive) > charts (reference). Primary CTA gold, secondary actions ghost/text.

### 8.2 — Reading Card Layout

Content is presented in card-based containers, not open-page flowing text. Each reading section = one card. This creates visual breathing room and makes long content scannable.

```
[Reading Card]
├── Card header: section title (Playfair)
├── Card body: reading content (Lora, 18px)
├── Card footer: source footnote (JetBrains Mono)
└── Bottom divider or spacing
```

### 8.3 — Information Hierarchy, Not Information Overload

Competitor lesson: "Nhiều thông tin không cần thiết với users, text rất nhiều"

Rules:
- No wall of text. Break content into short paragraphs (max 4 lines)
- Every heading visible without scrolling on mobile
- Key insight is the FIRST sentence of each section, not buried
- Technical details → footnotes or expandable accordions, never inline

### 8.4 — Daily Ritual UX (Sprint 2+)

Co-Star's strongest pattern: users come back daily because there's always something new.
Plan for Sprint 2: daily insight widget on Dashboard — 1 line from a different system each day.

---

## 9. Dark Mode

**Sprint 0: NOT implemented.**

Note: The competitor research shows appreciation for "dark mode warmth" (Linear.app style).
If implemented later, it should be WARM dark (like Linear's dark purple-gray), not cold dark (like Co-Star's pure black). Warm dark = `#1C1917` ink-toned background, gold accents glow.

---

## 10. Accessibility

- Minimum contrast: 4.5:1 for body text (ink on cream: verified 14.8:1)
- Focus rings: 2px solid gold, 2px offset
- Click/tap targets: minimum 44 x 44px
- Font minimum: **15px** rendered (Vietnamese diacritics requirement)
- All icons have `aria-label` or visible paired text
- `text-transform: uppercase` is BANNED on all Vietnamese content
- `prefers-reduced-motion` respected for all animations

---

## 11. shadcn/ui Theme Config

```json
{
  "style": "default",
  "rsc": true,
  "tsx": true,
  "tailwind": {
    "config": "tailwind.config.ts",
    "css": "src/app/globals.css",
    "baseColor": "stone",
    "cssVariables": true
  },
  "aliases": {
    "components": "@/components",
    "utils": "@/lib/utils"
  }
}
```

shadcn baseColor `stone` is the closest warm-neutral match. All colors above are applied via CSS variables in `globals.css`, overriding shadcn defaults.

---

## 12. Google Fonts Import

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=JetBrains+Mono&family=Lora:wght@400;500;600;700&family=Playfair+Display:wght@400;500;600;700&display=swap" rel="stylesheet">
```

Or via Next.js `next/font`:

```ts
import { Playfair_Display, Inter, Lora, JetBrains_Mono } from "next/font/google"

export const playfair = Playfair_Display({
  subsets: ["latin", "vietnamese"],
  variable: "--font-heading",
})

export const inter = Inter({
  subsets: ["latin", "vietnamese"],
  variable: "--font-body",
})

export const lora = Lora({
  subsets: ["latin", "vietnamese"],
  variable: "--font-reading",
})

export const jetbrainsMono = JetBrains_Mono({
  subsets: ["latin", "vietnamese"],
  variable: "--font-mono",
})
```
