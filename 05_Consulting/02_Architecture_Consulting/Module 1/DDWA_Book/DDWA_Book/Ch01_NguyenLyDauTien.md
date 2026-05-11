# CHƯƠNG 1: NGUYÊN LÝ ĐẦU TIÊN

---

## 1.1 Mệnh đề Gốc

> *Mọi doanh nghiệp, bất kể quy mô, đều thực hiện cùng 1 bộ **Chức năng Kinh doanh Phổ quát (Universal Business Functions)**. Chúng chỉ khác nhau về **độ phức tạp** của mỗi chức năng, không khác nhau về **số lượng** chức năng.*

Một quán cà phê 1 người và một tập đoàn 10.000 người đều phải:

- Có chiến lược (dù chỉ trong đầu hay trong 200 trang PowerPoint)
- Tạo ra sản phẩm
- Bán hàng & marketing
- Quản lý tài chính
- Vận hành & chăm sóc khách hàng

→ **Suy ra:** Cấu trúc folder của workspace PHẢI phản ánh các chức năng phổ quát này, chứ không phải phản ánh quy mô.

---

## 1.2 Sáu Quy luật Phái sinh

### Quy luật 1: Đối xứng (Isomorphism Rule)

> *Cây thư mục là "hình chiếu số" của sơ đồ tổ chức. Mỗi folder = 1 phòng ban logic.*

Nếu sơ đồ tổ chức có 7 phòng ban → workspace có 7 folders cấp 1. Thêm phòng ban → thêm folder. Gộp phòng ban → gộp folder. **1:1 mapping bắt buộc.**

### Quy luật 2: Ba Tầng (Tri-Layer Rule)

> *Mỗi phòng ban = **Chiến lược** (tài liệu hướng dẫn) + **Vận hành** (dữ liệu thực tế) + **Agent** (AI Workforce phụ trách).*

```
Zone_02_Production/
├── [Chiến lược]  Product_Strategy.md, SIPOC.md, JTBD.md
├── [Vận hành]    Sprint_Output/, Work_Logs/
└── [Agent]       Assigned: A-07 (YL_Producer)
```

### Quy luật 3: Tự Đủ (Self-Contained Rule)

> *Bất kỳ ai bước vào 1 folder cũng phải tìm được: "Phòng này làm gì? Ai chịu trách nhiệm? Dữ liệu ở đâu?"*

Test đơn giản: Nếu một Agent mới "sinh ra" và được giao Zone 03_Marketing, nó có thể tự vận hành mà không cần hỏi lại CEO không? Nếu không → Zone thiếu tài liệu.

### Quy luật 4: WIP/SSOT (Sprint vs Library Rule — v1.1)

> *Workspace PHẢI tách biệt rõ ràng giữa **Công trường** (Sprint — dang dở) và **Thư viện** (SSOT — hoàn thiện).*
>
> Single Source Of Truth

Chi tiết xem **Chương 5**.

### Quy luật 5: Discovery Before Delivery (v1.2)

> *CẤM mọi Agent triển khai sản phẩm/tính năng khi chưa hoàn thành bộ ba Discovery tối thiểu: **SIPOC** (hiểu quy trình) + **JTBD** (hiểu khách hàng) + **5 Whys** (hiểu nguyên nhân gốc rễ).*

Xem SDL v1.2 Domain 3, file P-10 → P-15. Chi tiết xem **Chương 11**.

### Quy luật 6: Multi-Pipeline (v1.2)

> *Khi workspace sản xuất nhiều loại sản phẩm khác biệt (Content vs Tool vs SaaS), mỗi pipeline PHẢI có SIPOC riêng. Không được gộp chung vì Input/Output/Quality Gate khác nhau.*

Chi tiết xem **Chương 12**.
