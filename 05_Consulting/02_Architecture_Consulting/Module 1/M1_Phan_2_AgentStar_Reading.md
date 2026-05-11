# Reading Material: Phần 2 — Framework Tổ Dức AI-Agent (AGENT STAR™)

> **Hướng dẫn đọc:** Bỏ qua ngay lập tức tư duy gõ phím "Bạn là chuyên gia Content...". Để sử dụng AI ở cấp độ doanh nghiệp, bạn phải mang tư duy của một Nhà Quản lý Nhân sự (HRM) kiến tạo Sơ đồ Tổ chức số.

---

## 1. Cơn Khủng Hoảng Của Sự Tùy Tiện (System Pollution)
Các SME thường mắc một sai lầm chết người: Họ mua một công cụ AI và để nhân viên tự do thả rông hàng nghìn câu Prompt (Chỉ thị). Hệ quả sinh ra sự rác rưởi của quá trình mờ: Không ai biết dòng lệnh của ai, các Bot dẫm chân lên nhau tạo ra cùng một Output, không có tính kế thừa.

👉 **Reframing (Đổi khung tư duy):** AI không bao giờ là "Công cụ trả lời". AI là một **Workforce (Lực lượng lao động)** sống động. Do đó, bạn không được phép đối xử với AI bằng những dòng prompt rời rạc. Bạn bắt buộc phải "Tuyển dụng" (Provision) và xếp AI vào Sơ đồ Tổ chức chuẩn chỉnh.

## 2. AGENT STAR™: 5 Cánh Sao Cai Trị
Triết lý thiết kế tổ chức của Jay R. Galbraith được tái thiết lập cho kỷ nguyên AI. Để vận hành hàng trăm Agent chạy ngầm song song, Giám đốc AI (CIO) buộc phải duy trì sự cân bằng của 5 cánh sao:

1. **Strategy (Bối cảnh chiến lược):** Core Team quy định hướng đi duy nhất. Mọi Agent từ MKT đến CODE phải đọc chung một `Strategy.md`. Không có bối cảnh gốc, Agent sẽ tự chế ra bối cảnh rác.
2. **Architecture (Kiến trúc Hình học):** Quyền lực tổ chức được phân bổ 3 Tầng: Chóp (CEO) định hướng toàn cục -> Trục (Director/RM) điều phối luồng -> Đáy (Specialist) chuyên biệt hóa thực thi. Thu hẹp quyền tự quyết (Autonomy) nếu Agent thường xuyên quyết định sai.
3. **Orchestration (Quy luật Điều phối):** Tránh giẫm chân bằng việc đặt ra sơ đồ truyền máu. Quy định rõ ràng tầng Workflow (Tiering) và thứ tự phối hợp chéo (Cross-calling).
4. **Capabilities (Năm Chân kiềng Năng lực):** Thay vì ném tài liệu training lung tung, hệ thống trang bị cho Agent 5 thẻ bài vật lý tách biệt:
   - **Agent:** Căn cước công dân.
   - **Workflow:** Bản mô tả nhiệm vụ (SOP) chỉ rõ bước 1-2-3 phải làm gì.
   - **Skill:** Sách giáo khoa tra cứu (Ví dụ: Thuyết AIDA).
   - **Rules:** Hiến pháp cấm cãi (Ví dụ: 100% Viết tiếng Việt).
   - **Knowledge:** Sổ tay dặn dò các bài học vỡ lòng sau mỗi dự án.
5. **Measurement (Vòng lặp Căn chỉnh):** Tuyệt đối không có chuyện thưởng tiền cho AI. Thưởng AI bằng cách "Nới thêm quyền tự quyết". Phạt AI bằng cách "Tước vũ khí (Tool), bắt học lại Skill".

🚨 **Định lý Alignment:** Hễ bạn sửa Chiến lược (Strategy), bạn chịu trách nhiệm sửa lại toàn bộ 4 cánh còn lại. Không có ngoại lệ.

## 3. Bản Khai Sinh Của Agent (The 12 Elements)
Rào cản lớn nhất của dân nghiệp dư là viết Prompt kiểu "Xin hãy làm...". Trong AGENT STAR™, một nhân sự số được "Đúc" ra thông qua Thẻ Khai Sinh mang 12 đoạn mã DNA cốt lõi:
- **Lớp Định Danh:** [1] Tên chuẩn `@`, [2] Sứ mệnh, [3] Thang tự chủ Quyền lực (L1-L5).
- **Lớp Năng Lực:** [4] Load file `SKILL` nào?, [5] Cầm trịch `WORKFLOW` gì?, [6] Biên giới bị nhốt (Context Scope) chỉ được rớ vào file nào.
- **Lớp Giao Diện Chéo:** [7] Báo cáo ai?, [8] Chỉ huy ai?, [9] Kêu cứu ai khi đứng máy?
- **Lớp Vận Hành Chống Cháy:** [11] Tuân thủ Rule gì?, [12] Vòng bảo vệ Guardrails cấm hủy hoại Token.

## 4. Tuyển Dụng Khắc Nghiệt (Reuse Before Create)
- Tuyệt đối cấm hành vi đẻ thêm Agent rác chỉ vì bạn lười tìm Agent cũ. Phương châm hàng đầu: **Nhồi thêm vũ khí (Skill) cho Agent hiện tại thay vì sinh ra 10 con Bot khác nhau**.
- Mọi Agent ra đời đều được cấp cho một Biệt viện vật lý `A_root_[AgentName]/` để đặt nhật ký công việc `ToDo.md`.

## 5. Tool-Oriented: Từ Lời Nói Suông Đến Mã Code Khống Chế
Antigravity đoạn tuyệt với "lý thuyết xuông".
- **Gài cứng bằng YAML:** Bất kỳ kiến trúc AI Agent hay Workflow nào không được viết dưới dạng hội thoại. Chúng phải được chốt cứng bằng định dạng File `.md` có chứa bảng biểu **YAML Frontmatter** (Các thẻ `calls`, `tier`, `owner`). Hệ thống dựa vào YAML để vẽ mạng nhện lưới quyền lực.
- **Mental Models vô cảm:** Yêu cầu một AI "Suy nghĩ theo chuẩn PDCA" qua tin nhắn là sự lãng phí vô ích. Hãy ép nó dùng PDCA bằng cách Hard-code "Bước Check chấm điểm" vào thẳng Cổng Kiểm Duyệt (Quality Gate) của Workflow. Khai thác sự tuân thủ vô cảm của máy móc mới là đỉnh cao quản trị.
