---
title: "Vietnamese Copy — All 8 Screens"
id: "FE-006"
updated: "2026-03-16"
status: "ready-for-review"
tone: "Wise elder — guidance, not fortune-telling. Warm, direct, never mystical."
---

# Vietnamese Copy — 360Human

> Tất cả copy dùng "bạn" (second person).
> Không dùng từ ngữ mê tín, không cải lương.
> Giọng điệu: ấm áp, rõ ràng, như người thầy hiểu biết — không như trang bói toán.

---

## S1 — Landing Page

### Meta
```
<title>360Human — Hiểu bản thân qua 5 hệ thống cổ đại</title>
<meta description="Kết hợp Tử Vi, Số học, Human Design, BaZi và Vedic Astrology để tạo ra bức tranh toàn diện nhất về con người bạn.">
```

### Header
```
Logo: 360Human
Nav link: Đăng nhập
```

### Hero Section
```
H1: Bạn phức tạp hơn một con số sinh nhật.

Subheadline:
5 hệ thống cổ đại kết hợp để cho bạn thấy điều mà từng hệ thống riêng lẻ không thể nói.

CTA chính: Khám phá bản thân
CTA phụ: Tìm hiểu cách hoạt động ↓
```

### Value Props (3 cards)
```
Card 1:
Icon: [compass]
Title: Không đoán mò
Body: Dựa trên ngày giờ sinh cụ thể của bạn — không phải câu hỏi trắc nghiệm.

Card 2:
Icon: [layers]
Title: Năm hệ thống, một bức tranh
Body: Tử Vi, Số học, Human Design, BaZi, Vedic — mỗi hệ thống thêm một chiều sâu.

Card 3:
Icon: [arrow-right-circle]
Title: Thực hành được ngay
Body: Phân tích kết thúc bằng hành động cụ thể, không phải lời tiên tri mơ hồ.
```

### Framework Section
```
Section label: Năm hệ thống phân tích

Tử Vi
BaZi
Human Design
Số học (Numerology)
Vedic Astrology
```

### Social Proof
```
Quote: "Lần đầu tiên tôi đọc một bài phân tích mà không thấy mình đang đọc về người khác."
— Minh Anh, 28 tuổi, TP.HCM
```

### Pricing Teaser
```
Text: Bắt đầu miễn phí — không cần thẻ tín dụng.
```

### Footer
```
Links:
- Về 360Human
- Chính sách bảo mật
- Điều khoản sử dụng
- Liên hệ

Copyright: © 2026 360Human. All rights reserved.
```

---

## S2 — Register / Login

### Page Meta
```
Register: <title>Tạo tài khoản — 360Human</title>
Login: <title>Đăng nhập — 360Human</title>
```

### Tab Labels
```
Tab 1: Đăng ký
Tab 2: Đăng nhập
```

### Register Form
```
Heading: Bắt đầu hành trình của bạn

Label: Email
Placeholder: email@example.com

Label: Mật khẩu
Placeholder: Tối thiểu 8 ký tự

Label: Xác nhận mật khẩu
Placeholder: Nhập lại mật khẩu

Button: Tạo tài khoản

Legal: Bằng cách tạo tài khoản, bạn đồng ý với
Điều khoản dịch vụ và Chính sách bảo mật của chúng tôi.

Switch prompt: Đã có tài khoản? Đăng nhập
```

### Login Form
```
Heading: Chào mừng trở lại

Label: Email
Placeholder: email@example.com

Label: Mật khẩu
Placeholder: Mật khẩu của bạn

Link: Quên mật khẩu?

Button: Đăng nhập

Switch prompt: Chưa có tài khoản? Đăng ký
```

### Error Messages
```
Email không hợp lệ: Vui lòng nhập địa chỉ email hợp lệ.
Email đã tồn tại: Email này đã được đăng ký. Đăng nhập hoặc đặt lại mật khẩu.
Mật khẩu không khớp: Mật khẩu xác nhận chưa đúng.
Mật khẩu quá ngắn: Mật khẩu cần ít nhất 8 ký tự.
Sai thông tin: Email hoặc mật khẩu không đúng. Vui lòng thử lại.
```

### Forgot Password
```
Heading: Đặt lại mật khẩu
Body: Nhập email của bạn — chúng tôi sẽ gửi đường dẫn để đặt lại mật khẩu.
Label: Email
Button: Gửi đường dẫn
Success: Kiểm tra hộp thư của bạn. Email đặt lại mật khẩu đã được gửi.
```

---

## S3 — Onboarding Wizard

### Top Navigation
```
Progress: Bước [X]/5
Back button: ← Quay lại
```

### Step 1 — Ngày sinh
```
Question: Bạn sinh ngày nào?
Labels: Ngày / Tháng / Năm
Placeholders: DD / MM / YYYY
Helper: Ngày sinh ảnh hưởng đến cả 5 hệ thống phân tích.
Error: Ngày sinh không hợp lệ. Vui lòng kiểm tra lại.
Button: Tiếp tục →
```

### Step 2 — Giờ sinh
```
Question: Bạn sinh lúc mấy giờ?
Label: Giờ sinh
Placeholder: HH:MM
Helper: Giờ sinh quan trọng cho Tử Vi và Human Design — càng chính xác càng tốt.

Checkbox: Tôi không biết giờ sinh
[When checked]:
Note: Không sao — bạn vẫn có thể dùng 360Human. Một số phân tích sẽ có độ chính xác thấp hơn.

Button: Tiếp tục →
```

### Step 3 — Nơi sinh
```
Question: Bạn sinh ở đâu?
Label: Thành phố khi sinh
Placeholder: Tìm kiếm thành phố...
Helper: Vị trí địa lý ảnh hưởng đến múi giờ và tọa độ trong biểu đồ.
Error: Không tìm thấy thành phố. Hãy thử tên khác.
Button: Tiếp tục →
```

### Step 4 — Giới tính
```
Question: Giới tính khi sinh của bạn?
Options: Nam / Nữ / Khác
Note: Thông tin này dùng để tính toán Tử Vi — không ảnh hưởng đến cách giải thích kết quả.
Button: Tiếp tục →
```

### Step 5 — Tên
```
Question: Bạn muốn chúng tôi gọi bạn là gì?
Label: Tên của bạn
Placeholder: Tên hoặc biệt danh
Helper: Nhập tên đầy đủ khi sinh để tính Số học được chính xác nhất.
Note: Bạn có thể thay đổi tên hiển thị sau trong phần Hồ sơ.
Button: Bắt đầu khám phá →
```

### Loading Screen (after step 5 submit)
```
Title: Đang tạo biểu đồ của bạn...
Body: Chúng tôi đang kết hợp dữ liệu từ 5 hệ thống phân tích.
[Animation placeholder]
```

### Welcome (first time on dashboard)
```
Banner: Biểu đồ của bạn đã sẵn sàng, [Name].
Sub: Khám phá các chủ đề bên dưới để bắt đầu.
```

---

## S4 — Dashboard / Home

### Top Bar
```
Greeting: Xin chào, [Name]
```

### Profile Summary Card
```
Birth info: [Ngày tháng năm] · [Thành phố]
System label: 5 hệ thống đã kết nối
Link: Xem biểu đồ chi tiết →
```

### Section Heading
```
Chủ đề phân tích
```

### 10 Topic Cards

```
1. Tổng quan bản thân
   Bạn thực sự là ai — bên dưới những gì mọi người nhìn thấy.
   [FREE]

2. Sứ mệnh & mục đích sống
   Bạn sinh ra để làm gì — và con đường nào phù hợp nhất.
   [FREE]

3. Tình cảm & các mối quan hệ
   Cách bạn yêu, những gì bạn cần, và những gì làm bạn tổn thương.
   [FREE]

4. Sự nghiệp & nghề nghiệp
   Môi trường làm việc phù hợp, vai trò tự nhiên, cách thành công.
   [PRO]

5. Tài chính & tiền bạc
   Mối quan hệ của bạn với tiền — bao gồm những điểm mù.
   [PRO]

6. Sức khỏe & năng lượng
   Cách cơ thể và năng lượng bạn vận hành theo chu kỳ.
   [PRO]

7. Gia đình & nguồn gốc
   Những mẫu hình từ gia đình — và cách bạn mang chúng theo.
   [PRO]

8. Điểm mạnh & tài năng
   Những khả năng tự nhiên bạn có thể chưa nhận ra.
   [PRO]

9. Thách thức & bóng tối
   Những khu vực cần nhìn thẳng — không phải để sợ, mà để hiểu.
   [MAX]

10. Thời điểm & chu kỳ
    Bạn đang ở đâu trong chu kỳ lớn — và giai đoạn này mang lại gì.
    [MAX]
```

### Upgrade Banner (FREE users)
```
Text: Mở khóa 7 chủ đề còn lại với gói PRO.
CTA: Xem các gói →
```

### Tier Gate Overlay
```
Lock label: Nội dung PRO
CTA: Nâng cấp để đọc →
```

---

## S5 — System Reading

### Breadcrumb
```
← Trang chủ
```

### Tab Labels
```
Tử Vi | BaZi | Human Design | Số học | Vedic
```

### System Headings & Taglines
```
Tử Vi — Bản đồ thiên mệnh
BaZi — Tứ trụ mệnh cục
Human Design — Thiết kế con người
Số học — Ngôn ngữ của con số
Vedic Astrology — Chiêm tinh Ấn Độ
```

### Missing Birth Time Banner
```
⚠ Bạn chưa nhập giờ sinh. Biểu đồ Tử Vi và Human Design có thể không chính xác hoàn toàn.
Link: Cập nhật thông tin →
```

### Key Facts Label
```
Điểm nổi bật
```

### CTA at bottom
```
Xem phân tích tổng hợp theo chủ đề →
```

---

## S6 — Topic Reading

### Breadcrumb
```
← Trang chủ
```

### Source Tags
```
Tử Vi  |  Human Design  |  BaZi  |  Số học  |  Vedic
```

### Standard Reading Structure Labels
```
Section labels used in readings:
- Con người bạn
- Cách bạn vận hành
- Điểm mạnh
- Điểm cần lưu ý
- Hướng đi
- Bóng tối
- Những bước tiếp theo
```

### Tier Gate
```
Heading: Tiếp tục đọc với gói PRO
Body: Bạn đang xem phiên bản rút gọn. Nâng cấp để đọc toàn bộ phân tích, bao gồm phần hành động cụ thể.
CTA: Xem gói PRO →
```

### Related Topics
```
Label: Chủ đề liên quan
```

---

## S7 — Pricing Page

### Page Heading
```
H1: Mở khóa toàn bộ hành trình của bạn.
Sub: Chọn gói phù hợp. Không cam kết dài hạn.
```

### Tier Cards

#### FREE
```
Tier: FREE
Price: 0đ / mãi mãi
Tagline: Bắt đầu khám phá bản thân.
Features:
✓ 3 chủ đề cơ bản
✓ 5 biểu đồ hệ thống đầy đủ
✓ Cập nhật miễn phí
CTA: Đang dùng (if current) / Bắt đầu miễn phí
```

#### PRO
```
Tier: PRO
Badge: Phổ biến nhất
Price: 99.000đ / tháng
Tagline: Cho những ai muốn hiểu sâu hơn.
Features:
✓ Tất cả tính năng FREE
✓ 10 chủ đề phân tích đầy đủ
✓ Phân tích chi tiết từng hệ thống
✓ Cập nhật định kỳ theo chu kỳ
CTA: Nâng cấp PRO
```

#### MAX
```
Tier: MAX
Price: 199.000đ / tháng
Tagline: Cho những ai muốn nhìn thẳng vào mọi thứ.
Features:
✓ Tất cả tính năng PRO
✓ Phân tích bóng tối & thách thức
✓ Chu kỳ & thời điểm (Đại vận, Personal Year)
✓ Ưu tiên cập nhật tính năng mới
CTA: Nâng cấp MAX
```

### Feature Table Header
```
So sánh chi tiết
```

### Payment Note
```
Thanh toán qua VietQR hoặc thẻ quốc tế.
Hủy bất kỳ lúc nào — không phí phạt.
```

### FAQ
```
Q: Tôi có thể hủy bất kỳ lúc nào không?
A: Có. Gói đăng ký có thể hủy bất kỳ lúc nào. Bạn vẫn có thể dùng đến hết kỳ thanh toán.

Q: Dữ liệu của tôi có được bảo mật không?
A: Dữ liệu sinh của bạn chỉ dùng để tính toán biểu đồ và không được chia sẻ với bên thứ ba.

Q: Nếu tôi thay đổi gói thì sao?
A: Bạn có thể nâng hoặc hạ gói bất kỳ lúc nào. Thay đổi có hiệu lực ngay trong kỳ thanh toán tiếp theo.
```

---

## S8 — Profile + Settings

### Page Heading
```
Hồ sơ của bạn
```

### Profile Section
```
Label: Tên hiển thị
Edit prompt: Nhấn để chỉnh sửa
Save: Lưu
Cancel: Hủy

Label: Email
Note: Không thể thay đổi sau khi đăng ký.

Tier section heading: Gói đăng ký
Link: Quản lý gói →
```

### Birth Data Section
```
Heading: Thông tin sinh
Label: Ngày sinh
Label: Giờ sinh
Label: Nơi sinh
Link: Cập nhật thông tin sinh →
Note: Thay đổi thông tin sinh sẽ tạo lại toàn bộ biểu đồ.
```

### Change Password Section
```
Heading: Bảo mật

Link/Button: Đổi mật khẩu

[Expanded form]
Label: Mật khẩu hiện tại
Label: Mật khẩu mới (tối thiểu 8 ký tự)
Label: Xác nhận mật khẩu mới
Button: Cập nhật mật khẩu
Cancel: Hủy

Success toast: Mật khẩu đã được cập nhật.
Error: Mật khẩu hiện tại không đúng.
```

### Subscription Section
```
Heading: Gói đăng ký
Current: Bạn đang dùng gói [TIER]
[PRO/MAX] Gia hạn tiếp theo: [Date]
Link: Nâng cấp gói →
Link: Hủy đăng ký
```

### Danger Zone
```
Heading: Vùng nguy hiểm
Button: Xóa tài khoản

[Confirm dialog]
Title: Xác nhận xóa tài khoản
Body: Tất cả dữ liệu của bạn — bao gồm biểu đồ và lịch sử — sẽ bị xóa vĩnh viễn. Hành động này không thể hoàn tác.
Confirm: Xóa tài khoản
Cancel: Giữ tài khoản
```

---

## Global Copy

### Navigation (Header Nav — Web)
```
Desktop nav links: Trang chủ | Hệ thống | Chủ đề | Hồ sơ
Mobile hamburger menu: same 4 items, stacked
```

### Empty States
```
No readings yet: Biểu đồ của bạn đang được tạo. Thử lại sau ít phút.
Error loading: Không tải được dữ liệu. Vui lòng thử lại.
```

### Generic Error
```
Có lỗi xảy ra. Vui lòng thử lại hoặc liên hệ hỗ trợ nếu vấn đề tiếp tục.
```

### Generic Success
```
Đã lưu thành công.
```

### Upgrade Success Banner
```
Chào mừng đến với [PRO/MAX]. Tất cả nội dung đã được mở khóa.
```
