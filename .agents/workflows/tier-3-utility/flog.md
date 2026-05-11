---
description: Log file changes vào Changelog.md — utility nhỏ gọn, gọi sau mọi thay đổi cấu trúc
tier: utility
version: v1.0
owner: "Any Agent"
calls: []
called_by:
  - Any workflow (Tier 0-2)
  - manual (bất kỳ agent nào)
input: "Mô tả ngắn về thay đổi đã làm (file nào, action gì)"
output: "1 dòng log mới trong Changelog.md"
---

# Workflow: /flog

> **Tier 3 — UTILITY**
> Ai chạy: Bất kỳ agent nào
> Khi nào: Sau mỗi thay đổi cấu trúc (tạo file, xóa file, đổi tên, restructure)

---

## Bước 1: Xác định Change Type

| Type | Khi nào dùng |
|------|-------------|
| `[STRUCTURE]` | Tạo/xóa folder, restructure cây thư mục |
| `[FILE]` | Tạo/sửa/xóa file nội dung |
| `[AGENT]` | Thêm/sửa/decommission agent JD.md |
| `[WORKFLOW]` | Tạo/sửa/xóa workflow file |
| `[DECISION]` | Ghi lại quyết định quan trọng |
| `[DEPLOY]` | Deploy lên staging/production |
| `[SPRINT]` | Mở/đóng sprint |

---

## Bước 2: Format Log Entry

```markdown
[YYYY-MM-DD] [TYPE] [Mô tả ngắn gọn — action + subject + context nếu cần]
```

**Ví dụ:**
```markdown
[2026-03-20] [WORKFLOW] /sprint-planning.md created in tier-0-meta/
[2026-03-20] [AGENT] @Specialist-Backend JD.md created
[2026-03-20] [DECISION] Chọn Neon over self-hosted PostgreSQL — cost và simplicity
[2026-03-20] [DEPLOY] Sprint S03 deployed to staging — all smoke tests pass
[2026-03-20] [SPRINT] Sprint S03 Foundation opened
[2026-03-20] [FILE] PRD-001 updated — Feature F-005 AstrologyChart added
```

**Rules:**
- Ngắn gọn (1 dòng duy nhất)
- Đủ để hiểu mà không cần đọc thêm context
- Không dùng tiếng Anh lẫn tiếng Việt tùy hứng — chọn 1 ngôn ngữ cho description

---

## Bước 3: Append vào Changelog.md

Thêm vào **đầu** file `Changelog.md` (entry mới nhất ở trên cùng):

```markdown
[2026-MM-DD] [TYPE] [Description]
```

---

## Output cam kết

- 1 dòng log mới trong `Changelog.md`
- Không modify gì khác

```
[/flog complete]
```

> Utility này stateless và idempotent. Gọi bất cứ lúc nào, bao nhiêu lần cũng được.
