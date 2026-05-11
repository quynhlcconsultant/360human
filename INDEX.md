# INDEX — 360Human Workspace

> **Last updated:** 2026-03-20
> **Tier:** M (Startup, 1-2 people + AI agents)
> **Framework:** DDWA + AGENT STAR™

---

## Workspace Map

### Root Files (Handoff Suite)
| File | Vai trò |
|------|---------|
| `INDEX.md` | Bản đồ workspace (file này) |
| `Guideline.md` | Quy tắc, naming conventions, dos/don'ts |
| `Onboarding.md` | Hướng dẫn cho agent/người mới |
| `Handoff.md` | Trạng thái bàn giao real-time |
| `Changelog.md` | Lịch sử thay đổi cấu trúc |
| `ToDo.md` | Sprint + Backlog tracking |
| `Notes/` | Scratch pad, ideas |
| `Archive/` | Tài liệu cũ (never delete) |
| `Temporary/` | File tạm (can delete) |

### Department Zones (SSOT)
| Folder | Code | Chức năng | Files |
|--------|------|----------|-------|
| `01_Governance/` | GOV | Strategy, Finance, Decisions | CEO-001→005, Master_Strategy.yaml |
| `02_Production/` | PRD | Product, Design, Architecture, Code, KB | PRD-001, FE-001→007, ARCH-001→005 |
| `03_Marketing/` | MKT | Market Research, Creative, RTM, Sales | MKT-001, CRE-001, RTM-001 |
| `04_Operations/` | OPS | DevOps, Monitoring, Support | Deployment, SLO, FAQ |
| `05_Consulting/` | CON | Advisory Layer — tư vấn trực tiếp CEO | 3 teams, 38 skills, Module 1 |

### WIP Zone
| Folder | Vai trò |
|--------|---------|
| `SPRINT/` | Construction site — chỉ chứa WIP |
| `SPRINT/Sprint_Log.md` | Master sprint tracker |

### Agent Zone
| Folder | Vai trò |
|--------|---------|
| `.agents/rules/` | Hiến pháp — mọi agent phải đọc |
| `.agents/skills/` | Thư viện skill chia sẻ |
| `.agents/workflows/` | Workflow definitions (Tier 0-3) |
| `.agents/agents/` | Agent definitions (JD.md per agent) |
| `.agents/knowledge/` | Bộ nhớ tổ chức (Knowledge Items) |

### Legacy & Training
| Folder | Vai trò |
|--------|---------|
| `_Legacy/` | Toàn bộ folder cũ (0-6) — giữ nguyên nội dung, không xóa |
| `backend/` | Source code (FastAPI) — giữ nguyên vị trí |

> **Note:** `Module 1/` đã chuyển vào `05_Consulting/02_Architecture_Consulting/Module 1/`
