---
title: "Technical Solutions"
id: "ARCH-002"
source: "Technical Solutions.docx"
converted: "2026-03-15 13:35"
status: "active"
---

Architecture

> **UPDATED 2026-03-15** — Xem [ARCH-004 Clarifications Log](ARCH-004_clarifications-log.md) cho toàn bộ changes.
> API Provider: **astrology-api.io** (không phải AstroVisor)

**Nguyên lý Cốt lõi: Độ chính xác, Chiều sâu và Phân tách Trách nhiệm**

**ƯU TIÊN HÀNG ĐẦU: TÍNH CHÍNH XÁC**

**Lớp 1: CÔNG CỤ TÍNH TOÁN (Xác định) - Vận hành qua astrology-api.io**

Dữ liệu đầu ra: Các thông số kỹ thuật chính xác, không bao gồm diễn giải (dữ liệu thô cho 5 hệ thống).

- Kết quả dữ liệu thô: Đóng vai trò cầu nối dữ liệu cho cơ sở tri thức L2.
- Kết quả diễn giải: Các thông tin diễn giải từ API sẽ được chuyển tiếp làm đầu vào cho Lớp 1.5.

**Lớp 1.5: LÀM GIÀU CƠ SỞ TRI THỨC TỪ DIỄN GIẢI API**

Các thông tin diễn giải từ phía API được lưu trữ tạm thời theo từng người dùng cụ thể, đảm bảo không gây nhiễu loạn cơ sở tri thức dùng chung.

**Lớp 2: CƠ SỞ TRI THỨC (Quy tắc)**

Thực hiện RAG (Truy xuất tạo phản hồi) dựa trên nguồn tài liệu hơn 2000 trang, tích hợp cùng các dữ liệu bổ trợ từ Lớp 1.5.

**Lớp 3: DIỄN GIẢI BẰNG AI (Sử dụng Claude, lấy L1 và L2 làm cơ sở đối chiếu)**

Dữ liệu đầu ra: Các phân tích dưới dạng văn xuôi có tính cá nhân hóa cao, đa chiều và sâu sắc.

Quy định về Độ dài văn bản (Word\_Length) theo Gói dịch vụ (Tier):

Hệ thống vận hành tối đa 20,000 từ, tuy nhiên việc hiển thị tại giao diện người dùng sẽ được phân cấp:

- **Gói FREE:** Giới hạn 2,000 từ — 2/10 chủ đề (Tổng quan & Tình yêu).
- **Gói PRO:** 10,000 từ — 10/10 chủ đề, mở khóa thêm 2 hệ thống (Human Design & BaZi).
- **Gói MAX:** 20,000 từ — 10/10 chủ đề, toàn bộ 5 hệ thống, PDF export.

Quy định về Độ dài văn bản theo Hệ thống: Trung bình khoảng 2,000 từ cho mỗi hệ thống. Nội dung có tính tương tác cao: người dùng có thể nhấp vào từng yếu tố cụ thể (như các sao, nhà hoặc nội dung chi tiết) để xem diễn giải sâu hơn.

**Tech Stack**

1. **Backend (Railway):**
   - ***Framework: FastAPI (Python 3.12, Docker)***
   - ORM: SQLAlchemy 2.0 async + Alembic migrations
   - Database: PostgreSQL 16 (Neon — serverless)
   - Cache: Redis 7 (Upstash — serverless)
   - Auth: JWT HS256 (python-jose + bcrypt)
     - access\_token: 30 ngày
     - refresh\_token: 30 ngay
   - AI: Anthropic Claude API (Haiku cho free, Sonnet cho paid - đảm bảo đủ thông tin về độ sâu và số lượng chữ → Prompt kỹ để trả lời theo khung câu hỏi)
   - External API: **astrology-api.io** (All 5 systems: Tử Vi, HD, BaZi, Vedic, Numerology — confirmed)
   - PDF: ReportLab
2. **Frontend (Vercel)**
   - ***Framework: Next.js 15 (App Router)***
   - Styling: Tailwind CSS v4 + shadcn/ui
   - State: Zustand (auth store)
   - Data fetching: TanStack Query (cache + refetch)
   - Charts: Recharts (RadarChart, custom components) — hoặc API chart rendering (test trước)
   - HTTP: **Axios** (JWT interceptor, auto refresh on 401)
3. **Payment — VietQR (Ưu tiên)**

**VietQR: Tạo QR code ngân hàng với mã giao dịch (transaction code)**
- Model: **One-time purchase** (không recurring subscription)
- Người dùng quét QR → chuyển khoản → mã giao dịch để đối soát tự động
- Không cần gateway trung gian, không phí gateway
- MoMo/ZaloPay/Bank Transfer đều quét được VietQR

1. **Deploy**

| **Service** | **Platform** | **Domain** |
| --- | --- | --- |
| Frontend | Vercel | ***Chưa setup*** |
| Backend | Railway | ***Chưa setup*** |
| Database | Neon | (managed) |
| Cache | Upstash | (managed) |

**Tier Model:** Backend LUÔN chạy/trả về kết quả của 5 systems và lưu vào dữ liệu của users đó. Frontend tier-gate.tsx xử lý truncate/blur ở phần UI để thể hiện theo đúng tier. Backend tier\_gate.py chi kiem soat max\_profiles va max\_words.

Việc phân cấp hiển thị theo từng gói dịch vụ (Tier) được thực hiện thông qua cơ chế phối hợp: ***tier-gate.tsx*** tại Frontend đảm nhận việc làm mờ (blur) hoặc cắt ngắn (truncate) nội dung trên giao diện, trong khi ***tier\_gate.py*** tại Backend thực thi kiểm soát các giới hạn về số lượng hồ sơ (max\_profiles) và giới hạn từ ngữ (max\_words).

| **Tính năng** | **Gói FREE** | **Gói PRO** | **Gói MAX** |
| --- | --- | --- | --- |
| Hệ thống | 5/5 (Bị giới hạn hiển thị) | 5/5 (Hiển thị đầy đủ) | 5/5 (Hiển thị đầy đủ) |
| Giới hạn từ ngữ (Frontend) | 2.000 từ (Dành cho 2 chủ đề) | 10.000 từ (Diễn giải theo chủ đề) | 20.000 từ (Phân tích chuyên sâu) |
| Chủ đề (Topics) | 2/10 (Tổng quan & Tình yêu) | 10/10 chủ đề | 10/10 chủ đề |
| Biểu đồ & Luận giải | Không hỗ trợ | 2/5 hệ thống (Bazi & Human Design) | Toàn bộ 5/5 hệ thống |
| Tiện ích bổ sung | - | Vận hạn theo năm | Xuất PDF 360 & Vận hạn năm |
| Mô hình Claude | Haiku | Sonnet | Sonnet |

**INTERPRETATION PIPELINE**

**User request**

*|*

*v*

*[Redis Cache Check] ── HIT ──> Response*

*|*

*MISS*

*|*

*v*

**[L1] Astrology.API**

*- Gọi API để thực hiện compute cả 5 hệ thống*

*- Trả về 3 loại dữ liệu*

*\* Raw data (Dữ Liệu Thô - Để diễn giải và RAG)*

*\* Chart data (biểu đồ - kiểm tra API có thể tạo charts trực tiếp vào web không)*

*\* Interpretation (Thêm vào dữ liệu để diễn giải cho users)*

*|*

*v*

**[L1.5] Knowledge Base Enrichment**

*- Ket hop output tu Astrology.API (interpreation)*

*voi Knowledge Base JSON files*

*- VD: knowledge\_base/zi\_wei/chinh\_tinh.json*

*- Output: enriched\_context*

*|*

*v*

**[L2] Claude AI**

*- Model: Haiku (free) / Sonnet (paid)*

*- Gioi han tu: 1000 / 10000 / 20000 theo tier*

*- Sinh van ban luan giai tieng Viet*

*- Prompt = system\_reading\_prompt(*

*framework, enriched\_context,*

*max\_words, language="vi"*

*)*

*|*

v

**[Validate + Cache]**

*- Kiem tra so tu, ngon ngu*

*- Truncate neu vuot gioi han*

*- Luu Redis: 30 ngày*

v

**Response**

**Backend Architecture (6 layers)**

1. **Layer 1: API Endpoints** - Compute cả 5 hệ thống và visualize output cả 5 hệ thống
2. **Layer 2: Middleware -** Control Tier Access thông qua Frontend Blur
3. **Layer 3: Services:** Diễn giải thông qua L1 → L1.5 → L2
4. **Layer 4: Engines:** Goi Astrology.API cho 5 systems, trả về raw + charts + interpretation
5. **Layer 5: Models (SQLAlchemy)**
6. **Layer 6: Core**)

**Frontend Architecture (5 layers)**

1. **Layer 1: Pages (Routes)**

Public & Private Diễn giải thông tin cho 10 chủ đề chi tiết - với khoảng 10000 từ (1000 từ/chủ đề) & Diễn giải 10000 từ cho 5 systems (2000 từ/system) → Chạy tất cả ở backend/ frontend sẽ kiểm soát phần hiển thị

1. **Layer 2: Components:** Chạy Backend luôn 5 charts về 5 hệ thống, các charts khác về tổng quan nếu có
2. ***Layer 3: Hooks (TanStack Query)***
3. ***Layer 4: State + Services***
4. ***Layer 5: Foundation***

**Auth Flow**

**Payment Flow (VietQR)**

**Chart Computation**

**CI/CD Pipeline**

Đầu ra cuối cùng là mô hình luận giải có hệ thống chủ đề/ hệ thống interactive charts + PDF Exports

—----------------------------------------------------------------------------------------------------------------------------

**LAYER 1: COMPUTE**

| **System** | **Input** | **Output (JSON)** | **Pitfall** |
| --- | --- | --- | --- |
| **Tử vi đẩu số** | - Ngày sinh Dương lịch (convert sang Âm lịch) - Giờ sinh - Giới tính *(một số trường phái dùng để tính chiều cung)* | menh\_cung · all\_palaces[12] (major\_stars) · dai\_van · menh\_chu · ngu\_hanh\_menh | - Dùng Tết Âm lịch làm mốc đổi năm trong BaZi - Thiếu xử lý tháng giêng âm lịch (sinh tháng 1-2 dương dễ nhầm năm) - Bỏ qua múi giờ khi tính giờ sinh (ảnh hưởng trực tiếp Cung Mệnh) |
| **Thần số học** | - Ngày/tháng/năm sinh đầy đủ (Dương lịch) - Họ tên đầy đủ (để tính Expression, Soul Urge, Personality) | life\_path · expression · soul\_urge · personal\_year · karmic\_debt · master\_numbers | - Validate: Master Numbers (11, 22, 33) KHÔNG rút gọn thêm - Validate: Karmic Debt Numbers (13, 14, 16, 19) ghi nhận trước khi rút gọn - Hệ Chaldean khác Pythagorean — phải thống nhất một hệ |
| **Human Design** | - Ngày/giờ/địa điểm sinh CHÍNH XÁC (sai 1 giờ → Type sai) - Dùng Swiss Ephemeris để tính Personality Sun + Design Sun (88 ngày trước sinh) | type · authority · profile · strategy · defined\_centers[9] · incarnation\_cross | - D026: Dùng atan(y/x) thay vì atan2(y,x) → sai góc hoàng đạo - D027: Timezone contamination qua new Date(y, m, d, h) → dùng Date.UTC() - D028: Date-only string → parse at UTC midnight → sai ngày |
| **Bazi** | - Ngày/tháng/năm/giờ sinh + địa điểm (múi giờ) | tu\_tru (năm/tháng/ngày/giờ Can-Chi) · nhat\_can · dung\_than · thap\_than · dai\_van |  |
| **Vedic (Jyotish)** | - Ngày/giờ/địa điểm sinh (lat/lon) - Ayanamsa: Lahiri (mặc định) - House system: Whole Sign (mặc định) | lagna · rashi · nakshatra · d1\_planets · vimshottari\_dasha (mahadasha/antardasha) | - Planet longitudes: ±0.1 degree so với astro.com - House cusps: ±0.5 degree - Ascendant/MC: ±0.1 degree |

**LAYER 2: KNOWLEDGE BASE**
Nguyên tắc: Từ điển ngữ nghĩa cố định. AI đọc, không được viết lại. Format: JSON/YAML files, validate bởi chuyên gia trước khi deploy.

| **Thông tin** | **Layer** | **Không được** |
| --- | --- | --- |
| Tên sao, vị trí cung | L1 | AI tự tính, và lưu dưới dạng JSON để reference với KB |
| Nội dung ý nghĩa cơ bản | L1.5 | Kết quả từ Astrology-API đẩy vào knowledge base (sử dụng riêng cho từng users) |
| Nội dung ý nghĩa sâu và chi tiết | L2 | RAG sử dụng kiến thức trong KB đã được setup để thực hiện |
| Nội dung ý nghĩa chi tiết thông tin | L3 | AI kết hợp kiến thức sẵn có |
| Đánh giá tổ hợp sao | L3 | AI kết hợp không có trong KB |
| Diễn giải cá nhân hoá | L3 | Nói sự thật L1/L2 sai |
| Ngôn ngữ tự nhiên, flow | L3 | Chỉ L3 làm điều này |

**LAYER 3:** Prompt Template chung cho cả 3 tier - chỉ kiểm soát phần hiển thị

**Separation: Hệ Thống vs Chủ Đề**

| **Tiêuu chí** | **Theo Hệ Thống** | **Theo Chủ Đề** |
| --- | --- | --- |
| **Góc nhìn** | "Vũ trụ sắp xếp bạn là ai"  (Why questions) | What > How > What’s Nexts  (Giảm bớt những thuật ngữ và tập trung vào những kiến thức có trọng lượng/quan trọng nhất) |
| **Lens** | 1 hệ thống, toàn diện các chủ đề theo từng hạng mục của hệ thống | 5 hệ thống để giải thích cho một domain duy nhất |
| **Time** | Trọn đời / vĩnh cửu | Hiện tại + 1–3 năm |
| **Vocabulary** | Thuật ngữ kỹ thuật của trường phái | Plain language, action-oriented - Hạn chế tối thiểu trong việc phân tích về kỹ thuật |