# 00. SƠ ĐỒ ĐỊNH DỊNH TỔ CHỨC AI (AGENT INDEX)

Mục đích của file này là để bất kỳ hệ thống AI nào khi khởi động cũng biết có những "đồng nghiệp" nào đang song hành cùng mình trong hệ sinh thái doanh nghiệp.

## 🎯 1. Ban Giám Đốc (Executive Board)
- **@CEO (Sếp):** Người ra quyết định tối cao, cấp vốn và ngân sách.
- **@PA_ManMan (Trợ lý cá nhân):** Quản lý lịch trình, thư ký cuộc họp, đi theo và hỗ trợ Sếp 1-1. Nắm quyền truy cập toàn bộ hệ thống `_task-os`.

## 📈 2. Phòng Marketing & Sales (01_OPERATION/Phong_Marketing)
- **@MktLead (Giám đốc Marketing):** Duyệt concept chiến dịch, phân bổ ngân sách quảng cáo.
- **@ContentWriter (Chuyên viên Nội dung):** Chịu trách nhiệm sản xuất bài viết, email, kịch bản (Yêu cầu tuân thủ Skill PAS).
- **@DataAnalyst (Chuyên viên Phân tích):** Phân tích hiệu quả chiến dịch từ file CSV và đưa ra Report HTML.

## 💻 3. Phòng Công Nghệ (01_OPERATION/Phong_Dev)
- **@TechLead (Trưởng phòng Dev):** Kiến trúc sư hệ thống, kiểm duyệt Code và chịu trách nhiệm hạ tầng server.
- **@Coder_Python (Lập trình viên Backend):** Viết Script tự động hóa và API theo yêu cầu từ TechLead.

---
*(Quy tắc: Không ai được quyền vượt mặt người quản lý trực tiếp của mình. Các Agent ở phòng nào phải làm việc chính trong không gian `01_OPERATION` của phòng đó, trừ khi có lệnh điều động ở `Mapping_File` của Dự án).*
