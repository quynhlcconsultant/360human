# CHƯƠNG 12: BÁT ĐẠI ĐỊNH LUẬT KIẾN TRÚC WORKSPACE (Bản Master)

> *"Kiến trúc không gian làm việc số không phải là nghệ thuật sắp xếp thư mục cho đẹp mắt. Nó là Kỹ thuật Định tuyến Dữ liệu (Data Routing Engineering) để Hệ thống AI có thể tự động bóc tách, tư duy và thực thi mà không gây ra vòng lặp vô tận hay ngộ độc bối cảnh. 8 Định luật dưới đây là Hiến pháp tối cao của DDWA."
> *

---

## ĐỊNH LUẬT 1: ĐỊNH LUẬT PHỔ QUÁT (Universal Functions)

> *Mọi doanh nghiệp, dù là Start-up 3 người hay Tập đoàn 3.000 người, đều bị đúc khuôn bởi 6-7 chức năng kinh doanh cốt lõi. Kiến trúc thư mục Root phải phản ánh chính xác các Lãnh thổ này.*

**Giải phẫu học:**
Sơ đồ tổ chức (Org Chart) của con người hình hài ra sao, Cây Thư mục (Directory Tree) của AI phải ánh xạ y hệt (Isomorphism). Đừng sáng tạo ra những Folder gốc mang tên "Dự án A" hay "Linh tinh". Phải chia lãnh thổ rạch ròi ngay từ Level 0:

- `A_Strategy_and_Market/` (Chiến lược & Thị trường)
- `B_Product_and_Tech/` (Sản phẩm & Kỹ thuật)
- `C_Marketing_and_Sales/` (Tiếp thị & Bán hàng)
- `D_Operations/` (Vận hành)
- `E_Finance_and_HR/` (Tài chính & Nhân sự)

**Chế tài:** Bất kỳ thư mục nào đẻ ngang hông ngoài 5 cụm chức năng phổ quát này đều bị coi là rác kiến trúc.

---

## ĐỊNH LUẬT 2: ĐỊNH LUẬT MÔ HÌNH DỮ LIỆU (The Tri-Layer Data Model)

> *AI không đọc văn xuôi như con người. Việc ép AI tự tóm tắt một file dài 50 trang là hành vi đốt tiền API lãng phí nhất lịch sử máy tính.*

Mọi thông tin trong DDWA được phân hóa thành 3 Tầng Dữ liệu rõ rệt:

1. **Tầng Strategy (Dành riêng cho Máy mổ xẻ):** Phải viết bằng cấu trúc `YAML Frontmatter` gắn ở đỉnh các file Markdown. Khi AI vào cuộc, nó chỉ việc bóp lấy khối YAML này là thấu hiểu ngay lập tức Parameter của công việc.
2. **Tầng Transaction (Dành cho tính toán):** Mọi con số, log giao dịch, dữ liệu biến thiên phải lưu bằng `CSV/Database`. Tuyệt đối cấm gõ bảng biểu phức tạp bằng Markdown Tables khi tần suất Write liên tục.
3. **Tầng Inter-communication (Dành cho Người):** Đây là những báo cáo Markdown sinh ra (Report Generation) chỉ để Sếp đọc duyệt. Bản thân AI không lội ngược dòng đọc lại chính mớ văn xuôi này để học.

---

## ĐỊNH LUẬT 3: ĐỊNH LUẬT GỘP - TÁCH (Entity Sizing)

> *Tiêu chí duy nhất để quyết định việc tạo File mới hay Thư mục mới là "ĐỘ LỚN CỦA ĐỐI TƯỢNG (OBJECT)", tuyệt đối không phụ thuộc vào "SỐ LƯỢNG CHỮ MÀ CON NGƯỜI ĐÃ GÕ".*

**Căn bệnh phổ biến:** Nhân sự thấy file Word quá dài (20 trang) bèn chia nó ra thành 5 file nhỏ cho "dễ đọc". Kết quả là AI mất hoàn toàn Context vì thông tin bị bẻ gãy khỏi cụm Entity của nó.
**Chuẩn DDWA:** Một tính năng lớn (Epic) đẻ ra một Thư mục. Một tính năng con (Feature) đẻ ra một File độc lập. Dù file Feature đó chỉ có 3 dòng hay 3000 dòng, nó vẫn phải đứng một mình để giữ toàn vẹn mã định danh vĩnh cửu.

---

## ĐỊNH LUẬT 4: ĐỊNH LUẬT TỰ ĐỦ (Self-Contained Load)

> *Thả một AI Agent vào một Thư mục bất kỳ, nó phải tự nhận thức được nó đang ở đâu, thuộc về dự án nào, và giới hạn sửa đổi của nó là bao nhiêu.*

Kiến trúc DDWA thiết đặt sự tĩnh lặng tự chủ tuyệt đối. Nhờ các khối YAML được mã hóa sẵn trên từng file (ID, Parent_ID, Trạng thái), Agent chạy lệnh `read_dir` và nạp toàn bộ danh sách file thẳng vào RAM làm Schema trong chưa tới 2 giây. Nó biết rõ mình được cung cấp cái gì mà không cần Human chạy theo gửi file đính kèm.

---

## ĐỊNH LUẬT 5: PHÂN RÃ WIP VÀ SSOT (Công Trường vs. Thư Viện Chuẩn)

> **Lằn ranh Tuyệt đối:** Không bao giờ trộn lẫn Cát Đá (Nháp) vào trong Bảo Tàng (Chân lý).

- **Khu vực SPRINT/ (Nơi chứa WIP):** Dành cho Công trường thực thi. File nháp, file sập, scratch idea, brainstorm gạch xóa... mọc lên như nấm. Đầy rẫy sự lộn xộn, nhưng được nhốt kín khóa chặt thời gian trong 1 Sprint. Xong Sprint là đổ bê tông, khóa thư mục.
- **Khu vực PHÒNG BAN (Nơi chứa SSOT - Single Source of Truth):** Cuốn từ điển vĩ đại của Doanh nghiệp. Chỉ những Output Đã Nghiệm Thu mới được đẩy lên đây. Sạch sẽ vô cực. AI khi cần tra cứu chiến lược chỉ được phép cắm vòi hút Data từ đây xuống, cấm bén mảng vào bãi bồi WIP của các Sprint quá khứ để chống "Ngộ độc Ảo giác".

---

## ĐỊNH LUẬT 6: ĐỊNH LUẬT CỖ MÁY (Machine-born Metadata)

> *Những File nặng mùi cấu trúc như Bản Tóm Tắt (Index), Nhật ký (Changelog) sinh ra là Dành cho Mắt của Máy Móc. Mắt người không cần rình mò.*

Tại Root của một Workspace, DDWA duy trì hệ quy tắc `INDEX.md` và `Changelog.md`.
**Sự ngạo mạn của Human:** PM thường thích tự gõ tay các bản tóm tắt này và quên update sau 3 ngày.
**Tôn chỉ DDWA:** Mọi Index và Changelog phải được tự động sinh ra và sửa đổi (Auto-update) thông qua Workflow Code/Script của AI. Cỗ máy sinh ra siêu dữ liệu cho chính cỗ máy đớp lại nó.

---

## ĐỊNH LUẬT 7: ĐỊNH LUẬT TRI-FRAMEWORK (Stress Test Toàn vẹn)

> *Đừng tin vào mắt mình khi thiết kế Folder. Hãy hành chuẩn nó qua 3 lớp Tẩy trần.*

Bất kỳ luồng kiến trúc nào trước khi Go-live áp dụng cho AI đều phải chui qua máy quét 3 tầng (Xem chi tiết tại **Chương 10**):

1. **SIPOC:** Ánh xạ chảy máu từ Nhóm Cung Cấp -> Đầu vào -> Đầu ra -> Khách Hàng.
2. **ISHIKAWA (Xương Cá):** Gắn nhãn 5 Nhánh lưu trú (Strategy, Tracking, Library, History, WIP).
3. **5-WHERE Roullete:** Nhắm mắt chỉ đại vào một Object và bắn ra 5 câu hỏi truy vết không gian "Nằm ở đâu?". Trả lời sai 1 câu = Phân hủy làm lại kiến trúc.

---

## ĐỊNH LUẬT 8: ĐỊNH LUẬT GIAO DIỆN CHÓP BU (The Conversational Interface)

> *Sứ mệnh của nhân loại đã thay đổi. Bạn sinh ra không phải để gõ Bàn phím tạo File Word. Bạn sinh ra để Giao tiếp Khẩu lệnh.*

Trong văn phòng DDWA, **Con người chỉ việc mở Promt và Chat thông số**. Mọi tác vụ tay gõ markdown, điền thuộc tính YAML, Update File, Đổi tên Folder — AI Agent sẽ đóng vai trò như những tay Keyboard-Warrior tốc độ ánh sáng đi thực thi sau lưng.

Cấm tiệt hành vi Giám đốc mở Notepade+ tự lạch cạch ngồi chỉnh YAML cấu hình. Lòi ra 1 lỗi cú pháp Dấu Phẩy `,` là đánh sập cả hệ thống Parsing của Python Workflow. Mọi thay đổi hệ thống đều phải ra lệnh bằng Miệng cho Agent_RM (Resource Manager).
