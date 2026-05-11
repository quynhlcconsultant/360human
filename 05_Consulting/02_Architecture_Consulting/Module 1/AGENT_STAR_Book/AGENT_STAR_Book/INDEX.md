# 📖 AI-Agent Organization Design
## Thiết kế tổ chức cho kỷ nguyên AI-Agent Workforce

> **Phiên bản:** 3.0 | **Ngày:** 09/03/2026
> **Nền tảng lý thuyết gốc:** Star Model™ (Jay R. Galbraith, 1973–2014)
> **Mô hình mới:** AGENT STAR™ — Adapted Star Model cho AI-Agent Workforce

---

## Cấu trúc cuốn sách

```
PHẦN I — NỀN TẢNG LÝ THUYẾT
  Hiểu Star Model gốc, phân tích điểm khác biệt AI vs Human,
  và đề xuất mô hình AGENT STAR mới.

PHẦN II — ARCHITECTURE (Cánh sao 2: Kiến trúc)
  4 sub-policies: Specialization, Shape, Distribution of Power, Departmentalization

PHẦN III — ORCHESTRATION (Cánh sao 3: Điều phối)
  Vertical/Lateral processes, Cross-calling patterns, Workflow Tiering

PHẦN IV — CAPABILITIES (Cánh sao 4: Năng lực)
  5 thành phần Agent-Workflow-Skill-Rules-Knowledge, Agent Definition 11 elements,
  Mental Models (PDCA, Lean, Systems Thinking)

PHẦN V — MEASUREMENT & ALIGNMENT (Cánh sao 5: Đo lường và Căn chỉnh)
  Quality Gates, Metrics, Configuration Feedback Loop

PHẦN VI — OPERATIONAL PLAYBOOK
  Nguyên tắc vận hành, Lộ trình triển khai, Templates
```

---

## Mục lục chi tiết

### PHẦN I: NỀN TẢNG LÝ THUYẾT

| Chapter | File                        | Nội dung                                                  |
| ------- | --------------------------- | --------------------------------------------------------- |
| **00**  | `CH00_Preface.md`           | Lời nói đầu — tại sao cần cuốn sách này                   |
| **01**  | `CH01_Star_Model_Origin.md` | Star Model™ gốc — 5 cánh sao, 3 nguyên lý, lịch sử        |
| **02**  | `CH02_AI_vs_Human.md`       | 7 tiên đề — khác biệt nền tảng giữa AI Agent và con người |
| **03**  | `CH03_Agent_Star_Model.md`  | Giới thiệu AGENT STAR™ — mô hình 5 cánh mới               |

---

### PHẦN II: ⭐ STRATEGY (Cánh sao 1)
*"Kim chỉ nam" — Làm sao để AI hiểu chiến lược khổng lồ mà không nghẽn bộ nhớ?*

| Chapter | File                                     | Nội dung                                                                  |
| ------- | ---------------------------------------- | ------------------------------------------------------------------------- |
| **04**  | `CH04_Strategy_Context_and_Biz_Model.md` | Biz Model Setup — 6 Strategy Domains, Triple-Layer Format, Hybrid Context |

---

### PHẦN III: 📐 ARCHITECTURE (Cánh sao 2)
*"Giải phẫu học" — Ai làm gì? Bao nhiêu tầng? Tập trung hay phân tán?*

| Chapter | File                            | Nội dung                                                                     |
| ------- | ------------------------------- | ---------------------------------------------------------------------------- |
| **05**  | `CH05_Specialization.md`        | Chuyên biệt hóa Agent — Generalist vs Specialist vs T-Shaped                 |
| **06**  | `CH06_Shape_Span_of_Control.md` | Hình dạng tổ chức — 3 tầng tối ưu, CEO Span ≤ 7                              |
| **07**  | `CH07_Distribution_of_Power.md` | Centralize vs Decentralize — Ma trận Impact×Reversibility, 5 Autonomy Levels |
| **08**  | `CH08_Departmentalization.md`   | Nhóm Agent thành Cluster — Hybrid Model, Dependency Map                      |

---

### PHẦN IV: 🔄 ORCHESTRATION (Cánh sao 3)
*"Sinh lý học" — Thông tin và công việc chảy thế nào?*

| Chapter | File                       | Nội dung                                                                       |
| ------- | -------------------------- | ------------------------------------------------------------------------------ |
| **09**  | `CH09_Processes.md`        | Vertical & Lateral Processes — 4 cấp lateral cho AI                            |
| **10**  | `CH10_Workflow_Tiering.md` | Phân tầng Workflow — Meta / Orchestration / Execution / Utility                |
| **11**  | `CH11_Cross_Calling.md`    | 5 Cross-calling Patterns — Sequential, Router, Fork-Join, Escalation, Callback |

---

### PHẦN V: 🔧 CAPABILITIES (Cánh sao 4)
*"DNA" — Agent được tạo ra, đào tạo, và bố trí thế nào?*

| Chapter | File                                   | Nội dung                                                         |
| ------- | -------------------------------------- | ---------------------------------------------------------------- |
| **12**  | `CH12_Five_Components.md`              | Hệ thống 5 thành phần: Agent—Workflow—Skill—Rules—Knowledge      |
| **13**  | `CH13_Agent_Anatomy.md`                | Giải phẫu 1 Agent — 11 Elements + System Prompt Structure        |
| **14**  | `CH14_Mental_Models_and_Frameworks.md` | Nạp tư duy cổ điển (PDCA, Lean, Systems Thinking) cho AI         |
| **15**  | `CH15_Context_Knowledge.md`            | Context Folder, Knowledge System, Backlinks, Dual-Level Briefing |

---

### PHẦN VI: 📏 MEASUREMENT & ALIGNMENT (Cánh sao 5)
*"Đo lường" — Biết Agent nào tốt, Agent nào cần tối ưu*

| Chapter | File                  | Nội dung                                            |
| ------- | --------------------- | --------------------------------------------------- |
| **16**  | `CH16_Measurement.md` | Metrics, Quality Gates, Configuration Feedback Loop |

---

### PHẦN VII: 🛠️ OPERATIONAL PLAYBOOK
*Templates, nguyên tắc vận hành, lộ trình triển khai*

| Chapter | File                                  | Nội dung                                                                     |
| ------- | ------------------------------------- | ---------------------------------------------------------------------------- |
| **17**  | `CH17_Operational_Principles.md`      | 5 Nguyên tắc vận hành: TOL, Sprint, Changelog, SSOT, Indexing & YAML Routing |
| **18**  | `CH18_Human_Roles.md`                 | Vai trò con người: Architect, Trainer, Governor, Documentarian               |
| **19**  | `CH19_Roadmap.md`                     | Lộ trình triển khai 4 Phase + Decision Canvas                                |
| **20**  | `CH20_Templates.md`                   | Templates: Agent Definition, Workflow Frontmatter, Alignment Check           |
| **21**  | `CH21_Antigravity_Implementation...`  | Hạn chế thực tiễn (Antigravity), Workarounds & Cost/Effort Trade-offs        |
| **22**  | `CH22_Digital_Workspace_IPO_Model...` | Kiến Trúc Không Gian Làm Việc Số: Mô hình IPO Factory (Workspace/Warehouse)  |

---
## Mapping từ tài liệu cũ

| Nội dung gốc                       | Nguồn                | → Chapter mới |
| ---------------------------------- | -------------------- | ------------- |
| Star Model gốc, 5 cánh sao         | v1 Ch1-2             | CH01, CH02    |
| Bộ lọc AI (Giữ/Chuyển đổi/Loại bỏ) | v1 Ch3               | CH02, CH03    |
| AI Agent Star Model (5 cánh mới)   | v1 Ch4               | CH03          |
| Tuyên ngôn, bảng so sánh           | v2 Ch I              | CH00          |
| Hệ thống 5 thành phần              | v2 Ch II             | CH11          |
| Agent Definition 11 elements       | v2 Ch II.2           | CH12          |
| System Prompt Structure            | v2 Ch II.3           | CH12          |
| Workflow Tiering                   | v2 Ch III            | CH10          |
| Cross-calling                      | v2 Ch III.3-4        | CH11          |
| Context, Knowledge, Backlinks      | v2 Ch IV             | CH15          |
| 5 Operational Principles           | v2 Ch V              | CH17          |
| Vai trò con người                  | v2 Ch VI             | CH18          |
| Lộ trình 4 Phase                   | v2 Ch VII            | CH19          |
| Decision Canvas + Templates        | v2 Ch VIII + Phụ lục | CH19, CH20    |
| **Strategy Context & Biz Model**   | SP-260308-03         | **CH04**      |
| **Mental Models & Frameworks**     | CEO Idea             | **CH14**      |
| **Specialization (MỚI)**           | CH01 cũ              | **CH05**      |
| **Shape & Span of Control (MỚI)**  | CH02 cũ              | **CH06**      |
| **Distribution of Power (MỚI)**    | CH03 cũ              | **CH07**      |
| **Departmentalization (MỚI)**      | CH04 cũ              | **CH08**      |
| **Processes (MỚI)**                | CH05 cũ              | **CH09**      |
| **Trade-offs & Constraints (MỚI)** | Yêu cầu CEO 09/03    | **CH21**      |
