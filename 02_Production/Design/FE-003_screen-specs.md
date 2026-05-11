---
title: "Screen Specifications — 10 Core Screens"
id: "FE-003"
updated: "2026-03-16"
status: "ready-for-review"
stack: "Next.js 15 / shadcn/ui / Tailwind v4"
---

# Screen Specifications — 360Human

> Web-based, responsive. Desktop 1280px → tablet 768px → mobile 375px.
> NOT a native app — standard web navigation: header nav + hamburger on mobile.
> Tier logic: FREE / PRO — blur/lock applied where noted. (MVP: 2 tiers only)
>
> **Typography**: Playfair Display (headings) / Inter (UI) / Lora (reading body) / JetBrains Mono (meta/sources)
> **Vietnamese rules**: min 15px, line-height >= 1.7, NEVER uppercase Vietnamese text, max 68 chars/line
> **Texture**: Warm cream background with subtle grain overlay ("cảm giác giấy nhám")
> **Info hierarchy**: Avoid text walls — short paragraphs, clear headings, key insight first

---

## S1 — Landing Page

### Purpose
Convert cold visitors → registration. Communicate concept: "bánh xe cuộc đời" — the wheel of life that rolls through your journey.

### Layout

Desktop: full-width sections, hero with visual left + text right.
Mobile: single column, stacked.

```
[Header: Logo + "Đăng nhập" button]
[Hero: Wheel visual (left) + headline + CTA (right)]
[Value Props: 3 cards row — accuracy/depth/personalization]
[Connection: Wheel → bản thể → 5 system icons]
[How It Works: 4 steps]
[Pricing Teaser]
[Footer]
```

### Hero Section

| Element | Detail |
|---------|--------|
| Visual (left) | Bánh xe cuộc đời — wheel rolling on a line that goes up & down with upward trend |
| H1 headline | Playfair Display 700, 40px. Concept: cuộc đời là hành trình, bánh xe lăn đi |
| Subheadline | Inter 400, 18px, muted color. 2 lines max |
| Primary CTA | Below headline — "Khám phá bản thân" gold button |
| Secondary CTA | "Tìm hiểu thêm ↓" — text link, scrolls to #how-it-works |

### Value Props — 3 Cards

Row on desktop, stacked on mobile. Focus: **accuracy is the top priority**.

| Card | Concept | Hint |
|------|---------|------|
| 1 | 5 hệ thống phân tích | Depth — not just one system, five cross-referenced |
| 2 | 20.000+ trang tài liệu | Knowledge base — backed by serious research |
| 3 | Cá nhân hóa cho riêng bạn | Personal — not generic horoscope, YOUR data |

### Connection Section

Visual: Bánh xe (wheel) connects to "bản thể" (self/essence) → bản thể radiates outward to 5 system icons.

| Element | Detail |
|---------|--------|
| Center | Bản thể — user's identity/avatar concept |
| Connections | 5 lines radiating to each system icon |
| System icons | Tử Vi / BaZi / Human Design / Số học / Vedic — circular, gold line art |

### How It Works — 4 Steps

Horizontal on desktop, vertical on mobile. Each step: number + icon + title + 1-line description.

| Step | Title | Description |
|------|-------|-------------|
| 1 | Nhập thông tin | Họ tên, Giới tính, Ngày, giờ (có thêm option tick không nhớ), nơi sinh |
| 2 | Phân tích | 5 hệ thống tính toán biểu đồ của bạn |
| 3 | Đọc chi tiết | 10 chủ đề phân tích chuyên sâu |
| 4 | Hỏi & Đáp | Đặt câu hỏi cụ thể, nhận câu trả lời cá nhân |

### Remaining Elements

| Zone | Element | Detail |
|------|---------|--------|
| Header | Logo text "360Human" | Left-aligned, Playfair Display, 20px |
| Header | Nav: "Đăng nhập" | Ghost button, right-aligned |
| Header | Nav: "Đăng ký" | Primary gold button, right-aligned, next to Đăng nhập |
| Pricing Teaser | "Bắt đầu miễn phí — Không cần thẻ" | Muted text, links to /pricing |
| Footer | Links: Về chúng tôi / Chính sách / Liên hệ | Small text |

### States
- **Default**: Static, no auth
- **Scroll-triggered**: Hero CTA becomes sticky bar on scroll past hero
- **Loading**: Skeleton on system icons + wheel visual

### User Flow
```
Arrive at landing
  → See wheel concept + headline
  → Scroll → value props (accuracy) → connection visual → how it works
  → Click "Khám phá bản thân" → /register
  → OR Click "Đăng nhập" → /login
  → OR Click "Tìm hiểu thêm" → anchor scroll to #how-it-works
```

### Tier Restrictions
None — public page.

### Notes
- Social Proof: removed — no sharable feature in MVP, will add post-launch
- Step 4 (Hỏi & Đáp): placeholder for future Q&A feature, shown in flow but greyed/coming soon if not ready

---

## S2 — Register / Login

### Purpose
Minimal friction account creation. Email + password only. Social proof present but subtle.

### Layout
```
[Logo — centered]
[Tab: Đăng ký | Đăng nhập]
[Form]
[Divider "hoặc"]
[Google Sign-In button]  ← Sprint 2 / defer
```

### Elements

| Zone | Element | Detail |
|------|---------|--------|
| Header | Logo only | Centered, no nav |
| Tab Switch | "Đăng ký" / "Đăng nhập" | Underline tab style |
| Form — Register | Email input | type="email", placeholder="email@example.com" |
| Form — Register | Password input | type="password", show/hide toggle |
| Form — Register | Confirm password | Only on register tab |
| Form — Register | Submit button | "Tạo tài khoản" — full width |
| Form — Login | Email input | Same |
| Form — Login | Password input | Same |
| Form — Login | "Quên mật khẩu?" | Text link, right-aligned |
| Form — Login | Submit button | "Đăng nhập" — full width |
| Error State | Inline error text | Red, below field, icon |

### States
- **Default**: Register tab active
- **Error**: Field-level validation, red border + message
- **Loading**: Button spinner during API call
- **Success — Register**: Auto-redirect to /onboarding
- **Success — Login**: Auto-redirect to /dashboard

### User Flow
```
/register (default tab: Đăng ký)
  → Fill email + password + confirm
  → Click "Tạo tài khoản"
  → API success → redirect /onboarding
  → API error → inline error message

/login (tab: Đăng nhập)
  → Fill email + password
  → Click "Đăng nhập"
  → API success → redirect /dashboard
  → "Quên mật khẩu?" → /forgot-password
```

### Tier Restrictions
None.

---

## S3 — Onboarding

### Purpose
Collect birth data needed to generate all 5 system charts. Single page form — not step-by-step wizard.

### Layout
```
[Progress bar — auto-fills as user completes each field]
[All fields on one page, vertical stack]
[Submit button at bottom]
```

### Fields (in order)

| # | Field | Input type | Detail |
|---|-------|-----------|--------|
| 1 | Họ tên | Text input | Max 50 chars, placeholder "Họ và tên khai sinh" |
| 2 | Giới tính | 3 toggle buttons | Nam / Nữ / Khác |
| 3 | Ngày sinh | DD / MM / YYYY | 3 separate fields, validation: valid date, not future |
| 4 | Giờ sinh | HH:MM (24h) | With checkbox "Tôi không nhớ giờ sinh" — if checked, skip |
| 5 | Nơi sinh | City autocomplete | Vietnam cities priority, fallback manual entry |

Submit button: "Bắt đầu khám phá" — gold, full width

### Progress Bar
- Auto-advances as user fills each field (not click-driven)
- 5 segments matching 5 fields
- Visual: thin gold bar at top of form

### States
- **Default**: All fields visible, empty, progress bar at 0
- **In progress**: Progress bar fills as fields completed
- **Error**: Field-level validation, red border + message
- **"Không nhớ giờ sinh"**: Checkbox checked → time field disabled, progress counts as complete
- **Loading (submit)**: Transitions directly into S4 5-layer loading animation (no separate overlay). S3 form fades out → S4 loading layers fade in on same page, then layout renders when complete.

### User Flow
```
/onboarding (single page)
  → Fill fields top to bottom, progress bar auto-fills
  → Click "Bắt đầu khám phá"
  → API: generate all 5 charts
  → S3 form fades out → S4 5-layer loading animation plays in-place
  → Each system lights up as it completes
  → All done → Dashboard layout renders (no extra redirect)
```

### Tier Restrictions
None — all users complete onboarding.

---

## S4 — Dashboard / Home

### Purpose
Main experience after login. 2-column layout: topic readings with inline actions (WHAT-HOW-WHAT'S NEXT) + system charts (WHY). No profile summary — users know their own info.

### Key Concept
- **Luận giải theo chủ đề** (Left) = WHAT - HOW - WHAT'S NEXT + inline actions sau mỗi topic
- **Phân tích charts** (Right) = WHY — the data behind the readings
- Users should understand: topics tell you what to do, charts tell you why

### Layout — 2 Columns

Desktop: 2-column — Left 2/3 (readings + inline actions), Right 1/3 (charts).
Mobile: single column, Left stacked above → Right collapsible at bottom.

```
┌──────────────────────────────────────────────────────────┐
│ Top Bar: [Name] [Tier Badge]              [Export PDF ↗] │
├──────────────────────────────────────────────────────────┤
│ Reading Progress Bar: ████████░░░░░░░░ 4/10 chủ đề      │
├────────────────────────────────┬─────────────────────────┤
│ Left (2/3)                     │ Right (1/3)              │
│                                │                          │
│ ┌─ Topic 1 (accordion) ──────┐│ Thông số hệ thống        │
│ │ Luận giải content (Lora)   ││                          │
│ │ ...                        ││ 5 systems collapsed      │
│ │ ── Inline Actions ──       ││ Click → expand full data │
│ │ Action 1 [BaZi badge]      ││                          │
│ │ Action 2 [Tử Vi badge]     ││ CTA: Xem luận giải chi   │
│ │ "Xem toàn bộ →" (→ S10)   ││ tiết theo hệ thống (PRO) │
│ └────────────────────────────┘│                          │
│ ┌─ Topic 2 (collapsed) ──────┐│                          │
│ └────────────────────────────┘│                          │
│ ┌─ Topic 3 🔒 PRO ──────────┐│                          │
│ └────────────────────────────┘│                          │
├────────────────────────────────┴─────────────────────────┤
│ Q&A Section: Hỏi đáp về luận giải                        │
└──────────────────────────────────────────────────────────┘
```

### Top Bar

| Element | Detail |
|---------|--------|
| Name | "[Name]" + TierBadge — left aligned (no greeting phrase) |
| Tier badge | Pill: "FREE" / "PRO" — next to name |
| Export PDF | Button, top-right — PRO only, hidden for FREE |
| Reading progress | Horizontal bar below top bar — "X/10 chủ đề". FREE users see "2/10 chủ đề — Mở khóa thêm 8 với PRO". Updates on accordion open |

### Left Column — Luận giải + Inline Actions (Accordion)

10 topics as **accordion** — click to expand, only 1 open at a time. Each topic contains: reading content + inline actions at the bottom.

| # | Topic | Tier |
|---|-------|------|
| 1 | Tổng quan bản thân | FREE |
| 2 | Sứ mệnh & mục đích sống | FREE |
| 3 | Tình cảm & các mối quan hệ | PRO |
| 4 | Sự nghiệp & nghề nghiệp | PRO |
| 5 | Tài chính & tiền bạc | PRO |
| 6 | Sức khỏe & năng lượng | PRO |
| 7 | Gia đình & nguồn gốc | PRO |
| 8 | Điểm mạnh & tài năng | PRO |
| 9 | Thách thức & bóng tối | PRO |
| 10 | Thời điểm & chu kỳ | PRO |

#### Expanded Topic Structure

```
┌─ [Topic Title] ─────────────────────────────────────────┐
│                                                          │
│  [Reading content — Lora 400 18px, max 680px]            │
│  Paragraph 1...                                          │
│  Paragraph 2...                                          │
│  nguồn: Tử Vi, BaZi — JetBrains Mono 13px              │
│                                                          │
│  ── Hành động ──────────────────────────────────────     │
│  1. [Action title] .............. [BaZi badge]           │
│     1-line description                                   │
│  2. [Action title] .............. [Tử Vi badge]          │
│     1-line description                                   │
│                                                          │
│  "Xem toàn bộ hành động →" (link to /actions S10)       │
└──────────────────────────────────────────────────────────┘
```

### Right Column — Thông số hệ thống (Charts = WHY)

5 system panels, collapsed by default. Click to expand full chart data.

| System | Default state | Expanded state |
|--------|--------------|----------------|
| Tử Vi | Collapsed — name + mini icon | Full palace chart data + key stars |
| BaZi | Collapsed | Full 4-pillar data + day master |
| Human Design | Collapsed | Type, authority, profile, centers |
| Số học | Collapsed | Life path, expression, soul urge |
| Vedic | Collapsed | Rashi, nakshatra, planets, houses |

Bottom of Right Column:
- CTA: "Xem luận giải chi tiết theo từng hệ thống" → deep per-system reading (PRO)

### Q&A Section (bottom)

Below the 2-column layout. Users can ask follow-up questions about their reading.

| Element | Detail |
|---------|--------|
| Input | Text field: "Hỏi về luận giải của bạn..." |
| Response | Câu trả lời dựa trên dữ liệu biểu đồ + nội dung luận giải của người dùng |
| Tier gate | FREE locked, PRO unlimited |

### Tier Restrictions

| Feature | FREE | PRO |
|---------|------|-----|
| Topic readings (luận giải) | Topics 1-2 only | All 10 topics |
| Inline actions | From topics 1-2 | All actions |
| System charts (Right col) | Locked | All 5 systems |
| Per-system deep reading (→ S5) | Locked | All 5 systems |
| Export PDF | Locked | Unlocked |
| Q&A | Locked | Unlimited |

### Mobile Layout (< 768px)

Single column stacked: Left column (accordion topics) → Right column collapsed as "Biểu đồ hệ thống ▾" expandable section at bottom → Q&A below. No tabs needed — accordion already handles focus.

### Loading Animation

5 layers stacked, each representing one system. Each starts **gray/muted**. As each system's data finishes loading, its layer transitions to **dark/active** (gold accent glow).

```
Loading sequence:
  [Số học    ] ████████████ → done → lights up
  [BaZi      ] ████████░░░ → loading...
  [Tử Vi     ] ████░░░░░░ → loading...
  [Vedic     ] ██░░░░░░░░ → loading...
  [Human Des.] ░░░░░░░░░░ → waiting...
```

Each layer: system icon + name + progress bar. Gray → gold transition on completion.

### States
- **Loading**: 5-layer system loading animation (see above)
- **FREE user**: Topics 3–10 blurred + lock, Col 3 locked, Q&A locked
- **PRO user**: All topics visible, only HD chart in Col 3, no PDF, no deep chart reading
- **MAX user**: Everything unlocked
- **Q&A active**: Input expanded, response streaming below

### User Flow
```
/dashboard
  → Reading loads with 5-layer animation
  → Scroll Col 1 topics (unlocked ones)
  → Col 2 shows corresponding actions
  → Click system in Col 3 → expands chart data
  → Click "Xem luận giải chi tiết" → /reading/system/[system] (MAX)
  → Click locked content → upgrade prompt → /pricing
  → Type question in Q&A → receive response
  → Click Export PDF (MAX) → download
```

---

## S5 — System Reading

### Purpose
Deep dive into one system's chart data + per-system luận giải. 2-column layout: chart (left) + reading (right).

### Layout
```
┌──────────────────────────────────────────────────────────┐
│ Breadcrumb: ← Dashboard > Tử Vi                         │
│ System Tabs: [Tử Vi] | BaZi | HD | Số học | Vedic       │
├────────────────────────┬─────────────────────────────────┤
│ Left: Chart            │ Right: Luận giải                │
│                        │                                 │
│ System visualization   │ ┌─ Tab: Phân tích sâu ────────┐│
│ (Cung chart / Body     │ │ Full reading, scroll         ││
│  graph / 4-pillar /    │ │ Lora 400 18px                ││
│  etc.)                 │ └──────────────────────────────┘│
│                        │ ┌─ Tab: Interactive ───────────┐│
│ Interactive:           │ │ Click element in chart →     ││
│ Click element →        │ │ shows explanation for that   ││
│ highlights + shows     │ │ specific element             ││
│ explanation on right   │ │ (No click = show full)       ││
│                        │ └──────────────────────────────┘│
├────────────────────────┴─────────────────────────────────┤
│ Q&A: Hỏi đáp về hệ thống này                            │
│ PRO: 5 lần | MAX: Unlimited                              │
└──────────────────────────────────────────────────────────┘
```

### Left Column — Chart Visualization

| System | Visualization |
|--------|--------------|
| Tử Vi | 12-palace grid (Cung chart) — clickable palaces |
| BaZi | 4-pillar table (Tứ Trụ) — clickable pillars/elements |
| Human Design | Body graph — clickable centers/channels |
| Số học | Number breakdown — clickable numbers |
| Vedic | Planetary house grid — clickable planets/houses |

### Right Column — Luận giải (2 modes)

| Mode | Behavior |
|------|----------|
| Phân tích sâu | Full reading, all content displayed, scrollable. Lora 400 18px, max-width 680px |
| Interactive | Linked to chart on left. User clicks an element (e.g. Cung Mệnh, Day Master, Sacral Center) → right column shows luận giải for that specific element. If user doesn't click anything → defaults to full display |

### Q&A Section (bottom)

| Element | Detail |
|---------|--------|
| Input | "Hỏi về [tên hệ thống] của bạn..." |
| Response | Dựa trên dữ liệu biểu đồ hệ thống đang xem |
| FREE | Locked — upgrade prompt |
| PRO | Unlimited |

### States
- **Loading**: Skeleton in chart area + reading text
- **Tab switch**: Instant (data pre-fetched) or loading skeleton
- **Interactive mode**: Chart element highlighted (gold border), right column updates
- **No birth time**: Banner "Thiếu giờ sinh — một số thông tin có thể không chính xác" on Tử Vi + HD tabs
- **FREE user on S5**: Redirect to /pricing — cannot access S5

### User Flow
```
/reading/system/tu-vi (default system tab)
  → View chart (left) + full reading (right, default)
  → Switch to Interactive tab → click chart element → right updates
  → Switch tab → /reading/system/bazi (etc.)
  → Ask question in Q&A → receive response
  → ← Breadcrumb back to /dashboard
```

### Tier Restrictions
- FREE: Cannot access S5 — redirect to /pricing
- PRO: All 5 systems + unlimited Q&A

---

## S6 — Topic Reading (merged into S4)

> **S6 không còn là trang riêng.** Nội dung Topic Reading đã được tích hợp vào S4 Dashboard — Col 1 (Luận giải) + Col 2 (Action Items).
>
> Xem S4 để biết chi tiết:
> - **Col 1** = 10 topics luận giải (WHAT - HOW - WHAT'S NEXT), Lora 400 18px
> - **Col 2** = Action items derived từ luận giải, có source tags
> - **Source footnotes**: JetBrains Mono 13px, muted color
> - **Tier gate**: FREE = topics 1-2, PRO = all 10
> - **Q&A**: Ở bottom S4, FREE locked, PRO unlimited
>
> Không có route `/reading/[topic-slug]` riêng — tất cả hiển thị trong `/dashboard`.

---

## S7 — Pricing Page

### Purpose
Convert FREE → PRO. 2-tier comparison. Clear value, no confusion, local payment context.

### Layout
```
[Hero: "Mở khóa toàn bộ hành trình của bạn"]
[Tier cards: FREE | PRO (highlighted)]
[Feature comparison table]
[FAQ — 3 questions]
[CTA footer]
[Note: profile pricing]
```

### Elements

#### Tier Cards (2 columns on desktop, stacked on mobile)

| Tier | Price | CTA |
|------|-------|-----|
| FREE | 0đ | "Gói hiện tại ✓" (text, no button) |
| PRO | 199.000đ | "Nâng cấp PRO" (gold button) |

Each card contains:
- Tier badge (pill)
- Price display (no "/tháng" — don't mention billing period)
- "Phù hợp với..." tagline (1 sentence)
- Top features (checkmarks)
- CTA button (PRO only)

PRO card: gold border accent, slightly elevated.

#### Feature Comparison Table

| Tính năng | FREE | PRO |
|-----------|------|-----|
| **Luận giải theo chủ đề** | 2 chủ đề | 10 chủ đề |
| **Action items** | Nền Móng (2 actions) | Cả 3 tầng |
| **Biểu đồ hệ thống** | — | Cả 5 hệ thống |
| **Luận giải chi tiết theo hệ thống** | — | Cả 5 hệ thống |
| **Time Oracle** | Tháng hiện tại | Lifetime + tất cả |
| **Hỏi đáp** | — | Không giới hạn |
| **Export PDF** | — | ✓ |

#### Profile Note (below table)

> Mỗi gói áp dụng cho 1 hồ sơ. Thêm hồ sơ mới với cùng mức giá tại **Cài đặt**.

### Checkout Flow (inline or modal)

| Step | Content |
|------|---------|
| 1. Payment method | "Chọn phương thức: VietQR / Thẻ quốc tế" |
| 2a. VietQR | QR code display + "Đang chờ thanh toán..." polling (check every 5s) |
| 2b. Card | Payment form embed (Stripe or local gateway) |
| 3. Success | Redirect to /dashboard with gold banner "Chào mừng bạn đến PRO!" |
| 3. Failure | "Thanh toán chưa thành công. Thử lại?" + retry button |

### States
- **FREE user**: PRO card highlighted with gold border
- **PRO user**: "Gói hiện tại ✓" on PRO card, no upgrade CTA
- **Loading payment**: Button spinner → checkout flow
- **Success**: Redirect to /dashboard with upgrade success banner

### User Flow
```
/pricing
  → View 2 tiers
  → Click "Nâng cấp PRO"
  → Checkout: choose VietQR or Card
  → VietQR: scan → polling → success
  → Card: fill form → submit → success
  → Success → /dashboard with banner
```

---

## S8 — Profile + Settings

### Purpose
View account info, manage subscription, change password, delete account.

### Layout
```
[Header: ← Back to Dashboard]
[Profile section: name + email + tier]
[Birth data section: read-only summary]
[Account section: change password]
[Subscription section: current plan + manage]
[Danger zone: delete account]
```

### Elements

| Zone | Element | Detail |
|------|---------|--------|
| Profile | Avatar initials circle | 64px, warm background |
| Profile | Display name (editable) | Click to edit inline |
| Profile | Email (read-only) | |
| Profile | Tier badge: "FREE" / "PRO" + "Quản lý gói" link | |
| Birth Data | Birth date / time / city (read-only) | Summarized |
| Birth Data | "Chỉnh sửa dữ liệu sinh" | Link → re-run onboarding partial |
| Profiles | "Thêm hồ sơ mới" | Button → onboarding flow for new person (e.g. partner, child). Requires separate purchase — each profile = 1 payment (199.000đ same as PRO) |
| Profiles | Profile list | List of saved profiles — click to switch active profile |
| Profiles | New profile state | Unpurchased profiles show as FREE-tier (2 topics only). User must buy PRO to unlock full access for that profile |
| Profiles | Active indicator | Current profile highlighted, name shown in TopBar |
| Password | "Đổi mật khẩu" | Expand form: current + new + confirm |
| Subscription | Current plan info | |
| Subscription | "Hủy đăng ký" | Text link, muted |
| Danger Zone | "Xóa tài khoản" | Red text button, confirm dialog |

### States
- **Editing name**: Inline edit, Save/Cancel
- **Changing password**: Expanded form, validation
- **Confirm delete**: Dialog "Bạn có chắc chắn? Dữ liệu sẽ không thể khôi phục."
- **Success actions**: Toast notification

### User Flow
```
/profile
  → Edit name → save inline
  → "Đổi mật khẩu" → expand form → submit
  → "Quản lý gói" → /pricing
  → "Xóa tài khoản" → confirm dialog → DELETE → /login
```

---

---

## S9 — Time Oracle / Forecast

### Purpose
Show timing & cycles — where the user is in their life journey. Drill-down: Lifetime → Yearly → Monthly → Weekly. The "when" complement to S4's "what/how". NO daily data.

### Layout — Drill-Down (3 Layers)

Single page, 3 layers that zoom in. Breadcrumb to jump back. Default: auto-drills to current month.

```
┌──────────────────────────────────────────────────────────┐
│ Top Bar: [Name] [Tier Badge]                             │
│ Breadcrumb: Cuộc đời > 2024-2033 > 2026 > Tháng 3       │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  LAYER 1 — Lifetime                                      │
│  ═══○═══════○═══════●═══════○═══════○═══                 │
│                      ↑ current phase                     │
│  Phase card + quote (accent) + reflection question       │
│                                                          │
│  Click phase or auto-drill ↓                             │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  LAYER 2 — Yearly (2026)                                 │
│  [T1][T2][T3●][T4][T5][T6][T7][T8][T9][T10][T11][T12]   │
│  Yearly summary + key months highlighted                 │
│                                                          │
│  Click month ↓                                           │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  LAYER 3 — Monthly (Tháng 3, 2026)                       │
│  ┌─────────────┬────────────────────────────────────────┐│
│  │ Monthly      │ Calendar grid                          ││
│  │ summary +    │ T2 T3 T4 T5 T6 T7 CN                  ││
│  │ chỉ số tháng │ 4 tuần highlighted, click week →      ││
│  │              │ weekly summary panel                    ││
│  └─────────────┴────────────────────────────────────────┘│
│                                                          │
└──────────────────────────────────────────────────────────┘
```

### Breadcrumb Navigation

```
Cuộc đời > 2024-2033 > 2026 > Tháng 3
  ↑ L1       ↑ phase     ↑ L2    ↑ L3 (current)
```

Click any level → scrolls/zooms back to that layer.

### Layer 1 — Lifetime Timeline

| Element | Detail |
|---------|--------|
| Timeline | Horizontal bar — all Đại Vận phases as segments |
| Current phase | Highlighted gold, glow effect |
| Phase card | "Giai đoạn: [tên]" + 3-5 key points |
| Quote | Accent nhỏ — Playfair Display italic, 1 line, dưới phase card |
| Reflection | "Câu hỏi suy ngẫm: [question]" — muted, below quote |
| Source tags | JetBrains Mono 13px, muted |
| Drill | Click current phase → zooms to Layer 2 (current year) |
| Browse | Click other phases → shows that phase's card |

### Layer 2 — Yearly View

| Element | Detail |
|---------|--------|
| Year | "2026" — Playfair Display, large |
| 12-month grid | 12 cards row (3x4 mobile), current month highlighted gold |
| Month cards | Month name + 1-line energy + color indicator |
| Key months | Notable months marked (career peak, caution, etc.) |
| Yearly summary | Top block: yearly theme + Personal Year number |
| Drill | Click month → zooms to Layer 3 |
| Navigate | ← 2025 \| 2026 \| 2027 → |

### Layer 3 — Monthly View (2-column)

#### Left — Monthly Summary

| Element | Detail |
|---------|--------|
| Theme | "Tháng của sự tập trung nội tâm" — Playfair Display |
| Metrics | 3-5 indicators: energy, focus area, caution dates |
| Navigate | ← Tháng 2 \| Tháng 3 \| Tháng 4 → |

#### Right — Calendar Grid

| Element | Detail |
|---------|--------|
| Calendar | Month grid (T2-CN), current week highlighted gold band |
| Week indicators | 4 weeks, each row = 1 week, color-coded energy level |
| Click week | Weekly summary panel slides in below calendar |

#### Weekly Panel (on week click)

| Element | Detail |
|---------|--------|
| Week range | "Tuần 10/03 — 16/03/2026" |
| Weekly energy | 3-4 line reading: theme, focus, caution |
| Key themes | 2-3 tags (e.g. "Sự nghiệp", "Nội tâm") |
| Context | How this week connects to monthly/yearly theme |
| Source | JetBrains Mono 13px |

### Default Behavior

- First visit: auto-drills Lifetime → current year → current month. All 3 layers visible on scroll.
- Return visits: lands on Layer 3 (current month).
- NO daily data — smallest unit is weekly.

### States
- **Loading**: Skeleton for timeline + month grid
- **Drill down**: Smooth scroll to next layer
- **Drill up**: Breadcrumb click → scroll back up
- **Week selected**: Gold band on week row, weekly panel expands
- **No week selected**: Calendar overview only
- **Year/month nav**: Updates content, maintains drill context

### User Flow
```
/forecast (auto-drill to current month)
  → Layer 1: lifetime phase + quote + reflection
  → Layer 2: 2026 overview, key months
  → Layer 3: Tháng 3, click week → weekly summary
  → Breadcrumb: click "Cuộc đời" → back to Layer 1
  → ← → arrows on year/month to navigate
```

### Tier Restrictions

| Feature | FREE | PRO |
|---------|------|-----|
| Layer 1 — Lifetime | Hidden | Unlocked |
| Layer 2 — Yearly | Hidden | All years |
| Layer 3 — Monthly | Current month only (auto-lands here) | All months |
| Weekly details | Locked | All weeks |

FREE users: skip Layer 1+2 entirely, land directly on Layer 3 (current month) + upsell banner "Mở khóa Lifetime & Yearly với PRO".

---

## S10 — Action Items / Growth System

### Purpose
Help users build a personal improvement system. 3-layer pyramid: Nền Móng → Nuôi Dưỡng → Khai Phóng. Each action is traced back to specific traits (WHAT) and systems (WHY).

### Layout — 2 columns

Left column (1/2): Pyramid + action items per layer.
Right column (1/2): WHAT & WHY panel — updates based on selected action.

```
┌──────────────────────────────────────────────────────────┐
│ Top Bar: [Name] [Tier Badge]                             │
├────────────────────────────┬─────────────────────────────┤
│ Left: Pyramid + Actions    │ Right: WHAT & WHY            │
│                            │                              │
│        /\                  │ ┌─ WHAT ──────────────────┐  │
│       /  \  KHAI PHÓNG     │ │ Action này xuất phát từ │  │
│      /    \                │ │ đặc điểm nào của bạn?   │  │
│     /──────\               │ │                          │  │
│    / NUÔI   \              │ │ "Bạn có Tham Lang miếu  │  │
│   /  DƯỠNG   \             │ │  địa — sức hút tự nhiên │  │
│  /────────────\            │ │  mạnh nhưng dễ phân tán" │  │
│ /   NỀN MÓNG   \           │ └──────────────────────────┘  │
│ ════════════════           │ ┌─ WHY ───────────────────┐  │
│                            │ │ Từ hệ thống nào?        │  │
│ [Actions for selected      │ │                          │  │
│  layer listed below        │ │ Tử Vi: Tham Lang miếu   │  │
│  pyramid]                  │ │ địa tại Cung Mệnh       │  │
│                            │ │ → giải nghĩa chi tiết   │  │
│                            │ └──────────────────────────┘  │
├────────────────────────────┴─────────────────────────────┤
│ (optional bottom section for future features)             │
└──────────────────────────────────────────────────────────┘
```

### Left Column — Pyramid + Actions

#### Pyramid Visual

3-layer triangle, clickable layers. Selected layer highlighted gold.

| Layer | Name | Concept |
|-------|------|---------|
| Tầng 1 (base) | **Nền Móng** | Thói quen cơ bản, nhận thức bản thân, nền tảng cần xây trước |
| Tầng 2 (mid) | **Nuôi Dưỡng** | Phát triển năng lực, bổ sung năng lượng, rèn luyện kỹ năng |
| Tầng 3 (top) | **Khai Phóng** | Phát huy tiềm năng cao nhất, thể hiện bản thân, tỏa sáng |

#### Action Items (below pyramid)

Hiển thị actions của layer đang chọn. Default: Nền Móng (base).

| Element | Detail |
|---------|--------|
| Layer label | "Nền Móng — 4 hành động" (count) |
| Action cards | Each card: number + title + 1-line description |
| Selected state | Click action card → Right column updates with WHAT & WHY |
| Completion | Checkbox on each action — user tracks progress |
| Progress | "2/4 hoàn thành" per layer |

### Right Column — WHAT & WHY

Updates when user clicks an action item on the left. 2 sections stacked.

#### WHAT — Đặc điểm bản thân

| Element | Detail |
|---------|--------|
| Heading | "Xuất phát từ đặc điểm nào?" |
| Trait description | 2-3 lines explaining which personal trait drives this action |
| Example | "Bạn có Canh Kim Nhật Chủ trong lửa đôi Ngọ — bản chất cứng rắn nhưng môi trường đòi hỏi linh hoạt" |

#### WHY — Hệ thống & giải nghĩa

| Element | Detail |
|---------|--------|
| Heading | "Từ hệ thống nào?" |
| System badge | Pill tag: "Tử Vi" / "BaZi" / "Human Design" etc. |
| System explanation | What this system says about the user — why it leads to this action |
| Link | "Xem chi tiết trong biểu đồ →" → links to S5 system reading (MAX) |

### Default State

- Pyramid: Nền Móng selected (base layer highlighted)
- Action list: Shows Nền Móng actions
- Right column: Shows WHAT & WHY for first action in list
- User clicks different layer → action list updates
- User clicks different action → right column updates

### Interaction Flow

```
Click pyramid layer (e.g. Nuôi Dưỡng)
  → Left: action list updates to Nuôi Dưỡng actions
  → Right: resets to first action's WHAT & WHY

Click action card
  → Right: WHAT & WHY updates for that specific action
  → Action card highlighted on left

Toggle checkbox
  → Action marked complete, progress counter updates
```

### States
- **Loading**: Skeleton pyramid + action cards
- **Layer selected**: Pyramid layer gold, others muted
- **Action selected**: Card highlighted, right column populated
- **No action selected**: Right column shows first action by default
- **Completion tracking**: Checkboxes persist across sessions
- **All complete in layer**: Layer on pyramid shows checkmark badge

### User Flow
```
/actions (default: Nền Móng layer)
  → View pyramid, click layer to switch
  → Click action → read WHAT & WHY on right
  → Check off completed actions
  → Click "Xem chi tiết trong biểu đồ" → /reading/system/[system] (MAX)
```

### Tier Restrictions

| Feature | FREE | PRO |
|---------|------|-----|
| Nền Móng actions | 2 actions visible | All actions |
| Nuôi Dưỡng actions | Locked | All actions |
| Khai Phóng actions | Locked | All actions |
| WHAT & WHY panel | Preview only | Full |
| System link (→ S5) | Locked | All systems |
| Completion tracking | Available | Available |

---

## Cross-Screen Navigation

```
Public:     / → /register → /onboarding → /dashboard
Auth base:  /dashboard ↔ /reading/system/* ↔ /forecast ↔ /actions ↔ /pricing ↔ /profile

Main paths:
  /dashboard                 ← S4: luận giải + actions + charts + Q&A
  /reading/system/[system]   ← S5: deep system reading (MAX)
  /forecast                  ← S9: Time Oracle (drill-down)
  /actions                   ← S10: Growth pyramid (Nền Móng → Nuôi Dưỡng → Khai Phóng)
  /pricing                   ← S7
  /profile                   ← S8
```

## Navigation Patterns

3 layout patterns across screens:

| Layout | Used in | Content |
|--------|---------|---------|
| `PublicLayout` | S1 (Landing) | Header: Logo left + "Đăng nhập" ghost + "Đăng ký" gold right. Footer |
| `AuthLayout` | S2 (Register/Login), S3 (Onboarding) | Logo centered, no nav, no footer. Route: `/auth`, `/auth?tab=login`, `/onboarding` |
| `AppLayout` | S4–S10 (all auth screens) | TopBar + SideNav (desktop) / hamburger (mobile). SideNav: Dashboard, Time Oracle, Actions, Settings |

Transition: Register success → onboarding (AuthLayout) → dashboard (AppLayout, 5-layer loading).

## Shared Components (All Screens)

| Component | Description |
|-----------|-------------|
| TopBar | Logo + nav, mobile hamburger |
| SideNav | Desktop left sidebar nav (collapsible on tablet) |
| MobileMenu | Hamburger dropdown nav for mobile browsers |
| TierBadge | FREE / PRO pill |
| TierGate | Blur overlay + upgrade CTA |
| LoadingSkeleton | Full-page and section variants |
| Toast | Success / Error notifications |
| ConfirmDialog | For destructive actions |

## Error & Empty States

| State | Screen(s) | Display |
|-------|-----------|---------|
| API failure (full) | All | Full-page: "Đã xảy ra lỗi. Vui lòng thử lại." + Retry button |
| API failure (section) | S4, S5, S9 | Section-level: "Không thể tải nội dung này." + Retry link, rest of page still visible |
| Q&A empty | S4, S5 | Placeholder: "Hỏi bất cứ điều gì về luận giải của bạn..." with example questions below input |
| S9 no data yet | S9 | "Dữ liệu đang được tạo. Vui lòng quay lại sau." (if charts not yet generated) |
| S10 no actions | S10 | "Hành động đang được tạo từ luận giải của bạn..." + skeleton |
| 404 Page | Any invalid route | "Trang bạn tìm không tồn tại." + CTA "Về trang chủ" → /dashboard or / |
| Offline | All | Top banner: "Bạn đang ngoại tuyến. Một số tính năng có thể không hoạt động." |
| Reading not ready | S4 (new user) | 5-layer loading animation. If stuck >30s: "Đang xử lý lâu hơn bình thường..." + contact link |
