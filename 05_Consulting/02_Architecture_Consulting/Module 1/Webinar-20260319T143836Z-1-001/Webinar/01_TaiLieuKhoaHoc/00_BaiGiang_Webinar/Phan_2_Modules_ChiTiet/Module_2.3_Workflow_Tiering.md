# MODULE 2.3: PHÂN TẦNG QUY TRÌNH (WORKFLOW TIERING)
*(Hướng dẫn thực hành Live: 6 phút)*

---

## 🧐 1. Lý Thuyết: Cơ Chế "Cross-Calling" (Gọi Chéo)
- AI không chỉ phục vụ Sếp. **AI có thể tự gọi AI khác làm việc**.
- Khi một quy trình dài (Workflow), Agent nhận lệnh từ Sếp, phân tích ngữ cảnh, sau đó kích hoạt các Agent thực thi khác theo dạng chuỗi.
- **Tiêu chuẩn 3 tầng Workflow:**
  - **Tier 1 (Định tuyến):** Ví dụ `/go` để phân tích ngữ cảnh Sếp nói gì và chia việc.
  - **Tier 2 (Thực thi):** Viết bài, Deploy Code.
  - **Tier 3 (Tiện ích):** Tự động dọn file, cập nhật log.

---

## 🛠️ 2. Kịch Bản Demo Live

**Mục tiêu:** Cho học viên xem một kịch bản Workflow bằng Markdown, trong đó một Agent kích hoạt 3 Agent khác.

**Bước 1:** Đặt vấn đề: Sếp chỉ muốn gõ 1 câu `/viet-bai-ban-khoa-hoc`, Sếp lười chat nhiều.
**Bước 2:** Show cái "não" của lệnh `/viet-bai-ban-khoa-hoc` (là một file Markdown Workflow).

---

## 📦 3. Template Workflow (Sếp mở file này trên IDE)

```markdown
# WORKFLOW: /viet-bai-ban-khoa-hoc (Thuộc Tier 1: Điều phối)

> Agent điều phối quá trình lên chiến lược nội dung và kêu gọi nhóm viết bài, duyệt bài.

## Bước 1: Khảo sát đối thủ (Cross-call)
- @MktLead Hãy gọi Agent @Researcher sử dụng lệnh `/research-competitors` để xem các TT Tiếng Anh đang bán giá bao nhiêu.

## Bước 2: Thiết kế khung Offer
- @MktLead Dựa vào kết quả B1, áp dụng Skill `offer-packaging` để lên thang giá trị. Cần có 3 mồi câu (Bonus).

## Bước 3: Triển khai viết bài (Sequential Chain)
- Giao cho @Writer viết bản nháp theo đúng định vị (Context trong thư mục `01_Biz_Strategy`).
- Sau khi viết xong, @Writer PHẢI tự gọi `/audit-bai-viet` để tự check chính tả.

## Bước 4: Chốt Output
- Chạy tiện ích `/log` để cập nhật lại nhật ký hoạt động vào file `SprintLog.md`.
```

---
> **🗣️ Kịch bản nói (Voiceover):**
*"Giao diện như một văn bản bình thường, nhưng dưới góc độ Antigravity, đây là một cỗ máy tự động. Sếp gõ 1 lệnh `/viet-bai-ban-khoa-hoc`, con Lead sẽ sai vặt con Research đi cào data, sau đó sai vặt con Writer đi viết bài, cuối cùng bảo con Bot Utility ghi chép log. Quản trị doanh nghiệp bằng File Markdown là như vậy đó!"*

*(CEO Live Demo: Bấm chạy thử một quy trình `/go` trên màn hình, mô phỏng việc 1 lệnh kích hoạt một chuỗi Agent tự nói chuyện với nhau, hiện log thời gian thực)*

---
> **BÀI HỌC CỐT LÕI:** 
> Giao diện như một văn bản bình thường, nhưng dưới góc độ Antigravity, đây là một cỗ máy tự động. Sếp gõ 1 lệnh `/viet-bai-ban-khoa-hoc`, con Lead sẽ sai vặt con Research đi cào data, sau đó sai vặt con Writer đi viết bài, cuối cùng bảo con Bot Utility ghi chép log. Quản trị doanh nghiệp bằng File Markdown là như vậy đó!
