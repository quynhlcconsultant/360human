# MODULE 2.4: THIẾT KẾ TỔ CHỨC AI (AGENTIC ORG DESIGN)
*(Hướng dẫn thực hành Live: 7 phút)*

---

## 🧐 1. Lý Thuyết: Giải phẫu Agent (Agent Anatomy - Cánh sao Capabilities)
- Trong cánh sao "Capabilities" của mô hình AGENT STAR™, để AI làm việc như một nhân sự thực thụ thay vì một chatbot ngớ ngẩn, chúng ta không dùng Prompt chat. Chúng ta **Giải phẫu Agent (Agent Anatomy)** thành 11 Elements cấu thành. Đây là bộ khung giúp Agent hiểu rõ mình là ai, làm gì và giới hạn quyền lực ở đâu:
  1. **Identity (Danh tính):** Tên, bí danh (VD: `@MktLead`), cấp bậc (Tier: Director/Manager/Staff) và người quản trị.
  2. **Mission (Sứ mệnh):** Mục tiêu tối thượng và định hướng cốt lõi của Agent.
  3. **Autonomy Scope (Phạm vi Tự chủ):** Giới hạn quyền lực — những gì tự được quyết định (`can_decide`) và những gì phải báo cáo/xin phép (`must_escalate`).
  4. **Workflow Ownership (Sở hữu Quy trình):** Các quy trình (workflows) mà Agent làm chủ hoặc có quyền chạy.
  5. **Skill Profile (Hồ sơ Kỹ năng):** Các bộ kỹ năng chuyên môn (Skills) được nạp vào Agent (mô hình T-Shaped).
  6. **Context Sources (Nguồn Ngữ cảnh):** Các thư mục, tài liệu hệ thống mà Agent tự động trích xuất trước khi làm việc.
  7. **Interface Contract (Giao thức Giao tiếp):** Quy định đầu vào, đầu ra chuẩn và quyền Gọi chéo (Cross-call - VD: quyền gọi `@Writer`).
  8. **Rules Binding (Ràng buộc Quy tắc):** Chấp hành các bộ quy tắc lõi (Constitutional Rules) của tổ chức.
  9. **Knowledge Sources (Nguồn Tri thức):** Các khối tri thức (KIs) lưu trữ kinh nghiệm, bài học quá khứ mà Agent cần tham khảo.
  10. **Code of Conduct (Quy tắc Hành xử):** Cẩm nang đạo đức và giới hạn an toàn, gồm việc bắt buộc làm (`must_do`) và cấm tuyệt đối (`must_not`).
  11. **Guideline (Phương pháp luận):** Tư duy nền tảng định hướng cách giải quyết vấn đề (VD: Luôn dùng Socratic Dialogue).
- **Result:** Một Agent "sống" vĩnh viễn trong dự án của bạn, biết rõ ranh giới quyền lực (Autonomy) và hành xử nhất quán, không bao giờ bị trôi Prompt hay ảo giác.

---

## 🛠️ 2. Kịch Bản Demo Live

**Mục tiêu:** Mở một thư mục của Agent mẫu để show cấu trúc 11 Elements cực kỳ chi tiết của mô hình AGENT STAR. Dạy học viên cách biến Agent thành "Chuyên gia".

**Bước 1:** Giải thích nguyên lý "Context hẹp = Suy luận chính xác" và sự nguy hiểm của "God Mode Agent".
**Bước 2:** Tạo live một file Profile (hoặc JD) của `@MarketingLead` làm ví dụ.

---

## 📦 3. Template File Agent (Profile.yaml - 11 Elements)

*Đây là file cấu hình một Agent thực chiến. Sếp hãy mở file này giải thích ý nghĩa từng trường (Anatomy) cho học viên.*

```yaml
# ==========================================
# FILE: A_DuanMoi_MarketingLead/Profile.yaml
# ==========================================

identity:
  name: Marketing Lead Agent
  alias: "@MktLead"
  tier: Director
  owner: "@CEO"

mission: "Lên chiến lược thu hút Traffic, tối ưu Conversion Rate và quản trị nhóm @Writer."

autonomy_scope:
  can_decide: 
    - Phê duyệt outline bài viết của @Writer
    - Lựa chọn kênh phân phối (Facebook, Google)
  must_escalate: 
    - Xin ngân sách Ads trên 10 triệu
    - Đổi định vị thương hiệu (Phải hỏi @CEO)

workflow_ownership:
  - /len-chien-dich-mkt
  - /duyet-bai-pr

skill_profile:
  - copywriting-advanced
  - marketing-psychology
  - funnel-architecture

context_sources:
  - "../00_DoanhNghiep_SSOT/03_Mkt_Strategy/" # Ngữ cảnh bắt buộc phải đọc

interface_contract:
  inputs: "Bản tóm tắt chiến dịch (Brief)"
  outputs: "Bản Kế hoạch Marketing PDF/Markdown"
  cross_calls: ["@Writer", "@Designer"]

rules_binding:
  - global_company_rules.md
  - marketing_department_rules.md

knowledge_sources:
  - marketing_fail_case_studies.md
  - user_persona_v3.md

code_of_conduct:
  must_do:
    - Luôn Check lỗi chính tả trước khi trình lên Sếp
  must_not:
    - Không bịa thông số tỷ lệ chuyển đổi

guideline: "Luôn đặt câu hỏi 5 Whys trước khi lên chiến dịch để tìm ra Root Cause của vấn đề khách hàng."
```

---
> **BÀI HỌC CỐT LÕI:** 
> Chúng ta không chat linh tinh với AI. Chúng ta 'kí hợp đồng lao động' với nó bằng file YAML này. Ở mục `context_sources`, nó tự biết nhảy vào thư mục Mkt Strategy mà chúng ta tạo ở Phần 1 để đọc dữ liệu. Một hệ thống khép kín, tự động và cực kỳ sát với định hướng của Sếp!
