---
system: bazi
display_name: "Bát Tự / Tứ Trụ"
display_name_en: "BaZi (Four Pillars of Destiny)"
total_files: 5
priority: P1
est_pages: ~400
---

# BaZi — KB Schema

## Files & Categories

| File | Category | Entries | Description |
|------|----------|---------|-------------|
| `heavenly_stems.md` | thien_can | 10 | 10 Thiên Can (Heavenly Stems) |
| `earthly_branches.md` | dia_chi | 12 | 12 Địa Chi (Earthly Branches) |
| `day_master.md` | nhat_chu | 10 | Nhật Chủ (Day Master analysis) |
| `ten_gods.md` | thap_than | 10 | Thập Thần (Ten Gods relationships) |
| `luck_pillars.md` | dai_van | — | Đại Vận (Luck Pillars, 10-year cycles) |

## Entry Schema: Thiên Can

```markdown
## Giáp (Jiǎ) — Yang Wood

**ID:** bazi_thien_can_giap
**Category:** thien_can
**Ngũ Hành:** Mộc (Wood)
**Âm Dương:** Dương (Yang)
**Hình tượng:** Cây đại thụ, cột trụ
**Keywords:** lãnh đạo, chính trực, bền bỉ, cứng rắn

### Ý nghĩa
Giáp là Yang Wood — hình ảnh cây cổ thụ vững chãi.
Người Giáp mộc thường ngay thẳng, có trách nhiệm,
bảo vệ người khác như tán cây che chở...

### Tính cách khi là Nhật Chủ
- Chính trực, không uốn cong
- Trách nhiệm cao, đáng tin cậy
- Cứng đầu, khó thay đổi quan điểm
- Cần "ánh sáng" (Hỏa) và "nước" (Thủy) để phát triển

### Quan hệ Ngũ Hành
- **Sinh:** Thủy sinh Mộc (nước nuôi cây)
- **Khắc:** Mộc khắc Thổ (rễ cây phá đất)
- **Bị khắc:** Kim khắc Mộc (rìu chặt cây)
- **Bị tiết:** Mộc sinh Hỏa (cây cháy thành lửa)
```

## Entry Schema: Thập Thần

```markdown
## Chính Tài (Direct Wealth)

**ID:** bazi_thap_than_chinh_tai
**Category:** thap_than
**Quan hệ:** Nhật Chủ khắc, cùng Âm Dương
**Keywords:** tài chính ổn định, lương, thu nhập cố định

### Ý nghĩa
Chính Tài đại diện cho tài sản ổn định, thu nhập
từ lương hoặc nguồn cố định. Cũng đại diện cho
vợ (trong lá số nam)...

### Biểu hiện tốt (có lực)
- Tài chính ổn định, biết quản lý tiền
- Thực tế, chăm chỉ
- Hôn nhân bền vững (nam giới)

### Biểu hiện xấu (quá nhiều hoặc quá yếu)
- Quá nhiều: Keo kiệt, sống vì tiền
- Quá yếu: Khó giữ tiền, tài chính bất ổn
```

## Checklists

### 10 Thiên Can
| # | Can | Pinyin | Ngũ Hành | Âm Dương |
|---|-----|--------|----------|----------|
| 1 | Giáp | Jiǎ | Mộc | Dương |
| 2 | Ất | Yǐ | Mộc | Âm |
| 3 | Bính | Bǐng | Hỏa | Dương |
| 4 | Đinh | Dīng | Hỏa | Âm |
| 5 | Mậu | Wù | Thổ | Dương |
| 6 | Kỷ | Jǐ | Thổ | Âm |
| 7 | Canh | Gēng | Kim | Dương |
| 8 | Tân | Xīn | Kim | Âm |
| 9 | Nhâm | Rén | Thủy | Dương |
| 10 | Quý | Guǐ | Thủy | Âm |

### 10 Thập Thần
| # | Thần | English | Quan hệ |
|---|------|---------|---------|
| 1 | Tỷ Kiên | Friend | Cùng hành, cùng Âm Dương |
| 2 | Kiếp Tài | Rob Wealth | Cùng hành, khác Âm Dương |
| 3 | Thực Thần | Eating God | Nhật Chủ sinh, cùng ÂD |
| 4 | Thương Quan | Hurting Officer | Nhật Chủ sinh, khác ÂD |
| 5 | Chính Tài | Direct Wealth | Nhật Chủ khắc, cùng ÂD |
| 6 | Thiên Tài | Indirect Wealth | Nhật Chủ khắc, khác ÂD |
| 7 | Chính Quan | Direct Officer | Khắc Nhật Chủ, cùng ÂD |
| 8 | Thất Sát | 7 Killings | Khắc Nhật Chủ, khác ÂD |
| 9 | Chính Ấn | Direct Seal | Sinh Nhật Chủ, cùng ÂD |
| 10 | Thiên Ấn | Indirect Seal | Sinh Nhật Chủ, khác ÂD |
