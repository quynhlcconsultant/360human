# Chương 17: Nguyên tắc vận hành — 5 Operational Principles

> **Câu hỏi cốt lõi:** *Tổ chức AI-Agent Workforce vận hành hàng ngày theo nguyên tắc nào?*

---

## 1. Think-Out-Loud (TOL) — Minh bạch hóa suy luận

```
NGUYÊN TẮC:
  Mọi Agent phải ghi lại QUÁ TRÌNH SUY LUẬN, không chỉ kết quả.

TẠI SAO:
  → CEO không "ngồi cạnh" Agent → cần biết Agent nghĩ gì
  → Debug: khi output sai, trace ngược → biết SAI Ở ĐÂU
  → Audit: kiểm tra Agent có "hiểu" hay chỉ "đoán"
  → Học hỏi: chưng cất Decision Log → Knowledge Items

CÁC VẬT:
  → Sprint Plan: TOL Recording section
  → Decision Log: danh sách lựa chọn + lý do chọn/bỏ
  → Process Notes: ghi lại quá trình thực hiện

QUY TẮC:
  → Agent LUÔN giải thích WHY trước khi làm WHAT
  → Khi có nhiều lựa chọn → liệt kê tất cả → giải thích chọn cái nào → tại sao
  → Ghi vào Sprint artifacts để CEO review
```

---

## 2. Sprint-Centric — Mọi việc thuộc 1 Sprint

```
NGUYÊN TẮC:
  Mọi task phải thuộc 1 Sprint cụ thể. Không có task "ngoài Sprint".

TẠI SAO:
  → Traceability: biết task thuộc đợt nào
  → Accountability: biết ai làm gì trong khoảng nào
  → Review: CEO review theo Sprint → có rhythms
  → Scope control: tránh scope creep

CẤU TRÚC SPRINT:
  SPRINTS/
  ├── SP-YYMMDD-NN-TenSprint/    ← Mỗi Sprint = 1 folder
  │   ├── Sprint_Plan.md          ← Kế hoạch, TOL
  │   ├── Sprint_Checklist.md     ← Tracking progress
  │   └── DOCS/                   ← Deliverables
  │       ├── output_1.md
  │       └── output_2.md

QUY TẮC:
  → Sprint ID format: SP-YYMMDD-NN-TenSprint
  → Task ID format: TASK-NNN (trong Sprint)
  → Mỗi Sprint có Definition of Done (DoD) rõ ràng
  → Sprint kết thúc → CEO review → close hoặc extend
```

---

## 3. Changelog — Ghi lại mọi thay đổi

```
NGUYÊN TẮC:
  Mọi thay đổi quan trọng phải được ghi vào Changelog.

TẠI SAO:
  → Audit trail: biết ai sửa gì khi nào
  → Rollback: nếu sai → biết version nào đúng
  → Communication: Agent khác biết hệ thống đã thay đổi gì
  → Compliance: đáp ứng yêu cầu governance

FORMAT:
  ## [YYYY-MM-DD]
  ### Thêm mới
  - Tạo Agent @NewRole với Skill Profile [...]
  ### Thay đổi
  - Cập nhật /deploy workflow: thêm bước rollback check
  ### Loại bỏ
  - Retire Skill "legacy-seo" → thay bằng "ai-seo"

ÁP DỤNG:
  → Agent Folder → Changelog.md (mỗi Agent)
  → Project → CHANGELOG.md (mỗi dự án)
  → Sprint Folder → trong Sprint_Checklist.md
```

---

## 4. SSOT (Single Source of Truth) — 1 nguồn duy nhất

```
NGUYÊN TẮC:
  Mỗi thông tin chỉ tồn tại ở 1 NƠI DUY NHẤT. Mọi nơi khác phải THAM CHIẾU.

TẠI SAO:
  → Consistency: không có 2 version khác nhau
  → Update: sửa 1 nơi = sửa toàn hệ thống
  → Trust: mọi người biết "source of truth" ở đâu

QUY TẮC:
  → Thông tin CHÍNH nằm ở SOURCE → mọi nơi khác LINK đến
  → Khi cập nhật → chỉ sửa SOURCE → link tự reflect
  → Khi phát hiện duplicate → merge về 1 source

VÍ DỤ:
  → Agent skill definition → SSOT: SKILL.md trong Skill_Hub
  → Workflow definition → SSOT: workflow.md trong Workflow_Hub
  → Strategy → SSOT: Strategy.md trong Context Folder
  → Agent identity → SSOT: JD.md trong Agent Folder
```

---

## 5. Indexing & Metadata Navigation (Đánh mục lục và Định vị bằng YAML)

```
NGUYÊN TẮC:
  Mọi file/folder mới tạo phải được ghi vào INDEX. Không có file "vô hình".

TẠI SAO:
  → Discoverability: Agent mới → đọc INDEX → biết hệ thống có gì
  → Trùng lặp: INDEX giúp phát hiện trước khi tạo duplicate
  → Audit: scan INDEX → biết có file nào thiếu
  → Navigation: CEO tìm nhanh tài liệu cần

CÁC LOẠI INDEX:
  → Workflow Index: danh sách tất cả Workflow + tier + owner
  → Skill Index: danh sách tất cả Skill + status + assigned agents
  → Agent Index: danh sách tất cả Agent + role + cluster
  → KI Index: danh sách tất cả Knowledge Items + topics
```

### 5.1. YAML Frontmatter — Trạm định vị tốc độ cao (Routing Station)

Bên cạnh việc lập file báo cáo INDEX định kỳ, một Best Practice bắt buộc là **luôn tạo khối YAML Frontmatter ở đầu mỗi file tài liệu**.
- **Định dạng:** Mở và đóng bằng `---`, chứa các thẻ như `id`, `type`, `description`, `owner`.
- **Tác dụng:** Giúp AI có thể **nhanh chóng điều hướng tới vị trí của tài liệu cần thiết** thông qua việc đọc lướt khối metadata (hoặc dùng script tự động), thay vì phải tốn Cost/Token dùng lệnh Grep search hoặc đọc toàn bộ nội dung text của file. YAML biến một file text phẳng thành một Data Node có thể tự động routing.

### 5.2. Cảnh báo Red Team: Documentation Fatigue (Kiệt sức vì Ghi chép)

**Lỗ hổng:** Việc bắt buộc Agent cập nhật Changelog, TOL, Naming Rules ngay lập tức một cách ĐỒNG BỘ trong mọi task sẽ làm cho hệ thống cạn kiệt Tokens nhanh chóng. Chi phí API tăng phi mã và Agent tốn 70% cost chỉ để làm tài liệu thay vì value creation.

**Giải pháp:** Triển khai **Asynchronous Batch Logging (Ghi chép mẻ bất đồng bộ)**. Các Agent đang xử lý core value chỉ được phép để lại "Notes/Draft mỏng" ở dạng JSON lộn xộn dọc đường. Sẽ có một *Utility Agent (VD: @Doc_Agent)* thức dậy vào cuối ca để gom "mẻ", format lại, và cập nhật chính quy vào INDEX / CHANGELOG. Con người không cần log real-time mà cần log định kỳ.

---

## 6. Tổng hợp 5 nguyên tắc

| #       | Nguyên tắc     | Một câu                                       |
| ------- | -------------- | --------------------------------------------- |
| **OP1** | Think-Out-Loud | Ghi lại quá trình suy luận, không chỉ kết quả |
| **OP2** | Sprint-Centric | Mọi task thuộc 1 Sprint cụ thể                |
| **OP3** | Changelog      | Mọi thay đổi có audit trail                   |
| **OP4** | SSOT           | 1 thông tin = 1 nguồn duy nhất                |
| **OP5** | Indexing       | File mới → phải có trong INDEX                |
