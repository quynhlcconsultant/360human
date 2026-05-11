# Chương 4: Departmentalization — Cách nhóm AI Agent thành "Phòng ban"

> **Nguồn gốc:** Structure Policy #4 — Star Model™ (Jay R. Galbraith)
> **Câu hỏi cốt lõi:** *Nhóm Agent theo chức năng (Engineering, Marketing...) hay theo dự án/BU (5Balance, Hoctap.tech...)?*

---

## 1. Lý thuyết gốc: Departmentalization trong tổ chức con người

Departmentalization trả lời: **Lấy tiêu chí gì để nhóm các vai trò thành phòng ban?**

Galbraith xác định 4 mô hình chính:

```
FUNCTIONAL          DIVISIONAL           MATRIX              HYBRID
Nhóm theo           Nhóm theo            Nhóm theo           Functional core +
chuyên môn          sản phẩm/BU          cả hai               Divisional overlay

┌──────────┐       ┌──────────┐        ┌──────────┐       ┌──────────┐
│   CEO    │       │   CEO    │        │   CEO    │       │   CEO    │
├──┬──┬──┤       ├──────┬───┤        ├──┬───┬──┤       ├──┬──┬──┤
│  │  │  │       │      │   │        │  │   │  │       │  │  │  │
│Eng│Mkt│Ops│   │ BU-A │BU-B│      │Eng│Mkt│Ops│     │Eng│Mkt│Ops│ ← Core
│  │  │  │       │(full)│(full)      ├──┴───┴──┤       │  │  │  │
└──┴──┴──┘       └──────┴───┘        │ BU-A overlay│     ├──┴──┴──┤
                                     │ BU-B overlay│     │5B │HT │ ← Overlay
                                     └────────────┘     └──┴──┘
```

**So sánh 4 mô hình:**

| Mô hình        | Nhóm theo                            | Ưu điểm                                     | Nhược điểm                           |
| -------------- | ------------------------------------ | ------------------------------------------- | ------------------------------------ |
| **Functional** | Chuyên môn (Eng, Mkt, Ops...)        | Chuyên sâu, tái sử dụng, economies of scale | Silo — phòng ban không hiểu nhau     |
| **Divisional** | Sản phẩm / BU / Thị trường           | Tự chủ, phản ứng nhanh, context sâu         | Trùng lặp nguồn lực, thiếu chuẩn hóa |
| **Matrix**     | Cả hai (dual reporting)              | Cân bằng chuẩn hóa + linh hoạt              | Phức tạp, xung đột quyền lực, chậm   |
| **Hybrid**     | Functional core + Divisional overlay | Linh hoạt, vừa tái sử dụng vừa có context   | Cần Lateral Processes rất mạnh       |

---

## 2. Chuyển đổi: Departmentalization trong AI-Agent Workforce

### 2.1. Tại sao AI-Agent thay đổi bài toán Departmentalization?

| Yếu tố                | Tổ chức con người                         | AI-Agent Workforce                        |
| --------------------- | ----------------------------------------- | ----------------------------------------- |
| **Chi phí duplicate** | Rất cao — mỗi department = team riêng     | Gần 0 — copy SKILL.md, Workflow.md        |
| **Silo problem**      | Nghiêm trọng — phòng ban không nói chuyện | Giải quyết bằng Cross-calling             |
| **Context switching** | Đau đớn — con người cần thời gian adapt   | **Context window** — bottleneck kỹ thuật  |
| **Dual reporting**    | Gây stress, confusion                     | Không — Agent không có ego hay stress     |
| **Tribal knowledge**  | Kiến thức "ở trong đầu người"             | Kiến thức trong SKILL.md, KI → share được |

**Hệ quả:** Nhiều nhược điểm của từng mô hình **biến mất** khi áp dụng cho AI:

- **Functional silo?** → Giải quyết bằng Cross-calling + Shared Knowledge
- **Divisional duplicate?** → Copy Skill gần free, hoặc dùng Federated Model
- **Matrix conflict?** → Agent không có ego — dual reporting không gây stress

### 2.2. Mô hình khuyến nghị: Functional Core + BU Overlay (Hybrid)

**Tại sao Hybrid là tối ưu cho AI-Agent Workforce:**

```
1. Agent có CORE IDENTITY theo chức năng
   → @Writer là Writer BẤT KỂ đang viết cho BU nào
   → Skill Profile = chuyên sâu về writing (Functional)
   → Không cần "Writer cho 5Balance" và "Writer cho Hoctap" riêng biệt

2. Agent có CONTEXT OVERLAY theo BU khi cần
   → Khi viết cho 5Balance → nạp context 05_5Balance/
   → Khi viết cho Hoctap → nạp context 06_Hoctap.tech/
   → Cùng Agent, cùng Skill, khác context

3. Domain-specific Agent tồn tại ở BU level
   → @BaziEngine chỉ cần cho 5Balance → không cần Global
   → @CourseDesigner chỉ cần cho Hoctap → không cần Global
```

---

## 3. Thiết kế "Department" trong AI-Agent Workforce

### 3.1. Department ≈ Cluster (Nhóm Agent cùng chức năng)

Trong tổ chức con người, department có phòng, tầng, meeting room. Trong AI, "department" là **cluster** — nhóm Agent cùng chức năng, chia sẻ Skill và Workflow.

```
┌─ CLUSTER: MARKETING ─────────────────────────────────┐
│                                                       │
│  Director: @MktLead                                   │
│  ┌─────────────────────────────────────────────────┐ │
│  │  Specialist Agents:                              │ │
│  │  @Writer — Content creation                      │ │
│  │  @SEOAuditor — SEO analysis & optimization       │ │
│  │  @ContentRepurposer — Cross-platform adaptation  │ │
│  │  @SocialManager — Social media scheduling        │ │
│  └─────────────────────────────────────────────────┘ │
│                                                       │
│  Shared Skills: copywriting, marketing-psychology,    │
│                 content-strategy, linkedin-content     │
│                                                       │
│  Shared Workflows: /content-post, /social-content,    │
│                    /email-sequence, /landing-page      │
│                                                       │
│  BU Overlay:                                          │
│    5Balance → nạp personas/hoang-duc-minh/            │
│    Hoctap   → nạp course-design/ context              │
└───────────────────────────────────────────────────────┘

┌─ CLUSTER: ENGINEERING ────────────────────────────────┐
│  Director: @EngLead                                    │
│  Specialists: @FrontEnd, @BackEnd, @DeployOps, @QA    │
│  Shared Skills: arch-guard, 5balance-design            │
│  Shared Workflows: /code, /deploy, /test, /fix        │
└───────────────────────────────────────────────────────┘

┌─ CLUSTER: OPERATIONS ─────────────────────────────────┐
│  Director: @OpsLead                                    │
│  Specialists: @PM, @DataAnalyst, @FinanceOps          │
│  Shared Skills: project_management, strategic-advisor  │
│  Shared Workflows: /pm, /sync, /refactor, /docs       │
└───────────────────────────────────────────────────────┘

┌─ CLUSTER: META (Kiến trúc hệ thống) ─────────────────┐
│  Director: @AI_RM (Resource Manager)                   │
│  Shared Workflows: /buildflow, /buildskill, /rm       │
│  Vai trò: Audit, restructure, maintain Tri-Hub         │
└───────────────────────────────────────────────────────┘
```

### 3.2. Cross-BU Agent vs. BU-Specific Agent

**Khi nào tạo Agent cấp Global (phục vụ nhiều BU)?**

```
→ Skill set của Agent ÁP DỤNG CHO MỌI BU
→ Chỉ context thay đổi, methodology KHÔNG đổi
→ Task volume ở mỗi BU KHÔNG ĐỦ để justify Agent riêng

Ví dụ:
  @Writer → Global: viết cho mọi BU, chỉ nạp context khác nhau
  @DeployOps → Global: deploy pipeline giống nhau, chỉ config khác
  @PM → Global: quản lý sprint giống nhau, chỉ project khác
```

**Khi nào tạo Agent cấp BU-Specific (chỉ phục vụ 1 BU)?**

```
→ Agent cần DOMAIN KNOWLEDGE rất sâu, riêng cho BU đó
→ Methodology KHÁC nhau giữa các BU
→ Task volume ở BU đó ĐỦ LỚN để justify Agent riêng

Ví dụ:
  @BaziEngine → BU-Specific (5Balance): thuật toán Bát Tự không áp dụng ở BU khác
  @CourseDesigner → BU-Specific (Hoctap): thiết kế khóa học riêng cho Hoctap
  @EventCoordinator → BU-Specific (Events): flow event registration riêng
```

**Ma trận quyết định:**

| Tiêu chí                     | → Global Agent | → BU-Specific Agent |
| ---------------------------- | -------------- | ------------------- |
| Skill áp dụng cho nhiều BU   | ✅              |                     |
| Skill chỉ 1 BU cần           |                | ✅                   |
| Task volume > 20/tuần ở 1 BU |                | ✅                   |
| Methodology giống nhau       | ✅              |                     |
| Methodology khác nhau        |                | ✅                   |
| Context switching rẻ         | ✅              |                     |
| Context switching đắt        |                | ✅                   |
| **Dễ audit**                 | ⭐⭐⭐            | ⭐                   |
| **Scalable**                 | ⭐⭐             | ⭐⭐⭐                 |

### 3.3. Rủi ro của Federated Model: Dependency Hell (Red Team Warning)
Khi dùng chung Global Skills/Workflows (`.agents/`), một bản cập nhật từ Architect có thể phá vỡ tính tương thích (backward compatibility) của các Local Agent ở dự án con mà không có cảnh báo.

**Giải pháp:** Mọi Skill và Workflow dùng chung phải có **Versioning (Phiên bản hóa)**. Local Agent phải gọi rõ `Skill: copywriting v1.2` thay vì trỏ URL file chung chung, tránh sụp đổ rớt dây chuyền.

---

## 4. Tương tác giữa các Cluster

### 4.1. Intra-Cluster (Nội bộ nhóm)

```
Trong CLUSTER MARKETING:
  @MktLead phân công → @Writer thực thi → @SEO review SEO → @MktLead tổng hợp

Đặc điểm:
  → Chia sẻ cùng Skill pool (copywriting, marketing-psychology)
  → Chia sẻ cùng Context Folder
  → Cross-calling mượt mà — "nói cùng ngôn ngữ"
  → Director Agent (@MktLead) điều phối
```

### 4.2. Cross-Cluster (Giữa các nhóm)

```
MARKETING ↔ ENGINEERING:
  @Writer tạo content → @FrontEnd implement landing page

ENGINEERING ↔ OPERATIONS:
  @DeployOps deploy → @PM update changelog

OPERATIONS ↔ META:
  @PM phát hiện workflow drift → @AI_RM audit + restructure
```

**Cơ chế Cross-Cluster:**

| Cơ chế               | Mô tả                                           | Khi nào dùng                      |
| -------------------- | ----------------------------------------------- | --------------------------------- |
| **Cross-calling**    | Workflow gọi Agent từ Cluster khác              | Task cần output liên chức năng    |
| **Shared Knowledge** | 2 Cluster cùng đọc/viết KI                      | Kinh nghiệm BU A hữu ích cho BU B |
| **Escalation Chain** | Agent Cluster A escalate lên Director Cluster B | Vấn đề cross-cutting              |
| **Joint Workflow**   | 1 Workflow có bước từ nhiều Cluster             | Pipeline liên chức năng           |

### 4.3. Dependency Map

Dependency Map trả lời: **"Cluster nào phụ thuộc Cluster nào?"**

```
                    ┌────────────────┐
                    │     META       │
                    │ (AI_RM)        │
                    │ Kiến trúc hệ   │
                    │ thống          │
                    └───────┬────────┘
                            │ audit/restructure
            ┌───────────────┼───────────────┐
            │               │               │
    ┌───────▼───────┐ ┌─────▼─────┐ ┌───────▼───────┐
    │  MARKETING    │ │ENGINEERING│ │  OPERATIONS    │
    │  @MktLead     │ │@EngLead   │ │  @OpsLead      │
    │               │ │           │ │                │
    │  @Writer ─────┼─┤ @FrontEnd │ │  @PM ──────────┤
    │  @SEO         │ │ @BackEnd  │ │  @DataAnalyst  │
    │               │ │ @DeployOps│ │  @FinanceOps   │
    └───────┬───────┘ └─────┬─────┘ └───────┬────────┘
            │               │               │
            └───────────────┼───────────────┘
                            │
                    ┌───────▼────────┐
                    │  SHARED LAYER  │
                    │ Knowledge Items│
                    │ Global Skills  │
                    │ Global Rules   │
                    └────────────────┘
```

---

## 5. Anti-patterns Departmentalization

### Anti-pattern 1: Pure Functional Silo

```
❌ Agent Engineering không biết Agent Marketing đang làm gì
→ @FrontEnd build UI mà không biết content strategy
→ @Writer viết content không biết technical limitations
→ FIX: Cross-calling + Shared Knowledge + Joint Workflows
```

### Anti-pattern 2: Pure Divisional Duplication

```
❌ Mỗi BU có bộ Agent riêng, Skills riêng, Workflows riêng
→ @Writer_5Balance, @Writer_Hoctap, @Writer_Events — cùng Skill copywriting!
→ Fix copywriting Skill → phải sửa 3 nơi → quên 1 → inconsistency
→ FIX: Federated Model — 1 Skill centralize, context overlay per BU
```

### Anti-pattern 3: Cluster không có Director

```
❌ 5 Specialist Agent trong Marketing, không ai điều phối
→ @Writer, @SEO, @Repurposer chạy độc lập — output rời rạc
→ Không ai tổng hợp, quality gate rỗng
→ FIX: Mỗi Cluster cần 1 Director Agent (Tier 1 Orchestration)
```

### Anti-pattern 4: Cluster quá lớn

```
❌ 1 Cluster Engineering chứa 20 Agent — FrontEnd, BackEnd, DevOps, QA, Security, Data...
→ Director @EngLead span quá rộng, orchestration quality giảm
→ FIX: Split thành sub-cluster khi > 10 Agent
   @DevLead (FrontEnd, BackEnd)
   @InfraLead (DevOps, Security, DataOps)
```

---

## 6. Nguyên tắc Departmentalization cho AI-Agent Workforce

| #       | Nguyên tắc                                        | Giải thích                                                          |
| ------- | ------------------------------------------------- | ------------------------------------------------------------------- |
| **DT1** | **Hybrid là mặc định**                            | Functional Core + BU Overlay — cân bằng tái sử dụng và context      |
| **DT2** | **Mỗi Cluster cần Director**                      | Không cluster nào không có orchestrator                             |
| **DT3** | **Cluster size ≤ 10–15 Agent**                    | Quá lớn → split thành sub-cluster                                   |
| **DT4** | **Global Agent cho Skill phổ quát**               | Skill dùng chung → Agent dùng chung, chỉ overlay context            |
| **DT5** | **BU-Specific Agent cho domain sâu**              | Domain knowledge riêng + volume cao → justify Agent riêng           |
| **DT6** | **Cross-cluster bằng Cross-calling, không merge** | 2 Cluster phối hợp qua Workflow, KHÔNG gộp thành 1 Cluster khổng lồ |
| **DT7** | **Dependency Map bắt buộc**                       | Vẽ rõ ai phụ thuộc ai — phát hiện coupling sớm                      |

---

## 7. Liên kết với các chương khác

- **Chương 1 (Specialization):** Cách chuyên biệt hóa Agent quyết định Agent thuộc Cluster nào
- **Chương 2 (Shape):** Mỗi Cluster có hình dạng riêng — Cluster nhỏ = flat, Cluster lớn = thêm sub-director
- **Chương 3 (Distribution of Power):** Mỗi Cluster có mức autonomy riêng — Cluster mature = decentralize hơn
- **Chương 5 (Processes):** Intra-cluster dùng vertical processes. Cross-cluster dùng lateral processes
