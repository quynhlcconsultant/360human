# CHƯƠNG 10: TRI-FRAMEWORK STRESS TEST — BÀI KIỂM CHỨNG TỬ THẦN CHO KIẾN TRÚC WORKSPACE

> *"Một kiệt tác thiết kế Workspace không bao giờ bắt đầu từ việc bạn vô tình nhấp chuột phải chọn 'New Folder'. Nó phải bắt đầu từ hình hài của một CHUỖI GIÁ TRỊ (Value Chain) đang chảy máu ngoài đời thực. Nếu bạn tạo ra một thư mục mà không biết ai làm gì, đầu vào lấy ở đâu, đầu ra ném đi đâu — Hệ thống đó chỉ là một nhà kho vứt rác."*

---

## 10.1 Tại sao Kiến trúc cần Stress Test?

Trong môi trường Data-Driven Workspace Architecture (DDWA) kết hợp sự vận hành của lực lượng AI Agent (AGENT STAR™), một file bị lưu lạc không đơn giản là "tốn 5 phút tìm kiếm" như thời đại Human. Khủng hoảng xảy ra khi:
- AI đọc nhầm bản nháp (Context Pollution).
- AI ghi đè nhầm bản SSOT (Single Source of Truth).
- AI bị mất tích (Dead Handoff) vì không biết báo cáo công việc tại đâu.

Để đảm bảo Bộ Rễ Thư Mục (Directory Tree) trụ vững trước các luồng công việc phức tạp, chúng ta phải đưa nó qua một **Hệ Phễu Kiểm Thử 3 Tầng — Tri-Framework Stress Test**, bao gồm: **SIPOC**, **Ishikawa (Xương cá)**, và Bài Test rát tát thẳng mặt **5-Where**.

---

## 10.2 TẦNG 1: Khởi nguồn từ SIPOC (Khám phẫu luồng chảy)

SIPOC là vũ khí vay mượn từ Six Sigma, viết tắt của: **S**upplier (Nhà cung cấp) → **I**nput (Đầu vào) → **P**rocess (Quy trình) → **O**utput (Đầu ra) → **C**ustomer (Khách hàng).

Tuyệt đối không vẽ sơ đồ thư mục (Folder/File) trước. Phải vẽ SIPOC trước!

### Cách thức nhúng SIPOC vào Workspace:
Mọi căn phòng (Department) đều là một chiếc hộp Đen (Process). Hãy ép Kiến trúc sư trả lời rành mạch:
1. **P (Process - Hành động thi công):** Phòng ban này làm cái gì? (Ví dụ: Viết bài Content SEO). Quá trình này sẽ sinh ra thư mục Nháp (WIP).
2. **I (Input - Nguyên liệu thô):** Để làm P, phòng ban này cần tài nguyên gì? (Ví dụ: Báo cáo thị trường, Persona, Keyword). AI sẽ tìm thư mục Input để hút dữ liệu.
3. **S (Supplier - Nguồn cấp Input):** Thằng nào ném Input vào đây? Nếu là Phòng Market Research, thì phải dựng luồng Handoff qua lại giữa 2 trạm.
4. **O (Output - Thành phẩm):** Sau khi làm xong P, cái gì nhảy ra khỏi xưởng? (Ví dụ: Bản nháp Content, File HTML, Slide C-Level). Lưu vị trí nào để không ngâm trong bãi rác nháp?
5. **C (Customer - Người mua rác):** Output đó đi về đâu? Ai sẽ đọc nó tiếp theo? (Thành Input cho thằng khác).

**Kết quả Tầng 1:** Bạn thu thập được một "Danh sách các Cuộn Cáp (Artifacts)" đang bò trườn khắp tổ chức. Lúc này, ta mới mang đám cáp đó đi định tuyến.

---

## 10.3 TẦNG 2: Định tuyến bằng ISHIKAWA (Sơ đồ Xương Cá 5 Nhánh)

Khi đã nắm trong tay Danh sách Output (Thành phẩm) sinh ra từ SIPOC, đừng vội quăng tất cả vào một Folder có tên `Final_Documents_2026/`. Đó là hành vi thiết kế thô sơ.

Chúng ta ép mọi Output đi qua Sơ đồ Xương Cá (Ishikawa). Mỗi nhánh xương đại diện cho một chiều không gian lưu trữ dữ liệu bắt buộc trong mô hình DDWA:

1. 🎯 **Nhánh Xương 1 — STRATEGY (Bộ gen):** Các Object mô tả bức tranh lớn. (Kế hoạch MKT Tổng, Tầm nhìn, OKR Quý). Đây là lãnh địa của File YAML/C-Level.
2. 📊 **Nhánh Xương 2 — TRACKING (Radar):** Các Object theo dõi nhịp đập tiến độ. (Master Sprint Log, Kanban Board, Database ToDo).
3. 📚 **Nhánh Xương 3 — LIBRARY (Bảo Tàng):** Nơi niêm phong các Thành phẩm chốt vĩnh viễn (SSOT), bản Hướng dẫn (Guideline), Bản mẫu (Template). 
4. ⏳ **Nhánh Xương 4 — HISTORY (Lịch Sử Thay Đổi):** Nơi chứa những file Tracking lưu gốc như Changelog, Log API.
5. 🚧 **Nhánh Xương 5 — WIP (Công Trường):** Nơi xả rác, file Nháp, Scratch pad, các Sprint đang thực thi dang dở. Bụi bẩn nhất, cấm mang ra ngoài.

**Kết quả Tầng 2:** Mọi Output không còn nằm ngổn ngang. Nó đã bị trói chặt vào 1 trong 5 Tầng Phân Loại Sinh Tử phía trên.

---

## 10.4 TẦNG 3: Bài Thi Vấn Đáp 5-WHERE (Tử huyệt của Workspace)

Đây là rào chắn cuối cùng. Kiến trúc sư Hệ thống (Architet) hãy đứng đối diện với PM hoặc Người vận hành, bốc đại MỘT OUTPUT bất kỳ từ luồng SIPOC ra và nã liên tục 5 phát đạn "Ở ĐÂU" (Tương ứng với 5 nhánh Xương Cá).

> **ĐỀ BÀI VÍ DỤ:** Xét đối tượng: "Bài viết Social Media Tháng 3". Hãy cho tôi biết:

| Đạn Stress Test | Câu hỏi "Tàn nhẫn" dành cho PM | Lời giải chuẩn DDWA |
| :--- | :--- | :--- |
| **WHERE-1: (STRATEGY)** | Kế hoạch lớn yêu cầu cái bài Social này đẻ ra... hiện **ĐANG NẰM Ở ĐÂU?** | *"Dưới thư mục `02_WAREHOUSE_STORAGE/Marketing/01_Strategic_Plan.md`"* |
| **WHERE-2: (TRACKING)** | Tiến độ giao rãnh (Thằng AI nào đang viết bài Social này, làm đến % bao nhiêu rồi)... **ĐƯỢC TRACK Ở ĐÂU?** | *"Nằm trong `SPRINT/SP-2603-xxx/ToDo.md` hoặc Master Boards."* |
| **WHERE-3: (LIBRARY)** | Nếu bài viết Social này đã được Giám đốc bấm nút Approve, cái bản SẠCH SẼ NHẤT (SSOT)... **CẤT VÀO KHO NÀO?** | *"Nằm trong Thư viện `02_WAREHOUSE_STORAGE/Marketing/03_Approved_Posts/`"* |
| **WHERE-4: (HISTORY)** | Lỡ đêm qua AI sửa nhầm câu Caption, lịch sử Edit Tracking của bài viết... **GHI LOG Ở ĐÂU?** | *"Trực tiếp trong Git Commit History hoặc `Changelog.md` của thư viện."* |
| **WHERE-5: (WIP)** | Vậy cái bản nháp dơ dáy, gạch xóa be bét lúc AI đang brainstorm ý tưởng... **ĐANG VỨT Ở ĐÂU?** | *"Chứa khóa kín tại `SPRINT/SP-2603-xxx/` (Tuyệt đối không vấy bẩn thư viện SSOT)."* |

### 🔥 Lời Tuyên Án:
Chỉ cần Nhân sự / Kiến trúc sư **Ố VÁ 1 TRONG 5 CÂU WHERE (Trả lời lúng túng, không chỉ rõ được Path cụ thể)**, hệ thống DDWA Workspace đó chính thức bị **ĐỨT GÃY**. 
Lúc đó, Kiến trúc sư phải quay lại bản thiết kế cây thư mục, dỡ ra làm lại từ đầu. Sự buông lỏng ở bước Stress Test này sẽ phải trả giá bằng hàng triệu file rác và sự sụp đổ của luồng tự động hóa AI trong một tháng sau đó.
