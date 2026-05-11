# KỊCH BẢN (WORKFLOW): TUYỂN DỤNG TỰ ĐỘNG
**Mã Workflow:** `/tuyen-dung-nhan-su`

>(Workflow nằm tại Trường đào tạo AI. Khi Sếp gõ lệnh này, toàn bộ hệ thống Agent sẽ phối hợp chạy theo chuỗi dây chuyền sau:)

## BƯỚC 1: Thu thập JD
- Thư ký @PA_ManMan (gọi tắt: Thư Ký) ping Trưởng phòng nhân sự để lấy file JD (Mô tả công việc) mới nhất.
- Đọc lướt yêu cầu lương, thưởng, chế độ tại gốc công ty.

## BƯỚC 2: Viết Content Kêu Gọi (Giao cho Marketing)
- @MktLead nhận JD từ Thư Ký. Giao việc cho @ContentWriter.
- @ContentWriter áp dụng Kỹ năng `Ky_nang_viet_PR_PAS.md` để viết bài đăng tuyển dụng hút máu.
- MktLead Duyệt.

## BƯỚC 3: Sàng lọc CV (Giao cho HR Agent)
- Cào 100 CV từ thư mục `99_Temp/CV_Nhap`. Dùng vòng lặp quét từ khóa chính.
- Output: Lập bảng Top 3 ứng viên có kinh nghiệm > 3 năm.

## BƯỚC 4: Kết thúc
- Trả kết quả bảng CSV cho Sếp.
- Cập nhật nhật ký tại `SprintLog.md`.

*(Sức mạnh của Workflow: Biến công việc kéo dài 1 tuần của 3 phòng ban thành quy trình AI chạy trong 1 phút).*
