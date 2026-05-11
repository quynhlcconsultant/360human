# Guideline — 360Human Workspace

> **Version:** 1.0
> **Last updated:** 2026-03-20
> **Áp dụng:** DDWA + AGENT STAR™

---

## 1. Naming Conventions (DDWA Ch09)

| Loại | Format | Ví dụ |
|------|--------|-------|
| Department Folder | `[##]_[DepartmentName]` | `01_Governance`, `02_Production` |
| Document File | `[PREFIX]-[###]_[description].md` | `CEO-001_business-requirements.md` |
| Sprint Folder | `SP-[YYMMDD]-[##]-[ShortName]` | `SP-260317-01-Foundation` |
| Agent Folder | `@[Role-Name]` | `@Director-Product`, `@Specialist-Frontend` |
| YAML SSOT | `[Description].yaml` | `Master_Strategy.yaml` |

## 2. File Prefixes

| Prefix | Department | Phạm vi |
|--------|-----------|---------|
| `CEO-` | 01_Governance | Strategy, decisions, tracking |
| `PRD-` | 02_Production/Product | Product requirements, features |
| `FE-` | 02_Production/Design + Frontend | UI specs, design system, components |
| `ARCH-` | 02_Production/Architecture | Technical blueprint, API, deployment |
| `MKT-` | 03_Marketing | Market research, campaigns |
| `CRE-` | 03_Marketing/Creative | Brand, content, creative assets |
| `RTM-` | 03_Marketing/RTM_Strategy | Route-to-market, distribution |
| `OPS-` | 04_Operations | DevOps, monitoring, support |

## 3. Quy Tắc WIP vs SSOT (DDWA Ch05)

- **SPRINT/** = Construction site (WIP). Draft, messy, experimental.
- **01-04_Departments/** = Library (SSOT). Finished, authoritative, reviewed.
- **Flow:** Idea → Sprint/WIP → CEO Review (QG-3) → Department/SSOT
- **KHÔNG BAO GIỜ** đặt draft vào department folder.
- **KHÔNG BAO GIỜ** xóa file — chuyển vào `Archive/`.

## 4. Năm Nguyên Tắc Vận Hành (AGENT STAR Ch17)

1. **Think-Out-Loud (TOL):** Ghi reasoning, không chỉ kết quả.
2. **Sprint-Centric:** Mọi task thuộc 1 sprint cụ thể.
3. **Changelog:** Mọi thay đổi cấu trúc phải log.
4. **SSOT:** Mỗi thông tin chỉ ở 1 nơi duy nhất.
5. **Indexing:** Mọi file mới phải có trong INDEX.md.

## 5. Workflow Rules (AGENT STAR Ch10)

- **Tier N chỉ gọi Tier N+1 hoặc Tier 3** (không gọi ngược).
- Mọi workflow phải có **Interface Contract** (input/output/calls/called_by).
- **max_depth: 3** — ngăn đệ quy vô hạn.

## 6. Quality Gates (AGENT STAR Ch16)

| Gate | Ai | Khi nào | Bắt buộc? |
|------|----|---------|----------|
| QG-1 | Agent tự check | Sau mỗi task | Luôn luôn |
| QG-2 | QA agent review | Sau mỗi feature | Recommended |
| QG-3 | CEO approve | Trước merge SSOT | Critical items |

## 7. Dos & Don'ts

### DO
- Đặt file đúng department zone
- Update INDEX.md khi thêm file mới
- Ghi Changelog khi thay đổi cấu trúc
- Archive thay vì xóa
- Backlink khi reference file khác

### DON'T
- Tạo God Folder (>30 files trực tiếp)
- Duplicate SSOT (cùng 1 thông tin ở 2 nơi)
- Để Orphan File (file không thuộc zone nào)
- Bỏ quên Handoff.md >14 ngày
- Edit YAML trực tiếp (dùng workflow/chat)
