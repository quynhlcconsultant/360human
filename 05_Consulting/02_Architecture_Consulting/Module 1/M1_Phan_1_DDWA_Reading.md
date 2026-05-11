# Reading Material: Phần 1 — Kiến trúc Workspace & Cốt lõi DDWA

> **Hướng dẫn đọc:** Bắt đầu bằng việc định giá "Sự đắt đỏ của Context Loss". Đừng học thao tác (How-to) trước khi bạn hiểu tường tận "Tại sao" (The WHY) một AI Agent lại sụp đổ vì ngộ độc dữ liệu.

---

## 1. Khủng hoảng Context Window và Mầm mống của Ảo giác (Hallucination)

Nguyên nhân gốc rễ dẫn đến sự sụp đổ của các doanh nghiệp dùng AI là coi AI như một "Công cụ Chat" thay vì một "Cỗ máy xử lý dữ liệu".

- **Giới hạn Context Window:** Bộ nhớ ngắn hạn của LLM luôn có trần (128k - 200k tokens). Nếu bạn nhồi nhét quy trình, dữ liệu nháp và kết quả vào cùng một luồng Chat, Agent sẽ "đẩy" các chỉ thị cốt lõi ra khỏi não bộ.
- **Ngộ độc Bối cảnh (Context Pollution):** Dữ liệu rác (Bản nháp) và Dữ liệu chuẩn (Single Source of Truth) đặt lộn xộn sẽ khiến Agent không thể phân biệt đâu là Chân lý. Hậu quả tức thì: AI ảo giác (Hallucination), tự bịa số liệu, kéo theo độ lệch chuẩn ở toàn bộ Pipeline.

**Chân lý thiết kế:** AI cần ngăn kéo. Cần cấu trúc "Văn phòng vật lý ảo". Từ đây, bộ khung **Data-Driven Workspace Architecture (DDWA)** chính thức thiết lập luật chơi.

## 2. 6 Quy luật Phái sinh (Biên giới của sự hỗn loạn)

Mọi pháp nhân kinh doanh đều vận hành qua các Chức năng Phổ quát. Do đó, DDWA áp đặt 6 Quy luật bất khả xâm phạm để chống lại sự vô kỷ luật của dữ liệu:

1. **Đối xứng (Isomorphism):** Bất kỳ Sơ đồ tổ chức nào có $n$ phòng ban, kiến trúc Folder bắt buộc phải có $n$ nhánh tương ứng. Không thừa, không thiếu.
2. **Ba Tầng (Tri-Layer):** Một phòng ban (Zone) không dùng để vứt file. Nó phải hoàn thiện 3 mảnh ghép: *Lớp Chiến lược* (Luật chơi), *Lớp Vận hành* (Dữ liệu), và *Lớp Agent* (Lực lượng xử lý).
3. **Tự đủ (Self-Contained):** Tuyệt đối không để Agent phải hỏi CEO nó là ai. Thả một con Agent vào nhánh nào, nó tự đọc `INDEX.md` và hiểu cấu trúc quyền lực ngay lập tức.
4. **Phân ly Nháp – Chuẩn (WIP vs SSOT):** File đang nháp cấm tuyệt đối nằm cạnh file đã nghiệm thu.
5. **Discovery Before Delivery:** Không cho phép khởi xướng Action (Thực thi) nếu nhánh đó chưa tồn tại bảng phân rã JTBD hoặc SIPOC. Ngăn chặn triệt để tư duy "Ăn xổi".
6. **Multi-Pipeline:** Quy trình chạy Quảng cáo không được dính líu đến quy trình viết Code. Mọi thứ phải nằm trên hai luồng băng chuyền tách biệt.

Hệ sinh thái thỏa mãn 6 quy luật trên là bộ khung **7 Zones Tiêu Chuẩn:** `01_Governance`, `02_Production`, `03_Marketing`, `04_Sales`, `05_Operations`, `06_Finance`, `07_HR`.

## 3. Mô hình IPO Factory: Trống rỗng Công trường, Gìn giữ Thư viện

DDWA biến thư mục từ "Cái kho" thành một "Nhà máy" với nguyên lý **Input - Process - Output (IPO)**:

- **Phân xưởng (SPRINT/ — Công trường WIP):** Nơi chém giết của các dòng lệnh. Là nơi Agent nháp, tư duy, vỡ trận, và thử lại. Bắt buộc có `Sprint_Log.md` báo cáo nhịp đập. File ở đây là phù du.
- **Thư viện (7 Zones — SSOT):** Tuyệt địa sạch sẽ. Nó cung cấp Đầu vào (Input) từ các file Reference do C-Level chỉ định, và nhận Đầu ra (Output) sạch sẽ từ SPRINT "Merge" ngược về khi kết thúc.

Sự phân cực này khóa chặt nguy cơ ô nhiễm Context cho AI.

## 4. Mô hình Dữ liệu 4 Tầng: Workspace là Database

Workspace trong mắt AI không phải là "thư mục máy tính". Nó là Data Warehouse:

- **Tầng 1 (YAML/JSON):** Cốt tủy của định nghĩa hệ thống. Tầng này dành cho Máy tự nói chuyện với Máy (Machine-readable).
- **Tầng 2 (CSV/Database):** Hệ thống Log, ghi nhật ký giao dịch và Vận hành thô.
- **Tầng 3 (Markdown/Views):** Vỏ bọc Giao diện (Frontend) phiên dịch Tầng 1 và Tầng 2 thành file `.md` cho CEO đọc hiểu một cách gọn gàng.
- **Tầng 4 (Agent):** Lớp nhân sự AI điều hướng toàn bộ 3 tầng dưới.

## 5. Handoff Suite và Chốt chặn Căng thẳng (Stress Test)

Bất cứ dự án nào tồn tại mà thiếu **9 File Root Ràng Buộc** (như `INDEX.md`, `Changelog.md`, `ToDo.md`, `Guideline.md`) đều bị hệ thống xem là "Dự án Khuyết tật".
Để bảo chứng độ vững, hệ thống dùng công cụ **Stress Test 5-Where**: Truy ngược bất cứ file nào sinh ra xem nó có thỏa mãn: Nguồn gốc gốc (Strategy)? Tracking tiến độ nằm ở đâu? Bản cuối lưu nơi nào (Library)? Biến động sửa lỗi (History)? File nháp đang rác ở đâu (WIP)? Mất 1 trong 5, Workspace thủng context!
