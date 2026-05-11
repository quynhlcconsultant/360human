---
description: Tạo workflow mới từ scratch hoặc từ pattern đã có — meta workflow
tier: meta
version: v1.0
owner: "@CEO-Winston"
calls:
  - /flog (Tier 3)
called_by:
  - manual (CEO/Architect khi cần workflow mới)
input: "Tên workflow, tier, owner, mô tả ngắn purpose, các bước thô"
output: "File workflow mới trong .agents/workflows/tier-N-xxx/[name].md"
---

# Workflow: /buildflow

> **Tier 0 — META**
> Ai chạy: @CEO-Winston (hoặc @Consultant-Architecture)
> Khi nào: Khi cần tạo workflow mới cho hệ thống

---

## Bước 1: Xác định Tier của workflow mới

Hỏi và trả lời các câu sau:

| Câu hỏi | Nếu YES |
|---------|---------|
| Workflow này TẠO RA workflows/skills/agent khác? | → Tier 0 META |
| Workflow này ĐIỀU PHỐI nhiều workflow con? | → Tier 1 ORCHESTRATION |
| Workflow này tạo ra OUTPUT cụ thể (code, doc, design)? | → Tier 2 EXECUTION |
| Workflow này nhỏ, nhanh, không thay đổi state chính? | → Tier 3 UTILITY |

---

## Bước 2: Xác định thư mục đích

| Tier | Folder |
|------|--------|
| Tier 0 | `.agents/workflows/tier-0-meta/` |
| Tier 1 | `.agents/workflows/tier-1-orchestration/` |
| Tier 2 | `.agents/workflows/tier-2-execution/` |
| Tier 3 | `.agents/workflows/tier-3-utility/` |

---

## Bước 3: Điền YAML frontmatter

Dùng template chuẩn (CH20 Template 2):

```yaml
---
description: [1 câu mô tả workflow làm gì]
tier: meta | orchestration | execution | utility
version: v1.0
owner: "@AgentName"
calls:
  - /workflow-nó-gọi (Tier N)
called_by:
  - /workflow-gọi-nó
  - manual (nếu CEO gọi trực tiếp)
input: "Mô tả input mong đợi"
output: "Mô tả output cam kết"
---
```

**Validate trước khi tiếp:**
- [ ] `tier` đúng với phân loại ở Bước 1?
- [ ] `owner` có phải agent đúng tier không? (Tier 0 → CEO, T1 → Director, T2 → Specialist)
- [ ] `calls` không vi phạm Cross-Calling Rule (Tier N chỉ gọi N+1 hoặc T3)?

---

## Bước 4: Viết nội dung workflow

Cấu trúc bắt buộc:

```markdown
# Workflow: /tên-workflow

> Tier | Owner | Khi nào dùng

---

## Bước 1: [Tên bước]
[Mô tả chi tiết — agent làm gì, đọc file gì, output trung gian là gì]

## Bước 2: ...

## [Gate nếu là T1]
Điều kiện để tiếp tục / escalate

## Output cam kết
[Liệt kê cụ thể]

[QG-1] Checklist tự đánh giá
```

**Nguyên tắc khi viết:**
- Mỗi bước phải đủ cụ thể để agent thực thi không cần hỏi thêm
- Tier 2: thường 3-7 bước
- Tier 1: thường 5-10 bước + quality gate
- Tier 3: thường 2-4 bước, < 50 dòng tổng
- KHÔNG viết quá chung chung ("làm điều này", "thực hiện điều kia")

---

## Bước 5: Validate workflow mới

Trước khi save, kiểm tra:

- [ ] Tên file đúng format: `[tên-kebab-case].md`
- [ ] YAML frontmatter đầy đủ và hợp lệ
- [ ] Cross-Calling Rules không bị vi phạm
- [ ] Không có God Workflow anti-pattern (> 10 bước → cân nhắc tách)
- [ ] Output cam kết rõ ràng
- [ ] QG-1 checklist ở cuối

---

## Bước 6: Cập nhật JD.md của owner agent

Trong `JD.md` của agent owner, thêm workflow mới vào section **Workflow Ownership**:

```markdown
| /tên-workflow | Tier N | Mô tả ngắn |
```

---

## Bước 7: Gọi /flog

```
/flog — [tên-workflow].md created in tier-N-xxx/, JD.md of @AgentName updated
```

---

## Output cam kết

- File workflow mới tại đúng tier folder
- JD.md của owner agent đã cập nhật
- Changelog.md đã log `[WORKFLOW] /tên-workflow created`

```
[QG-1] Tự kiểm: Tier đúng ✓ | YAML valid ✓ | Cross-call rules OK ✓ | JD updated ✓
```
