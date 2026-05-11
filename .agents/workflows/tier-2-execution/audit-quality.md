---
description: Kiểm tra chất lượng output — content, code, hoặc design theo tiêu chuẩn 360Human
tier: execution
version: v1.0
owner: "@Specialist-QA"
calls:
  - /qg-check (Tier 3)
  - /flog (Tier 3)
called_by:
  - /launch-campaign (@Director-Growth)
  - /build-feature (@Director-Product)
  - /build-sprint (@Director-Tech)
input: "Scope audit (content/code/design) + files cần review + tiêu chuẩn áp dụng"
output: "QA Report với PASS/FAIL + danh sách issues cụ thể + recommendations"
---

# Workflow: /audit-quality

> **Tier 2 — EXECUTION**
> Ai chạy: @Specialist-QA (hoặc Director cùng level — peer review)
> Khi nào: Được gọi khi cần QG-2 Peer Review

---

## Bước 1: Xác định Scope Audit

```
[TOL] Audit Scope:
→ Type: Content / Code / Design / All
→ Files cần review: [list cụ thể]
→ Context: Sprint S## / Feature F-### / Campaign [Tên]
→ Tiêu chuẩn: [xem Bước 2-4 tương ứng]
→ Ai request: [@Director-X]
→ Deadline: [date nếu có]
```

---

## Bước 2: Audit Content (nếu scope = content)

### Checklist Content 360Human:

**Brand Voice:**
- [ ] Tone: Thân thiện, am hiểu, không phán xét (KHÔNG kiểu "bạn sinh ra đã thất bại")
- [ ] Giọng điệu phù hợp gen Z Việt (gần gũi nhưng professional)
- [ ] KHÔNG dùng từ nặng nề, mê tín, dọa nạt
- [ ] KHÔNG hứa hẹn quá mức ("sẽ giàu có", "sẽ gặp người yêu")

**Accuracy (quan trọng nhất với 360Human):**
- [ ] Mọi claims về astrology có source hoặc expert-validated?
- [ ] KHÔNG tự ý "sáng tạo" interpretation không có cơ sở
- [ ] Số liệu, dates đúng không?
- [ ] Tên frameworks viết đúng không? (Tử vi, Tứ trụ, Nhân số học...)

**Vietnamese Language:**
- [ ] Câu văn tự nhiên, không máy móc (không phải dịch từ tiếng Anh)
- [ ] Từ xưng hô phù hợp (bạn/mình — tránh "quý khách")
- [ ] Không lỗi chính tả, dấu câu

**Content Structure:**
- [ ] Hook (3 giây đầu) đủ mạnh không?
- [ ] CTA rõ ràng, 1 action duy nhất?
- [ ] Không quá dài (caption < 150 từ, video < 60s cho TikTok)

---

## Bước 3: Audit Code (nếu scope = code)

### Checklist Code 360Human:

**Security (Critical):**
- [ ] Không có hardcoded secrets / API keys
- [ ] SQL injection: dùng ORM / parameterized queries
- [ ] Input validation ở tất cả API endpoints
- [ ] Auth check đúng (JWT verification)
- [ ] CORS config đúng (không wildcard `*` ở production)

**Code Quality:**
- [ ] Naming conventions đúng (snake_case Python, camelCase/PascalCase TS)
- [ ] Functions không quá dài (> 50 dòng → xem xét tách)
- [ ] Không có TODO comments chưa resolve
- [ ] Logging đủ cho debugging (không log sensitive data)
- [ ] Error messages user-friendly (tiếng Việt)

**Tests:**
- [ ] Unit tests coverage cho happy path + error cases?
- [ ] Tests pass local trước khi PR?

**Performance:**
- [ ] Không có N+1 query (eager load relationships)
- [ ] API response time < 2s (chart generation < 5s có AI)
- [ ] Images optimized (Next.js `<Image>` component)

---

## Bước 4: Audit Design (nếu scope = design)

### Checklist Design 360Human:

**Design System Compliance:**
- [ ] Colors đúng FE-001 tokens (không dùng custom hex ngoài system)
- [ ] Typography đúng scale (H1-H3, body, caption)
- [ ] Spacing đúng (8px grid — multiples of 8)
- [ ] Border radius consistent (`rounded-lg` = 8px standard)

**UX:**
- [ ] User flow không có dead ends?
- [ ] Error states có đủ không?
- [ ] Loading states dễ phân biệt với content?
- [ ] Touch targets đủ lớn (min 44px mobile)?

**Accessibility basic:**
- [ ] Color contrast đủ (≥ 4.5:1 text, ≥ 3:1 UI elements)?
- [ ] Không chỉ dùng màu để truyền thông tin (có icon/text kèm)?

---

## Bước 5: Tổng hợp QA Report

Format report:

```markdown
# QA Report — [Scope] — [Sprint/Feature/Campaign]

> **Date:** YYYY-MM-DD
> **Auditor:** @Specialist-QA
> **Requested by:** @Director-X

## Verdict: ✅ PASS / ❌ FAIL / ⚠️ PASS WITH CONDITIONS

## Summary
[2-3 câu tổng quan chất lượng]

## Issues Found

### 🔴 Critical (phải fix trước khi ship)
| # | File/Content | Issue | Recommendation |
|---|-------------|-------|----------------|
| 1 | [file] | [mô tả issue cụ thể] | [fix cụ thể] |

### 🟡 Major (nên fix)
| # | File/Content | Issue | Recommendation |
|---|-------------|-------|----------------|

### 🟢 Minor (nice-to-fix)
| # | File/Content | Issue | Recommendation |
|---|-------------|-------|----------------|

## What's Good
- [Điểm tốt 1]
- [Điểm tốt 2]

## Next Steps
- [ ] Fix critical issues: @[owner] — by [date]
- [ ] Re-audit after fixes: @Specialist-QA
```

---

## Bước 6: Gửi Report + Gọi /flog

Gửi report cho @Director người yêu cầu audit.

**Nếu FAIL:** Tag cụ thể issues, ai fix, deadline.
**Nếu PASS:** Confirm QG-2 passed, sẵn sàng cho bước tiếp.

```
/flog — QA Audit done: [Scope] [PASS/FAIL]. Report: [path].
```

---

## Output cam kết

- QA Report đầy đủ với issues cụ thể (không chung chung)
- Verdict rõ ràng PASS / FAIL / CONDITIONAL
- Nếu FAIL: issues có priority + owner + deadline
- @Director đã nhận report

```
[QG-1] Tự kiểm:
- [ ] Review tất cả files trong scope?
- [ ] Issues mô tả đủ cụ thể để fix được?
- [ ] Verdict dứt khoát (không mơ hồ)?
- [ ] "What's Good" section có (không chỉ criticize)?
```
