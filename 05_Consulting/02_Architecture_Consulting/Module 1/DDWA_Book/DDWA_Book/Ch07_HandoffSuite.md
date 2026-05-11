# CHƯƠNG 7: HANDOFF SUITE — 9 MÓN BẮT BUỘC

Bộ 9 file/folder tại ROOT mỗi workspace đảm bảo bất kỳ Agent nào bước vào cũng tự vận hành được.

| # | Món | File/Folder | Vai trò |
|:---:|:---|:---|:---|
| 1 | **Index** | `INDEX.md` | Bản đồ tổng quan workspace |
| 2 | **Guideline** | `Guideline.md` | Luật lệ, convention, quy ước |
| 3 | **Onboarding** | `Onboarding.md` | Hướng dẫn Agent/Human mới |
| 4 | **Handoff** | `Handoff.md` | Trạng thái bàn giao real-time |
| 5 | **Changelog** | `Changelog.md` | Lịch sử thay đổi lớn |
| 6 | **ToDo** | `ToDo.md` | Sprint + Backlog tracking |
| 7 | **Notes** | `Notes/` | Scratch pad (WIP, ý tưởng) |
| 8 | **Archive** | `Archive/` | Tài liệu cũ, không xóa |
| 9 | **Temporary** | `Temporary/` | File tạm, có thể xóa |

**Quy tắc:**
1. **Bắt buộc:** 9 món PHẢI có ở ROOT. Thiếu 1 = Audit Fail.
2. **Single Source:** Mỗi thông tin chỉ sống ở 1 nơi trong Suite. VD: Changelog ≠ Notes.
3. **Handoff.md là QUAN TRỌNG NHẤT:** File này Agent đọc ĐẦU TIÊN khi khởi tạo session mới. Phải có: Current State, WIP, Blockers, Next Actions.
4. **Archive, không xóa:** Tài liệu cũ chuyển vào Archive/, KHÔNG BAO GIỜ xóa.
