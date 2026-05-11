---
description: Thiết kế spec cho 1 screen — layout, components, states, interactions
tier: execution
version: v1.0
owner: "@Specialist-Designer"
calls:
  - /qg-check (Tier 3)
  - /flog (Tier 3)
called_by:
  - /build-feature (@Director-Product)
input: "PRD Feature section + target screen name + existing design system reference"
output: "Design spec file FE-[###]_[tên-screen]-spec.md trong 02_Production/Design/"
---

# Workflow: /design-screen

> **Tier 2 — EXECUTION**
> Ai chạy: @Specialist-Designer (hoặc @Director-Product)
> Khi nào: Cần spec design chi tiết cho screen/component mới

---

## Bước 1: Load Design Context

Đọc bắt buộc:
1. `02_Production/Design/FE-001_design-system.md` — tokens, colors, typography, spacing
2. `02_Production/Design/FE-002_component-library.md` — existing components
3. `02_Production/Design/FE-003_screen-map.md` — toàn bộ screen hiện có (tránh duplicate)
4. PRD Feature section liên quan (từ PRD-001)

**Xác định:**
- Screen này NEW hay UPDATE existing?
- Entry point? (User đến screen này từ đâu?)
- Exit points? (User có thể đi đâu từ screen này?)
- User state? (Logged in / Logged out / First time / Returning)

---

## Bước 2: Viết Design Spec

Tên file: `FE-[###]_[screen-name]-spec.md`

Template:

```markdown
# Screen Spec: [Tên Screen]

> **File ID:** FE-[###]
> **Feature:** F-[###] — [Tên Feature]
> **Sprint:** S##
> **Status:** Draft / Review / Approved
> **Entry from:** [Screen trước]
> **Exit to:** [Screens có thể đi tiếp]

---

## 1. Screen Overview

**Purpose:** [1 câu — screen này làm gì cho user]

**User type:** Guest / Free user / Paid user / All

**Responsive:** Mobile (primary) → Tablet → Desktop

---

## 2. Layout Structure

Mô tả layout dạng text wireframe:

```
┌─────────────────────────────────┐
│ [Header / Nav Bar]              │  Height: 60px, bg: slate-900
├─────────────────────────────────┤
│                                 │
│ [Hero / Title Area]             │  Padding: 24px
│ Title text (H1)                 │  Font: 28px bold
│ Subtitle text                   │  Font: 16px, slate-400
│                                 │
├─────────────────────────────────┤
│ [Main Content]                  │
│                                 │
│ ┌──────────┐  ┌──────────┐     │
│ │ Card 1   │  │ Card 2   │     │  2-col on md+, 1-col mobile
│ └──────────┘  └──────────┘     │
│                                 │
├─────────────────────────────────┤
│ [CTA Section]                   │
│ [Primary Button]                │  violet-600, full-width mobile
└─────────────────────────────────┘
```

---

## 3. Components Inventory

| Component | From Library? | Props | Notes |
|-----------|-------------|-------|-------|
| `<Navbar />` | ✅ FE-002 | `variant="dashboard"` | |
| `<AstrologyCard />` | ❌ New | `sign, date, isLocked` | Cần tạo mới |
| `<Button />` | ✅ FE-002 | `variant="primary"` | |
| `<LoadingSkeleton />` | ✅ FE-002 | `height="200px"` | |

> Components đã có trong FE-002 → REUSE, KHÔNG tạo lại.

---

## 4. States cần handle

| State | Trigger | UI hiển thị |
|-------|---------|-------------|
| Loading | Dữ liệu chưa load xong | Skeleton loader thay cho content |
| Empty | User chưa nhập data | Illustration + CTA "Bắt đầu" |
| Error | API fail | Error message + Retry button |
| Locked | Content cần paid tier | Blur overlay + Upgrade CTA |
| Success | Action hoàn thành | Toast notification |

---

## 5. Color & Typography

Áp dụng từ FE-001 design system:

| Element | Class Tailwind | Hex |
|---------|---------------|-----|
| Background | `bg-slate-950` | #020617 |
| Card background | `bg-slate-900` | #0f172a |
| Border | `border-slate-800` | #1e293b |
| Primary text | `text-white` | #ffffff |
| Secondary text | `text-slate-400` | #94a3b8 |
| Accent / CTA | `bg-violet-600` | #7c3aed |
| Gold accent | `text-amber-500` | #f59e0b |

Typography:
- H1: `text-3xl font-bold` (30px)
- H2: `text-2xl font-semibold` (24px)
- Body: `text-base` (16px)
- Caption: `text-sm text-slate-400` (14px)

---

## 6. Interactions & Animations

| Interaction | Animation | Duration |
|------------|----------|----------|
| Button hover | Scale 1.02 + brightness | 150ms |
| Card hover | Border glow violet | 200ms |
| Page transition | Fade in | 200ms |
| Loading → Content | Skeleton fade out | 300ms |

```tsx
// Tailwind transition pattern:
className="transition-all duration-200 hover:scale-[1.02]"
```

---

## 7. Mobile-specific considerations

- Touch targets: minimum 44x44px (buttons, links)
- Bottom navigation bar (nếu có): luôn visible, không bị keyboard che
- Swipe gestures: [mô tả nếu có]
- Safe area: `pb-safe` (iOS notch)

---

## 8. Copy (Text content)

| Element | Vietnamese text |
|---------|---------------|
| Page title | "[Tên trang]" |
| CTA primary | "[Nút chính]" |
| Empty state | "[Thông báo khi trống]" |
| Error message | "Đã có lỗi xảy ra. Vui lòng thử lại." |
| Loading | "Đang tải..." |

---

## 9. Navigation Flow

```
[Màn hình trước] ──tap button──► [Screen này] ──tap X──► [Màn hình sau]
                                       │
                                  ──swipe back──► [Trở lại]
```
```

---

## Bước 3: Self QG-check — Gọi /qg-check

```
/qg-check
Level: QG-1
Scope: Design spec — FE-### [Tên Screen]
```

Checklist:
- [ ] Tất cả states đã define (loading, empty, error, locked, success)?
- [ ] Components reuse từ FE-002 tối đa?
- [ ] Colors đúng theo FE-001 token?
- [ ] Mobile layout là primary?
- [ ] Copy tiếng Việt đã có đầy đủ?
- [ ] Navigation flow rõ ràng?
- [ ] Developer có thể implement mà không cần hỏi thêm?

---

## Bước 4: Cập nhật Screen Map + Gọi /flog

Thêm entry vào `02_Production/Design/FE-003_screen-map.md`:

```markdown
| FE-### | [Tên Screen] | F-### | S## | Draft/Approved |
```

```
/flog — Design spec FE-### [Tên Screen] created.
```

---

## Output cam kết

- File `FE-[###]_[screen-name]-spec.md` đầy đủ trong `02_Production/Design/`
- Screen Map (FE-003) updated
- QG-1 passed
- Developer không cần hỏi lại khi đọc spec

```
[QG-1] Tự kiểm:
- [ ] Layout wireframe có?
- [ ] Tất cả states covered?
- [ ] Components list rõ (reuse vs new)?
- [ ] Colors/typography đúng token?
- [ ] Mobile-first?
```
