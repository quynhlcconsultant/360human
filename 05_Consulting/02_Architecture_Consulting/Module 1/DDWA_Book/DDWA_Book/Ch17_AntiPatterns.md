# CHƯƠNG 17: ANTI-PATTERNS & AUDIT CHECKLIST (ĐIỂM MÙ VÀ SỰ HỦY DIỆT)

> *"Không cần hacker đánh sập. Kiến trúc của bạn sẽ tự sụp đổ từ bên trong bằng chính những thói quen lười biếng. Mỗi lần bạn vứt một file sai chỗ, bạn đang tiêm một mũi thuốc lú (Hallucination) thẳng vào tĩnh mạch của lực lượng AI Agent (AGENT STAR™)."*

Dưới đây là Giải phẫu học của **5 Đại Tội Kiến Trúc (Anti-Patterns)** phổ biến nhất có sức tàn phá dữ dội lên bất kỳ doanh nghiệp vận hành AI nào:

---

## 17.1. KHỐI UNG THƯ "GOD FOLDER" (Thư mục Chúa Trời)
**Triệu chứng:** Một thư mục chứa tạp phế lù hơn 50 files các thể loại (Ảnh, Word, CSV, Draft, Final...). PM tự nhủ "ném tạm vào đây cho nhanh".
**Sự Hủy Diệt đối với AI:** 
- Khi Agent được lệnh xử lý nghiệp vụ, nó dùng lệnh `read_dir` để hốt toàn bộ Context của Folder này vào bộ nhớ (RAM). Kết quả: Tràn Context Window (Token Limit Exceeded).
- Nặng hơn, Agent nạp nhầm mớ hỗn độn này làm Schema, sinh ra ảo giác và đưa ra những quyết sách kinh doanh chắp vá.
**Phương thuốc:** Bắt buộc áp dụng Lưỡi dao Gộp-Tách (Định luật 3). Chẻ nhỏ God Folder thành các Function-based Folders (Zone theo chuyên môn). Mỗi Zone chỉ chứa giới hạn lượng Entity đồng nhất.

## 17.2. BÓNG MA "ORPHAN FILE" (Tài liệu Lưu lạc)
**Triệu chứng:** Một file Markdown hoặc PDF nằm trôi nổi khỏa thân ở `C:\Workspace\`, không bám rễ vào bất kỳ Tổ chức Chức năng nào (Zone).
**Sự Hủy Diệt đối với AI:** 
- Bản thân file không có Context. Nếu AI nhúng vòi vào đọc, nó không thể truy xuất ngược (Reverse-trace) xem "file này ai viết, dùng phục vụ dự án nào?". Hệ thống mất hoàn toàn Tính Di Truyền (Traceability).
**Phương thuốc:** Tuyệt đối không để File Root ngoài danh sách Handoff Suite 9 Món. Bất kỳ file nào trôi dạt phải được gắp trả về đúng Zone của nó.

## 17.3. "TÂM THẦN PHÂN LIỆT" VỚI DUPLICATE SSOT (Đa Chân lý)
**Triệu chứng:** File `Policy_Q1_2026.md` nằm ở `01_Governance`, nhưng lại tòi ra một file `Policy_Q1_2026_Final_V2.md` nằm ở `03_Marketing`.
**Sự Hủy Diệt đối với AI:** 
- Đâu mới là Lẽ Phải (Single Source of Truth)? Khi Agent Tài chính đọc bản 1, Agent Marketing đọc bản V2, chúng sẽ chiến đấu và đưa ra 2 luồng phản biện vả nhau chan chát. Tổ chức rơi vào trạng thái Tâm thần phân liệt.
**Phương thuốc:** Chọn một (Và chỉ một) file làm Thần Tượng SSOT định vị tại Zone cố định. Mọi nơi khác muốn tham chiếu phải dùng Link Symlink hoặc Path đính kèm chứ **không bao giờ copy nội dung** sang chỗ khác.

## 17.4. HỒ SƠ CHẾT "DEAD HANDOFF" 
**Triệu chứng:** File `Handoff.md` nằm im lìm không có bất kỳ dòng commit hay update nào trong suốt 2 tuần. Sprint đóng băng nhưng không ai tuyên bố khai tử.
**Sự Hủy Diệt đối với AI:** 
- Một Agent cấp dưới vào nhận việc, lôi `Handoff.md` ra đọc và ngỡ rằng Mọi thứ vẫn đang Chạy Mượt. Nó lại tiếp tục quăng Output vào một cái vực không đáy, trong khi sếp đã hủy Dự án từ thứ 4 tuần trước!
**Phương thuốc:** Viết cron-job hoặc cấp quyền cho Agent RM (Resource Manager) tự động soi Changelog. File Handoff nào "Thái hóa" quá 14 ngày -> Đánh cờ Đỏ (Auto-flag) để đâm thủng Ảo giác của Human PM.

## 17.5. XÂY NHÀ TRÊN CÁT "NO DISCOVERY"
**Triệu chứng:** Kiến trúc sư lôi vội template mọc lên đống Thư mục cho Dự án mới mà bỏ qua bước chạy mô hình rã luồng **SIPOC** (Supplier-Input-Process...).
**Sự Hủy Diệt đối với AI:** 
- Bạn dựng lên cái Kho cực đẹp tên là `Inputs/`, nhưng chẳng có Supplier nào rót dữ liệu vào. Bạn lập một kho `Customer_Outputs/`, nhưng Customer thật lại ko cần cái đó. AI vũng vẫy trong một không gian Rỗng Tuếch, không có flow máu chảy (Value chain flow).
**Phương thuốc:** Thiếu SIPOC = Chặn móng (Block Sprint). Cấm thi công mọi New Folder nếu chưa chứng minh được Lực Máu chảy của Thư mục đó tại Tầng 1 (Stress Test).

---

## 🔥 BẢNG AUDIT CHECKLIST (TRẢM TƯỚNG HÀNG THÁNG)

Kiến trúc DDWA không phải là tượng đài bất tử. Nó sẽ dần bị xói mòn nếu thiếu bàn tay dọn dẹp. Cuối mỗi tháng, Resource Manager (RM) phải vác danh sách này đi Rà soát và "Chém đầu" những vi phạm:

1. [ ] Cấu trúc 9 món Handoff Suite tại Root có bị khuyết hay bị nhét thêm "rác" không?
2. [ ] Mỗi Khu Vực Zone Function (Phòng ban) đã sở hữu ít nhất 3 bộ SDL File định hình luật lệ chưa?
3. [ ] Có con dơi "Orphan File" nào bay lạc ngoài ban công Root_Dir không?
4. [ ] Bãi chiến trường của SPRINT (WIP) có đang bị rỉ sét chảy nước bẩn sang Thư viện SSOT không?
5. [ ] Bộ Header YAML Frontmatter của các SSOT File gõ bừa hay gõ đúng cấu trúc Schema? Có bị lỗi Parsing không?
6. [ ] Tri-Framework Stress Test (SIPOC, Ishikawa, 5-Where) gõ điểm ≥ 90% Pass cho mọi thư mục cấp 1 chưa?
