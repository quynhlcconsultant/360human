---
title: "Knowledge Base Digitization Guide"
id: "ARCH-005"
updated: "2026-03-15"
status: "active"
---

# KB Digitization — 2000+ PDF Pages → JSON

> Goal: Chuyển 2000+ trang PDF thành JSON/YAML files cho RAG pipeline
> Timeline: 10 ngày (chạy song song với Sprint 1)
> Approach: AI-assisted extraction, KHÔNG đọc/gõ tay từng trang

---

## Strategy: 3-Phase Pipeline

### Phase A: Extract (2 days)
PDF → Raw text → Structured chunks

### Phase B: Structure (5 days)
Chunks → JSON rules per system

### Phase C: Validate (3 days)
Expert review → Fix errors → Deploy

---

## Phase A: PDF → Text Extraction

### Option 1: Claude (Recommended — bạn đã có API)
```python
# Dùng Claude để extract + structure cùng lúc
import anthropic
import fitz  # PyMuPDF

client = anthropic.Anthropic()

def extract_pdf_to_json(pdf_path, system_name):
    doc = fitz.open(pdf_path)
    results = []

    # Process 10 pages at a time
    for i in range(0, len(doc), 10):
        pages_text = ""
        for j in range(i, min(i + 10, len(doc))):
            pages_text += f"\n--- Page {j+1} ---\n"
            pages_text += doc[j].get_text()

        response = client.messages.create(
            model="claude-haiku-4-5-20251001",  # Fast + cheap
            max_tokens=4096,
            messages=[{
                "role": "user",
                "content": f"""Extract astrology knowledge from this text into JSON format.
System: {system_name}

Rules:
- Each entry = one concept/rule/star/position
- Include: key, name_vi, name_en, category, meaning, interpretation
- Keep original Vietnamese terms
- Skip table of contents, page numbers, headers

Text:
{pages_text}

Output JSON array:"""
            }]
        )
        results.append(response.content[0].text)

    return results
```

### Option 2: PyMuPDF + Manual (Free, slower)
```bash
pip install PyMuPDF
```
```python
import fitz
doc = fitz.open("tuvi_reference.pdf")
for page in doc:
    text = page.get_text()
    # Process text...
```

### Option 3: marker (Best quality OCR)
```bash
pip install marker-pdf
marker_single input.pdf output/ --langs vi
```
Tự động convert PDF → Markdown với layout preservation.

---

## Phase B: JSON Structure per System

### Target folder structure:
```
backend/knowledge_base/
├── zi_wei/
│   ├── chinh_tinh.json      ← 14 Chính Tinh (meanings + interpretations)
│   ├── phu_tinh.json         ← Phụ Tinh
│   ├── cung_menh.json        ← 12 Cung meanings
│   ├── dai_van.json          ← Đại Vận cycles
│   └── combinations.json     ← Star combinations
├── numerology/
│   ├── life_path.json        ← 1-9, 11, 22, 33
│   ├── expression.json       ← Expression numbers
│   ├── soul_urge.json        ← Soul urge meanings
│   ├── personal_year.json    ← Yearly cycles
│   └── karmic_debt.json      ← 13, 14, 16, 19
├── human_design/
│   ├── types.json            ← 4 types (Generator, Projector, Manifestor, Reflector)
│   ├── authorities.json      ← 7 authorities
│   ├── profiles.json         ← 12 profiles
│   ├── centers.json          ← 9 centers
│   └── gates_channels.json   ← 64 gates, 36 channels
├── bazi/
│   ├── heavenly_stems.json   ← 10 Thiên Can
│   ├── earthly_branches.json ← 12 Địa Chi
│   ├── day_master.json       ← Nhật Chủ analysis
│   ├── ten_gods.json         ← Thập Thần
│   └── luck_pillars.json     ← Đại Vận
└── vedic/
    ├── rashis.json            ← 12 Rashis/signs
    ├── nakshatras.json        ← 27 Nakshatras
    ├── planets.json           ← 9 Grahas
    ├── houses.json            ← 12 Bhavas
    └── dashas.json            ← Vimshottari Dasha periods
```

### JSON Schema (per entry):
```json
{
  "key": "that_sat",
  "name_vi": "Thất Sát",
  "name_en": "Seven Killings",
  "system": "zi_wei",
  "category": "chinh_tinh",
  "keywords": ["leadership", "courage", "conflict"],
  "meaning_short": "Sao chủ về quyền lực, dũng cảm, xung đột",
  "meaning_detail": "Thất Sát đại diện cho sức mạnh chiến đấu...",
  "in_cung": {
    "menh": "Người có cá tính mạnh, quyết đoán...",
    "tai_bach": "Kiếm tiền bằng năng lực cạnh tranh...",
    "phu_the": "Hôn nhân có tính tranh đấu..."
  },
  "combinations": [
    {"with": "tu_vi", "meaning": "Tử Vi + Thất Sát = Quyền uy..."},
    {"with": "liem_trinh", "meaning": "Liêm Trinh + Thất Sát = Sát Phá Liêm..."}
  ],
  "source_page": 45
}
```

---

## Phase C: Validate

| Validation Step | Method |
|----------------|--------|
| Completeness | Count entries vs known total (e.g., 14 Chính Tinh ✓) |
| Accuracy | Cross-check 10% random sample against source PDF |
| Consistency | All entries follow same JSON schema |
| Vietnamese | Correct dấu/accents preserved |
| No hallucination | All meanings exist in source material |

---

## Priority Order (by user demand)

| # | System | Est. Pages | Priority | Why |
|---|--------|-----------|----------|-----|
| 1 | Tử Vi | ~600 | P0 | 5-9M users in Vietnam, core differentiator |
| 2 | Numerology | ~200 | P0 | Simplest to digitize, most viral (400% growth) |
| 3 | Human Design | ~400 | P1 | Growing demand, younger audience |
| 4 | BaZi | ~400 | P1 | Overlaps with Tử Vi audience |
| 5 | Vedic | ~400 | P2 | Niche, can launch later |

### MVP Strategy:
- Sprint 1 (Week 2-3): Digitize **Tử Vi + Numerology** (P0) → enough for FREE tier
- Sprint 2-3: Add **HD + BaZi** → enough for PRO tier
- Post-launch: Complete **Vedic** → MAX tier full coverage

---

## Speed Tips

1. **Batch with Claude:** Process 10 pages per API call → 200 calls for 2000 pages → ~$5-10 with Haiku
2. **Use existing open-source:** Many astrology JSON datasets exist on GitHub for Numerology and Vedic
3. **Parallelize:** Run extraction scripts overnight, review in morning
4. **Start with skeleton:** Create JSON files with just keys/names first, fill meanings progressively
5. **Don't perfectionate:** 80% accuracy at launch → improve with user feedback post-launch
