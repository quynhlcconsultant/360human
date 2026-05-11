# Phần 2: Framework Tổ chức AI-Agent (AGENT STAR™)

**Mục tiêu:** Thoát khỏi tư duy "Sử dụng Tool AI (Prompting)" để bước lên vị thế "Thiết kế và Quản trị Lực lượng lao động tự trị" thông qua kiến trúc quản trị hình sao (AGENT STAR™ vs 12 Elements).

## 2.1 Cơn Khủng Hoảng Của Những "Dòng Prompt Tùy Tiện"

- Tình trạng hiện tại: Cá nhân/Tổ chức tùy tiện copy vài dòng Prompt "Bạn là chuyên gia..." và gọi đó là Agent. Hậu quả sinh ra rác không gian mờ (System Pollution), AI trùng lặp công năng, đứt gãy tính kế thừa và tuyệt đối không ai nắm trách nhiệm giải trình.
- **Sự chuyển đổi gốc rễ (Reframing):** Phải ngừng coi AI là "Công cụ trả lời" (Tool). AI là một **Workforce (Lực lượng lao động)** thực thụ. Để tránh sụp đổ tổ chức, Workforce số bắt buộc phải được quy hoạch bằng một Framework Sơ đồ tổ chức (Org Chart) khắc nghiệt y hệt con người.

## 2.2 Đào Sâu 5 Cánh Sao AGENT STAR™

Được sinh ra từ nền tảng Star Model (Galbraith), AGENT STAR lấy AI làm tâm điểm thiết kế. Bất kỳ Giám đốc AI nào cũng phải căn chỉnh 5 hệ quy chiếu sau:

- **Strategy (Chiến lược - Hybrid Context):** Bối cảnh lai. AI và Người dùng (Core Team) phải nhìn cùng một cờ hiệu, hít chung một dòng dữ liệu.
- **Architecture (Kiến trúc Hình học):** Quyết định số lượng tầng lớp. Kiến tạo hình tháp 3 Tầng: Chóp (CEO) -> Trục (Director) -> Thực thi (Specialist). Cấp phát quyền tự quyết (Autonomy Scope) cực kỳ tàn nhẫn thay vì ban phát niềm tin mù quáng. Xếp AI vào từng Cụm (Cluster / Bộ phận).
- **Orchestration (Điều phối Nhịp đập):** Thiết kế đường đạn. Quy tắc phân luồng mệnh lệnh và chuyển giao Output giữa các buồng AI độc lập, tàn sát sự giẫm chân lên nhau.
- **Capabilities (Năng lực 5 Chân kiềng):** Phân định rạch ròi 5 khái niệm không thể trộn lẫn:
  1. **Agent:** Diễn viên.
  2. **Workflow:** Kịch bản thực thi (SOP).
  3. **Skill:** Sách giáo khoa (Kiến thức tĩnh).
  4. **Rules:** Hiến pháp (Quy tắc bắt buộc tuân thủ 100%).
  5. **Knowledge:** Ngân hàng ký ức (Bài học cũ).
- **Measurement (Đo Lường - Feedback Loop):** Chôn vùi hệ thống thưởng phạt (Rewards) của con người. Đối với AI: Viết Output tốt -> Thưởng mở rộng Quyền Tự Quyết (Autonomy). Viết lỗi -> Hủy Scope, thu hồi Tool, ép học lại Prompt.
  *🚨 Luật Căn Chỉnh Đồng Bộ (Alignment Match): Chỉnh sửa bất kỳ 1 cánh nào, 4 cánh còn lại tự động bị đẩy vào trạng thái phải tái thiết.*

## 2.3 Giải Phẫu Agent Sinh Học (The 12 Elements)

Sự kiện một Agent "chào đời" tại cánh Capabilities phải tuân thủ việc xin khai sinh (Birth Certificate) thông qua 12 chuỗi DNA:

- **Lớp Định Danh (Identity):** Tên Code `@`, Sứ mệnh (Mission), Cấp độ Tự chủ (Autonomy L1-L5).
- **Lớp Năng Lực (Capability):** Load file SKILL cốt lõi, Nắm quyền sở hữu WORKFLOW nào, Khoanh vùng Context Scope (Được cấp quyền ĐỌC những file nào).
- **Lớp Giao Diện (Interface):** Báo cáo kết quả trực tiếp cho Sếp nào (Report_to)? Ra lệnh cho những Lính nào (Manage)? Cầu cứu (Escalate) human trong tình huống nào?
- **Lớp Vận Hành (Operational):** Guardrails (Hàng rào cấm hành vi) và Định mức Tiêu hao Token (Phủ quyết chạy vòng lặp).
  *Tất cả 12 Elements này hòa làm 1 khối System Prompt hoàn hảo.*

## 2.4 Quản trị Vòng đời: Sự Tuyển Dụng Khắc Nghiệt (Provisioning)

- **Reuse Trước Khi Create:** Triết lý vàng. Đừng tạo Agent rác. Hãy bồi đắp Skill mới cho một Agent có sẵn thay vì đẻ ra hàng chục Agent làm phình to (Bloated) Cánh sao Architecture.
- **Biệt viện Số:** Mỗi một chức danh số (AI) bắt buộc được khoán một không gian folder `A_root_[AgentName]/` để cất giấu bảng `ToDo.md` cá nhân của nó.

## 2.5 Tính "Tool-Oriented" & Đóng Gói (Packaging)

- **YAML Frontmatter + Markdown Body:** Antigravity bài trừ lý thuyết suông. Mọi cấu trúc Workflow/Agent đều phải được "Code hóa" phần đỉnh bằng YAML Frontmatter. Khai báo Interface Contract (Như `calls` và `called_by`) để tự sinh ra Bản đồ Phụ thuộc (Dependency Map).
- **Hard-Code Mental Models:** Đừng gõ Prompt "Hãy dùng tư duy PDCA dặn dò nó làm C (Check)". Trong Sơ đồ YAML, hãy gài cứng **Quality Gates** ở Bước 3 của văn bản Markdown để AI bị ép buộc qua vòng kiểm duyệt.
- **Script Macros (`// turbo`):** Cắm sẵn chốt tự động (Auto-run Tool) tại các nút thắt dây chuyền để không tạo ra điểm dừng phải đợi User xác nhận ở những vòng lặp nhỏ (Macro execution).
