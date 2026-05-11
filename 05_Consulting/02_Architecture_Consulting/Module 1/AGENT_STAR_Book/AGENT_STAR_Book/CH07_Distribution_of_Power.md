# Chương 3: Distribution of Power — Tập trung vs. Phân tán quyền lực

> **Nguồn gốc:** Structure Policy #3 — Star Model™ (Jay R. Galbraith)
> **Câu hỏi cốt lõi:** *Ai được quyết định gì? Quyền quyết định tập trung ở CEO hay phân tán xuống từng Agent?*

---

## 1. Lý thuyết gốc: Distribution of Power trong tổ chức con người

Galbraith xác định Distribution of Power quyết định **mức độ tập trung (centralization) vs. phân tán (decentralization)** quyền ra quyết định.

**2 chiều phân phối quyền lực:**

```
VERTICAL (Dọc):
  Quyền lực ở đỉnh (CEO) ◄──────────────► Quyền lực ở tuyến đầu (IC)
  Centralization                             Decentralization

LATERAL (Ngang):
  Quyền lực dịch chuyển sang đơn vị nào đang xử lý vấn đề trọng yếu nhất
  → VD: Khi sản phẩm đang launch → Product team có "quyền lực tạm thời"
  → VD: Khi khủng hoảng tài chính → Finance team "nắm cương"
```

**Phổ Centralization — Decentralization:**

```
CENTRALIZED                                         DECENTRALIZED
(Trung ương quyết tất cả)                          (Tuyến đầu tự quyết)
├───────────┼───────────┼───────────┼───────────┤
│           │           │           │           │
│  Mọi qđ   │  Qđ lớn   │  Qđ nhỏ   │  Mọi qđ   │
│  qua CEO  │  qua CEO  │  tự quyết  │  tự quyết  │
│           │  Qđ nhỏ   │  Qđ lớn    │           │
│           │  tự quyết  │  qua CEO   │           │
```

**Trade-off kinh điển:**

| Chiều                 | Centralized (Tập trung)                 | Decentralized (Phân tán)             |
| --------------------- | --------------------------------------- | ------------------------------------ |
| **Nhất quán**         | Cao — 1 người quyết = 1 giọng nói       | Thấp — mỗi nơi quyết khác nhau       |
| **Tốc độ quyết định** | Chậm (bottleneck ở đỉnh)                | Nhanh (quyết định ngay tại chỗ)      |
| **Chất lượng qđ**     | Cao (nếu đỉnh có đủ thông tin)          | Cao (nếu tuyến đầu đủ thẩm quyền)    |
| **Tải CEO**           | Rất cao — phải quyết tất cả             | Thấp — ủy quyền                      |
| **Rủi ro sai**        | Tập trung — 1 qđ sai ảnh hưởng rộng     | Phân tán — nhiều qđ sai nhỏ cục bộ   |
| **Học hỏi tổ chức**   | Chậm — chỉ 1 người tích lũy kinh nghiệm | Nhanh — nhiều điểm tích lũy          |
| **Khả năng mở rộng**  | Kém — CEO là nút cổ chai                | Tốt — thêm đơn vị = thêm quyền quyết |

**Nguyên tắc Galbraith:** Không có "đúng" hay "sai" — chỉ có **"phù hợp"**. Mức centralization phải match với **strategy** (cần consistency hay speed?) và **complexity** (đơn giản hay phức tạp?).

---

## 2. Chuyển đổi: Distribution of Power trong AI-Agent Workforce

### 2.1. Đặc thù mới: AI Agent và bài toán Autonomy

Trong tổ chức con người, "phân tán quyền lực" có nghĩa là **tin tưởng** nhân viên ra quyết định đúng — dựa vào kinh nghiệm, phán đoán, và văn hóa.

Trong AI-Agent Workforce, "phân tán quyền lực" có nghĩa hoàn toàn khác:

| Chiều               | Tổ chức con người                       | AI-Agent Workforce                                           |
| ------------------- | --------------------------------------- | ------------------------------------------------------------ |
| **Cơ sở tin tưởng** | Kinh nghiệm, track record, phán đoán    | **System Prompt, Skill Profile, Code of Conduct**            |
| **Rủi ro khi sai**  | Nhân viên rút kinh nghiệm               | **Agent lặp lại lỗi vô hạn** (nếu không sửa cấu hình)        |
| **Cách thu hồi**    | Sa thải, kỷ luật, coaching              | **Reconfigure System Prompt** (tức thời)                     |
| **Mức tự chủ**      | Phụ thuộc cá nhân (năng lực, tính cách) | **Phụ thuộc cấu hình** (Autonomy Scope — Element 3)          |
| **Escalation**      | Tự phán đoán khi nào cần hỏi            | **Programmatik** — code sẵn trong Workflow (`must_escalate`) |

> **Nguyên lý Distribution of Power cho AI:**
> *Trong AI-Agent Workforce, "tin tưởng" không phải là cảm xúc — mà là **cấu hình**. Quyền tự quyết của Agent được **lập trình sẵn**, không phải "trao" dựa trên niềm tin.*

### 2.2. Centralization = CEO quyết tất cả

```
Mô hình Centralized:

  CEO (con người)
    ├── Mọi quyết định chiến lược     ← CEO quyết
    ├── Mọi quyết định chiến thuật    ← CEO quyết
    ├── Chọn giải pháp kỹ thuật       ← CEO quyết
    ├── Approve mọi output            ← CEO quyết
    └── Agent chỉ thực thi lệnh       ← Agent = "bàn tay" của CEO

  Ưu điểm:
    ✅ Nhất quán — mọi output theo 1 vision
    ✅ Kiểm soát chặt — CEO luôn biết đang làm gì
    ✅ An toàn — ít rủi ro Agent tự ý sai

  Nhược điểm:
    ❌ CEO = BOTTLENECK — tổ chức chạy nhanh bằng tốc độ CEO approve
    ❌ Không scale — thêm Agent không tăng tốc, vì mọi thứ vẫn đợi CEO
    ❌ CEO kiệt sức — phải ra 50+ quyết định/ngày
    ❌ Agent "ngu" — không tích lũy khả năng tự quyết
```

### 2.3. Decentralization = Agent tự quyết trong phạm vi

```
Mô hình Decentralized:

  CEO (con người)
    ├── Quyết định chiến lược lớn     ← CEO quyết
    ├── Thiết kế cấu hình Agent        ← CEO quyết (1 lần)
    │
    ├── @MktLead tự quyết:
    │   ├── Chọn angle content          ← @MktLead tự quyết
    │   ├── Phân công task cho Writer   ← @MktLead tự quyết
    │   └── Approve bài viết đã qua QA ← @MktLead tự quyết
    │
    ├── @EngLead tự quyết:
    │   ├── Chọn giải pháp kỹ thuật    ← @EngLead tự quyết
    │   ├── Deploy hotfix              ← @EngLead tự quyết
    │   └── Code review                ← @EngLead tự quyết
    │
    └── Escalation rules:
        → Thay đổi chiến lược          → hỏi CEO
        → Budget > threshold           → hỏi CEO
        → Chủ đề nhạy cảm             → hỏi CEO

  Ưu điểm:
    ✅ Scale — thêm Agent = thêm khả năng tự xử lý
    ✅ Tốc độ — quyết định tại chỗ, không đợi CEO
    ✅ CEO tập trung — chỉ chiến lược, kiến trúc, audit
    ✅ Tổ chức "thông minh hơn" — nhiều điểm ra quyết định

  Nhược điểm:
    ❌ Rủi ro inconsistency — 2 Agent quyết khác nhau
    ❌ Cần cấu hình tốt — Autonomy Scope không rõ → Agent lạm quyền
    ❌ Khó audit — CEO phải tin vào Quality Gate
    ❌ Lỗi cascade — Agent tự quyết sai → chưa ai biết → thiệt hại lan rộng
```

---

## 3. Decision Framework: Khi nào Centralize, khi nào Decentralize?

### 3.1. Ma trận quyết định theo loại quyết định

| Loại quyết định                   | Centralize (CEO) | Decentralize (Agent) | Lý do                                            |
| --------------------------------- | :--------------: | :------------------: | ------------------------------------------------ |
| **Tầm nhìn / Strategy**           |        ✅         |                      | Chỉ CEO có bức tranh tổng → cần nhất quán        |
| **Brand voice / Persona DNA**     |        ✅         |                      | Thay đổi = thay đổi "linh hồn" sản phẩm          |
| **Budget allocation**             |        ✅         |                      | Tác động tài chính rộng                          |
| **Chọn giải pháp kỹ thuật riêng** |                  |          ✅           | Agent Specialist hiểu sâu hơn CEO ở lĩnh vực hẹp |
| **Chọn hook angle bài viết**      |                  |          ✅           | Creativity cần tự do, QA bắt lỗi sau             |
| **Deploy routine hotfix**         |                  |          ✅           | Nhanh, rủi ro thấp, đã có rollback protocol      |
| **Publish nội dung**              |   ✅ (approve)    |     ✅ (thực thi)     | Agent tạo → QA kiểm → CEO approve                |
| **Thay đổi Workflow**             |        ✅         |                      | Meta-level — ảnh hưởng toàn bộ hệ thống          |
| **Thêm/sửa Skill**                |        ✅         |                      | Skill = "kiến thức" — cần Architect giám sát     |
| **Tối ưu CSS/UI cục bộ**          |                  |          ✅           | Phạm vi hẹp, rủi ro thấp, dễ rollback            |

### 3.2. Quy tắc ngón tay cái (Rules of Thumb)

```
→ CENTRALIZE khi:
  [1] Quyết định ảnh hưởng > 1 BU/dự án          (cross-cutting)
  [2] Quyết định không thể rollback dễ dàng       (irreversible)
  [3] Quyết định liên quan đến brand/identity      (strategic)
  [4] Chưa có precedent / chưa ai làm trước đó    (first-time)
  [5] Tác động tài chính trực tiếp                 (financial)

→ DECENTRALIZE khi:
  [1] Quyết định chỉ ảnh hưởng 1 BU/dự án cục bộ  (local)
  [2] Quyết định dễ rollback nếu sai               (reversible)
  [3] Agent Specialist hiểu sâu hơn CEO            (domain expertise)
  [4] Cần tốc độ — chờ CEO = bottleneck             (speed)
  [5] Đã có precedent / đã làm nhiều lần            (routine)
  [6] Đã có Quality Gate tự động bắt lỗi            (safety net)
```

### 3.3. Ma trận 2 chiều: Impact × Reversibility

```
                    DỄ ROLLBACK ◄──────────────► KHÓ ROLLBACK
                         │                            │
    TÁC ĐỘNG LỚN        │   ★ DECENTRALIZE          │   ★ CENTRALIZE
    (Cross-BU,           │   + Quality Gate            │   CEO phải approve
     Strategic)          │   VD: Chọn tech stack       │   VD: Thay đổi brand
                         │   cho feature mới           │   voice, pivot strategy
                         │                            │
    ─────────────────────┼────────────────────────────┤
                         │                            │
    TÁC ĐỘNG NHỎ        │   ★ FULL AUTONOMY          │   ★ DECENTRALIZE
    (Local, 1 BU,        │   Agent tự quyết hoàn toàn │   + Notify CEO sau
     Operational)        │   VD: Chọn CSS color,       │   VD: Delete production
                         │   rewrite 1 function        │   data, change API keys
                         │                            │
```

---

## 4. Áp dụng cho 5 thành phần: Centralize hay Decentralize cái gì?

### 4.1. Agent — Centralize CẤU HÌNH, Decentralize THỰC THI

```
┌────────────────────────────────────────────────────────────────┐
│  CENTRALIZE (CEO / Architect quyết):                           │
│  ○ Tạo/loại bỏ Agent (Provisioning / Decommissioning)         │
│  ○ Định nghĩa 11 Elements (Identity, Mission, Autonomy...)    │
│  ○ Gán Skill Profile → Agent                                  │
│  ○ Thay đổi Escalation Protocol                               │
│  ○ Thiết lập Code of Conduct                                  │
│                                                                │
│  DECENTRALIZE (Agent tự quyết — trong Autonomy Scope):         │
│  ○ Chọn approach/methodology cho task cụ thể                   │
│  ○ Quyết định trình tự thực thi bên trong Workflow            │
│  ○ Tạo/sửa file trong phạm vi BU context                     │
│  ○ Cross-call Agent khác theo Interface Contract               │
│  ○ Tự ghi Changelog, tạo Notes trong Agent Folder             │
└────────────────────────────────────────────────────────────────┘
```

**Lý do:** Agent Definition là "hiến pháp cá nhân" — phải do Architect thiết kế. Nhưng bên trong phạm vi đã cấu hình, Agent phải TỰ QUYẾT — nếu không, CEO trở thành bottleneck.

### 4.2. Workflow — Centralize THIẾT KẾ, Decentralize THỰC THI

```
┌────────────────────────────────────────────────────────────────┐
│  CENTRALIZE (Architect / Meta-Workflow):                       │
│  ○ Tạo Workflow mới (/buildflow)                              │
│  ○ Gán Tier (Meta/Orchestration/Execution/Utility)            │
│  ○ Định nghĩa Cross-calling Interface                         │
│  ○ Thay đổi quy trình Workflow đã có                          │
│  ○ Loại bỏ / gộp Workflow                                    │
│                                                                │
│  DECENTRALIZE (Agent Owner thực thi):                          │
│  ○ Chọn biến thể (variant) khi Workflow cho phép              │
│  ○ Skip bước optional nếu context không cần                   │
│  ○ Thêm ghi chú, observation vào output                       │
│  ○ Gọi Utility Workflow (Tier 3) khi cần                      │
│  ○ Escalate khi gặp edge case                                 │
└────────────────────────────────────────────────────────────────┘
```

**Lý do:** Workflow là "quy trình chuẩn" — nếu mỗi Agent tự ý sửa quy trình, toàn bộ hệ thống mất nhất quán. Nhưng Agent cần linh hoạt **bên trong** quy trình.

### 4.3. Skill — LUÔN CENTRALIZE quản lý

```
┌────────────────────────────────────────────────────────────────┐
│  CENTRALIZE (Architect / Trainer):                             │
│  ○ Viết / cập nhật SKILL.md                                   │
│  ○ Quyết định Agent nào nạp Skill nào                         │
│  ○ Version control Skill                                      │
│  ○ Audit Skill overlap / conflict                             │
│  ○ Dịch / localize Skill                                     │
│                                                                │
│  Agent KHÔNG TỰ Ý:                                            │
│  ✗ Tạo Skill mới                                              │
│  ✗ Sửa SKILL.md                                              │
│  ✗ Tự nạp Skill chưa được assign                             │
│  ✗ Reinterpret Skill theo cách riêng                         │
│                                                                │
│  Ngoại lệ:                                                    │
│  ○ Meta Agent (VD: @AI_RM) có thể đề xuất Skill mới —        │
│    nhưng vẫn cần Architect approve                             │
└────────────────────────────────────────────────────────────────┘
```

**Lý do:** Skill là **kiến thức** — nếu Agent tự ý tạo/sửa Skill, kiến thức bị biến dạng không kiểm soát. Skill phải được quản lý như "sách giáo khoa" — chỉ Trainer/Architect có quyền viết.

### 4.4. Rules — LUÔN CENTRALIZE (Hiến pháp)

```
┌────────────────────────────────────────────────────────────────┐
│  CENTRALIZE TUYỆT ĐỐI (CEO / Architect):                      │
│  ○ Định nghĩa Global Rules (MEMORY files)                     │
│  ○ Thêm / sửa / xóa Rules                                    │
│  ○ Enforce Rules cho mọi Agent                                │
│                                                                │
│  KHÔNG BAO GIỜ DECENTRALIZE:                                  │
│  ✗ Agent không tự ý tạo Rule mới                              │
│  ✗ Agent không được "giải thích" Rule theo cách riêng          │
│  ✗ Agent không có ngoại lệ                                    │
│                                                                │
│  Lý do: Rules = Hiến pháp                                     │
│  → Thay đổi Rules = thay đổi nền tảng toàn tổ chức           │
│  → Chỉ "Quốc hội" (CEO + Architect) có quyền sửa              │
└────────────────────────────────────────────────────────────────┘
```

### 4.5. Knowledge — Centralize QUẢN TRỊ, Decentralize TẠO MỚI

```
┌────────────────────────────────────────────────────────────────┐
│  CENTRALIZE (Knowledge Agent / @AI_RM):                        │
│  ○ Index toàn bộ Knowledge Items                              │
│  ○ Merge / deduplicate KI                                     │
│  ○ Retire KI outdated                                         │
│  ○ Thiết lập ownership cho từng KI                            │
│                                                                │
│  DECENTRALIZE (Mọi Agent có quyền):                            │
│  ○ Tra cứu KI bất kỳ lúc nào                                 │
│  ○ Tạo KI mới từ cuộc hội thoại (/beat)                      │
│  ○ Đề xuất cập nhật KI                                       │
│  ○ Tham chiếu KI trong output                                │
│                                                                │
│  Lý do: Knowledge là "bộ nhớ tập thể"                         │
│  → Mọi Agent cần truy cập (đọc = decentralize)               │
│  → Nhưng cần 1 "thủ thư" quản lý chất lượng (viết = centralize) │
└────────────────────────────────────────────────────────────────┘
```

### 4.6. Tổng hợp: Ma trận Centralize/Decentralize theo thành phần

| Thành phần    | CẤU HÌNH / QUẢN TRỊ |  THỰC THI / SỬ DỤNG  | Lý do ngắn gọn                        |
| ------------- | :-----------------: | :------------------: | ------------------------------------- |
| **Agent**     |     Centralize      |     Decentralize     | Thiết kế tập trung, thực thi phân tán |
| **Workflow**  |     Centralize      |     Decentralize     | "Luật chơi" tập trung, "chơi" tự do   |
| **Skill**     |     Centralize      |      (Chỉ đọc)       | Kiến thức phải chuẩn, không biến dạng |
| **Rules**     |     Centralize      |    (Chỉ tuân thủ)    | Hiến pháp — không ai sửa ngoài CEO    |
| **Knowledge** | Centralize quản trị | Decentralize tạo/đọc | Bộ nhớ tập thể cần quản lý chất lượng |

---

## 5. Mô hình bố trí tài nguyên trên File System

### 5.1. Centralized Model: Mọi thứ ở Root

```
Command Center/
├── .agents/                    ← TẤT CẢ Agent, Workflow, Skill
│   ├── workflows/
│   │   ├── content-post.md
│   │   ├── deploy.md
│   │   ├── seo-audit.md
│   │   └── ... (100+ files)
│   └── skills/
│       ├── copywriting/SKILL.md
│       ├── marketing-psychology/SKILL.md
│       └── ... (50+ files)
│
├── 05_5Balance/               ← Chỉ có SOURCE CODE + DOC
│   ├── src/
│   └── DOC/
├── 06_Hoctap.tech/            ← Chỉ có SOURCE CODE + DOC
└── ...

Ưu điểm:
  ✅ Không duplicate Skill/Workflow → SSOT tự nhiên
  ✅ Dễ audit — tất cả ở 1 nơi
  ✅ 1 Skill update → mọi Agent cùng lúc

Nhược điểm:
  ❌ Context switching: Agent phải "nhảy" giữa root và BU
  ❌ Pollution: Skill không liên quan đến BU vẫn hiển thị
  ❌ Không customize: Mọi BU dùng chung config
     → Ví dụ: /deploy cho 5Balance KHÁC HẲN /deploy cho Hoctap.tech
```

### 5.2. Distributed Model: Mỗi BU tự chứa

```
Command Center/
├── 05_5Balance/
│   ├── .agent/                ← Agent/Workflow/Skill RIÊNG cho 5Balance
│   │   ├── workflows/
│   │   │   ├── deploy.md      ← Deploy flow riêng cho 5Balance
│   │   │   └── ...
│   │   └── skills/
│   │       ├── bazi-engine/SKILL.md   ← Domain-specific
│   │       └── ...
│   ├── src/
│   └── DOC/
│
├── 06_Hoctap.tech/
│   ├── .agent/                ← Agent/Workflow/Skill RIÊNG cho Hoctap
│   │   ├── workflows/
│   │   │   ├── deploy.md      ← Deploy flow riêng cho Hoctap
│   │   │   └── ...
│   │   └── skills/
│   └── ...

Ưu điểm:
  ✅ Context sâu — Agent chỉ thấy Skill/Workflow liên quan
  ✅ Customize — mỗi BU có pipeline riêng
  ✅ Self-contained — cắt 1 BU ra vẫn hoạt động

Nhược điểm:
  ❌ Duplicate: Skill "copywriting" copy ở 5 nơi → sửa 1 quên 4
  ❌ Drift: /deploy ở BU A khác BU B → không ai biết cái nào đúng
  ❌ Audit khó: Phải scan tất cả BU để tìm hết Workflow
```

### 5.3. Federated Model (Hybrid) — Khuyến nghị

```
Command Center/
├── .agents/                    ← GLOBAL: Core Skill, Workflow dùng chung
│   ├── workflows/
│   │   ├── go.md               ← Router — dùng chung
│   │   ├── content-post.md     ← Orchestration — dùng chung
│   │   ├── fix.md              ← Utility — dùng chung
│   │   └── ...
│   └── skills/
│       ├── copywriting/        ← Core Skill — dùng chung
│       ├── sprint-centric/     ← Core Skill — dùng chung
│       └── ...
│
├── 05_5Balance/
│   ├── .agent/                ← PROJECT: Override + Domain-specific
│   │   ├── workflows/
│   │   │   ├── deploy.md      ← Override: deploy RIÊNG cho 5Balance
│   │   │   └── bazi-pipeline.md ← Domain-specific: chỉ 5Balance có
│   │   └── skills/
│   │       ├── bazi-engine/    ← Domain Skill: chỉ 5Balance cần
│   │       └── 5balance-design/ ← Domain Skill: design tokens riêng
│   └── ...
│
├── 06_Hoctap.tech/
│   ├── .agent/                ← PROJECT: Override + Domain-specific
│   │   ├── workflows/
│   │   │   ├── deploy.md      ← Override: deploy RIÊNG cho Hoctap
│   │   │   └── course-pipeline.md ← Domain-specific: chỉ Hoctap có
│   │   └── skills/
│   │       └── course-design/  ← Domain Skill: chỉ Hoctap cần
│   └── ...

QUY TẮC TÌM KIẾM (Resolution Order):
  1. Tìm trong .agent/ (project-level) TRƯỚC
  2. Nếu không có → tìm trong .agents/ (global-level)
  3. Project-level OVERRIDE global-level nếu trùng tên
```

**Tại sao Federated Model tốt nhất:**

| Tiêu chí            | Centralized | Distributed | Federated ✅ |
| ------------------- | ----------- | ----------- | ----------- |
| **Tái sử dụng**     | ⭐⭐⭐         | ⭐           | ⭐⭐⭐         |
| **Context sâu**     | ⭐           | ⭐⭐⭐         | ⭐⭐⭐         |
| **Không duplicate** | ⭐⭐⭐         | ⭐           | ⭐⭐          |
| **Customize**       | ⭐           | ⭐⭐⭐         | ⭐⭐⭐         |
| **Dễ audit**        | ⭐⭐⭐         | ⭐           | ⭐⭐          |
| **Scalable**        | ⭐⭐          | ⭐⭐          | ⭐⭐⭐         |

---

## 6. Lateral Power Shift — Quyền lực dịch chuyển ngang

### 6.1. Khái niệm

Galbraith nhận ra rằng quyền lực không chỉ chảy **dọc** (CEO ↔ IC) mà còn chảy **ngang** — tạm thời dịch chuyển sang đơn vị nào đang xử lý vấn đề trọng yếu nhất.

**Trong AI-Agent Workforce, lateral power shift xảy ra qua:**

```
Tình huống: Bug critical trên production 5Balance

Bình thường:
  CEO → @MktLead → @Writer (content creation pipeline)
  @EngLead chạy song song, không can thiệp

Khi có bug critical:
  CEO → @EngLead "TAKE OVER"
    → @EngLead tạm thời có quyền:
      ✓ Dừng deployment mọi BU
      ✓ Yêu cầu @Writer tạm ngừng publish
      ✓ Gọi @DeployOps direct (bypass chain)
      ✓ Quyết định rollback không cần CEO approve

  → Sau khi fix:
    → @EngLead trả lại quyền về trạng thái bình thường
    → Ghi incident vào Knowledge (/beat)
```

### 6.2. Khi nào xảy ra Lateral Power Shift?

| Trigger                           | Agent nhận quyền     | Quyền tạm thời                         |
| --------------------------------- | -------------------- | -------------------------------------- |
| **Bug critical production**       | @EngLead             | Freeze deploy, bypass chain            |
| **PR crisis / nội dung nhạy cảm** | @MktLead             | Freeze publish, recall content         |
| **Data breach / security**        | @SecurityAgent       | Shutdown external access               |
| **Deadline campaign launch**      | Campaign Owner Agent | Ưu tiên resource, skip non-critical QA |
| **Budget overrun**                | @FinanceOps          | Freeze mua sắm, yêu cầu justify        |

### 6.3. Thiết kế Lateral Power Shift Protocol

```yaml
lateral_power_shift:
  trigger: "production_incident_p0"
  activated_agent: "@EngLead"
  temporary_powers:
    - freeze_all_deployments
    - bypass_chain_to_specialist
    - rollback_without_ceo_approval
  duration: "until_incident_resolved"
  notification: ["CEO", "@MktLead", "@PM"]
  post_resolution:
    - return_to_normal_power
    - write_postmortem_to_knowledge
    - update_agent_folder_changelog
```

---

## 7. Autonomy Levels — Cấu hình quyền tự chủ

### 7.1. Mô hình 5 mức Autonomy

| Level  | Tên               | Agent quyết gì?                    | CEO can thiệp khi nào?               |
| ------ | ----------------- | ---------------------------------- | ------------------------------------ |
| **L1** | Execute Only      | Không quyết gì — chỉ thực thi lệnh | CEO phải ra lệnh từng bước           |
| **L2** | Suggest & Execute | Đề xuất → đợi approve → thực thi   | CEO approve từng quyết định          |
| **L3** | Decide & Inform   | Tự quyết → thông báo CEO sau       | CEO review log, can thiệp nếu sai    |
| **L4** | Full Autonomy     | Tự quyết hoàn toàn trong scope     | CEO chỉ audit định kỳ                |
| **L5** | Self-Evolving     | Tự quyết + tự điều chỉnh approach  | CEO chỉ thiết lập boundaries ban đầu |

### 7.2. Gán Autonomy Level theo vai trò

| Agent Role     | Level mặc định | Lý do                                              |
| -------------- | -------------- | -------------------------------------------------- |
| **@Writer**    | L3             | Tự chọn hook/style, CEO review output cuối         |
| **@EngLead**   | L4             | Tech decisions cần chuyên môn sâu, CEO audit sau   |
| **@DeployOps** | L3–L4          | Routine deploy = L4. Major deployment = L3         |
| **@PM**        | L3             | Tự quản sprint, escalate khi scope change          |
| **@AI_RM**     | L2–L3          | Đề xuất restructure, CEO approve trước khi áp dụng |
| **@QA**        | L4             | Quality gate phải tự động — không đợi CEO          |
| **Router /go** | L4             | Routing phải instant — đợi CEO = bottleneck        |

### 7.3. Dynamic Autonomy: Level thay đổi theo ngữ cảnh

```
Agent @Writer trong điều kiện bình thường:
  → Autonomy Level: L3 (Decide & Inform)
  → Tự chọn hook, cấu trúc, viết bài → thông báo CEO

Agent @Writer khi viết về chủ đề nhạy cảm:
  → Autonomy Level: L2 (Suggest & Execute)
  → Đề xuất nội dung → đợi CEO approve → mới publish

Agent @Writer khi có precedent (đã viết 10 bài tương tự, đều tốt):
  → Autonomy Level: L4 (Full Autonomy)
  → Tự viết tự publish, CEO chỉ audit mẫu định kỳ
```

---

## 8. Anti-patterns Distribution of Power

### Anti-pattern 1: Bot Army — Centralize quá mức

```
❌ CEO phải approve MỌI output, kể cả commit message và CSS tweak
→ CEO = bottleneck, Agent = "bàn tay" thụ động
→ Không scale, CEO kiệt sức
→ FIX: Cấu hình Autonomy Scope rõ ràng. L3–L4 cho operational tasks
```

### Anti-pattern 2: Wild West — Decentralize quá mức

```
❌ Mọi Agent tự quyết tất cả, không ai kiểm tra
→ Output inconsistent, lỗi cascade, brand voice biến dạng
→ CEO không biết hệ thống đang chạy thế nào
→ FIX: Quality Gate bắt buộc. Escalation Protocol rõ ràng
```

### Anti-pattern 3: Permission Vacuum

```
❌ Không rõ ai quyết gì — Agent không biết nên tự quyết hay hỏi CEO
→ Agent có xu hướng "hỏi cho chắc" → mọi thứ lên CEO → thành Centralized
→ HOẶC Agent "tự quyết cho nhanh" → mọi thứ sai mà không ai biết
→ FIX: Định nghĩa rõ Autonomy Scope (Element 3) cho TỪNG Agent
```

### Anti-pattern 4: Frozen Autonomy

```
❌ Autonomy Level cố định — Agent mới và Agent 6 tháng tuổi cùng mức
→ Agent có kinh nghiệm (nhiều precedent) vẫn bị kìm
→ Agent mới (chưa có precedent) được tự do quá mức
→ FIX: Dynamic Autonomy — tăng Level khi có track record, giảm khi đổi domain
```

### Anti-pattern 5: Niềm tin ngây thơ vào Quality Gates (Red Team Warning)

```
❌ Trao quyền L4/L5 cho Agent và tin rằng Agent QA (Quality Gate) sẽ luôn bắt lỗi kịp thời.
→ Khi cả nhóm thực thi và nhóm QA cùng bị "ảo giác" (Shared hallucination), hệ thống sẽ gây hậu quả khôn lường.
→ FIX: Phân tán quyền lực luôn phải đi kèm **Circuit Breakers (Cầu dao tự động ngắt)** bằng code cứng. (Vd: Hard-code giới hạn chỉ được thao tác tối đa 10 email/phút, nếu vượt trigger Error cứng chấm dứt tiến trình).
```

---

## 9. Nguyên tắc Distribution of Power cho AI-Agent Workforce

| #       | Nguyên tắc                                           | Giải thích                                                          |
| ------- | ---------------------------------------------------- | ------------------------------------------------------------------- |
| **DP1** | **Centralize cấu hình, Decentralize thực thi**       | CEO thiết kế Agent, Agent tự chạy bên trong phạm vi                 |
| **DP2** | **Autonomy = Cấu hình, không phải niềm tin**         | Tự chủ được lập trình sẵn, không "trao" dựa trên cảm tính           |
| **DP3** | **Escalation Protocol bắt buộc**                     | Mọi Agent phải biết khi nào hỏi cấp trên — cấu hình trong Element 3 |
| **DP4** | **Impact × Reversibility quyết định mức centralize** | Tác động lớn + khó rollback = CEO quyết. Ngược lại = Agent quyết    |
| **DP5** | **Rules và Skill luôn centralize**                   | "Hiến pháp" và "sách giáo khoa" phải do trung ương quản lý          |
| **DP6** | **Knowledge decentralize tạo, centralize quản trị**  | Mọi Agent tạo KI, nhưng thủ thư giữ chất lượng                      |
| **DP7** | **Federated Model cho file system**                  | Global core + Project-specific overlay = cân bằng tốt nhất          |
| **DP8** | **Dynamic Autonomy theo ngữ cảnh**                   | Cùng Agent có thể L2 hoặc L4 tùy loại task                          |
| **DP9** | **Lateral Power Shift cho khẩn cấp**                 | Quyền lực tạm dịch ngang khi có incident — có protocol rõ           |

---

## 10. Decision Canvas bổ sung: Distribution of Power

### Cho từng Agent, trả lời:

| Câu hỏi                                   | Trả lời       |
| ----------------------------------------- | ------------- |
| Agent này có Autonomy Level nào? (L1–L5)  | _____________ |
| Những gì Agent tự quyết? (`can_decide`)   | _____________ |
| Những gì phải escalate? (`must_escalate`) | _____________ |
| Khi nào Autonomy Level thay đổi?          | _____________ |
| Agent này có quyền tạo Knowledge mới?     | _____________ |
| Agent này có quyền cross-call Agent nào?  | _____________ |

### Cho toàn tổ chức, trả lời:

| Câu hỏi                                                 | Trả lời         |
| ------------------------------------------------------- | --------------- |
| Tỷ lệ quyết định qua CEO vs. Agent tự quyết?            | _____ / _____ % |
| Có Lateral Power Shift Protocol?                        | Có / Chưa       |
| File system dùng Centralized / Distributed / Federated? | _____________   |
| Quality Gate tự động bao phủ bao nhiêu % output?        | _____ %         |
| CEO có thể vắng 1 ngày mà hệ thống vẫn chạy?            | Có / Chưa       |

> **Litmus Test:** Nếu CEO vắng 1 ngày mà hệ thống **dừng hoàn toàn** → centralize quá mức. Nếu CEO vắng 1 ngày mà **không biết xảy ra chuyện gì** → decentralize quá mức.

---

## 11. Liên kết với các chương khác

- **Chương 1 (Specialization):** Agent Specialist cần Autonomy Level cao hơn trong domain — vì chỉ Agent đó có đủ chuyên môn
- **Chương 2 (Shape):** Tổ chức flat → cần decentralize nhiều hơn (không có tầng trung gian). Tổ chức tall → có thể centralize hơn ở tầng Director
- **Chương 4 (Departmentalization):** Mỗi "department" (nhóm Agent) nên có mức autonomy riêng — BU mature = decentralize hơn
- **Chương 5 (Processes):** Vertical processes (escalation) là cơ chế centralize. Lateral processes (cross-calling) là cơ chế decentralize
