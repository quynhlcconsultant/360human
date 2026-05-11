---
title: "Clarifications Log"
id: "ARCH-004"
source: "CEO Q&A session 2026-03-15"
converted: "2026-03-15"
status: "active"
---

# Clarifications Log — 360Human

> Resolved: 2026-03-15 | Source: CEO (Winston) answers to 18 architecture questions
> Purpose: Single source of truth khi có mâu thuẫn giữa các documents

---

## 1. DATA & ACCURACY

| # | Question | Answer | Impact |
|---|---------|--------|--------|
| 1 | API Provider | **astrology-api.io** (KHÔNG phải AstroVisor). Chưa có API Key. Xem [ARCH-003](ARCH-003_api-integration-guide.md) | Đổi tên trong toàn bộ docs. **All 5 systems confirmed available** (CEO verified on demo page) |
| 2 | Knowledge Base 2000+ pages | Đang ở dạng **PDF cần digitize** | Thêm task digitize KB vào Phase 1. Timeline risk cao |
| 3 | Numerology | Dùng **Astrology API** luôn, không tính local | Giảm complexity, phụ thuộc API |

## 2. THỐNG NHẤT CÁC CON SỐ

| # | Question | Answer | Supersedes |
|---|---------|--------|------------|
| 4 | Word limits | **FREE=2,000w / PRO=10,000w / MAX=20,000w** | ARCH-001 ghi 80/500/1500 → SAI, đã sửa |
| 5 | Tier names | **FREE / PRO / MAX** | ARCH-001 ghi "20° / 180° / 360°" → đổi thành FREE/PRO/MAX |
| 6 | FREE topics | **2/10** (Tổng quan & Tình yêu) | Confirmed |
| 7 | Screen count | **8 screens** (theo PRD-001) — chưa chốt final | ARCH-001 ghi 11-14 → dùng PRD làm baseline |

## 3. PAYMENT & BUSINESS

| # | Question | Answer | Impact |
|---|---------|--------|--------|
| 8 | Payment method | **VietQR là ưu tiên** — MoMo/ZaloPay/Bank đều quét VietQR được | Simplify: 1 payment flow thay vì 3 |
| 9 | Subscription model | **One-time purchase** (không recurring) | Không cần auto-renewal logic, webhook đơn giản hơn |
| 10 | Pricing | **PRO = 199,000 VND, MAX = 499,000 VND** | Confirmed |

## 4. FRONTEND & DESIGN

| # | Question | Answer | Impact |
|---|---------|--------|--------|
| 11 | Figma/Design file | **Chưa có** — đang chuẩn bị xây wireframe/mockup | Frontend build dựa trên Co-Star vibe + UX writing guidelines |
| 12 | Co-Star reference | **Overall vibe only**: sạch, typography rõ, whitespace cao, KHÔNG cải lương phương Đông | Design direction rõ ràng |
| 13 | Charts visualization | **Check API trước** — nếu API render được thì dùng, nếu không thì frontend render | Decision pending sau khi test API |
| 14 | HTTP client | **Axios** (không dùng ky) | Confirmed |

## 5. TEAM & TIMELINE

| # | Question | Answer | Impact |
|---|---------|--------|--------|
| 15 | Team size | **1 fullstack developer** | 105 tasks / 1 người → cần ưu tiên ruthless, parallel work không khả thi |
| 16 | Checklist | **Cần build mới** (CEO-002 trống) | Tạo sprint tracker — xem [CEO-002](../0.%20CEO%20-%20Winston/CEO-002_project-checklist.md) |
| 17 | Launch date | **29/04/2026** (45 days from now) | ~6.5 weeks, cần cắt scope nếu cần |

## 6. TECHNICAL

| # | Question | Answer | Impact |
|---|---------|--------|--------|
| 18 | Database schema | Confirmed 5 tables: `users`, `profiles`, `chart_cache`, `subscriptions`, `payments` | Schema chi tiết đã được CEO provide — xem bên dưới |

### Confirmed Schema

```sql
-- users
id          UUID PK
email       VARCHAR UNIQUE
password_hash VARCHAR
tier        ENUM('FREE','PRO','MAX') DEFAULT 'FREE'
is_active   BOOLEAN DEFAULT true
created_at  TIMESTAMP
updated_at  TIMESTAMP

-- profiles
id          UUID PK
user_id     UUID FK → users.id
full_name   VARCHAR
birth_date  DATE
birth_time  TIME
birth_city  VARCHAR
latitude    FLOAT
longitude   FLOAT
timezone    VARCHAR
gender      ENUM('male','female')
is_primary  BOOLEAN DEFAULT true
created_at  TIMESTAMP
updated_at  TIMESTAMP

-- chart_cache
cache_key   VARCHAR PK  -- format: ${date}_${HHMM}_${lat}_${lon}_${gender}
profile_id  UUID FK → profiles.id
frameworks  ENUM('tuvi','numerology','human_design','bazi','vedic')
result_json JSONB       -- L1 raw data, lưu vĩnh viễn
l3_interpretation TEXT  -- L3 AI output
created_at  TIMESTAMP
updated_at  TIMESTAMP

-- subscriptions
id          UUID PK
user_id     UUID FK → users.id
tier        ENUM('FREE','PRO','MAX')
provider    VARCHAR DEFAULT 'vietqr'
provider_txn VARCHAR
started_at  TIMESTAMP
expires_at  TIMESTAMP  -- NULL = lifetime (one-time purchase)
status      ENUM('active','expired','cancelled')

-- payments
id          UUID PK
user_id     UUID FK → users.id
amount      DECIMAL
currency    VARCHAR DEFAULT 'VND'
status      ENUM('pending','completed','failed','refunded')
provider    VARCHAR DEFAULT 'vietqr'
provider_txn VARCHAR
created_at  TIMESTAMP
```

---

## Decision Matrix — Open Items

| Item | Options | Recommendation | Status |
|------|---------|---------------|--------|
| Human Design API | astrology-api.io `/human-design-system` | Confirmed available — test after API key | **RESOLVED** |
| Tử Vi API | astrology-api.io Chinese & Eastern | Confirmed available — test output format | **RESOLVED** |
| Chart rendering | a) API (10 credits) b) Recharts | Test API first, fallback Recharts | **OPEN** |
| KB digitization | PDF → JSON/YAML pipeline | Need to scope: how many pages per system? | **OPEN** |
