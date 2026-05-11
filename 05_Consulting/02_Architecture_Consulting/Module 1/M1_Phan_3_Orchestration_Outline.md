# Phần 3: Thiết kế và Điều phối Workflow (Orchestration & Quality)

**Mục tiêu:** Kiểm soát và cấu trúc hóa hàng trăm luồng lệnh đan xen. Khai tử tư duy "Lệnh vạn năng" (God Prompt). Hình thành hệ miễn dịch doanh nghiệp bằng hệ thống Quality Gates và Phanh ngắt mạch tài nguyên.

## 3.1 Cấu trúc Phân tầng Workflow (Workflow Tiering)

Không có sự ngang hàng trong kiến trúc phần mềm vận hành kinh doanh. Mọi Workflow được chế tạo bắt buộc phải được gắn sao định danh một trong 4 Tầng uy quyền sau:

- **Tier 0 (META):** Lệnh tối cao. Loại Workflow này can thiệp và làm thay đổi Sơ đồ kiến trúc toàn tổ chức (Tạo thêm phòng ban, Xóa Agent). Chỉ được kích hoạt bởi C-Level (CEO / Resource Manager).
- **Tier 1 (ORCHESTRATION):** Lệnh quản đốc. Bản thân nó không làm việc tay chân. Nó là băng chuyền rẽ nhánh quy tụ kết quả từ nhiều khâu chuyên môn lại với nhau. Thẩm quyền thuộc về Director Agent.
- **Tier 2 (EXECUTION):** Mắt xích thực thi. Đây là nơi duy nhất trực tiếp đổ mồ hôi: Code, Design, Phân tích số liệu. Do Specialist Agent phó nháy.
- **Tier 3 (UTILITY):** Lõi Tool-Oriented. Các đoạn Script (Python, Bash) siêu vi, vô hình. Chạy ngầm, gọi đâu đáp đấy (Extract file, kiểm lỗi, đếm chữ). Mọi Tầng T0, T1, T2 đều có đặc quyền gắn Tier 3 vào bên trong lõi hệ thống.

**Anti-patterns chí mạng:** Tuyệt đối né tránh **God Workflow** (Nhồi 500 yêu cầu vào một dòng Prompt duy nhất gây nổ bộ nhớ) hoặc **Flat Workflow** (Bầy nhầy không phân định chủ/tớ).

## 3.2 Kỹ thuật Điều phối, Gọi chéo & Vai trò AI_RM

- **Quyết định Quyền lực (Call Hierarchy):** Tầng trên (N) vung lệnh cho Tầng dưới (N+1). Hoặc gọi nhờ bạn Ngang hàng (Cross-calling). Lệnh 1 chiều, **KHÁNG CHỈ** cấp dưới gọi ngược tước quyền cấp trên.
- **Mạng lưới Khai báo (Dependency Map):** Mọi sự kiện gọi chéo (Sequential, Router, Parallel) đều không được "nói miệng", phải được cấu hình chết bằng mã `calls` và `called_by` trên thẻ YAML.
- **Ách thống trị AI_RM:** Resource Manager là "Giám đốc nhân sự" của Hub. Khước từ quyền đẻ cấu trúc của các đặc vụ cấp thấp, AI_RM cầm trịch việc sinh/diệt và gán quyền Autonomy. Không có RM, Hub sẽ chìm vào bãi rác sinh thái.

## 3.3 Hệ Thống Đo Lường (Measurement) & Red Team Rủi Ro

Để LLM chạm ngưỡng tự hành, cỗ máy AI đó phải được lập trình sự tự trọng (Năng lực tự nhận biết đúng sai).

- **Tầng 1 - Biến số Mấu chốt (Metrics):** Cân đối giữa *Quality* (Chất lượng đúng định luật) và *Velocity* (Tốc độ xuất xưởng). Tiên lượng vùng nổ tung (Blast Radius): Nếu Workflow này khựng lại, bao nhiêu Zone sẽ gãy dây chuyền?
- **Tầng 2 - Quality Gates (QG):** 4 Lớp Gác Cổng Sinh Tử:
  - `QG-0:` Đọc và Từ Chối - Không đưa đủ file -> Agent hất về.
  - `QG-1 & QG-2:` Peer Check (Đồng nghiệp AI đấu chéo nhau) & Guideline Check (Máy rà format).
  - `QG-3:` Human Approval (Quyền sinh sát gốc).
  - *Khắc phục Thông Đồng (AI Collusion):* Boss sử dụng vòng lặp Chaos Monkey thỉnh thoảng giật tập tin chấm lại tự động, dội án phạt nếu phát hiện AI chấm láo điểm cho nhau.
- **Tầng 3 - Configuration Feedback Loop:** Vòng luân hồi thưởng phạt qua quy mô Quyền tự trị (Autonomy).
- **Phân đội Red Team (Chốt chặn Tài nguyên):** Nhúng hệ thống Phanh khẩn cấp (Circuit Breaker) dựa trên hạn mức Tokens và Quotas. Số lần làm bài bị QG đẩy rớt chạm trần (Timeout limit) -> Ngắt toàn bộ để tránh Lặp Đệ Quy đốt hàng nghìn GB đô-la API vô ích.
