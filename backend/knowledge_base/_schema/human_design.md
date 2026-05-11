---
system: human_design
display_name: "Thiết Kế Con Người"
display_name_en: "Human Design"
total_files: 5
priority: P1
est_pages: ~400
---

# Human Design — KB Schema

## Files & Categories

| File | Category | Entries | Description |
|------|----------|---------|-------------|
| `types.md` | types | 4 | Generator, Projector, Manifestor, Reflector |
| `authorities.md` | authorities | 7 | Inner Authority decision-making |
| `profiles.md` | profiles | 12 | 12 Profile combinations (1/3, 1/4, ..., 6/3) |
| `centers.md` | centers | 9 | 9 Energy Centers (defined/undefined) |
| `gates_channels.md` | gates_channels | 64+36 | 64 Gates + 36 Channels |

## Entry Schema: Types

```markdown
## Generator (Máy Phát)

**ID:** hd_type_generator
**Category:** types
**Population:** ~37% nhân loại
**Aura:** Enveloping, magnetic
**Strategy:** Wait to Respond (Chờ phản hồi)
**Not-Self Theme:** Frustration (Bực bội)
**Signature:** Satisfaction (Hài lòng)
**Keywords:** năng lượng bền bỉ, xây dựng, phản hồi, sacral

### Ý nghĩa tổng quát
Generator là type phổ biến nhất, sở hữu năng lượng Sacral
bền bỉ. Họ không nên khởi xướng mà chờ đợi cuộc sống
đưa đến cơ hội, rồi dùng "gut response" để quyết định...

### Strategy: Wait to Respond
- KHÔNG chủ động bắt đầu (initiating)
- Chờ tín hiệu từ bên ngoài (người hỏi, cơ hội xuất hiện)
- Lắng nghe phản ứng Sacral: "uh-huh" (yes) hoặc "uh-uh" (no)
- Khi respond đúng → Satisfaction; sai → Frustration

### Sacral Center
- Luôn Defined (bật) ở Generator
- Nguồn năng lượng làm việc dồi dào
- Cần "sử dụng hết" năng lượng trong ngày → ngủ ngon

### Sự nghiệp
Phù hợp công việc họ YÊU THÍCH (Sacral says yes).
Không phù hợp nếu ép làm việc mình ghét → burnout...

### Tình yêu
Cần partner mà Sacral "respond" mạnh.
Đừng commit vì logic — listen to the gut...

### Sub-type: Manifesting Generator
- Có thêm kết nối tới Throat Center
- Nhanh hơn, multi-passionate, hay skip steps
- Strategy vẫn là Wait to Respond, nhưng tốc độ cao hơn
```

## Entry Schema: Centers

```markdown
## Sacral Center (Trung tâm Sacral)

**ID:** hd_center_sacral
**Category:** centers
**Position:** Bụng dưới
**Theme:** Life force, sexuality, work energy
**Keywords:** năng lượng sống, sinh lực, phản hồi ruột

### Khi Defined (Bật — màu đỏ)
- Năng lượng làm việc bền bỉ
- Có "gut response" rõ ràng (uh-huh / uh-uh)
- Cần làm việc mình yêu thích
- Type: Generator hoặc Manifesting Generator

### Khi Undefined (Tắt — màu trắng)
- KHÔNG có năng lượng làm việc bền vững
- Amplify năng lượng của người khác → dễ làm quá sức
- Cần nghỉ ngơi trước khi mệt
- Type: Projector, Manifestor, hoặc Reflector
- Bài học: biết khi nào "đủ rồi"

### Câu hỏi tự vấn (Undefined Sacral)
"Mình có biết khi nào nên dừng lại không?"
```

## Checklists

### 4 Types
| Type | Strategy | Not-Self | Signature |
|------|----------|----------|-----------|
| Generator | Wait to Respond | Frustration | Satisfaction |
| Manifesting Generator | Wait to Respond | Frustration | Satisfaction |
| Projector | Wait for Invitation | Bitterness | Success |
| Manifestor | Inform before acting | Anger | Peace |
| Reflector | Wait 28 days (lunar) | Disappointment | Surprise |

### 9 Centers
| Center | Theme | Defined = | Undefined = |
|--------|-------|-----------|-------------|
| Head | Inspiration | Consistent mental pressure | Amplifies others' questions |
| Ajna | Conceptualization | Fixed thinking | Open-minded |
| Throat | Communication | Consistent expression | Variable voice |
| G/Self | Identity/Direction | Fixed identity | Chameleon |
| Heart/Will | Willpower | Reliable willpower | Proving self-worth |
| Sacral | Life Force | Sustained energy | Amplified energy |
| Solar Plexus | Emotions | Emotional wave | Empathic |
| Spleen | Intuition | Consistent immunity | Holding on too long |
| Root | Adrenaline | Consistent drive | Rushed by pressure |
