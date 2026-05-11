---
description: Viết hoặc cập nhật PRD section cho một feature cụ thể
tier: execution
version: v1.0
owner: "@Director-Product"
calls:
  - /qg-check (Tier 3)
  - /flog (Tier 3)
called_by:
  - /build-feature (@Director-Product)
input: "Feature name + user story + acceptance criteria + priority"
output: "PRD section mới trong PRD-001_product-requirements.md"
---

# Workflow: /write-prd

> **Tier 2 — EXECUTION**
> Ai chạy: @Director-Product
> Khi nào: Cần document feature mới hoặc update existing feature spec

---

## Bước 1: Load Product Context

Đọc bắt buộc:
1. `02_Production/Product/PRD-001_product-requirements.md` — full PRD hiện tại
2. `01_Governance/Strategy/CEO-001_business-requirements.md` — strategic direction
3. `02_Production/Architecture/ARCH-001*.md` — tech constraints

Xác định:
- Feature này là MỚI hoàn toàn hay UPDATE section đã có?
- Nằm trong tier nào của product? (Free / Paid / Premium)
- Liên quan đến astrology framework nào? (Tử vi / Tứ trụ / Numerology / Tarot / Bát tự)

---

## Bước 2: Viết Feature Section theo cấu trúc chuẩn

Template PRD Feature Section:

```markdown
## Feature: [Tên Feature]

> **ID:** F-[###]
> **Priority:** P0 / P1 / P2
> **Tier:** Free / Paid / Premium
> **Framework:** [Tử vi / Tứ trụ / Numerology / Tarot / Bát tự / Cross-framework]
> **Sprint:** S##
> **Status:** Draft / Review / Approved / In Dev / Done

### 1. Overview

**Problem:** [Vấn đề user đang gặp — 1-2 câu]

**Solution:** [Feature giải quyết vấn đề như thế nào — 1-2 câu]

**User Story:**
> Với tư cách là [loại người dùng], tôi muốn [làm gì], để [đạt được gì].

### 2. Acceptance Criteria

| # | Criteria | Testable? |
|---|---------|---------|
| AC-1 | [Điều kiện rõ ràng, có thể test] | ✅ Yes |
| AC-2 | [Điều kiện rõ ràng] | ✅ Yes |
| AC-3 | [Điều kiện rõ ràng] | ✅ Yes |

> **Quy tắc viết AC:** Mỗi AC phải trả lời được "Làm sao biết feature này DONE?"
> Format: "Khi [user làm X], thì [hệ thống phản hồi Y]"

### 3. Screens & UX Flow

| Step | User Action | System Response | Screen |
|------|------------|----------------|--------|
| 1 | [User làm gì] | [App hiển thị gì] | [Tên screen] |
| 2 | ... | ... | ... |

### 4. Data Requirements

**Input từ user:**
- [Field 1]: [type, validation]
- [Field 2]: [type, validation]

**Output từ hệ thống:**
- [Output 1]: [mô tả]
- [Output 2]: [mô tả]

**Stored data (nếu có):**
- [Cần lưu gì vào DB?]

### 5. AI/Logic Requirements (nếu có)

**Prompt context:**
- [Thông tin nào cần đưa vào prompt?]

**Expected output format:**
- [Claude cần trả về format gì?]

**Accuracy requirement:**
- Target: [X]% accuracy
- Validation method: [Cách verify accuracy]

### 6. Edge Cases

| Case | Expected Behavior |
|------|-----------------|
| [User không nhập đủ info] | [Hiển thị validation message cụ thể] |
| [API timeout] | [Fallback behavior] |
| [Data không hợp lệ] | [...] |

### 7. Out of Scope (Sprint này)

- [Điều không làm trong sprint này — rõ ràng để tránh scope creep]

### 8. Dependencies

- **Blocks:** [Feature khác bị block nếu feature này chưa done]
- **Blocked by:** [Feature khác phải done trước]
- **Tech dependencies:** [API, library, external service]
```

---

## Bước 3: Review Astrology Accuracy (đặc thù 360Human)

Nếu feature liên quan đến astrology readings:

- [ ] Công thức tính toán có được tham chiếu từ nguồn uy tín không?
- [ ] Interpretation rules được expert validate chưa?
- [ ] Edge cases cho ngày sinh đặc biệt (giờ sinh không rõ, dương/âm lịch) đã handle?
- [ ] AI prompt có đủ context để cho ra accurate reading không?

---

## Bước 4: Self QG-check — Gọi /qg-check

```
/qg-check
Level: QG-1
Scope: PRD — Feature [Tên]
```

Checklist:
- [ ] Mọi AC có thể test được (không mơ hồ)?
- [ ] User story rõ loại người dùng và mục tiêu?
- [ ] Edge cases đã cover?
- [ ] Out of scope định nghĩa rõ ràng?
- [ ] Không conflict với features đã có trong PRD?
- [ ] Priority và Sprint ID đã gán?

---

## Bước 5: Cập nhật PRD + Gọi /flog

Thêm feature section vào file `02_Production/Product/PRD-001_product-requirements.md` tại đúng vị trí (theo priority order).

Cập nhật **PRD Changelog** ở cuối file PRD:
```markdown
| [Date] | F-### | [Tên Feature] | Added | [Sprint ID] |
```

```
/flog — PRD updated: Feature F-### [Tên] added to PRD-001.
```

---

## Output cam kết

- Feature section đầy đủ trong PRD-001
- ACs có thể test được
- PRD Changelog updated
- QG-1 passed

```
[QG-1] Tự kiểm:
- [ ] Mọi AC testable?
- [ ] Không mơ hồ, không nước đôi?
- [ ] Tech sẽ không cần hỏi lại khi đọc spec này?
- [ ] PRD Changelog updated?
```
