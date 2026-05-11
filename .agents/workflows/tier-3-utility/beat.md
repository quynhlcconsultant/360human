---
description: Extract Knowledge Item từ conversation/task — đóng gói insight để dùng lại
tier: utility
version: v1.0
owner: "Any Agent"
calls:
  - /flog (Tier 3)
called_by:
  - Any workflow sau task quan trọng
  - /sprint-review (Tier 0)
  - manual (bất kỳ agent nào khi phát hiện insight đáng lưu)
input: "Tên insight/knowledge + nội dung muốn đóng gói"
output: "KI file mới trong .agents/knowledge/ + KI_Index.md updated"
---

# Workflow: /beat

> **Tier 3 — UTILITY**
> Ai chạy: Bất kỳ agent nào
> Khi nào: Sau task quan trọng, phát hiện pattern mới, giải quyết blocker khó, hoặc quyết định kiến trúc

---

## Khi nào nên gọi /beat?

✅ Gọi khi:
- Vừa giải quyết xong một vấn đề khó → muốn lưu solution
- Phát hiện anti-pattern → muốn warn agents khác
- Quyết định kiến trúc quan trọng → muốn ghi lý do
- Domain knowledge astrology phức tạp → muốn encode cho AI dùng lại
- Pattern code/workflow hiệu quả → muốn đóng gói thành KI

❌ Không gọi khi:
- Output là thứ đã có trong code/file (KI không duplicate SSOT)
- Chỉ là task bình thường không có insight đặc biệt
- Thông tin sẽ outdated nhanh chóng (< 1 tháng)

---

## Bước 1: Xác định KI ID

Xem `KI_Index.md` tại `.agents/knowledge/KI_Index.md` → Tìm ID lớn nhất hiện có → KI mới = ID + 1.

Format: `KI-[###]` (ví dụ: KI-003, KI-047)

---

## Bước 2: Tạo KI File

Tạo file: `.agents/knowledge/KI-[###]_[ten-ngan-kebab].md`

Template:

```markdown
# KI-[###]: [Tên Knowledge Item]

> **ID:** KI-[###]
> **Created:** YYYY-MM-DD
> **Owner:** @[AgentHandle]
> **Tags:** #[tag1] #[tag2] #[tag3]
> **Status:** active
> **Sprint:** S##

---

## Summary (2-3 câu)

[Tóm tắt ngắn — đây là gì, tại sao quan trọng, ai cần biết]

---

## Content

### Problem / Context
[Vấn đề hoặc context dẫn đến KI này]

### Solution / Insight
[Insight chính, giải pháp, hoặc pattern đã học được]

### How to Apply
[Cụ thể — khi nào dùng KI này, cách áp dụng ra sao]

### Examples (nếu có)
[Code snippet, ví dụ, hoặc case study]

### Anti-patterns (nếu có)
[Những gì KHÔNG làm — và tại sao]

---

## Backlinks

- Sprint: SPRINT/SP-YYMMDD-##-TenSprint/
- Related KIs: [KI-### nếu liên quan]
- Source: [conversation/task/document gốc]
```

---

## Bước 3: Cập nhật KI_Index.md

Thêm dòng mới vào bảng trong `.agents/knowledge/KI_Index.md`:

```markdown
| KI-[###] | [Tên KI] | #tag1 #tag2 | YYYY-MM-DD | active |
```

---

## Bước 4: Gọi /flog

```
/flog — KI-### [Tên] extracted and saved to .agents/knowledge/
```

---

## Output cam kết

- File `KI-[###]_[tên].md` trong `.agents/knowledge/`
- `KI_Index.md` updated với dòng mới
- Changelog logged qua /flog

```
[/beat complete — KI-### saved]
```
