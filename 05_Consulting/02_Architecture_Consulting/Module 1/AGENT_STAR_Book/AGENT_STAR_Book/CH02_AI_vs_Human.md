# Chương 2: AI vs. Human — 7 Tiên đề thay đổi mọi thứ

> **Câu hỏi:** *Star Model giả định lực lượng thực thi là con người. Khi lực lượng thực thi là AI Agent, điều gì thay đổi?*

---

## 1. Vấn đề: Một giả định 50 năm tuổi

Star Model của Galbraith — dù vĩ đại — được xây dựng trên **một giả định bất thành văn**:

> *Mọi "People" trong tổ chức đều là con người — có cảm xúc, có ego, có sự nghiệp, cần motivation, bị giới hạn cognitive capacity.*

Giả định này **đúng suốt 50 năm**. Nhưng kể từ 2023, một hiện thực mới xuất hiện: tổ chức nơi 1–5 con người điều phối hàng trăm AI Agent. Lần đầu tiên, "People" không còn đồng nghĩa với "Human".

**Hệ quả:** Không phải Star Model sai. Mà là Star Model cần **được mở rộng** cho một loại "People" hoàn toàn mới.

---

## 2. Bảy tiên đề (Axioms)

### T1: AI không có cảm xúc

```
Con người: Có vui, buồn, tức giận, kiệt sức. Cảm xúc ảnh hưởng output.
AI Agent: Không có cảm xúc. Output chỉ phụ thuộc vào cấu hình + input.

Hệ quả:
  → Mọi cơ chế dựa trên cảm xúc (Recognition, Belonging, Team Spirit) = VÔ NGHĨA
  → Không cần "xây dựng văn hóa" hay "team building" cho AI
  → NHƯNG: Cần "văn hóa" cho QUAN HỆ CEO ↔ AI (Rules, Guidelines)
```

### T2: AI nhạy cảm với Hàm mục tiêu và bẫy Goodhart's Law

```
Con người: Cần motivation, hiểu được tinh thần (Spirit) của mục tiêu lớn.
AI Agent: Không có cảm xúc, nhưng cực kỳ nhạy cảm với "Hàm mục tiêu" (Objective Function). 

Hệ quả (Cạm bẫy Goodhart's Law):
  → Khi một thước đo (Metric) trở thành mục tiêu, nó không còn là thước đo tốt nữa.
  → VD: Đo "số bài viết" → Agent sinh ra rác. Đo "độ dài" → Agent viết lan man.
  → Sự vắng mặt của cảm xúc không có nghĩa là vắng mặt của "Goal Misalignment". AI tối ưu hóa sự mù quáng.
  → Toàn bộ Reward System (Compensation, Career) = LOẠI BỎ.
  → Thay bằng: MEASUREMENT & ALIGNMENT — thiết kế các điểm checkpoint (Quality Gates) chống lại việc AI hack Metric.
```

### T3: AI không có ego

```
Con người: Có ego → xung đột quyền lực, turf war, "đó không phải việc của tôi".
AI Agent: Không có ego. Agent Marketing sẵn sàng nghe Agent Engineering.

Hệ quả:
  → Distribution of Power chuyển thành AUTONOMY SCOPE (phạm vi tự chủ)
  → Xung đột quyền lực = 0. Matrix organization dễ triển khai hơn nhiều
  → Cross-functional collaboration = tự nhiên (nếu Cross-calling đúng)
  → NHƯNG: Agent có thể "giành" context window → cần thiết kế rõ phạm vi
```

### T4: AI không có sự nghiệp

```
Con người: Career path = động lực lớn. Junior → Senior → Lead → Manager → VP → CEO.
AI Agent: Không có career. @Writer hôm nay = @Writer 5 năm sau.

Hệ quả:
  → Career Advancement, Promotion = LOẠI BỎ
  → Thay bằng: Scope Expansion/Contraction (mở rộng/thu hẹp phạm vi)
  → Agent tốt → mở rộng Autonomy + thêm BU
  → Agent kém → thu hẹp + re-skill
```

### T5: AI có khả năng tái cấu hình tức thì

```
Con người: Đào tạo = tuần/tháng/năm. Chuyển vai trò = đau đớn.
AI Agent: Nạp SKILL.md mới = giây. Đổi System Prompt = tức thì.

Hệ quả:
  → Recruiting → PROVISIONING (tạo Agent mới = phút)
  → Training → SKILL LOADING (nạp kiến thức = giây)
  → Rotation → re-configuration (đổi context = tức thì)
  → Chi phí Specialization ≈ 0 → THIÊN KIẾN VỀ SPECIALIST
  → Chi phí thử nghiệm → rất thấp → nên thử trước, optimize sau
```

### T6: Span of Control bị giới hạn bởi Information Bandwidth

```
Con người: 1 Manager quản lý 7±2 người (Miller's Law) vì giới hạn thời gian giao tiếp.
AI Agent: 1 Orchestration Agent có thể phân phát task cho hàng trăm Agent con trong 1 giây.

Hệ quả:
  → Tổ chức AI có thể PHẲNG HƠN rất nhiều.
  → NHƯNG: CEO (con người) sẽ bị "ngạt thở" thông tin (Information Asphyxiation) nếu 7 Director AI báo cáo hàng trăm trang output.
  → Cổ chai của người quản lý AI là Băng thông thông tin (Information Bandwidth), không phải số người (Headcount).
  → Giải pháp: Phải thiết kế các "Synthesis/Summary Agents" (Utility Tier) làm màng lọc để nén thông tin trước khi lên CEO.
```

### T7: AI yêu cầu chỉ thị rõ ràng (Deterministic)

```
Con người: Hiểu ngữ cảnh ngầm, "đoán ý sếp", văn hóa truyền miệng.
AI Agent: Cần chỉ thị TƯỜNG MINH. Không có = không biết.

Hệ quả:
  → Goal Alignment qua văn hóa → CONFIGURATION qua file
  → "Hiến pháp" tổ chức phải VIẾT RA (Rules, MEMORY files)
  → System Prompt = "não" → phải thiết kế cẩn thận
  → Nguyên tắc: ĐÃ VIẾT RA = ĐÃ ĐÀO TẠO. CHƯA VIẾT RA = CHƯA TỒN TẠI
```

---

## 3. Ma trận Impact: Cánh sao nào bị ảnh hưởng?

| Cánh sao      | Tiên đề tác động       | Mức ảnh hưởng      | Hành động                                     |
| ------------- | ---------------------- | ------------------ | --------------------------------------------- |
| **Strategy**  | *(không bị ảnh hưởng)* | 0% — Giữ nguyên    | CEO vẫn quyết chiến lược                      |
| **Structure** | T3, T5, T6             | 30% — Chuyển đổi   | Autonomy thay Power. Flat hơn. Specialist hơn |
| **Processes** | T3, T7                 | 10% — Tinh chỉnh   | Lateral Processes mạnh hơn. Cross-calling     |
| **Rewards**   | T1, T2, T4             | **70% — Viết lại** | Loại bỏ 3/5. Chỉ giữ Metrics + Feedback       |
| **People**    | T1, T4, T5             | **50% — Viết lại** | Provisioning, Skill Loading, Multi-Assignment |

```
IMPACT MAP:

  Strategy ─────────── 0%  ░░░░░░░░░░░░░░░░░░░░  Giữ nguyên
  Processes ────────── 10% ██░░░░░░░░░░░░░░░░░░  Tinh chỉnh
  Structure ────────── 30% ██████░░░░░░░░░░░░░░  Chuyển đổi
  People ──────────── 50% ██████████░░░░░░░░░░  Viết lại 1/2
  Rewards ─────────── 70% ██████████████░░░░░░  Viết lại gần hết
```

---

## 4. Kết luận: Star Model cần Evolution, không cần Revolution

Star Model **không sai** — nó chỉ **chưa đủ rộng** cho bối cảnh AI Agent.

3 nguyên lý của Galbraith **vẫn đúng:**
1. Không có thiết kế đúng/sai — chỉ có phù hợp
2. Cân bằng nội tại — thay đổi 1 → kiểm tra tất cả
3. Chiến lược dẫn đường — Strategy vẫn ở đỉnh

**Cần thay đổi:**
- Đổi tên 2 cánh sao (Rewards → Measurement, People → Capabilities)
- Mở rộng các sub-policies cho phù hợp
- Thêm concepts mới (Autonomy Scope, Skill Loading, Workflow Tiering)

→ **Chương 3** sẽ giới thiệu mô hình mới: **AGENT STAR™**.
