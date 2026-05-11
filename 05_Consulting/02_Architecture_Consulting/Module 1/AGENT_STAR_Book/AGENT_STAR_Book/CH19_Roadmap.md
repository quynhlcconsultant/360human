# Chương 19: Roadmap — Lộ trình triển khai 4 Phase

> **Câu hỏi cốt lõi:** *Bắt đầu từ đâu? Thứ tự triển khai thế nào?*

---

## 1. Tổng quan 4 Phase

```
PHASE 1: FOUNDATION          PHASE 2: STRUCTURE          PHASE 3: SCALE          PHASE 4: OPTIMIZE
"Xây nền"                    "Dựng khung"                "Mở rộng"               "Tối ưu"
──────────────────           ────────────────           ──────────────          ────────────────
✓ Strategy rõ               ✓ Workflow Tiering          ✓ Multi-BU              ✓ Dynamic Autonomy
✓ 3-5 Core Agent            ✓ Cross-calling             ✓ Federated Model       ✓ Measurement mature
✓ Core Skills               ✓ Autonomy Scope            ✓ Tri-Hub Library       ✓ Self-evolving
✓ Basic Workflows           ✓ Quality Gates             ✓ Full KI system        ✓ Process Debt = 0
✓ Rules/MEMORY              ✓ Agent Clusters            ✓ Director Agents       ✓ Org as Product

Timeline:                   Timeline:                   Timeline:               Timeline:
Tuần 1-4                    Tháng 2-3                   Tháng 4-6               Tháng 7+
```

---

## 2. Phase 1: Foundation — Xây nền (Tuần 1–4)

### Checklist

```
STRATEGY:
  [ ] Xác định Direction (tầm nhìn, sứ mệnh)
  [ ] Xác định Competitive Advantage
  [ ] Xác định Scope (danh sách BU)
  [ ] Phân bổ ưu tiên giữa các BU

ARCHITECTURE:
  [ ] Liệt kê 3-5 vai trò cốt lõi cần Agent
  [ ] Provision Agent đầu tiên (VD: @Writer, @EngLead)
  [ ] Thiết kế tổ chức 2 tầng đơn giản: CEO → Specialists

ORCHESTRATION:
  [ ] Tạo 5-10 Workflow cơ bản (/deploy, /code, /content-post)
  [ ] Thiết lập vertical flow: CEO → Agent → CEO (review)
  [ ] Tạo /go Router (nếu > 5 Workflow)

CAPABILITIES:
  [ ] Viết Core Skills (ngôn ngữ, quy tắc chung)
  [ ] Viết 2-3 Functional Skills cho Agent chính
  [ ] Tạo Agent Folder (JD, ToDo) cho mỗi Agent
  [ ] Thiết lập Rules/MEMORY files

MEASUREMENT:
  [ ] Xác định 1 metric per Agent
  [ ] Quality Gate Level 1 (self-check)
```

### Kết quả Phase 1

```
✓ Tổ chức 2 tầng hoạt động: CEO → 3-5 Specialist Agent
✓ 5-10 Workflow cơ bản chạy được
✓ Rules và Core Skills tồn tại
✓ Agent Folder cho mỗi Agent
✓ Sprint-centric operation bắt đầu
```

---

## 3. Phase 2: Structure — Dựng khung (Tháng 2–3)

### Checklist

```
ARCHITECTURE:
  [ ] Áp dụng Workflow Tiering (Meta/Orch/Exec/Utility)
  [ ] Thiết lập Autonomy Scope cho mỗi Agent (Level L2-L3)
  [ ] Bắt đầu nhóm Agent thành Clusters (nếu > 5 Agent)
  [ ] Provision Director Agent nếu cần

ORCHESTRATION:
  [ ] Thiết lập Cross-calling patterns (Interface Contract)
  [ ] Tạo Tier 1 Orchestration Workflows
  [ ] Escalation Protocol rõ ràng cho mỗi Agent
  [ ] Backlinks giữa Workflows

CAPABILITIES:
  [ ] Mở rộng Skill Library (15-20 Skills)
  [ ] Thiết lập Context Folder structure (always_read, on_demand)
  [ ] Bắt đầu tạo Knowledge Items (/beat)

MEASUREMENT:
  [ ] Quality Gate Level 2 (peer review)
  [ ] Sprint velocity tracking
  [ ] Configuration Feedback Loop bắt đầu
```

---

## 4. Phase 3: Scale — Mở rộng (Tháng 4–6)

### Checklist

```
ARCHITECTURE:
  [ ] Triển khai Federated Model (Global + Project overlay)
  [ ] Scale lên 15-30 Agent
  [ ] Sub-clusters cho Cluster lớn (> 10 Agent)
  [ ] Dynamic Shape (simple task = flat, complex = layered)

ORCHESTRATION:
  [ ] Triển khai Tri-Hub Architecture (Skill Hub, Agent Hub, Workflow Hub)
  [ ] Dependency Graph vẽ đầy đủ
  [ ] Chain Workflows hoàn chỉnh (/chain-build, /chain-plan, /chain-ship)

CAPABILITIES:
  [ ] Full Knowledge System (50+ KI)
  [ ] Source Library Lifecycle (Training → Adopt → Backup)
  [ ] Multi-Assignment cho Agent dùng chung cross-BU

MEASUREMENT:
  [ ] Quality Gate Level 3 (CEO approval cho critical tasks)
  [ ] Comprehensive Metrics dashboard
  [ ] Audit Agent performance quarterly
```

---

## 5. Phase 4: Optimize — Tối ưu (Tháng 7+)

### Checklist

```
ARCHITECTURE:
  [ ] Dynamic Autonomy theo context (Agent cùng 1 = L2 hoặc L4 tùy task)
  [ ] Lateral Power Shift Protocol cho emergency
  [ ] Org Design Audit cycle (quarterly)

ORCHESTRATION:
  [ ] Process Debt = 0 (no orphan workflows, no circular deps)
  [ ] Meta-Workflow mature (/buildflow, /buildskill tự động hóa cao)
  [ ] Cross-calling 100% có Interface Contract + Backlinks

CAPABILITIES:
  [ ] Self-evolving Agents (L5 cho Agent mature)
  [ ] KI System auto-maintenance (/stale, /beat cycle)
  [ ] Tri-Hub fully maintained by @AI_RM

MEASUREMENT:
  [ ] Full alignment check automated
  [ ] Proactive optimization (đo → phát hiện sớm → fix trước khi thành vấn đề)
  [ ] "Organization as Product" — iterate org design like product design
```

---

## 6. Decision Canvas — Template áp dụng toàn cuốn sách

### Cho mỗi lần thiết kế hoặc re-design, điền:

```
⭐ STRATEGY
  [ ] Phục vụ bao nhiêu BU?          _______________
  [ ] Lợi thế cạnh tranh?            _______________
  [ ] BU ưu tiên?                     _______________

📐 ARCHITECTURE
  [ ] Bao nhiêu Agent Role?           _______________
  [ ] Bao nhiêu tầng?                 _______________
  [ ] Autonomy Scope per Agent?       _______________
  [ ] Nhóm theo Functional/BU/Hybrid? _______________

🔄 ORCHESTRATION
  [ ] Bao nhiêu Tier 1 Workflow?      _______________
  [ ] Router Agent?                   _______________
  [ ] Escalation mấy cấp?            _______________
  [ ] Cross-calling patterns?          _______________

🔧 CAPABILITIES
  [ ] 5 thành phần đủ chưa?           _______________
  [ ] Mỗi Agent đủ 11 Elements?      _______________
  [ ] Knowledge System?               _______________

📏 MEASUREMENT
  [ ] Metrics per Agent?              _______________
  [ ] Quality Gate mấy cấp?           _______________
  [ ] Feedback Loop hoạt động?        _______________
```

### Alignment Check

```
  [ ] Strategy ↔ Architecture : Agent roles match BU count?
  [ ] Strategy ↔ Orchestration: Priority BU has better Workflows?
  [ ] Architecture ↔ Orchestration: Every Agent in a Workflow?
  [ ] Architecture ↔ Capabilities: Every Agent has Skills?
  [ ] Orchestration ↔ Measurement: Every Process has Metrics?
  [ ] Measurement ↔ Capabilities: Feedback → Skill update?
  [ ] Capabilities ↔ Strategy: Skills serve Strategy?
```
