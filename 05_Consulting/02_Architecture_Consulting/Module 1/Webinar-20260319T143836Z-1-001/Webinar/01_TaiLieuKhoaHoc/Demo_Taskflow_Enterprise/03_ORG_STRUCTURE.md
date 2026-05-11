# 03. CƠ CẤU TỔ CHỨC NHÂN SỰ & QUYỀN LỰC (ORG_STRUCTURE.md)

Phân bổ quyền điều phối giữa con người và hệ thống AI Agents tại Doanh nghiệp.

## Sơ đồ Phân quyền (Autonomy Tier)
**1. Tier 0 (The Architect - Sếp):** 
- Quyền duyệt ngân sách, quyền đổi định hướng chiến lược.
- Quyền gõ lệnh `Terminal` để cấu hình thư mục Root.

**2. Tier 1 (Director Agents):**
- Vận hành tại `01_OPERATION`. 
- **Quyền:** Tự phân bổ task con (Sub-tasks) cho cấp dưới. 
- **Agent:** @MktLead, @TechLead.

**3. Tier 2 (Staff Agents):**
- Thực thi công việc tại các `Sprint Folders`.
- BẮT BUỘC gọi tiện ích báo cáo `/log` sau khi hoàn thành.
- **Agent:** @ContentWriter, @DataAnalyst, @Coder_Python.

## Nguyên tắc Truyền tin
Agent KHÔNG tự động gửi email cho Khách hàng nếu chưa có sự xác nhận chéo (Cross-check) từ **@MktLead** phê duyệt nội dung. Mọi file thành phẩm từ Sprint phải Merge vào `03_My_Projects` trước khi thực thi lệnh xuất bản.
