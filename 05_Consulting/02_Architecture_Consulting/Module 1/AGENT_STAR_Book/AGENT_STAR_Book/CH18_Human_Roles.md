# Chương 18: Vai trò con người — 4 Human Roles

> **Câu hỏi cốt lõi:** *Trong tổ chức nơi AI Agent thực thi, con người làm gì?*

---

## 1. Nguyên lý: Con người thiết kế, AI thực thi

```
Trong tổ chức truyền thống:
  Con người = THỰC THI 80% + Quản lý 20%

Trong AI-Agent Workforce:
  Con người = THIẾT KẾ 30% + ĐÀO TẠO 25% + KIỂM SOÁT 20% + TÀI LIỆU 15% + THỰC THI 10%
```

---

## 2. Bốn vai trò cốt lõi

### Role 1: 📐 Architect — Kiến trúc sư

```
Trách nhiệm:
  → Thiết kế Architecture (Specialization, Shape, Power, Department)
  → Thiết kế Orchestration (Workflow Tiering, Cross-calling)
  → Quyết định khi nào Provision/Decommission Agent
  → Thiết kế Federated Model (Global vs Project)
  → Vẽ Dependency Graph
  → Giải quyết Misalignment giữa 5 cánh sao

Công cụ:
  → /buildflow, /buildskill, /refactor, /rm
  → Decision Canvas, Alignment Check
  → Workflow/Skill/Agent Index

Outputs:
  → Framework documents
  → Workflow definitions
  → Architecture decisions (ADR)
  → Dependency Maps

Thời gian: ~30% tổng thời gian CEO
```

### Role 2: 🎓 Trainer — Huấn luyện viên

```
Trách nhiệm:
  → Viết và maintain SKILL.md files
  → Thiết kế System Prompt cho từng Agent
  → Cấu hình Agent Definition (11 Elements)
  → Audit Skill quality — detect overlap, conflict, outdated
  → Skill Loading — assign Skill cho Agent

Công cụ:
  → /buildskill
  → Tri-Hub Architecture (Skill Hub)
  → Skill Index

Outputs:
  → SKILL.md files
  → Agent JD.md files
  → System Prompt configurations
  → Skill audit reports

Thời gian: ~25% tổng thời gian CEO
```

### Role 3: ⚖️ Governor — Kiểm soát viên

```
Trách nhiệm:
  → Kiểm tra output qua Quality Gates
  → Ra quyết định chiến lược (Strategy)
  → Approve Escalation (Level 2, 3)
  → Audit Agent performance → Configuration Feedback
  → Enforce Rules compliance
  → Sprint Review & close

Công cụ:
  → /sync, /done, /explain
  → Sprint artifacts review
  → Measurement dashboard

Outputs:
  → Approval/rejection decisions
  → Strategy documents
  → Configuration changes
  → Sprint review minutes

Thời gian: ~20% tổng thời gian CEO
```

**Cảnh báo Red Team: Governor Bottleneck (Tử huyệt tại Con người)**
- Lỗ hổng: Quality Gate Level 3 (CEO Approval) hay Escalation Level 2 (To CEO) khiến toàn bộ tổ chức Agent "chết đứng" nếu người duyệt ngủ, đi vắng hoặc bận họp. Single Point of Failure xuất hiện.
- Giải pháp: Cần áp dụng **SLA Fallback (Cơ chế dự phòng theo thời gian)**. Khi một workflow phải chờ Governor >24h (hay X giờ), hệ thống tự động lưu trạng thái (Save State), hoặc được phép Bypass với **Safe Mode** (Chế độ an toàn, ko public database) và bắn email khẩn cấp cho con người. Không được để tắc nghẽn vô thời hạn.

### Role 4: 📝 Documentarian — Người tài liệu hóa

```
Trách nhiệm:
  → Maintain Knowledge Items (Thủ thư)
  → Update INDEX files
  → Enforce SSOT — merge duplicates
  → Changelog maintenance
  → Audit documentation freshness (/stale)

Công cụ:
  → /docs, /update, /stale, /beat
  → KI Index
  → /doccheck, /docclean

Outputs:
  → Knowledge Items (KI)
  → INDEX files
  → Changelog entries
  → Stale reports

Thời gian: ~15% tổng thời gian CEO
```

---

## 3. Role Mapping — Ai có thể nhờ AI Agent?

| Human Role        | Có thể ủy quyền cho AI?                           |
| ----------------- | ------------------------------------------------- |
| **Architect**     | Một phần — @AI_RM hỗ trợ audit, đề xuất           |
| **Trainer**       | Một phần — /buildskill tự động hóa phần mechanics |
| **Governor**      | Một phần — Quality Gate tự động ở Level 1-2       |
| **Documentarian** | Phần lớn — /beat, /stale, /docs tự động hóa       |

> **Nguyên tắc:** Ủy quyền **execution** cho AI, giữ **decision** cho con người.

---

## 4. Evolution theo quy mô

```
1 CEO (Solo Founder):
  → 1 người làm cả 4 roles
  → Phân bổ: Architect 30% | Trainer 25% | Governor 20% | Doc 15% | Execute 10%

CEO + 1-2 người:
  → CEO: Governor + Architect
  → Người 2: Trainer + Documentarian
  → AI @AI_RM: hỗ trợ Architect

CEO + 3-5 người:
  → CEO: Governor (chủ yếu)
  → CTO/Architect: Architect + Trainer
  → PM: Documentarian
  → Team: Trainer (domain-specific)
  → AI: Hỗ trợ cả 4 roles
```
