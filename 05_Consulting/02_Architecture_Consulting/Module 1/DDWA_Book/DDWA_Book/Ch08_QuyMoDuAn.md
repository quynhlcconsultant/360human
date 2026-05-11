# CHƯƠNG 8: QUY MÔ DỰ ÁN VÀ TEMPLATE SCALING

## 8.1 Phân loại Quy mô (Tier System)

| Tier | Mô tả | Headcount | Số folder gốc | Ví dụ |
| :---: | :--- | :---: | :---: | :--- |
| **S** | Solo / Side Project | 1-2 | **3** | Blog cá nhân, Tool nhỏ |
| **M** | Startup / Small Team | 3-10 | **4-5** | YLake, Hoctap.tech |
| **L** | Scale-up / Mid-size | 10-50 | **5-7** | 5Balance, Product Academy |
| **XL** | Enterprise | 50+ | **7+** | Tập đoàn, Multi-BU |

## 8.2 Template Chuẩn cho Tier M (Baseline)

```
[PROJECT]/
├── Readme.md                     # Tổng quan
├── Index.md                      # ★ Bắt buộc: Bản đồ thư mục
├── Guideline.md                  # ★ Bắt buộc: Khung tiêu chuẩn
├── Onboarding.md                 # ★ Bắt buộc: Nhập môn dự án
├── Changelog.md                  # ★ Bắt buộc: Nhật ký thay đổi
├── Handoff.md                    # ★ Bắt buộc: Bàn giao Context
├── ToDo.md                       # ★ Bắt buộc: Sprint tracker
├── Notes/                        # ★ Bắt buộc: Khung ý tưởng nháp
├── Archive/                      # ★ Túi cát: Lưu trữ lạnh
├── Temporary/                    # ★ Túi cát: Trung chuyển dữ liệu
│
├── .agents/workflows/            # Workflows chuyên biệt
│
├── SPRINT/                       # Công trường (WIP)
│   ├── Sprint_Log.md             # ★ Bắt buộc
│   └── SP-YYMMDD-##-[Name]/
│
├── 01_Governance/                # GOV + FIN + HRM
│   ├── Master_Strategy.md
│   ├── Daily_Operations.md
│   ├── Org_Chart.md
│   ├── Staffing_Plan.md
│   └── Finance/
│       └── Revenue_Expense_Tracker.md
│
├── 02_Production/                # PRD
│   ├── Product_Backlog/
│   │   └── Product_Roadmap.md
│   └── Content_Library/
│
├── 03_Marketing/                 # MKT + SAL
│   └── Strategy/
│       ├── Content_Strategy.md
│       ├── Marketing_Plan.md
│       └── Campaign_Log.md
│
└── 04_Operations/                # OPS
    ├── Members/
    │   └── Member_Registry.md
    └── Community_Changelog.md
```
