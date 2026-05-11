# MODULE 2.1: KHỞI TẠO KHÔNG GIAN LÀM VIỆC SỐ (BIZ MODEL SETUP)
*(Hướng dẫn thực hành Live: 10 phút)*

---

## 🧐 1. Lý Thuyết: Framework 6 Trụ Cột (6 Strategy Domains)
- **Sai lầm phổ biến:** Mỗi lần mở cửa sổ chat mới, AI lại quên hết ngữ cảnh (context). Chúng ta thường xuyên phải copy-paste lại bối cảnh doanh nghiệp.
- **Giải pháp:** Cung cấp cho AI một **Single Source of Truth (SSOT)** – "La bàn doanh nghiệp" (Business Navigator Hub) chứa mọi thực tại của công ty.
- 6 Trụ cột phân bổ không gian số bao gồm:
  1. **Biz Strategy (Chiến lược Kinh doanh):** Định vị thương hiệu (Positioning), Lợi thế cạnh tranh (USP), Thông điệp cốt lõi, Phân tích đối thủ.
  2. **Product Strategy (Sản phẩm):** Danh mục sản phẩm (Portfolio), Chiến lược định giá (Pricing), Mức độ phù hợp thị trường (PMF), Roadmap.
  3. **Mkt & Sales (Tiếp thị & Bán hàng):** Chân dung khách hàng (Persona JTBD - Nỗi đau/Sung sướng), Phễu chuyển đổi, Quy trình chốt sale, Kênh phân phối.
  4. **Ops Strategy (Vận hành):** Chuỗi giá trị (Value Chain), Cấu trúc team (Org Chart), Tiêu chuẩn dịch vụ (SLA).
  5. **Financial Model (Tài chính):** Phân tích Dòng tiền, Chi phí (Cost), Unit Economics (Kinh tế học đơn vị), Tính toán điểm hòa vốn.
  6. **MBO (Quản trị Mục tiêu):** Kim chỉ nam (North Star Metric), OKRs, Bộ chỉ số KPI phân rã cho 5 phòng ban.

---

## ⚙️ 2. Quy trình "Điền Vào Chỗ Trống" (Socratic Workflow)
- Ai sẽ là người điền từng này thông tin cho doanh nghiệp? **Sẽ cực kỳ tốn thời gian nếu con người tự gõ.**
- Tại Command Center, chúng ta thiết kế một **Workflow Độc Quyền** (mang số hiệu `/biz-model-setup`):
  - **B1: Diagnostic Interview (Phỏng vấn ngược):** AI đọc File `question_bank.md` để tự động đặt ra 18 câu hỏi sắc bén chia làm 3 tầng, bắt CEO phải tư duy. Lối tiếp cận: Socratic Dialogue (Hỏi đáp để tìm ra chân lý).
  - **B2: Anti-Bullshit Process:** Áp dụng logic ba lớp "Kỳ vọng → Hiện trạng → Khoảng trống (Gap)" để khử các mục tiêu ảo tưởng, định lượng hóa các chỉ số.
  - **B3: Auto-Generate Workspace:** Dựa trên câu trả lời, AI tự động sinh ra 6 Thư mục cốt lõi và nhét các file `Template Master` (Tổng quan) và `Template Detail` (Chi tiết từng SP/Phòng ban) vào đúng vị trí.
  - **B4: Report:** Phun ra báo cáo Top 3 Gaps (Lỗ hổng) tác động lớn nhất đến Doanh thu trong 30 ngày tới.
- *(Note: Hệ thống workflow đồ sộ này hiện là một "Tài sản doanh nghiệp" có thể chuyển giao/thương mại hóa riêng biệt).*

---

## 🛠️ 3. Kịch Bản Demo Live

**Mục tiêu:** Khoe sức mạnh của việc có một hệ thống Workflow đồ sộ, và tốc độ khởi tạo 6 thư mục trong 1 giây.

**Bước 1:** Bật nội dung file code `biz-model-setup.md` lên cho học viên xem trước mặt (nhấn mạnh vào sự phức tạp của 1 quy trình được chuẩn hóa).
**Bước 2:** Mở Terminal ngay trong Antigravity Editor.
**Bước 3:** Chạy đoạn lệnh dưới đây để mô phỏng kết quả Bước 3 của Workflow (Auto-Generate Workspace). 

---

## 📦 4. Đoạn Mã Khởi Tạo Nhanh (Sếp Copy & Chạy Terminal)

*Chỉ cần copy khối mã dưới đây paste vào Terminal của dự án mô phỏng, nó sẽ tự tạo 6 thư mục và 6 file Master đại diện:*

```bash
# Tạo thư mục gốc cho Business Context
mkdir "00_DoanhNghiep_SSOT"
cd "00_DoanhNghiep_SSOT"

# Tạo 6 trụ cột chiến lược
mkdir "01_Biz_Strategy" "02_Product_Strategy" "03_Mkt_Strategy" "04_Ops_Strategy" "05_Financial_Model" "06_MBO"

# Đặt các file Master Template vào trong để AI điền thông tin sau khi phỏng vấn
echo "# Tuyên Ngôn Định Vị Doanh Nghiệp" > "01_Biz_Strategy/biz_strategy_master.md"
echo "# Danh mục Sản phẩm & Giá" > "02_Product_Strategy/product_strategy_master.md"
echo "# Phễu Marketing & Chân dung Khách hàng" > "03_Mkt_Strategy/mkt_strategy_master.md"
echo "# Quy trình Vận hành & SLA" > "04_Ops_Strategy/ops_strategy_master.md"
echo "# Kế hoạch Tài chính & Dòng tiền" > "05_Financial_Model/financial_model_master.md"
echo "# Mục tiêu OKRs & Chỉ số KPIs" > "06_MBO/mbo_master.md"

echo "✅ ĐÃ TẠO XONG 6 TRỤ CỘT BIZ MODEL - Sẵn sàng cho AI đọc Context!"
```

---

### 🎙️ KỊCH BẢN NÓI (VOICEOVER & LIVE DEMO)
*(Sếp vừa thao tác chạy lệnh tạo folder vừa đọc đoạn này)*

> *"Để AI làm việc hiệu quả, nó cần nắm trọn vẹn 6 trụ cột của doanh nghiệp. Chúng ta tự động hóa việc tạo ra các Thư mục SSOT (Single Source of Truth) bằng tư duy Biz Model Setup.*
> *Mỗi thư mục này có 1 file Master (vd: `mkt_strategy_master.md`). Tại sao? Để đây trở thành "Context Folder". Bất cứ khi nào tạo Agent Marketing, chúng ta không cần ngồi giải thích lại cho nó công ty ta bán gì, mà chỉ việc gán link: `context: [03_Mkt_Strategy/]` là xong!"*
> **BÀI HỌC CỐT LÕI:** 
> Thay vì ngồi tự nghĩ, quy trình `/biz-model-setup` của chúng ta sẽ phỏng vấn liên tục rồi trong đúng 3 giây, gen ra toàn bộ cấu trúc thư mục này. Từ nay về sau, nếu @Writer cần viết báo cáo mảng nào, nó tự động vào `01_Biz_Strategy` đọc định vị, rồi sang `03_Mkt_Strategy` đọc phễu. Con AI giờ đã có linh hồn của công ty bạn, mà bạn không tốn 1 giọt mồ hôi gõ chữ!
