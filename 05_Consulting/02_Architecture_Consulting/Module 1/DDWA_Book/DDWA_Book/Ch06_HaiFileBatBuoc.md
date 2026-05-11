# CHƯƠNG 6: HAI FILE BẮT BUỘC DÀNH CHO MÁY — DIRECTORY INDEX & CHANGELOG

> *Mỗi workspace PHẢI có 2 file quản trị cấu trúc. **LƯU Ý CỐT LÕI:** Hai file này DÀNH CHO MÁY MÓC ĐỌC. Con người KHÔNG BAO GIỜ chạm tay vào. AI Agent sẽ chịu trách nhiệm ghi lại mọi Vết Chân.*

## 6.1 `Directory_Index.md` — Bản đồ thư mục

**Vị trí:** Root của workspace (`[PROJECT]/Directory_Index.md`)
**Mục đích:** Để bất kỳ Agent nào được drop vào workspace đều tự động scan file này và biết mình đang ở đâu, tài liệu nào nằm ở đâu (Context Loading).
**Cập nhật:** Tự động bằng Script/Workflow quét cây thư mục.

## 6.2 `Changelog.md` — Nhật ký thay đổi

**Vị trí:** Root của workspace (`[PROJECT]/Changelog.md`)
**Mục đích:** Ghi vết MỌI thay đổi về cấu trúc thư mục để Audit và Rollback.
**Tự động hoá:** Các lệnh có tính cưỡng chế thay đổi cấu trúc/file (Sprint Merge, Setup Workspace) đều được nhúng sẵn Node ghi Changelog vào cuối Workflow.

## 6.3 Quy tắc Tự động hoá (Automation Integrity)
> ❗ **MỌI thao tác hệ thống PHẢI gọi workflow. Bên trong workflow ĐÃ ĐÓNG GÓI SẴN lệnh đè Changelog. Con người thoát khỏi gánh nặng admin data.**
