# CHƯƠNG 3: QUY TẮC GỘP & TÁCH (MERGE/SPLIT RULES)

## 3.1 Khi nào GỘP 2 folder?
- Khi cùng 1 người/agent chịu trách nhiệm cho cả 2 chức năng.
- Khi khối lượng artifact của 1 chức năng < 10 files.

**Ví dụ:** YLake gộp `SAL` vào `MKT` → `03_Marketing_And_Growth` vì cùng A-06 xử lý.

## 3.2 Khi nào TÁCH 1 folder thành 2?
- Khi 1 folder vượt quá 30 files/subfolders ở tầng con trực tiếp.
- Khi xuất hiện 2 Stakeholders/Agent khác nhau quản lý 2 mảng riêng.

## 3.3 Ví dụ thực tế
| Tình huống | Hành động | Kết quả |
|:---|:---|:---|
| YLake startup: CEO kiêm tài chính | GỘP FIN vào GOV | `01_Governance/` chứa P&L |
| YLake scale: Thuê kế toán | TÁCH FIN | `06_Finance/` riêng |
| YLake: Sales = Marketing | GỘP SAL vào MKT | `03_Marketing/` chứa pipeline |

> 💡 **Nguyên tắc:** Gộp/Tách Entity dựa trên **độ lớn của Object**, không phải độ dài văn bản.
