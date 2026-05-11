# CHƯƠNG 18: PLAYBOOK — DỰNG WORKSPACE TỪ NGÀY 1 (KỊCH BẢN THỰC CHIẾN)

> *"Đừng ném cho nhân viên một cuốn sách lý thuyết rồi hy vọng họ tự ngộ đạo. Bạn phải là Người Nặn Đất Sét (Mud-molder). Dưới đây là Playbook Từng-Bước-Một (Step-by-Step) để một Kiến trúc sư Hệ thống (Architet) tay không dựng lên một Tòa lâu đài DDWA vững chãi chỉ trong 48 giờ."*

---

## 🏗️ PHASE 1: ĐỔ BÊ TÔNG MÓNG (NGÀY 1)

**Mục tiêu:** Xây dựng Khung xương gốc (Root Skeleton) và thiết lập lề thói bắt buộc trước khi nhồi bất kỳ Dữ liệu nào vào. Tuyệt đối không vội tạo Folder con.

1. **Khởi tạo Lãnh thổ Phổ quát (Zone):** 
   - Đứng tại Thư mục gốc, đẻ ra 6-7 Thư mục Chức năng (Đại diện cho các Phòng ban: `01_Strategy`, `02_Product`, v.v... theo Định luật 1).
   - Thêm 2 Phân khu Hoạt động Cứng: `Archive/` (Nghĩa địa) và `SPRINT/` (Công trường WIP).
2. **Triệu hồi "9 Món Pháp Bảo" (Handoff Suite):** 
   - Rải đúng, đủ 9 File/Folder bắt buộc (`INDEX.md`, `Handoff.md`, `ToDo.md`, `Guideline.md`...) ngay tại vỉa hè Root_Dir. (Tham khảo Chương 7).
3. **Soạn Thảo Hiến pháp (Guideline.md):** 
   - Architet phải tự tay gõ những dòng đầu tiên vào `Guideline.md` để răn đe hệ thống Naming Convention (Quy tắc đặt tên file). Ví dụ: *Cấm dùng Tiếng Việt có dấu, Cấm dùng dấu cách, Yêu cầu cấu trúc [Mã_Dự_án]_[Tên_File].md*.
4. **Viết Lời Gọi Hồn (INDEX.md):** 
   - Vẽ lại Sơ đồ Cây (Directory Tree) của bạn vào file Index. Việc này giúp AI Agent có bản đồ định vị ngay khi vừa rơi xuống Workspace.

---

## ⚙️ PHASE 2: BƠM MÁU VÀO ĐỘNG MẠCH (NGÀY 2)

**Mục tiêu:** Nhồi Nhận thức (Awareness) và Triết lý Vận hành (Business Logic) vào hệ thống tĩnh.

1. **Trồng Cây Sinh Mệnh (Master SSOT):** 
   - Khởi tạo file `Master_Strategy.yaml` đặt vào trong `01_Governance`. 
   - Điền rành mạch Tầm nhìn BOST, OKR của Quý vào đó. File này chính là Cục Pin Năng lượng để điều hướng mọi LLM sau này. Khống chế ảo giác tuyệt đối.
2. **Kích hoạt Xưởng Mổ SIPOC (Stress Test):** 
   - Lùa toàn bộ Trưởng phòng (Các PM) vào một phòng họp. Yêu cầu vẽ luồng SIPOC cho các chức năng của họ (Ai cung cấp? Cần nguyên liệu gì? Đẻ rác ở đâu?). (Xem Ch.10).
3. **Tra khảo Đạn Thật 5-Where:** 
   - Architet chĩa súng vào Từng Hạng mục Output của PM, ép họ trả lời 5-Where (Nháp nằm đâu? Duyệt cất đâu? Log ở đâu?). Sót 1 lỗ = Đập thư mục làm lại.
4. **Thu nạp Biểu mẫu (SDL Hook):** 
   - Nhặt khoảng 10 File Biểu mẫu cốt lõi (Từ hệ thống FW-01_AI_Workflow_Design) nhúng vào Thư viện của các Zone tương ứng. Làm mồi cho AI copy-paste.

---

## 🔄 PHASE 3: NHỊP TIM VẬN HÀNH (VÒNG LẶP SỐNG)

Workspace chỉ sống khi có luồng khí thở. Nếu Architet bỏ đi, rác sẽ lại ứ đọng. Bắt buộc kích hoạt Nhịp Sinh Học sau:

### 1. Nhịp Thở Hàng Tuần (Thiết thực)
- **Kiểm định Handoff:** PM (Hoặc AI_RM) bắt buộc phải vạch file `Handoff.md` ra viết cập nhật Tiến độ/Blocker/Next action mới nhất.
- **Dọn dẹp ToDo:** Dọn file `ToDo.md`, gạch bỏ việc đã Done. Quăng ý tưởng tào lao vào `Notes/`.

### 2. Kích Hoạt Mỗi Cuối Sprint (Áp lực)
- **Đổ Bê Tông (Merge 2 SSOT):** Chắt lọc những viên Kim Cương sáng nhất từ bãi lầy `SPRINT/` và dán thẳng lên Bảo Tàng của các Phòng Ban (`Zone`). 
- **Đóng Quan Tài:** Khóa chặt Thư mục `SP-2603-xxx` vừa chạy xong, ném thẳng vào `Archive/`. Cấm thò tay sửa bài cũ. Giữ rạch ròi không gian WIP.

### 3. Máy Chém Hàng Tháng (Làm sạch)
- Lôi Bảng **Audit Checklist (Chương 17)** ra. Đi rà soát từng mục từ Thư mục Chúa (God Folder) tới File Mồ côi (Orphan File). Chém sạch rác tàn dư để giữ cho Token Window của Agent luôn ở mức tối ưu. 
- Nếu Tri-Framework Test thủng lỗ → Lập tức triệu tập các bên điều chỉnh lại Luồng SIPOC. Kiến trúc phải tiến hoá, ko được gỉ sét.
