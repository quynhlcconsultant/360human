# CHƯƠNG 2: BỘ 7 CHỨC NĂNG KINH DOANH PHỔ QUÁT

Dựa trên Porter's Value Chain, điều chỉnh cho mô hình doanh nghiệp số + AI-Agent:

| # | Chức năng | Mã | Mô tả | Luôn có? |
| :---: | :--- | :---: | :--- | :---: |
| 1 | **Chỉ huy & Chiến lược** | GOV | Tầm nhìn, sứ mệnh, BMC, SWOT, P&L, ra quyết định | ✅ Bắt buộc |
| 2 | **Sản xuất / R&D** | PRD | Tạo ra Sản phẩm/Dịch vụ cốt lõi | ✅ Bắt buộc |
| 3 | **Marketing & Tăng trưởng** | MKT | Thu hút khách hàng, branding, content | ✅ Bắt buộc |
| 4 | **Bán hàng & Chuyển đổi** | SAL | Chốt deal, thanh toán, onboarding | ✅ Bắt buộc |
| 5 | **Vận hành & CSKH** | OPS | Giao hàng, hậu mãi, giữ chân | ✅ Bắt buộc |
| 6 | **Tài chính & Kế toán** | FIN | Thu chi, dòng tiền, báo cáo tài chính | ✅ Bắt buộc |
| 7 | **Nhân sự & Tổ chức** | HRM | Tuyển dụng, onboarding, org chart | ⚠️ Tuỳ quy mô |

> 💡 6 chức năng đầu KHÔNG THỂ THIẾU bất kể quy mô. HRM tách riêng khi headcount > 10.

**Lưu ý:** FIN và HRM thường được nhúng vào GOV ở giai đoạn Startup. Khi Scale → TÁCH.

### Ánh xạ sang Cây Thư mục chuẩn
```
[WORKSPACE]/
├── 01_Governance/          # GOV (+ FIN, HRM khi quy mô nhỏ)
├── 02_Production/          # PRD
├── 03_Marketing/           # MKT (+ SAL khi quy mô nhỏ)
├── 04_Operations/          # OPS
```
