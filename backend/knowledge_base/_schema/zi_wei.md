---
system: zi_wei
display_name: "Tử Vi Đẩu Số"
display_name_en: "Purple Star Astrology (Zi Wei Dou Shu)"
total_files: 6
priority: P0
est_pages: ~600
---

# Tử Vi — KB Schema

## Files & Categories

| File | Category | Entries | Description |
|------|----------|---------|-------------|
| `chinh_tinh.md` | chinh_tinh | 14 | 14 Chính Tinh (Major Stars) |
| `phu_tinh.md` | phu_tinh | ~30 | Phụ Tinh + Tạp Tinh (Minor Stars) |
| `cung.md` | cung | 12 | 12 Cung (Palaces) |
| `dai_van.md` | dai_van | 12 | Đại Vận (Major Cycles, 10-year periods) |
| `ngu_hanh.md` | ngu_hanh | 5 | Ngũ Hành (Five Elements interaction) |
| `combinations.md` | combinations | ~20 | Tổ hợp sao nổi bật (Star Combinations) |

## Entry Schema: Chính Tinh

```markdown
## Tử Vi (Emperor Star)

**ID:** zi_wei_tu_vi
**Category:** chinh_tinh
**Ngũ Hành:** Thổ (Earth)
**Âm Dương:** Dương
**Nhóm:** Tử Vi Tinh Hệ
**Keywords:** hoàng đế, lãnh đạo, cao quý, tự trọng

### Ý nghĩa tổng quát
Tử Vi là chủ tinh trong Tử Vi Đẩu Số, đại diện cho vị trí hoàng đế.
Người có Tử Vi tọa mệnh thường có phong thái cao quý, tự trọng cao,
có năng lực lãnh đạo bẩm sinh...

### Tại Cung Mệnh
{Tính cách, bản chất khi Tử Vi ở cung Mệnh}

### Tại Cung Tài Bạch
{Tài chính, cách kiếm tiền}

### Tại Cung Quan Lộc
{Sự nghiệp, công việc}

### Tại Cung Phu Thê
{Hôn nhân, tình cảm}

### Tại Cung Phúc Đức
{Phúc đức, tâm linh, tinh thần}

### Tại Cung Thiên Di
{Quan hệ xã hội, di chuyển}

### Miếu / Vượng / Đắc / Bình / Hãm
- **Miếu (Tý, Ngọ):** Phát huy tối đa...
- **Hãm (...):** Suy yếu, cần phụ tinh hỗ trợ...

### Tổ hợp nổi bật
- **Tử Vi + Thiên Phủ:** Cách "Tử Phủ" — quyền quý song toàn
- **Tử Vi + Thất Sát:** Cách "Tử Sát" — uy quyền, áp lực lớn
- **Tử Vi + Phá Quân:** Cách "Tử Phá" — phá cách, đổi mới
- **Tử Vi + Tham Lang:** Cách "Tử Tham" — đa tài, hưởng thụ
```

## Entry Schema: Cung (Palace)

```markdown
## Cung Mệnh (Life Palace)

**ID:** zi_wei_cung_menh
**Category:** cung
**Vị trí:** Palace #1
**Domain mapping:** Overview, Identity
**Keywords:** bản mệnh, tính cách, cuộc đời, bản chất

### Ý nghĩa
Cung Mệnh là cung quan trọng nhất, thể hiện bản chất con người,
tính cách gốc, và hướng đi chính của cuộc đời...

### Cách luận giải
1. Xem chủ tinh tọa cung Mệnh (sao nào ngồi ở đây)
2. Xem cung Mệnh thuộc địa chi nào (Tý, Sửu, Dần...)
3. Xem tam hợp: Mệnh — Tài Bạch — Quan Lộc
4. Xem đối cung: Mệnh ↔ Thiên Di

### Sao tọa cung Mệnh → ý nghĩa tóm tắt
- **Tử Vi:** Cao quý, lãnh đạo
- **Thiên Cơ:** Thông minh, mưu lược
- **Thái Dương:** Nhiệt huyết, quảng đại
- ...
```

## Entry Schema: Đại Vận (Major Cycle)

```markdown
## Đại Vận — Cách tính và luận giải

**ID:** zi_wei_dai_van
**Category:** dai_van
**Keywords:** đại vận, tiểu vận, lưu niên, thời vận

### Nguyên lý
Đại vận là chu kỳ 10 năm, mỗi đại vận tương ứng với 1 cung
trong 12 cung lá số. Chiều đi thuận/nghịch phụ thuộc Âm Dương...

### Cách tính
1. Xác định cung khởi đại vận (Mệnh + tuổi khởi vận)
2. Chiều đi: Dương nam/Âm nữ → thuận; Âm nam/Dương nữ → nghịch
3. Mỗi 10 năm chuyển sang cung kế tiếp

### Luận giải Đại Vận tại từng cung
- **Đại Vận tại Cung Mệnh:** Giai đoạn tự lập, khẳng định bản thân
- **Đại Vận tại Cung Phụ Mẫu:** Ảnh hưởng từ gia đình, truyền thống
- ...
```

## 14 Chính Tinh Checklist

| # | Sao | ID | Ngũ Hành | Nhóm |
|---|-----|----|----------|------|
| 1 | Tử Vi | tu_vi | Thổ | Tử Vi |
| 2 | Thiên Cơ | thien_co | Mộc | Tử Vi |
| 3 | Thái Dương | thai_duong | Hỏa | Tử Vi |
| 4 | Vũ Khúc | vu_khuc | Kim | Tử Vi |
| 5 | Thiên Đồng | thien_dong | Thủy | Tử Vi |
| 6 | Liêm Trinh | liem_trinh | Hỏa | Tử Vi |
| 7 | Thiên Phủ | thien_phu | Thổ | Thiên Phủ |
| 8 | Thái Âm | thai_am | Thủy | Thiên Phủ |
| 9 | Tham Lang | tham_lang | Thủy/Mộc | Thiên Phủ |
| 10 | Cự Môn | cu_mon | Thủy | Thiên Phủ |
| 11 | Thiên Tướng | thien_tuong | Thủy | Thiên Phủ |
| 12 | Thiên Lương | thien_luong | Mộc | Thiên Phủ |
| 13 | Thất Sát | that_sat | Kim | Thiên Phủ |
| 14 | Phá Quân | pha_quan | Thủy | Thiên Phủ |

## 12 Cung Checklist

| # | Cung | ID | Domain Mapping |
|---|------|----|----------------|
| 1 | Mệnh | cung_menh | Overview, Identity |
| 2 | Phụ Mẫu | cung_phu_mau | Family |
| 3 | Phúc Đức | cung_phuc_duc | Growth, Wellness |
| 4 | Điền Trạch | cung_dien_trach | Finance (property) |
| 5 | Quan Lộc | cung_quan_loc | Career |
| 6 | Nô Bộc | cung_no_boc | Social |
| 7 | Thiên Di | cung_thien_di | Social, Travel |
| 8 | Tật Ách | cung_tat_ach | Health |
| 9 | Tài Bạch | cung_tai_bach | Finance |
| 10 | Tử Tức | cung_tu_tuc | Family (children) |
| 11 | Phu Thê | cung_phu_the | Love |
| 12 | Huynh Đệ | cung_huynh_de | Social (siblings) |
