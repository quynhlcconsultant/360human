---
description: Điều phối chiến dịch marketing — từ research → content → distribute → measure
tier: orchestration
version: v1.0
owner: "@Director-Growth"
calls:
  - /research-market (Tier 2)
  - /write-content (Tier 2)
  - /audit-quality (Tier 2)
  - /qg-check (Tier 3)
  - /flog (Tier 3)
called_by:
  - manual (@CEO-Winston khởi động campaign hoặc launch)
input: "Campaign brief: mục tiêu, audience, timeline, budget (nếu có), channel"
output: "Campaign plan + Content assets + Distribution schedule + KPI tracking setup"
---

# Workflow: /launch-campaign

> **Tier 1 — ORCHESTRATION**
> Ai chạy: @Director-Growth
> Khi nào: Khởi động campaign marketing hoặc product launch

---

## Bước 1: Load Campaign Context

Đọc bắt buộc:
1. `01_Governance/Strategy/CEO-001_business-requirements.md` — ICP, North Star
2. `03_Marketing/INDEX.md` — campaigns hiện có
3. `03_Marketing/Market_Research/MKT-001*.md` — insights thị trường

Xác nhận với CEO:
- **Objective:** Awareness / Acquisition / Activation / Retention / Revenue
- **Target audience:** [ICP segment cụ thể]
- **Channel:** TikTok / Instagram / Facebook / SEO / Email / Referral / All
- **Timeline:** [Start → End]
- **Success metric:** [KPI chính — số follower, số sign-up, conversion rate...]
- **Budget constraint:** [nếu có]

**[TOL] Decision Log:**
```
[TOL] Campaign Brief:
→ Objective: [AARRR stage]
→ Audience: [segment]
→ Channel: [channel(s)]
→ Timeline: [dates]
→ KPI: [metric + target số]
→ Approach: [strategy gợi ý]
→ Confidence: X%
```

---

## Bước 2: Market Research — Gọi /research-market

```
/research-market
Focus: [Competitor content analysis + Vietnam audience behavior + Channel best practices]
Question: "Content gì đang viral trong segment [target] trên [channel]?"
```

Output: Research brief tóm tắt 1-2 trang, insights actionable.

---

## Bước 3: Content Strategy

Dựa trên research, xây dựng Content Matrix:

| Content Type | Format | Frequency | Channel | Hook angle | Goal |
|-------------|--------|-----------|---------|-----------|------|
| Educational | Short video | 3x/week | TikTok | "Bạn có biết..." | Awareness |
| Social proof | Story | Daily | Instagram | Testimonial | Trust |
| Conversion | Long-form | 1x/week | Facebook | Pain point | Acquisition |

**Chọn 2-3 content types tập trung** — không trải mỏng.

---

## Bước 4: Tạo Content Assets — Gọi /write-content

Với mỗi content type đã chọn:

```
/write-content
Type: [Educational/Conversion/Social proof]
Format: [Short video script / Caption / Blog / Email]
Tone: [Thân thiện, gen Z, tiếng Việt tự nhiên]
Hook: [Mở đầu gây chú ý]
CTA: [Call to action cụ thể]
```

Tạo minimum: 5-10 content pieces sẵn sàng để post.

---

## Bước 5: Quality Review — Gọi /audit-quality

```
/audit-quality
Scope: Campaign content assets
Criteria: Brand voice + Accuracy + Vietnamese natural + CTA clear + No misleading claims
```

**Đặc biệt với 360Human:** Kiểm tra astrology claims có accurate không (đây là vấn đề brand critical).

---

## Bước 6: Tạo Distribution Schedule

Tạo file `03_Marketing/RTM_Strategy/RTM-[##]_[campaign-name]-schedule.md`:

```markdown
# Distribution Schedule — [Campaign Name]

| Date | Platform | Content ID | Format | Status |
|------|----------|-----------|--------|--------|
| MM-DD | TikTok | CNT-001 | Video | ⬜ |
| MM-DD | Instagram | CNT-002 | Story | ⬜ |
| ... | ... | ... | ... | ... |

## Daily Checklist
- [ ] Post theo schedule
- [ ] Reply comments trong 2 tiếng đầu
- [ ] Track engagement metrics

## Emergency Protocol
- Nếu post nhận reaction tiêu cực > 20%: Tạm dừng → Báo @CEO-Winston
```

---

## Bước 7: Setup KPI Tracking

Tạo KPI baseline tại `03_Marketing/MKT-[##]_[campaign]-kpi.md`:

```markdown
# KPI Tracker — [Campaign Name]

| Metric | Baseline | Target | Current | Week 1 | Week 2 | Week 3 |
|--------|---------|--------|---------|--------|--------|--------|
| Reach | | | | | | |
| Engagement rate | | | | | | |
| Sign-ups | | | | | | |
| Conversion rate | | | | | | |

## Review Schedule
- Weekly: @Director-Growth tự review
- Bi-weekly: Report lên @CEO-Winston
```

---

## Bước 8: CEO Sign-off (QG-3)

Báo cáo lên @CEO-Winston:

```
[CAMPAIGN READY] [Campaign Name]
→ Objective: [X]
→ Strategy: [tóm tắt 2-3 câu]
→ Content: [N] pieces sẵn sàng
→ Schedule: [Date start] → [Date end]
→ KPI target: [metric = X]
→ Review: Weekly
→ Xin approve để bắt đầu distribute
```

**Gate:** Chờ QG-3 approval từ CEO trước khi public post.

---

## Bước 9: Launch & Monitor

Sau approval:
- Execute schedule theo từng ngày
- Monitor comments, DMs, engagement real-time
- Flag bất thường → escalate ngay nếu cần

---

## Bước 10: Gọi /flog

```
/flog — Campaign [Tên] launched. [N] content pieces. KPI tracker created. Schedule active.
```

---

## Output cam kết

- Content assets (minimum 5-10 pieces) trong `03_Marketing/Creative/`
- Distribution schedule `RTM-###` trong `03_Marketing/RTM_Strategy/`
- KPI tracker `MKT-###` trong `03_Marketing/`
- CEO approval documented
- Campaign live (hoặc scheduled)

```
[QG-1] Tự kiểm:
- [ ] Research-backed (không đoán mò audience behavior)?
- [ ] Content đã qua /audit-quality?
- [ ] Schedule realistic (không quá tải)?
- [ ] KPI baseline có trước campaign?
- [ ] CEO đã approve?
- [ ] Emergency protocol có sẵn?
```
