# Global Rules — 360Human AI Workforce

> **Version:** 1.0
> **Áp dụng:** TẤT CẢ agents PHẢI đọc file này (always_read)
> **Nguồn:** AGENT STAR™ Ch17 — 5 Operational Principles

---

## Hiến Pháp Tổ Chức

### Rule 1: Think-Out-Loud (TOL)

Mọi agent PHẢI ghi lại reasoning process, không chỉ output:
- **Decision Log:** Các alternatives đã xem xét + rationale chọn
- **Uncertainty Flag:** Nếu confidence < 80%, phải flag rõ ràng
- **Format:** `[TOL] Reasoning: ... → Decision: ... → Confidence: X%`

### Rule 2: Sprint-Centric

- Mọi task PHẢI thuộc về 1 sprint cụ thể
- Format Sprint: `SP-YYMMDD-##-ShortName`
- Mọi output PHẢI gắn Sprint ID
- KHÔNG làm task "ngoài sprint" (orphan task)

### Rule 3: Changelog

- Mọi thay đổi cấu trúc (thêm/sửa/xóa file) PHẢI log vào `Changelog.md`
- Format: `[YYYY-MM-DD] [TYPE] Description`
- Types: `[STRUCTURE]`, `[FILE]`, `[AGENT]`, `[WORKFLOW]`, `[DECISION]`
- KHÔNG bao giờ xóa file — chuyển vào `Archive/`

### Rule 4: SSOT (Single Source of Truth)

- Mỗi thông tin chỉ tồn tại ở **1 nơi duy nhất**
- Tất cả references khác PHẢI dùng backlink, KHÔNG copy nội dung
- Khi phát hiện duplicate → báo cáo ngay, giữ 1 bản, xóa bản còn lại
- Department folders (01-04) = SSOT zone (chỉ chứa finished output)
- SPRINT/ = WIP zone (draft, experimental)

### Rule 5: Indexing

- Mọi file mới PHẢI được thêm vào INDEX.md tương ứng
- Mọi folder mới PHẢI có INDEX.md riêng
- YAML frontmatter cho routing (khi applicable)

---

## Quy Tắc Giao Tiếp

### Escalation Protocol (3 Levels)

| Level | Điều kiện | Hành động |
|-------|----------|-----------|
| L1 | Routine issues (naming, format, minor bug) | → Gửi Director → Log decision |
| L2 | Critical (arch change, scope change, cost >$5) | → Gửi @CEO-Winston → Chờ approval |
| L3 | IMMEDIATE (security, data loss, brand damage) | → Gửi @CEO-Winston NGAY LẬP TỨC |

### Autonomy Rules

- **L1 agents:** Execute only — không được tự quyết định
- **L2 agents:** Suggest & Execute — đề xuất, chờ approval
- **L3 agents:** Decide & Inform — quyết định, report sau
- **L4 agents:** Full autonomy within scope
- **L5 agents:** Self-evolving (chỉ CEO)

### Cross-Calling Rules (AGENT STAR Ch10)

1. Tier N chỉ gọi Tier N+1 hoặc Tier 3 (KHÔNG gọi ngược)
2. max_depth: 3 (ngăn đệ quy vô hạn)
3. Mọi cross-call PHẢI có Interface Contract (input/output/calls/called_by)
4. KHÔNG gọi trực tiếp agent cùng tier — phải qua Director

---

## Anti-Patterns (TUYỆT ĐỐI TRÁNH)

| # | Anti-Pattern | Hậu quả | Cách tránh |
|---|-------------|---------|-----------|
| 1 | **God Agent** | Context pollution, hallucination | Max 10 skills per agent |
| 2 | **God Folder** | Token overflow | Max 30 files per folder |
| 3 | **Orphan File** | Lost traceability | Mọi file phải thuộc 1 zone |
| 4 | **Duplicate SSOT** | Multi-truth conflict | 1 source only, backlink elsewhere |
| 5 | **Dead Handoff** | Agent works on dead project | Update Handoff.md weekly |
| 6 | **WIP in SSOT** | Draft pollutes library | Draft → SPRINT/ only |

---

## Context Management

### Progressive Loading (AGENT STAR Ch15)

- **always_read:** INDEX.md, Handoff.md, global-rules.md, own JD.md (≤5 files)
- **on_demand:** Department files loaded when task requires
- **project:** Full project context only when doing cross-department work
- **KHÔNG BAO GIỜ** load toàn bộ workspace vào context (context pollution)

### Knowledge Items

- Sau mỗi task quan trọng: extract KI via `/beat`
- KI format: Title + Content + Backlinks + Tags
- Lưu tại `.agents/knowledge/`
- Monthly review: update hoặc retire stale KIs
