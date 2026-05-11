# Reading Material: Phần 3 — Điều phối Workflow & Phanh Ngắt Tài Nguyên

> **Tài liệu đọc thêm dành cho Học viên**  
> **Nguồn đối chiếu:** Sách AGENT STAR™ (Chương 9, Chương 16) & Sách Giáo khoa Antigravity.

---

## 1. Cấu trúc Phân tầng Băng chuyền (Workflow Tiering)
Ở thời đại quy mô hóa tổ chức AI, bản thân dòng chảy công việc (Workflow) chính là cốt tủy của tổ chức. Hệ sinh thái này được bóp khung trong 4 tầng (Tier) cực đoan để trị dứt điểm sự giẫm đạp:
- **TIER 0 (META):** Kiến trúc vĩ mô. Gồm các luồng cực độc (như sửa quyền, bẻ nhánh phòng ban, tái lập Sơ đồ tổ chức). Nếu hệ thống báo cáo Workflow này chạy, Chủ Doanh nghiệp buộc phải duyệt tay tuyệt đối.
- **TIER 1 (ORCHESTRATION):** Bác tài điều phối. Quy trình khổng lồ (Ví dụ: Chạy 1 chiến dịch). Nhiệm vụ của T1 là thâu tóm Output từ Cấp 2 ráp lại thành hình. Dành riêng cho cấp Director.
- **TIER 2 (EXECUTION):** Khối óc lao công. Đi thẳng vào sản xuất chuyên môn mảnh vỡ (Code UI, Dựng nội dung, Check lỗi chính tả). Specialist xả thân ở đây.
- **TIER 3 (UTILITY):** Nơi chế ngự của Script Automation (Python/Bash...). Tính chất Tool-Oriented cực mạnh, ví dụ: Bot trích text, Bot chụp ảnh màn hình ngầm. Là những phân mảng vô danh tàng hình (Stateless), không bao giờ làm trượt gốc History.

**Cảnh cáo God Workflow:** Nếu một CEO có tư tưởng nhét kịch bản dài 5 trang A4 vào 1 cú Enter, bạn đang phá hỏng dự án. Lệnh quá to làm AI bị mờ Context Window. Phải chém nhỏ (Tiering) làm nền tảng dây chuyền băng tải.

## 2. Kỹ Thuật Routing (Gọi chéo) & Ranh Giới AI_RM
- **Mã hóa Sự phối hợp (Call Hierarchy):** Đừng bắt AI "tự hiểu ý". Quan hệ chủ tớ phải gài bằng YAML Frontmatter (Ông Tier 1 quyền gọi xuống n thằng Tier 2). Còn lại cấm vận Tier 2 tự tiện khởi phát gọi ngược Tier 1.
- **Mạng lưới Router:** Cắt lớp đường đạn (Tới ngã ba nếu Rẽ Trái gọi Bot Sale, Rẽ Phải gọi Bot Support).
- **Bộ não Lõi AI_RM:** Đây là trái tim của Hub. RM Agent cung cấp giấy thông hành (Birth Certificate) cho tất cả các Bot mới. Thiếu Đặc vụ Kiến trúc sư hệ thống này, bộ Gen năng lực sẽ thoái hóa vì trùng rác Skill.

## 3. Hệ Thống Rà Quét Vận Hành (Measurement & Circuit Breaker)
Thiết lập quyền tự trị (Autonomy) vĩ đại nhất là dạy cỗ máy làm sao tự kết liễu bản thân khi nó đi sai đường, chứ không phải bắt người vào gỡ.
- **Tầng 1 - Bảng điện Mấu chốt (Metrics):** Cân đối ngặt nghèo Velocity (Nhanh) và Quality (Đúng). Đo cả vụ nổ dây chuyền (Blast Radius): Nếu 1 lệnh sai, nó sẽ đẩy n file bị ngộ độc context theo.
- **Tầng 2 - Ma trận Cửa tử (Quality Gates):** 
  - `QG-0:` Chế độ Ngạo mạn. Agent thấy Input mờ nhạt -> Quăng Error không chạy, bắt Sếp nhập lại.
  - `QG-1 & QG-2:` Peer Review (Đâm sườn). Lấy Agent QA chuyên trách chém lại bản nháp của Agent Thực thi.
  - `QG-3:` Cổng kiểm duyệt sau cùng do Human xét duyệt (Merge to Master).
  - *Diệt Thông đồng (AI Collusion):* Rủi ro Bot khen Bot (Chấm chéo dễ dãi). Chủ doanh nghiệp dùng Chaos Monkey Randomize (Rút lõi bất chợt) để soát lại.
- **Tầng 3 - Khắc Nghiệt Red Team (Phanh Ngắt Mạch - Circuit Breaker):** Sự khác biệt giữa Dân Chuyên và Dân Nghiệp dư nằm ở đây. LLM bị mắc kẹt tại Quality Gate sẽ tự sinh ra vòng đệ quy kinh hoàng (Lấy Output vỡ, gõ lại Prompt). Phải cắm cứng giới hạn Resource Quota và Timeout Limit: Khựng 3 Lần -> Nổ Hệ Thống Cầu Dao (Circuit Breaker) lập tức, ngăn chặn quá trình "đốt tiền" của C-Level vô nghĩa.
