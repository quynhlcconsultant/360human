# Quality Gates — 360Human

> **Version:** 1.0
> **Nguồn:** AGENT STAR™ Ch16 — Measurement System
> **Áp dụng:** Tất cả agents

---

## 3-Layer Quality Gate System

### QG-1: Self-Check (Agent tự đánh giá)

**Khi nào:** Sau mỗi task hoàn thành
**Ai:** Agent thực hiện task
**Bắt buộc:** Luôn luôn

**Checklist:**
- [ ] Output đúng format yêu cầu?
- [ ] Đã đọc đủ context trước khi làm?
- [ ] Không vi phạm 5 Operating Principles?
- [ ] Không tạo anti-pattern (God Folder, Orphan File, Duplicate SSOT)?
- [ ] File mới đã thêm vào INDEX.md?
- [ ] Changelog đã update?
- [ ] Sprint ID đã gắn?
- [ ] Confidence ≥ 80%? (Nếu không → flag uncertainty)

**Output:** `[QG-1] PASS/FAIL — [Agent] — [Task] — [Notes]`

---

### QG-2: Peer Review (QA agent kiểm tra chéo)

**Khi nào:** Sau mỗi feature hoàn thành
**Ai:** @Specialist-QA hoặc Director cùng level
**Bắt buộc:** Recommended (skip cho tasks trivial)

**Checklist:**
- [ ] QG-1 đã pass?
- [ ] Output consistent với PRD/specs?
- [ ] Không conflict với SSOT hiện có?
- [ ] Cross-reference correct? (backlinks valid)
- [ ] Naming conventions đúng? (Guideline.md)
- [ ] Cho code: Tests pass? Security check? Performance OK?
- [ ] Cho content: Tone đúng? Facts accurate? Vietnamese natural?

**Output:** `[QG-2] PASS/FAIL — [Reviewer] — [Feature] — [Findings]`

---

### QG-3: CEO Approval (Winston review)

**Khi nào:** Trước merge vào SSOT (department folders)
**Ai:** @CEO-Winston
**Bắt buộc:** Critical items only

**Trigger conditions:**
- New file vào department zone (01-04)
- Architecture decision
- Feature scope change
- Pricing/business model change
- External-facing content
- Security-sensitive change

**Checklist:**
- [ ] QG-1 + QG-2 đã pass?
- [ ] Aligned với strategy (CEO-001)?
- [ ] Không conflict với existing decisions?
- [ ] Resource cost acceptable?
- [ ] Timeline impact assessed?

**Output:** `[QG-3] APPROVED/REJECTED — [CEO] — [Item] — [Decision + Rationale]`

---

## Configuration Feedback Loop

Sau mỗi sprint review, CEO đánh giá agent performance:

| Rating | Hành động |
|--------|----------|
| **Excellent** | Mở rộng autonomy (L2→L3), thêm responsibility |
| **Good** | Duy trì, có thể thêm BU scope |
| **Average** | Audit skill, tối ưu system prompt, thêm context |
| **Poor** | Giảm autonomy (L3→L2), re-skill, pair với senior agent |
| **Failure** | Decommission + provision agent mới |

**Principle:** "Measure to Configure, not to Punish"

---

## Metrics per Tier

| Tier | Metrics |
|------|---------|
| Tier 0 (META) | Workflow creation quality, org alignment score |
| Tier 1 (ORCH) | Pipeline completion rate, routing accuracy, bottleneck detection |
| Tier 2 (EXEC) | Task quality score, velocity (tasks/sprint), rework rate |
| Tier 3 (UTIL) | Uptime, response time, error rate |

## Đặc Thù 360Human — Accuracy Metrics

| Phase | Target Accuracy | Measurement |
|-------|----------------|-------------|
| Pre-pilot | 70% | Internal review vs expert knowledge |
| Pilot | >85% | User feedback + expert validation |
| Scale | 99% | Automated + manual audit |

**Accuracy = Weighted Score:**
- Accuracy of readings: 60%
- Specificity to individual: 20%
- Performance: 5%
- UI quality: 5%
- CI/CD reliability: 10%
