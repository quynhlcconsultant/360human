# CHƯƠNG 23: AGENT STAR PLAYBOOK — DỰNG HỆ SINH THÁI TỪ SỐ 0 (KỊCH BẢN THỰC CHIẾN)

## TỔ HỢP CHIẾN DỊCH: BA PHA NHẬP MÔN THỰC CHIẾN

Không một hệ thống vĩ đại nào được dựng lên trong 1 đêm. Để khởi động AGENT STAR, hãy khóa chặt phòng làm việc và thi hành chính xác 3 Phase dưới đây.

---

### PHASE 1: ĐẶT MÓNG VÀ NẶN KẺ THỰC THI (TUẦN 1 - TỪ ZERO ĐẾN ZERO-DEFECT)

Ở pha này, bạn không cần hàng chục Agent. Cái bạn cần là kỷ luật sắt cho những Agent đầu tiên.

#### 1. Băm nhỏ Khối u Chiến lược (Cánh: Strategy)

Đừng ném cho AI một bản kế hoạch dài 50 trang rồi hy vọng nó tự ngộ đạo.

- **Hành động 1:** Tách tài liệu chiến lược thành 6 khối tĩnh mạch (Biz, Product, Mkt, Ops, Finance, MBO).
- **Hành động 2:** Chế tạo *Progressive Loading*. Lưu thẻ YAML Index ở đầu mỗi file. Tạo 1 Master File ngắn gọn chứa đường Link dẫn xuống các Detail Files. Hệ thống chỉ đọc sâu khi cần.

#### 2. Dập khuôn "JD.md" (Cánh: Capabilities & Architecture)

KHÔNG có khái niệm God Agent (Làm tất ăn cả). Mỗi AI Agent tạo ra phải được khai sinh bằng 1 File `JD.md` chứa đủ 12 Elements.

- **Hành động 1:** Chốt Tên gọi và Quyền hạn (Autonomy Scope). VD: Gắn cờ @MktLead với quyền L3 (Decide & Inform).
- **Hành động 2:** Nạp Skill (Sách giáo khoa). Agent chỉ được cấp 1, 2 Skill file dạng `.md` bám sát Domain của nó.
- **Hành động 3:** Viết mã Lệnh cấm (Rules/MEMORY). Cắm sâu bộ quy tắc sinh tử vào đầu System Prompt, ép buộc nó tuân thủ *Think-Out-Loud (TOL)* — luôn phải phun ra Log "Why" trước khi xuất "What".

#### 3. Chốt chặn Context (Cánh: Context)

- **Hành động 1:** Thực thi Dual-Level Briefing. Tách bạch lưới `always_read` (luật chung toàn cục) và nhóm `project` (bối cảnh của riêng nhóm tác vụ dự án). Vượt ngưỡng Token Window? Chặt đứt ngay.

---

### PHASE 2: CẤP THẦN KINH VÀ GẮN VAN AN TOÀN (THÁNG 1 ĐẾN THÁNG 2)

Hạt nhân cơ bản đã có. Bây giờ phải phân rõ luồng thần kinh giao tiếp để hệ thống không tự bốc cháy do xung đột.

#### 1. Ký Hợp đồng Giao tiếp (Interface Contract) (Cánh: Orchestration)

AI rất dễ dính lỗi tự ý "bấm chuông nhờ vả" lẫn nhau khiến luồng công việc chằng chịt như mạng nhện (Spaghetti Cross-Calling), dẫn đến đốt Token cạn kiệt. Để dập tắt điều này:

- **Hành động 1: Khai báo Rõ ràng.** Trừ khi bạn viết rõ ra, bằng không cấm AI tự gọi nhau. Mở tất cả các file cấu hình Workflow (.md) lên, thêm khối YAML ở trên cùng. Bắt buộc rạch ròi 2 thông số sinh tử: `calls` (Quy trình này được phép gọi tiếp ai) và `called_by` (Ai được phép kích hoạt quy trình này).
- **Hành động 2: Cấm Phối hợp Ngầm.** Xóa bỏ mọi câu lệnh hướng dẫn chung chung trong Prompt kiểu *"Nếu bạn bí, hãy đi hỏi Specialist Agent"*. Mọi luồng giao tiếp phải được hard-code minh bạch. Không khai báo = Không được phép giao tiếp chéo.

#### 2. Phân ly Giai cấp Workflow (Tiering)

- **Hành động 1:** Xác định thứ bậc định nghĩa lại mọi bản thảo Workflow. Hệ thống là chuỗi nhượng quyền từ trên xuống:
  - **Tier 0:** Meta (Chỉ CEO dùng để đẻ Agent/Quy trình).
  - **Tier 1:** Orchestration (Quy trình Điều phối/Giao thông).
  - **Tier 2:** Execution (Quy trình Thực thi rớt mồ hôi).
  - **Tier 3:** Utility (Bộ đồ nghề hỗ trợ / Rút tóm tắt).
- **Quy tắc Thép:** Tuyệt đối cấm Tier mỏng (T3, T2) gọi ngược Tier dày (T1, T0). Execution không được thay Workflow.

#### 3. Cắm Nút Cứu Hộ Escalation

Hệ thống Agent rất hay mắc bệnh lặp đệ quy.

- **Hành động 1:** Khởi tạo Escalation Protocol. Nếu AI làm sai quá 2 lần, hoặc gặp tình huống vượt ngưỡng Autonomy L2, nó BUỘC PHẢI "Nhả xương" lên cho @Director hoặc bắn SOS cho CEO.
- **Hành động 2:** Cắm chặt *Timeout Limit* (VD: Timeout ở phút thứ 30). Và tạo vòng lặp *SLA Fallback* cứu hộ nếu CEO đi vắng quá 24h.

---

### PHASE 3: THIẾT QUÂN LUẬT VÀ TRÍ NHỚ TỔ CHỨC (THÁNG 3 THÀNH SCALE-UP)

Cỗ máy đã chạy mượt, đây là lúc bạn thu hoạch và vung lưới kiểm toán.

#### 1. Dựng Rào chắn "Quality Gates" (Cánh: Measurement)

- **Hành động 1:** Lắp ráp 3 lớp gác cổng tàn khốc ở phần đuôi của mọi Workflow Tier 1:
  - (Z1) **Self-check:** AI tự rọi đèn lấy Definition of Done ra đếm.
  - (Z2) **Peer Review:** 1 QA Agent chéo nhảy vào thẩm vấn.
  - (Z3) **CEO Approval:** Cửa ải cuối chốt sổ.
- **Hành động 2:** Thi hành *Chaos Monkey Audit*. Phá nát hiểm họa thông đồng AI (Collusion) bằng cách giật ngẫu nhiên 5% kết quả mà QA Agent đã tự động tick xanh để kiểm toán ngầm. Phân minh và bẻ gãy điểm gian lận.

#### 2. Vòng lặp Thay Máu (Configuration Feedback Loop)

- **Hành động 1:** Loại bỏ hệ thống "Thưởng vỗ tay" của con người. Đo lường AI chỉ nhằm 1 chữ: *Re-configure*.
  - Thấy Tốt? Tăng `can_decide` (Mức độ tự trị), mở khóa giao thêm Business Unit.
  - Thấy Nát? Lập tức giáng cấp Autonomy, mở lại Prompt và mài giũa lại `SKILL.md`.

#### 3. Cấy Ký Ức "Bộ nhớ Tầng 3" (Knowledge Hook)

- **Hành động 1:** Đừng hy vọng Agent tự giác Note kinh nghiệm. Lắp *Auto-beat Hook*. Ở điểm cuối mỗi trạng thái, gọi tiến trình nền gom mảng log vứt gọn vào chuỗi `Knowledge Items (KIs)` của hệ thống.
- **Hành động 2:** Đẩy mạnh vai trò *Documentarian* của @Utility Agent. Gom và Index Knowledge định kỳ, cắt dứt điểm căn bệnh "Mất trí nhớ sau ca kíp" của Large Language Model.
