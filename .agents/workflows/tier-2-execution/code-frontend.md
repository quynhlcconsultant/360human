---
description: Viết code frontend Next.js — screen, component, UI, integrate API
tier: execution
version: v1.0
owner: "@Specialist-Frontend"
calls:
  - /qg-check (Tier 3)
  - /flog (Tier 3)
called_by:
  - /build-sprint (@Director-Tech)
input: "Screen spec (FE-###.md) + component cần làm + API endpoint đã có"
output: "React/Next.js component files hoàn chỉnh + responsive + follow design system"
---

# Workflow: /code-frontend

> **Tier 2 — EXECUTION**
> Ai chạy: @Specialist-Frontend (hoặc @Director-Tech)
> Khi nào: Được gọi từ /build-sprint để implement frontend task

---

## Bước 1: Load Frontend Context

Đọc bắt buộc:
1. `02_Production/Design/FE-001_design-system.md` — colors, typography, spacing
2. `02_Production/Design/FE-002_component-library.md` — existing components (KHÔNG reinvent wheel)
3. `02_Production/Design/FE-[###]_[screen-name]-spec.md` — spec screen cụ thể cần làm
4. Scan `02_Production/Frontend/` — hiểu existing file structure

Tech stack 360Human frontend (KHÔNG tự ý thay đổi):
- **Framework:** Next.js 14 App Router
- **Styling:** Tailwind CSS
- **State:** Zustand (global), useState (local)
- **Data fetching:** TanStack Query (React Query)
- **UI Components:** shadcn/ui (base), custom trên top
- **Auth:** NextAuth.js / JWT stored in httpOnly cookie
- **Deploy:** Vercel

---

## Bước 2: Phân tích Task

```
[TOL] Frontend Task Analysis:
→ Task: [Tên screen/component]
→ Type: New page / New component / Modify existing / API integration
→ Files cần tạo: [list]
→ Files cần sửa: [list]
→ APIs cần call: [list endpoints]
→ State management: [local useState / global Zustand]
→ Responsive breakpoints: Mobile-first? (default: YES)
→ Confidence: X%
```

---

## Bước 3: Viết Code

### Conventions bắt buộc:

**File structure Next.js App Router:**
```
02_Production/Frontend/
├── app/
│   ├── (auth)/          ← Auth routes
│   ├── (dashboard)/     ← Protected routes
│   ├── api/             ← API routes (Next.js)
│   └── layout.tsx       ← Root layout
├── components/
│   ├── ui/              ← shadcn/ui base
│   ├── shared/          ← Shared components
│   └── [feature]/       ← Feature-specific
├── lib/                 ← Utils, helpers, API clients
├── store/               ← Zustand stores
└── types/               ← TypeScript types
```

**Naming conventions:**
- Components: `PascalCase.tsx` (UserProfile.tsx, AstrologyChart.tsx)
- Pages: `page.tsx` trong folder (Next.js convention)
- Hooks: `use[Name].ts` (useUserProfile.ts)
- Utils: `camelCase.ts` (formatDate.ts)
- Types: `PascalCase` với suffix (UserProfile**Type**, ApiResponse**Type**)

**Component structure chuẩn:**
```tsx
// components/feature/ComponentName.tsx
"use client"; // chỉ khi cần client-side

import { useState } from "react";
import { cn } from "@/lib/utils"; // shadcn utility

interface ComponentNameProps {
  // TypeScript props — LUÔN define interface
  userId: string;
  className?: string;
}

export function ComponentName({ userId, className }: ComponentNameProps) {
  // 1. Hooks
  // 2. Derived state
  // 3. Handlers
  // 4. JSX return

  return (
    <div className={cn("base-classes", className)}>
      {/* content */}
    </div>
  );
}
```

**Design system — 360Human colors (từ FE-001):**
```tsx
// Dùng Tailwind classes theo design system:
// Primary: bg-violet-600, text-violet-600
// Secondary: bg-amber-500
// Background: bg-slate-950 (dark mode default)
// Text: text-white, text-slate-300
// Card: bg-slate-900 border border-slate-800
```

**API calls với React Query:**
```tsx
import { useQuery, useMutation } from "@tanstack/react-query";

// Fetch data:
const { data, isLoading, error } = useQuery({
  queryKey: ["user-profile", userId],
  queryFn: () => fetchUserProfile(userId),
});

// Mutations:
const { mutate, isPending } = useMutation({
  mutationFn: createChart,
  onSuccess: () => { /* invalidate cache, redirect */ },
  onError: (err) => { /* show toast */ },
});
```

**Loading & Error states (bắt buộc):**
```tsx
if (isLoading) return <LoadingSkeleton />;
if (error) return <ErrorState message={error.message} />;
```

---

## Bước 4: Responsive Design

Mobile-first là default. Kiểm tra ở các breakpoints:

| Breakpoint | Tailwind | Thiết bị |
|-----------|---------|---------|
| Base | (none) | Mobile 375px |
| sm | `sm:` | 640px |
| md | `md:` | 768px (tablet) |
| lg | `lg:` | 1024px (desktop) |

Pattern:
```tsx
// Mobile stacked → Desktop side-by-side
<div className="flex flex-col md:flex-row gap-4">
```

---

## Bước 5: Accessibility basics

```tsx
// Images always have alt
<Image src={src} alt="Meaningful description" />

// Buttons have clear labels
<button aria-label="Xem chi tiết biểu đồ tử vi">...</button>

// Form inputs có label
<label htmlFor="birthdate">Ngày sinh</label>
<input id="birthdate" type="date" />
```

---

## Bước 6: Self QG-check — Gọi /qg-check

```
/qg-check
Level: QG-1
Scope: Frontend task — [tên screen/component]
```

Checklist:
- [ ] TypeScript — không có `any` type?
- [ ] Responsive đúng ở mobile?
- [ ] Loading + Error states có đủ?
- [ ] Follow design system (colors, spacing, typography)?
- [ ] Không có hardcoded strings tiếng Anh (dùng Vietnamese)?
- [ ] `"use client"` chỉ dùng khi thực sự cần?
- [ ] API calls dùng React Query (không fetch trực tiếp trong component)?

---

## Bước 7: Báo cáo lên @Director-Tech + Gọi /flog

```
[CODE-FRONTEND DONE] [Tên screen/component]
✅ Files created/modified: [list]
✅ Responsive: Mobile ✓ Tablet ✓ Desktop ✓
✅ Screens covered: [list]
⚠️ Notes: [nếu có deviation từ spec]
```

```
/flog — Frontend [Tên] done. Files: [list].
```

---

## Output cam kết

- Component/page files tại đúng vị trí
- TypeScript đúng (không any)
- Responsive (mobile-first)
- Follow design system
- Loading/error states
- QG-1 passed

```
[QG-1] Tự kiểm:
- [ ] Render không có console error?
- [ ] Mobile layout đúng spec?
- [ ] Design system colors đúng?
- [ ] TypeScript clean?
- [ ] Loading/error handled?
```
