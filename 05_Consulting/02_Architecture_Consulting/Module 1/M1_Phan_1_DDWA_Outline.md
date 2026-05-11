# Phần 1: Kiến trúc Không gian làm việc Số (DDWA)

**Mục tiêu:** Giải quyết triệt để sự vô kỷ luật trong việc lưu trữ dữ liệu AI. Sinh viên phải nắm vững cách thiết kế một kiến trúc định hướng dữ liệu trước khi cấp quyền cho bất kỳ Agent nào hoạt động.

## 1.1 Tràn Context Window và Ảo giác AI (Hallucination)

- **Vấn đề cốt lõi:** Nhồi nhét hàng loạt tác vụ vào một giao diện chat duy nhất chắc chắn sẽ làm AI "tràn bộ nhớ" (Context Loss). Khi đó, Agent sẽ sinh ra ảo giác và tự bịa dữ liệu.
- **Tác hại của việc thiếu SSOT (Single Source of Truth):** Khi bản nháp và bản chốt nằm chồng chéo, AI sẽ ngộ độc thông tin. Hệ quả: Ra quyết định sai lệch, tự động lan truyền sự sai lệch đó cho toàn hệ thống.
- **Giải pháp:** Thiết lập "Văn phòng vật lý ảo" — **Data-Driven Workspace Architecture (DDWA)** để đóng gói và cô lập bộ nhớ của AI.

## 1.2 Nguyên lý Vận hành và 6 Quy luật Phái sinh

- **Mệnh đề gốc:** Tổ chức con người và tổ chức AI đều chia sẻ chung các chức năng kinh doanh phổ quát.
- **6 Quy luật Bất di bất dịch (Compliance Rules):**
  1. **Đối xứng (Isomorphism):** Sơ đồ tổ chức có $n$ phòng ban, không gian làm việc bắt buộc có $n$ thư mục (Mapping 1:1).
  2. **Ba Tầng (Tri-Layer):** Mỗi Zone phải đủ 3 cấu phần: *Chiến lược chỉ đạo* + *Dữ liệu tích lũy* + *Agent thực thi*.
  3. **Tự đủ (Self-Contained):** Agent thả vào thư mục nào phải tự định vị được nhiệm vụ tại đó mà không cần CEO can thiệp.
  4. **WIP vs SSOT (Phân ly Nháp – Chuẩn):** Nghiêm cấm đặt thư mục làm việc đan xen với thư mục lưu trữ chốt.
  5. **Discovery Before Delivery:** Cấm Agent khởi tạo chuỗi thực thi nếu thiếu bảng phân rã cấu trúc (SIPOC hoặc JTBD).
  6. **Multi-Pipeline:** Các sản phẩm khác luồng giá trị buộc phải chạy trên các dây chuyền (Pipeline) tách biệt.
- **Kiến trúc 7 Zones Chuẩn:** Governance, Production, Marketing, Sales, Operations, Finance, Human Resources. Không được tự ý gộp/tách nếu không có nghiệp vụ đặc thù.

## 1.3 Mô hình IPO Factory: Công trường (WIP) và Thư viện (SSOT)

- **Tư duy Dây chuyền (IPO Factory):** Không gian làm việc là cỗ máy khổng lồ, luân chuyển qua 3 trạm: Input (Đầu vào) → Process (Phân xưởng) → Output (Đầu ra).
- **Process (Công trường - SPRINT/):** Nơi dòng lệnh chạy. Bản nháp (WIP), log suy nghĩ, và vòng lặp lỗi được thực thi tại đây.
- **Input/Output (Thư viện - 7 Zones):** Kho chứa Single Source of Truth. Hoàn toàn sạch rác. Kết quả từ SPRINT sau khi vượt qua Quality Gate sẽ "Merge" ngược về đây làm Input cho Zone tiếp theo.

## 1.4 Mô hình Dữ liệu 4 Tầng (4-Layer Data Model)

Mọi tài liệu không phải là văn bản thô, chúng là Database Schema thu nhỏ.

- **Tầng 1 (YAML/JSON):** Chân lý cốt lõi (Machine-readable) - Dành riêng cho hệ thống và Agent đọc.
- **Tầng 2 (CSV/Database):** Nhật ký giao dịch - Ghi nhận Log và Ops Data.
- **Tầng 3 (Markdown/Views):** Phiên dịch T1 & T2 thành báo cáo cho con người.
- **Tầng 4 (Agent):** Lớp tương tác AI tự nhận thức và xử lý 3 tầng trên.

## 1.5 Handoff Suite và Kiểm thử Chịu tải (Stress Test)

- **Chuẩn 9 File Handoff:** Yêu cầu gắt gao tại mọi Root Folder (`INDEX.md`, `Changelog.md`, `ToDo.md`, v.v.). Trong đó, có ranh giới rõ ràng giữa file dành cho Máy đọc và file dành cho CEO đọc.
- **Đo lường đứt gãy bằng 5-Where (Ishikawa + SIPOC):** Rà soát nguồn gốc (Strategy), tiến độ (Tracking), lưu trữ (SSOT), lịch sử xáo trộn (History), và vết nháp (WIP). Mất 1 trong 5 đồng nghĩa workspace bị lỗi nứt gãy context.
