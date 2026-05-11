---
title: "Component Map — shadcn/ui → 360Human"
id: "FE-005"
updated: "2026-03-16"
status: "ready-for-review"
stack: "Next.js 15 / shadcn/ui / Tailwind v4"
---

# Component Map — shadcn/ui → 360Human

> Maps each shadcn/ui component to its 360Human usage.
> Install command per component. Customization notes per usage.

---

## Install Base Setup

```bash
npx shadcn@latest init
# Choose: TypeScript, style=default, baseColor=stone, CSS variables=yes

# Then add components as needed:
npx shadcn@latest add [component-name]
```

---

## Component Registry

### 1. Button
**shadcn component:** `button`
```bash
npx shadcn@latest add button
```

| Variant | Usage | Customization |
|---------|-------|---------------|
| `default` | Primary CTA ("Khám phá bản thân", "Tạo tài khoản") | `bg-gold text-white hover:bg-gold/90` |
| `outline` | Secondary actions ("Tìm hiểu thêm") | `border-border text-charcoal` |
| `ghost` | Nav buttons, back links | `text-charcoal hover:bg-sand` |
| `destructive` | Delete account | Default red — keep |
| `link` | Inline text links ("Quên mật khẩu?") | Default — keep |

Sizes used: `default` (48px height), `sm` (36px), `lg` (56px — hero CTA only)

---

### 2. Input
**shadcn component:** `input`
```bash
npx shadcn@latest add input
```

| Usage | Notes |
|-------|-------|
| Email field | `type="email"` |
| Password field | `type="password"` + show/hide toggle (Eye icon from Lucide) |
| City autocomplete | Pair with `Combobox` — see item 9 |
| Name input | Standard text |
| Date fields (DD/MM/YYYY) | 3 separate `Input` components, narrow width |

Customization:
```css
/* Override border color in globals.css */
.input {
  border-color: var(--color-border);
  background: var(--color-warm-white);
}
.input:focus {
  border-color: var(--color-gold);
  ring-color: var(--color-gold);
}
```

---

### 3. Card
**shadcn component:** `card`
```bash
npx shadcn@latest add card
```

| Usage | Variant |
|-------|---------|
| Dashboard topic cards | `Card` + `CardHeader` + `CardContent` |
| Profile summary card | `Card` + `CardContent` |
| Pricing tier cards | `Card` with conditional `border-gold` / `border-sage` |
| System key facts | `Card` with compact padding |

Topic Card with lock overlay:
```tsx
<Card className="relative overflow-hidden">
  <CardHeader>
    <div className="flex items-center gap-3">
      <TopicIcon />
      <CardTitle>{topic.title}</CardTitle>
    </div>
  </CardHeader>
  <CardContent>{topic.teaser}</CardContent>
  {isLocked && <TierGate tier={requiredTier} />}
</Card>
```

---

### 4. Tabs
**shadcn component:** `tabs`
```bash
npx shadcn@latest add tabs
```

| Usage | Notes |
|-------|-------|
| Register / Login switch | `Tabs` with 2 `TabsTrigger` |
| System Reading (5 systems) | `Tabs` horizontal scroll on mobile |
| Profile sections | `Tabs` vertical on desktop |

System Reading tabs:
```tsx
<Tabs defaultValue="tu-vi">
  <TabsList className="overflow-x-auto flex-nowrap">
    <TabsTrigger value="tu-vi">Tử Vi</TabsTrigger>
    <TabsTrigger value="bazi">BaZi</TabsTrigger>
    <TabsTrigger value="hd">Human Design</TabsTrigger>
    <TabsTrigger value="numerology">Số học</TabsTrigger>
    <TabsTrigger value="vedic">Vedic</TabsTrigger>
  </TabsList>
  {/* TabsContent per system */}
</Tabs>
```

---

### 5. Badge
**shadcn component:** `badge`
```bash
npx shadcn@latest add badge
```

| Usage | Variant + Style |
|-------|----------------|
| Tier badge (FREE) | `variant="secondary"` — `bg-sand text-charcoal border-border` |
| Tier badge (PRO) | Custom — `bg-gold-bg text-gold border-gold` |
| System source tags | Small pills per system — each with distinct muted color |
| "Mới" / New labels | `variant="default"` with gold bg |

```tsx
const tierBadgeStyles = {
  FREE: "bg-sand text-charcoal border-border",
  PRO: "bg-gold-bg text-gold border-gold",
}

<Badge className={cn("border", tierBadgeStyles[tier])}>
  {tier}
</Badge>
```

---

### 6. Progress
**shadcn component:** `progress`
```bash
npx shadcn@latest add progress
```

| Usage | Notes |
|-------|-------|
| Onboarding wizard progress bar | `value={(step/5) * 100}` — color: gold |

```tsx
<Progress
  value={(currentStep / totalSteps) * 100}
  className="h-1 bg-sand [&>div]:bg-gold"
/>
```

---

### 7. Dialog
**shadcn component:** `dialog`
```bash
npx shadcn@latest add dialog
```

| Usage | Notes |
|-------|-------|
| Delete account confirm | `AlertDialog` preferred — see item 8 |
| Cancel subscription confirm | `AlertDialog` |
| Chart detail expand | `Dialog` for chart zoom |

---

### 8. AlertDialog
**shadcn component:** `alert-dialog`
```bash
npx shadcn@latest add alert-dialog
```

| Usage | Notes |
|-------|-------|
| Delete account | "Bạn có chắc chắn? Hành động này không thể hoàn tác." |
| Destructive confirmations | Standard pattern |

```tsx
<AlertDialog>
  <AlertDialogTrigger asChild>
    <Button variant="ghost" className="text-error">Xóa tài khoản</Button>
  </AlertDialogTrigger>
  <AlertDialogContent>
    <AlertDialogHeader>
      <AlertDialogTitle>Xác nhận xóa tài khoản</AlertDialogTitle>
      <AlertDialogDescription>
        Tất cả dữ liệu của bạn sẽ bị xóa vĩnh viễn. Hành động này không thể hoàn tác.
      </AlertDialogDescription>
    </AlertDialogHeader>
    <AlertDialogFooter>
      <AlertDialogCancel>Hủy</AlertDialogCancel>
      <AlertDialogAction className="bg-error">Xóa tài khoản</AlertDialogAction>
    </AlertDialogFooter>
  </AlertDialogContent>
</AlertDialog>
```

---

### 9. Combobox (Command + Popover)
**shadcn component:** `command` + `popover`
```bash
npx shadcn@latest add command popover
```

| Usage | Notes |
|-------|-------|
| City search (onboarding step 3) | Searchable list, Vietnam cities prioritized |
| Fallback: plain Input | If city list API not ready in Sprint 0 |

---

### 10. Toast (Sonner)
**shadcn component:** `sonner`
```bash
npx shadcn@latest add sonner
```

| Usage | Toast type |
|-------|-----------|
| Save success | Success (green) |
| API error | Error (red) |
| Upgrade success | Custom gold toast |
| Password changed | Success |

```tsx
// In layout.tsx
import { Toaster } from "@/components/ui/sonner"
<Toaster position="bottom-center" richColors />

// Usage
import { toast } from "sonner"
toast.success("Đã lưu thành công")
toast.error("Có lỗi xảy ra. Vui lòng thử lại.")
```

---

### 11. Skeleton
**shadcn component:** `skeleton`
```bash
npx shadcn@latest add skeleton
```

| Usage | Notes |
|-------|-------|
| Topic cards loading | 10 skeleton cards, same dimensions |
| Reading content loading | 3-4 paragraph-width skeletons |
| Chart placeholder | Rectangular skeleton with aspect ratio |

```tsx
// Topic card skeleton
function TopicCardSkeleton() {
  return (
    <div className="p-4 rounded-lg border border-border">
      <Skeleton className="h-5 w-3/4 mb-2 bg-sand" />
      <Skeleton className="h-4 w-full bg-sand" />
      <Skeleton className="h-4 w-2/3 bg-sand" />
    </div>
  )
}
```

---

### 12. Separator
**shadcn component:** `separator`
```bash
npx shadcn@latest add separator
```

| Usage | Notes |
|-------|-------|
| Section dividers in reading content | `className="bg-border"` |
| "hoặc" divider on login page | Horizontal with text |
| Profile section separators | Between profile / password / danger zone |

---

### 13. Avatar
**shadcn component:** `avatar`
```bash
npx shadcn@latest add avatar
```

| Usage | Notes |
|-------|-------|
| Profile page initials circle | No image — initials fallback only |
| Testimonial on landing | If added |

```tsx
<Avatar className="h-16 w-16">
  <AvatarFallback className="bg-gold-bg text-gold text-xl font-semibold">
    {initials}
  </AvatarFallback>
</Avatar>
```

---

### 14. ScrollArea
**shadcn component:** `scroll-area`
```bash
npx shadcn@latest add scroll-area
```

| Usage | Notes |
|-------|-------|
| System tabs (mobile horizontal scroll) | `ScrollArea` + `orientation="horizontal"` |
| Related topics carousel | Horizontal scroll |

---

### 15. Form (react-hook-form + zod)
**shadcn component:** `form`
```bash
npx shadcn@latest add form
# Also: npm install react-hook-form zod @hookform/resolvers
```

| Usage | Schema |
|-------|--------|
| Register form | `z.object({ email, password, confirmPassword })` |
| Login form | `z.object({ email, password })` |
| Change password form | `z.object({ current, new: min(8), confirm })` |
| Onboarding (each step) | Per-step zod schema |

---

## Custom 360Human Components (Not from shadcn)

These need to be built from scratch:

| Component | Description | Used in |
|-----------|-------------|---------|
| `TierGate` | Blur overlay + upgrade CTA for locked content | S4, S5, S9, S10 |
| `TopicCard` | Card with icon + title + teaser + optional lock | S4 Dashboard |
| `InlineActions` | Actions block at bottom of each accordion topic — numbered list + system badges | S4 Left Col |
| `SystemIcon` | 5 custom SVG icons per system | Dashboard, S5 |
| `ReadingSection` | Section with heading + body + source footnote | S4 Col 1 |
| `ActionItem` | Numbered action with label, body, step list | S4 Col 2 |
| `ChartPlaceholder` | System-specific chart skeleton/visualization | S5 |
| `TierCard` | Pricing tier card with features list | S7 |
| `SiteNav` | Responsive header + sidebar navigation | All auth screens |
| `TimelineBar` | Horizontal timeline with phase segments + gold current marker | S9 Layer 1 |
| `MonthGrid` | 12-month card grid (3x4 mobile), clickable months | S9 Layer 2 |
| `WeeklyPanel` | Expandable week summary: range, energy, themes | S9 Layer 3 |
| `DrillBreadcrumb` | Multi-level breadcrumb: Cuộc đời > Year > Month | S9 |
| `PyramidVisual` | 3-layer triangle SVG, clickable layers, gold highlight | S10 |
| `GrowthActionCard` | Action card with checkbox + source badge + click → WHAT/WHY | S10 |
| `TraitPanel` | WHAT & WHY stacked panels — trait description + system badge | S10 |
| `SystemLoadingLayers` | 5 stacked layers, gray → gold transition on load complete | S4 loading |
| `ReadingProgressBar` | "X/10 chủ đề" with FREE upsell message | S4 |
| `QAInput` | Text input + streaming response + counter display | S4, S5 |
| `ErrorState` | Full-page or section-level error with retry button | All screens |
| `ProfileSwitcher` | Profile list + "Thêm hồ sơ mới" button | S8 |

---

## TierGate Component Spec

```tsx
interface TierGateProps {
  currentTier: "FREE" | "PRO"
}

// Renders blur overlay + CTA if user doesn't have required tier
function TierGate({ currentTier }: TierGateProps) {
  if (currentTier === "PRO") return null

  return (
    <div className="absolute inset-0 backdrop-blur-sm bg-cream/60 flex flex-col items-center justify-center gap-3 rounded-lg">
      <LockIcon className="h-6 w-6 text-muted" />
      <p className="text-sm text-charcoal text-center px-4">
        Mở khóa với gói PRO
      </p>
      <Button size="sm" asChild>
        <Link href="/pricing">Nâng cấp</Link>
      </Button>
    </div>
  )
}
```

---

## Component Priority for Sprint 0

Install these immediately:

```bash
npx shadcn@latest add button input card tabs badge progress dialog alert-dialog form skeleton separator avatar sonner accordion checkbox collapsible tooltip breadcrumb
npm install react-hook-form zod @hookform/resolvers
```

Build custom components in this order:
1. `SiteNav` + `ErrorState` — needed for all screens
2. `TierGate` — needed for Dashboard + S5 + S9 + S10
3. `SystemLoadingLayers` — needed for onboarding→dashboard transition
4. `ReadingProgressBar` — needed for Dashboard
5. `ReadingSection` + `InlineActions` — needed for S4 accordion topics
6. `QAInput` — needed for S4 + S5
7. `ChartPlaceholder` + `SystemIcon` — needed for S5
8. `TimelineBar` + `MonthGrid` + `WeeklyPanel` + `DrillBreadcrumb` — needed for S9
9. `PyramidVisual` + `GrowthActionCard` + `TraitPanel` — needed for S10
10. `TierCard` — needed for S7
11. `ProfileSwitcher` — needed for S8
