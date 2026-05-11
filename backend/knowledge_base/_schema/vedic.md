---
system: vedic
display_name: "Chiêm Tinh Vedic"
display_name_en: "Vedic Astrology (Jyotish)"
total_files: 5
priority: P2
est_pages: ~400
---

# Vedic — KB Schema

## Files & Categories

| File | Category | Entries | Description |
|------|----------|---------|-------------|
| `rashis.md` | rashis | 12 | 12 Rashis (Zodiac Signs — sidereal) |
| `nakshatras.md` | nakshatras | 27 | 27 Nakshatras (Lunar Mansions) |
| `planets.md` | grahas | 9 | 9 Grahas (Planets) |
| `houses.md` | bhavas | 12 | 12 Bhavas (Houses) |
| `dashas.md` | dashas | 9 | Vimshottari Dasha (planetary periods) |

## Entry Schema: Nakshatras

```markdown
## Ashwini (Mã Tinh)

**ID:** vedic_nakshatra_ashwini
**Category:** nakshatras
**Number:** 1/27
**Span:** 0°00' — 13°20' Aries
**Ruling Planet:** Ketu (South Node)
**Deity:** Ashwini Kumaras (Twin Horsemen)
**Symbol:** Horse head
**Guna:** Rajas
**Keywords:** healing, speed, new beginnings, miracles

### Ý nghĩa tổng quát
Ashwini là Nakshatra đầu tiên, mang năng lượng khởi đầu
mạnh mẽ. Người sinh dưới Ashwini thường nhanh nhẹn,
có khả năng chữa lành, và thích bắt đầu mọi thứ...

### Tính cách
- Nhanh nhẹn, quyết đoán
- Thích giúp đỡ người khác
- Có năng khiếu chữa lành (y tế, tâm lý)
- Nóng vội, thiếu kiên nhẫn

### Sự nghiệp
Y tế, cấp cứu, thể thao, startup, lĩnh vực cần tốc độ

### Tình yêu
Yêu nhanh, nhiệt tình, nhưng cần người kiên nhẫn bên cạnh

### Dasha Period (Ketu)
7 năm — giai đoạn chuyển đổi tâm linh, buông bỏ
```

## Entry Schema: Grahas (Planets)

```markdown
## Sun / Surya (Thái Dương)

**ID:** vedic_graha_sun
**Category:** grahas
**Sanskrit:** Sūrya
**Rules:** Leo (Simha)
**Exalted:** Aries 10° (Mesha)
**Debilitated:** Libra 10° (Tula)
**Friends:** Moon, Mars, Jupiter
**Enemies:** Venus, Saturn
**Keywords:** soul, ego, father, authority, vitality

### Ý nghĩa
Sun/Surya đại diện cho linh hồn (Atman), bản ngã,
quyền lực, và sức sống. Trong lá số, Sun cho thấy
mục đích sống và mối quan hệ với cha...

### Sun trong 12 Houses
- **1st House:** Mạnh mẽ, tự tin, sức khỏe tốt
- **7th House:** Dominant trong hôn nhân
- **10th House:** Sự nghiệp thành công, có quyền lực
- ...
```

## Checklists

### 27 Nakshatras
| # | Name | Span | Ruler | Symbol |
|---|------|------|-------|--------|
| 1 | Ashwini | 0-13°20' Ari | Ketu | Horse |
| 2 | Bharani | 13°20'-26°40' Ari | Venus | Yoni |
| 3 | Krittika | 26°40' Ari - 10° Tau | Sun | Razor |
| ... | ... | ... | ... | ... |
| 27 | Revati | 16°40'-30° Pis | Mercury | Fish |

### 9 Grahas
| # | Planet | Sanskrit | Rules | Karakas |
|---|--------|----------|-------|---------|
| 1 | Sun | Surya | Leo | Soul, Father |
| 2 | Moon | Chandra | Cancer | Mind, Mother |
| 3 | Mars | Mangala | Aries, Scorpio | Energy, Siblings |
| 4 | Mercury | Budha | Gemini, Virgo | Intellect, Speech |
| 5 | Jupiter | Guru | Sagittarius, Pisces | Wisdom, Children |
| 6 | Venus | Shukra | Taurus, Libra | Love, Art |
| 7 | Saturn | Shani | Capricorn, Aquarius | Karma, Discipline |
| 8 | Rahu | Rahu | — | Obsession, Foreign |
| 9 | Ketu | Ketu | — | Liberation, Past |
