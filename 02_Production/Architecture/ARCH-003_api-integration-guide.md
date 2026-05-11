---
title: "API Integration Guide"
id: "ARCH-003"
source: "generated from astrology-api.io research"
converted: "2026-03-15"
status: "active"
---

# Astrology API Integration Guide

> Provider: **astrology-api.io** (NOT AstroVisor)
> Status: API Key chưa có — cần đăng ký

## 1. API Overview

| Item | Detail |
|------|--------|
| Provider | https://astrology-api.io |
| Auth | API Key (header) |
| Format | REST JSON |
| Rate Limit | 50 req/min (adjustable), 5-10 concurrent |
| Docs | https://astrology-api.io/demo (Swagger/ReDoc) |
| SDKs | Python, JS/Node, PHP, Go, Ruby, Java, C# |

## 2. Pricing — Recommended Plan

| Plan | Cost/month | Credits/month | House Systems | AI Interpret | Notes |
|------|-----------|---------------|---------------|-------------|-------|
| Free | $0 | 50 | 5 | No | Dev/test only |
| Pro | $11 | 1,000 | 12 | No | Early MVP |
| Pro Plus | $21 | 7,000 | 18 | Yes | **MVP Launch** |
| Ultra | $37 | 55,000 | 23 | Advanced | **Scale phase** |
| Business | $99 | 220,000 | 23 | Custom fine-tune | Growth |
| Enterprise | $399+ | Unlimited | 23 | Full | Enterprise |

### Credit Cost per Feature
| Feature | Credits |
|---------|---------|
| Standard endpoint (natal, transit, etc.) | 1 |
| Horary Astrology | 2 |
| Kabbalah Numerology | 2 |
| Astrocartography | 5 |
| **Chart Image Rendering** | **10** |
| PDF Reports | 35 |
| Palm Reading | 100 |

### 360Human Cost Estimate
- Per user reading: ~5-7 credits (5 systems x 1 credit + chart rendering)
- MVP (Pro Plus @ $21): ~7,000 credits = **~1,000 users/month**
- Scale (Ultra @ $37): ~55,000 credits = **~7,800 users/month**
- Growth (Business @ $99): ~220,000 credits = **~31,400 users/month**
- Target 50,000 PU/month → **Enterprise plan needed ($399+)**

## 3. Systems Mapping for 360Human

| 360Human System | Astrology API Coverage | Endpoint Type | Status |
|-------------------|----------------------|---------------|--------|
| **Tử Vi (Zi Wei Dou Shu)** | Chinese & Eastern | Chinese endpoints | Available (CEO confirmed via demo) |
| **Numerology** | Numerology & Number Analysis | Numerology endpoints | Available |
| **Human Design** | Human Design System | `/human-design-system` tag | Available (CEO confirmed via demo) |
| **BaZi (Four Pillars)** | Chinese & Eastern | Chinese endpoints | Available |
| **Vedic (Jyotish)** | Vedic Astrology | Vedic endpoints | Available |

### All 5 Systems Confirmed Available

> **Updated 2026-03-15:** CEO đã verify trực tiếp trên https://astrology-api.io/demo
> - Human Design: `#tag/-human-design-system` — có endpoint riêng
> - Tử Vi: nằm trong nhóm Chinese & Eastern astrology
> - Cả 5 hệ thống đều được cover bởi astrology-api.io

**Next step:** Đăng ký API key → test từng endpoint → xác nhận output format cho mỗi hệ thống

## 4. Integration Architecture

```
360Human Backend (FastAPI)
│
├─ /engines/
│   ├─ astrology_api.py      ← Wrapper cho astrology-api.io
│   │   ├─ get_vedic()       ← Vedic/Jyotish natal
│   │   ├─ get_bazi()        ← BaZi Four Pillars
│   │   ├─ get_numerology()  ← Numerology calculations
│   │   └─ get_chart_image() ← Chart rendering (10 credits)
│   │
│   ├─ get_tuvi()        ← Chinese & Eastern endpoints
│   └─ get_human_design() ← Human Design System endpoints
│
├─ /services/
│   └─ interpret_service.py   ← L1 → L1.5 → L2 → L3 pipeline
│
└─ /core/
    └─ api_client.py          ← HTTP client, retry, rate limit
```

## 5. Request Format (Expected)

```python
# Example: Vedic Natal Chart
import httpx

headers = {"Authorization": "Bearer <API_KEY>"}

response = httpx.post(
    "https://api.astrology-api.io/v1/vedic/natal",
    headers=headers,
    json={
        "year": 1995,
        "month": 3,
        "day": 15,
        "hour": 14,
        "minute": 30,
        "second": 0,
        "city": "Ho Chi Minh City",
        "country_code": "VN"
    }
)
# Auto geocoding + timezone via city/country
```

## 6. Chart Visualization

API supports chart image rendering (10 credits/call).
- Cần test xem output format (SVG vs PNG)
- Nếu API không đủ customization → dùng Recharts/D3.js render từ raw data
- **Decision: Test API chart rendering trước, fallback sang Recharts nếu không đủ**

## 7. Caching Strategy

```
Cache Key Format: ${system}_${birth_date}_${birth_time}_${lat}_${lon}_${gender}

L1 (Raw API data):     Redis TTL = permanent (birth data không đổi)
L1.5 (KB enrichment):  Redis TTL = permanent
L2 (RAG context):      Redis TTL = 30 days (KB có thể update)
L3 (AI interpretation): Redis TTL = 30 days

→ Mỗi user chỉ gọi API 1 lần duy nhất cho mỗi profile
→ Giảm đáng kể credit usage
```

## 8. Action Items

- [ ] Đăng ký Free account tại astrology-api.io
- [ ] Test các endpoint: Vedic, BaZi, Numerology
- [ ] Test Tử Vi endpoint (confirm Zi Wei Dou Shu output: 14 Chính Tinh, 12 Cung)
- [ ] Test Human Design endpoint (confirm output: Type, Authority, Profile, Centers)
- [ ] Estimate credit usage per user flow
- [ ] Decide chart rendering approach (API vs frontend)
