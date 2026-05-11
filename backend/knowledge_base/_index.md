---
title: "360Human Knowledge Base — Master Index"
total_systems: 5
total_files: 33
total_entries: "~400+"
format: Markdown (RAG-optimized)
chunking: "Split by ## headers"
updated: "2026-03-16"
---

# Knowledge Base — Master Index

## Coverage Map

| System | Files | Words | Priority | Status |
|--------|-------|-------|----------|--------|
| Tử Vi (zi_wei) | 7 | ~2,023,735 | P0 | ✅ Complete |
| Numerology | 5 | ~247,164 | P0 | ✅ Complete |
| Human Design | 5 | ~485,870 | P1 | ✅ Complete |
| BaZi | 5 | ~972,749 | P1 | ✅ Complete |
| Vedic | 6 | ~(check) | P2 | ✅ Complete |

## File Map

### zi_wei/ (P0) — ZWDS / Zi Wei Dou Shu
- `chinh_tinh.md` — 14 Major Stars (856,091w) — detailed star descriptions + palace positions
- `chinh_tinh_supplement.md` — Joseph Yu + Aloysius Han English extracts (230,587w)
- `phu_tinh.md` — Minor Stars incl. 4 Killings, 6 Auspicious, 4 Transformations (146,448w)
- `cung.md` — 12 Palaces with star-in-palace cross-reference (173,733w)
- `combinations.md` — Cach Cuc formations, star pairs, Si Hua combos (370,927w)
- `dai_van.md` — 10-year luck cycles, annual charts, timing analysis (115,128w)
- `ngu_hanh.md` — Five Elements, Heavenly Stems, Earthly Branches, brightness table (130,821w)

### numerology/ (P0)
- `life_path.md` — 12 Life Path numbers (1-9, 11, 22, 33)
- `expression.md` — 12 Expression numbers
- `soul_urge.md` — 12 Soul Urge numbers
- `personal_year.md` — 9 Personal Year cycles
- `karmic_debt.md` — 4 Karmic Debt numbers (13, 14, 16, 19)

### human_design/ (P1)
- `types.md` — 4 Types + MG
- `authorities.md` — 7 Authorities
- `profiles.md` — 12 Profiles
- `centers.md` — 9 Centers
- `gates_channels.md` — 64 Gates + 36 Channels

### bazi/ (P1)
- `heavenly_stems.md` — 10 Thiên Can
- `earthly_branches.md` — 12 Địa Chi
- `day_master.md` — 10 Day Master analyses
- `ten_gods.md` — 10 Thập Thần
- `luck_pillars.md` — Đại Vận cycles

### vedic/ (P2)
- `rashis.md` — 12 Rashis
- `nakshatras.md` — 27 Nakshatras
- `planets.md` — 9 Grahas
- `houses.md` — 12 Bhavas
- `dashas.md` — 9 Dasha periods

## Domain ↔ System Mapping

| Domain | Tử Vi | Numerology | HD | BaZi | Vedic |
|--------|-------|------------|-----|------|-------|
| Overview | Cung Mệnh | Life Path | Type | Nhật Chủ | Lagna |
| Mission | Cung Quan Lộc | Expression | Incarnation Cross | Thiên Can | 10th House |
| Identity | Mệnh + Thân | Soul Urge | Profile | Tứ Trụ | 1st House |
| Love | Cung Phu Thê | Compatibility | Sacral + G | Chính Tài/Quan | 7th House |
| Finance | Cung Tài Bạch | Personal Year | Will Center | Tài Tinh | 2nd + 11th |
| Health | Cung Tật Ách | — | Spleen Center | Ngũ Hành balance | 6th House |
| Family | Cung Phụ Mẫu | — | G Center | Ấn Tinh | 4th House |
| Career | Cung Quan Lộc | Expression | Type Strategy | Quan Tinh | 10th House |
| Growth | Cung Phúc Đức | Master Numbers | Authority | Đại Vận | 9th House |
| Social | Cung Nô Bộc | Life Path | Throat Center | Tỷ Kiên | 11th House |

## RAG Retrieval Flow

```
User query: "Tử Vi nói gì về tài chính của tôi?"
    ↓
1. Identify: system=zi_wei, domain=finance → cung=Tài Bạch
    ↓
2. Retrieve chunks:
   - zi_wei/cung.md ## Cung Tài Bạch
   - zi_wei/chinh_tinh.md ## {user's star} → section "Tại Cung Tài Bạch"
   - zi_wei/combinations.md (if relevant combos)
    ↓
3. Combine with L1 API data (user's actual chart)
    ↓
4. Feed to Claude L3 prompt
```
