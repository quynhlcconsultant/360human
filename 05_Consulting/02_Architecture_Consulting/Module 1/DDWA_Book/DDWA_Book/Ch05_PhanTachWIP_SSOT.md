# CHƯƠNG 5: PHÂN TÁCH WIP vs SSOT (CÔNG TRƯỜNG vs THƯ VIỆN)

> *Đây là nguyên lý quan trọng nhất được rút ra từ bài học YLake: Sprint là Công trường dang dở, Phòng ban là Thư viện hoàn thiện. Hai loại không gian này PHẢI tách biệt.*

## 5.1 Mô hình 2 Không gian

```
[WORKSPACE]/
│
├── 📁 SPRINT/                    # ═══ CÔNG TRƯỜNG (WIP) ═══
│   ├── Sprint_Log.md             # ★ Bắt buộc: Sổ tổng quản lý TẤT CẢ Sprint
│   ├── SP-YYMMDD-##-[Name]/     # Mỗi Sprint = 1 phiên làm việc có mục tiêu
│   │   ├── Sprint_Plan.md
│   │   ├── [deliverables...]     # Output đang hoàn thiện
│   │   └── handoffs/
│   └── Archive/                  # Sprint đã xong → lưu trữ lạnh
│
├── 📁 01_Governance/             # ═══ THƯ VIỆN (SSOT) ═══
├── 📁 02_Production/             # Chỉ chứa tài liệu ĐÃ HOÀN THIỆN
├── 📁 03_Marketing/              # Single Source of Truth
└── 📁 04_Operations/             # Không bao giờ chứa WIP
```

## 5.2 Vòng đời của Tài liệu (Document Lifecycle)

```
[Ý tưởng] → [Sprint/SP-XX/ — Draft WIP] → [CEO Duyệt] → [Copy về XX_PhòngBan/ — SSOT]
                    ↑                                              ↓
              Cập nhật tại Sprint                          Cập nhật tại SSOT
              (phiên bản nháp)                       (phiên bản chính thức duy nhất)
```

## 5.3 Quy tắc Bất biến
1. **Sprint folder = WIP.** Mọi output trong Sprint là bản nháp cho đến khi được merge.
2. **Phòng ban folder = SSOT.** Chỉ chứa tài liệu đã hoàn thiện, là nguồn sự thật duy nhất.
3. **Merge ritual:** Khi Sprint Done → output phải được copy/merge về folder phòng ban tương ứng. Sprint folder vẫn giữ nguyên làm archive (không xoá).
4. **Sprint_Log.md là BẮT BUỘC.** Nằm ở `SPRINT/Sprint_Log.md`, ghi track tất cả Sprint: mã, tên, ngày, trạng thái, deliverables, phòng ban liên quan.

## 5.4 Template Sprint_Log.md

```markdown
# SPRINT LOG — [TÊN DỰ ÁN]

| Mã Sprint | Tên | Ngày | Phòng ban | Trạng thái | Deliverables | Đã merge? |
| :--- | :--- | :--- | :--- | :---: | :--- | :---: |
| SP-260315-09 | HR & Org Design | 2026-03-15 | GOV | ✅ Done | 5 files | 🟡 Pending |
```
