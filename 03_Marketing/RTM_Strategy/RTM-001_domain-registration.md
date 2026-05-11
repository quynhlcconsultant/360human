---
title: "Domain Registration Guide"
id: "RTM-001"
updated: "2026-03-15"
status: "active"
---

# Domain Registration — 360human.vn

---

## Option 1: Tên miền .vn (Recommended for Vietnam market)

### Nhà đăng ký phổ biến:

| Nhà cung cấp | Giá .vn/năm | Ưu điểm | Link |
|-------------|-------------|----------|------|
| **Tenten.vn** | ~350,000 VND | UI tốt, DNS nhanh, hỗ trợ tiếng Việt | tenten.vn |
| **MatBao.net** | ~390,000 VND | Lâu đời, ổn định | matbao.net |
| **INET.vn** | ~330,000 VND | Giá rẻ nhất | inet.vn |
| **PA Vietnam** | ~350,000 VND | VNNIC authorized | pavietnam.vn |
| **NameCheap** | ~$8-12 USD | Quốc tế, nhưng .vn cần CMND/CCCD | namecheap.com |

### Yêu cầu đăng ký .vn:
- **Cá nhân:** CMND/CCCD (scan or photo)
- **Doanh nghiệp:** Giấy ĐKKD
- **Thời gian:** 1-3 ngày làm việc (VNNIC duyệt)

### Các bước:
1. Vào tenten.vn (hoặc nhà cung cấp khác)
2. Tìm `360human.vn` → Check available
3. Đăng ký → Upload CMND/CCCD
4. Thanh toán (~350K VND/năm)
5. Chờ VNNIC duyệt (1-3 ngày)
6. Nhận email xác nhận → Domain active

---

## Option 2: Tên miền quốc tế (Backup)

Nếu `.vn` bị trùng hoặc muốn global:

| Domain | Giá/năm | Note |
|--------|---------|------|
| 360human.co | ~$25 | Short, clean backup |
| 360human.io | ~$30 | Startup standard |
| 360human.app | ~$14 | Modern, tech-friendly |

---

## DNS Setup sau khi có domain

### Cho Vercel (Frontend):
```
Type: CNAME
Name: @
Value: cname.vercel-dns.com

Type: CNAME
Name: www
Value: cname.vercel-dns.com
```

### Cho Railway (Backend API):
```
Type: CNAME
Name: api
Value: your-app.up.railway.app
```

### Kết quả:
- `360human.vn` → Vercel (frontend)
- `api.360human.vn` → Railway (backend)
- SSL tự động bởi Vercel + Railway

---

## Action Items

- [ ] Check `360human.vn` availability
- [ ] Đăng ký domain (ưu tiên tenten.vn hoặc inet.vn)
- [ ] Upload CMND/CCCD
- [ ] Chờ VNNIC approve (1-3 ngày)
- [ ] Setup DNS records (khi deploy Sprint 3)

**Tip:** Đăng ký ngay hôm nay vì cần 1-3 ngày duyệt. Đến Sprint 3 (W6) là cần domain sẵn sàng.
