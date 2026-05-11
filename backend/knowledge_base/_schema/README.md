---
title: "Knowledge Base Schema"
id: "KB-SCHEMA"
updated: "2026-03-15"
status: "active"
---

# Knowledge Base — Data Schema

> Format: **Markdown** (optimized for RAG chunking + Claude context)
> Chunking strategy: Split by `##` headers → 1 concept = 1 retrievable chunk
> Naming: `{system}/{category}.md`

---

## Universal Frontmatter (mỗi file .md)

```yaml
---
system: zi_wei | numerology | human_design | bazi | vedic
category: chinh_tinh | life_path | types | ...
entries: 14              # Số entries trong file
last_verified: 2026-03-15
source: "Tử Vi Đẩu Số Toàn Thư, tr.45-120"
---
```

## Universal Entry Structure (mỗi `##` section)

```markdown
## {Tên Tiếng Việt} ({Tên Tiếng Anh})

**ID:** {system}_{snake_case_key}
**Category:** {category}
**Element/Group:** {nhóm/ngũ hành/type}
**Keywords:** keyword1, keyword2, keyword3

### Ý nghĩa tổng quát
{Mô tả core meaning — 2-5 câu}

### Chi tiết theo lĩnh vực
{Phân tích theo từng domain/cung/aspect — tuỳ system}

### Tổ hợp / Tương tác
{Khi kết hợp với elements khác — nếu có}
```

---

## Per-System Schemas
