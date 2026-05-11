# Chương 4: Strategy Context & Biz Model — Nền tảng Chiến lược cho AI

> **Nguồn gốc:** Cánh sao số 1 — Strategy (Star Model™)
> **Câu hỏi cốt lõi:** *Làm thế nào để 100 AI Agent cùng hiểu sâu sắc một chiến lược khổng lồ mà không bị "tràn bộ nhớ" (Context Window Pollution)?*

---

## 1. Bài toán: Nghịch lý của Context Window

Trong Start Model, Strategy là "Norh Star" (Kim chỉ nam). Để tổ chức căn chỉnh (aligned), mọi Agent đều phải thấu hiểu chiến lược.

Nhưng trong mô hình AI-Agent:
- Giọng văn thương hiệu, phân tích đối thủ, dòng tiền, OKRs, Tech Stack... tổng cộng có thể dài vài trăm trang tài liệu.
- Rất tốn kém (về token) và làm giảm IQ của Agent nếu nhồi nhét *tất cả* vào một prompt. Gọi là **Context Window Pollution** (Ô nhiễm bộ nhớ ngữ cảnh).
- Nhưng nếu không cấp đủ, Agent sẽ "halucinate" (bịaa ra) quyết định sai lệch khỏi lợi ích cốt lõi của doanh nghiệp.

**Giải pháp:** Chúng ta không thể đưa cho AI 1 file khổng lồ. Chúng ta phải chia chiến lược thành một **Mạng lưới SSOT Navigator (Single Source of Truth Navigator)**.

---

## 2. Biz Model Setup Framework: 6 Strategy Domains

Để AI nắm bắt toàn cảnh mà không bị "ngộp", chiến lược doanh nghiệp phải được cấu trúc hóa chặt chẽ thành **6 miền chiến lược (Strategy Domains)**:

| Domain (Miền chiến lược)                  | Chứa thông tin gì?                                                        | Vai trò đối với AI                                                  |
| :---------------------------------------- | :------------------------------------------------------------------------ | :------------------------------------------------------------------ |
| **01. Biz Strategy** (Nền tảng Biz)       | Tầm nhìn, Sứ mệnh, Lợi thế cốt lõi (USP), Mô hình kinh doanh (BMC).       | Agent dùng để trả lời: *"Hành động này có đúng với định vị không?"* |
| **02. Product Strategy** (Sản phẩm)       | Product Portfolio, Roadmap, Pricing, Product-Market Fit.                  | Agent dùng để hiểu: *"Mình đang bán cái gì, giá bao nhiêu?"*        |
| **03. Mkt & Sales Strategy** (Thị trường) | Chân dung khách hàng (JTBD, Persona), Kênh phân phối, Kịch bản chốt sale. | Agent dùng để: Viết content, chạy ads, thiết kế phễu.               |
| **04. Ops Strategy** (Vận hành)           | Chuỗi giá trị, Tech Stack, Đối tác, Sơ đồ tổ chức, Cam kết dịch vụ (SLA). | Agent dùng để: Rút trích dữ liệu, setup workflow, chia việc.        |
| **05. Financial Model** (Tài chính)       | Dòng tiền, Unit Economics, Burn Rate, Hợp đồng pháp lý.                   | Agent dùng để: Phân tích Risk, duyệt ngân sách, làm báo cáo.        |
| **06. MBO Tracking** (Mục tiêu)           | North Star Metric, OKRs, Bảng rủi ro (Risk Heatmap).                      | Agent dùng để: Ưu tiên (Prioritize) task nào trước/sau.             |

---

## 3. Cấu trúc Hybrid: Master Files & Detail Files (Progressive Loading)

Để giải quyết triệt để Context Window Pollution, mô hình này sử dụng **Hybrid Architecture**:

*   **Master Files (Bức tranh tổng thể):** Mỗi Domain có đúng 1 file Master (VD: `biz_strategy_master.md`). Nó chứa thông tin tóm tắt, bao quát nhất.
*   **Detail Files (Chi tiết sâu):** Khi 1 khía cạnh quá phức tạp, nó được tách ra file Detail (VD: `customer_personas.md`, `department_kpis.md`).

**Progressive Loading (Tải lũy tiến) hoạt động như sau:**
Khi 1 Agent (VD: `@Writer`) nhận task viết bài facebook:
1. Nó **luôn luôn** đọc `biz_strategy_master.md` để hiểu hướng đi chung.
2. Tại đây có chứa 1 Backlink báo rằng: *"Đọc chi tiết khách hàng tại `03_Mkt_Sales_Strategy/customer_personas.md`"*.
3. `@Writer` chạy lệnh đọc đúng file Detail đó, bỏ qua hàng chục file Detail không liên quan khác (như cơ cấu tài chính hay pháp lý).

→ *Kết quả: Agent nhận ĐÚNG và ĐỦ Context, độ trễ và chi phí token thấp nhất.*

---

## 4. Triple-Layer Format: Cấu trúc bên trong 1 File Chiến lược

Theo Best Practice của việc Setup Business Model cho AI, mọi file chiến lược không được phép là "bản nháp mơ mộng". Nó bắt buộc tuân theo định dạng 3 lớp **(Triple-Layer Format)**:

1.  **Expected System (Kỳ vọng):** Doanh nghiệp MUỐN đạt được gì (Mô hình lý thuyết, tiêu chuẩn).
2.  **Current State (Thực trạng):** HIỆN TẠI đang có gì (Con số cụ thể, tài nguyên thực tế).
3.  **The Gap & Priority Action (Lỗ hổng & Cứu hỏa):** Khoảng cách giữa (1) và (2) là gì? Ai (Agent nào/Con người nào) đang chịu trách nhiệm vá lỗ hổng đó?

**Vì sao AI cần định dạng này?**
Nếu chỉ nhập "Kỳ vọng", Agent sẽ tưởng doanh nghiệp đã hoàn hảo và hành xử kiêu ngạo sai thực tế. Nếu chỉ nhập "Thực trạng", Agent không biết đích đến để tư vấn. Lớp thứ 3 "The Gap" biến chiến lược tĩnh thành **Mệnh lệnh hành động (Actionable Tasks)** cho AI_RM hoặc Architect Agent.

---

## 5. Anti-Patterns trong Thiết kế Chiến lược cho Agent

### Anti-pattern 1: "The Monolith" (Khối bự)
❌ **Lỗi:** Gom toàn bộ kế hoạch kinh doanh vào 1 file `Company_Strategy.md` dài 10.000 từ.
→ **Kết cục:** Agent cắt bớt (truncate) file, mất sạch insight quan trọng ở cuối.
→ **Giải pháp:** Chia 6 Domains, dùng Backlinks đan chéo.

### Anti-pattern 2: "The Static Dream" (Giấc mơ tĩnh)
❌ **Lỗi:** Viết tài liệu chiến lược một lần rồi bỏ xó. Tháng sau sản phẩm thay đổi nhưng file không update.
→ **Kết cục:** Agent @Writer mang thông số sản phẩm cũ đi quảng cáo. Khủng hoảng truyền thông.
→ **Giải pháp:** Thiết lập luồng **Update/Dual-Path Sync**. Khi thay đổi (VD: Cập nhật giá), quy trình phải gạch bỏ (strikethrough) cái cũ và thêm metadata `last_updated`, để AI nhận diện được lịch sử thay đổi thông qua `/beat` hoặc `/doccheck` workflows.

### Anti-pattern 3: "Empty Bullshit" (Ngôn từ rỗng tuếch)
❌ **Lỗi:** Viết "Tối ưu hóa trải nghiệm khách hàng vượt trội".
→ **Kết cục:** AI không hiểu phải làm gì. Nó sinh ra nội dung sáo rỗng tương tự.
→ **Giải pháp:** Chain of Thought + Anti-Bullshit. Phải đo lường được (VD: "Phản hồi ticket < 15 phút qua Zalo ZCA, CSAT > 4.5").

---

## 6. Tổng kết Cánh sao Strategy

| #       | Nguyên tắc              | Giải thích                                            | Câu lệnh / Tool gợi ý |
| :------ | :---------------------- | :---------------------------------------------------- | :-------------------- |
| **ST1** | **6 Strategy Domains**  | Phân tách chiến lược thành 6 miền rành mạch.          | `/biz-model-setup`    |
| **ST2** | **Hybrid Architecture** | Dùng Master File tóm quát + Detail File chi tiết.     | `Master vs Detail`    |
| **ST3** | **Progressive Loading** | Agent chỉ đọc Master, thấy Link nào cần mới đọc tiếp. | `Backlinks`           |
| **ST4** | **Triple-Layer Format** | Luôn nêu: Kỳ vọng → Thực trạng → Lỗ hổng (Gap).       | `Gap Dashboard`       |
| **ST5** | **Anti-Bullshit**       | Cấm dùng từ ngữ chung chung. Phải đo được.            | `DoD/Guidelines`      |

---
## 7. Liên kết với các chương khác
- **Chương 13 (Context & Knowledge):** Progressive loading là cốt lõi của việc nạp Rule và Context cho Agent.
- **Chương 15 (Operational Principles):** SSOT (Single Source of Truth) bắt buộc file Master luôn là nguồn chuẩn nhất, mọi Agent đều phải trỏ vào đó.
