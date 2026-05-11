# CHƯƠNG 11: ĐỊNH LUẬT GIAO DIỆN VÀ DATA MODEL (HUMAN-AI INTERFACE)

> *Bản chất của Workspace Design là ERP Database Design. Filesystem chỉ là medium lưu trữ.*

## 11.1 Định luật "YAML là Chân lý, Markdown là Giao diện" (YAML SSOT)

**SSOT (Single Source of Truth) KHÔNG PHẢI Markdown. Nó là cấu trúc dữ liệu YAML/JSON.**

File Blueprint Strategy của một doanh nghiệp bản chất là một Object rẽ nhánh. AI lưu trữ nó dưới dạng `.yaml`. File `.md` mà CEO đọc chỉ là một "GUI Report" (View) do AI render ra từ YAML.

## 11.2 Định luật Rỗng (Null-Field Triggers Survey)

Thuật toán phân tích Gap trở nên vô cùng đơn giản và toán học:
1. AI parse file `Strategy.yaml` thành Object.
2. Quét toàn bộ Object, Data field nào `= null` hoặc `""` → Missing Input.
3. AI tự động sinh bảng hỏi Survey cho các trường Null đó để hỏi CEO qua Chat.
4. CEO chat trả lời → AI parse thành Structured Data → Update vào `YAML` → Render lại File `Markdown` báo cáo.

## 11.3 Renderer Pattern: YAML → HTML/PDF View

```
YAML (Data)  →  Python Script (Renderer)  →  HTML (View)
strategy.yaml → render_strategy.py        → strategy_view.html
```

**Lợi ích:**
1. **Data integrity:** Sửa 1 nơi (YAML), View tự update.
2. **Multi-format:** 1 YAML → HTML + PDF + Dashboard + Email.
3. **Validation:** Script validate data trước khi render.
4. **Versioning:** YAML track changes dễ hơn Markdown.
