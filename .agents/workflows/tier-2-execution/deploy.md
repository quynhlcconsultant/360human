---
description: Deploy ứng dụng lên staging hoặc production — Railway (backend) + Vercel (frontend)
tier: execution
version: v1.0
owner: "@Director-Tech"
calls:
  - /qg-check (Tier 3)
  - /flog (Tier 3)
called_by:
  - /build-sprint (@Director-Tech — sau khi code done)
input: "Environment target (staging/production) + Sprint ID + confirmation QG-2 passed"
output: "App live tại URL staging hoặc production + deploy log"
---

# Workflow: /deploy

> **Tier 2 — EXECUTION**
> Ai chạy: @Director-Tech
> Khi nào: Sau khi code đã pass QG-2 và được @CEO-Winston approve (production)

---

## ⚠️ Safety Gate — Đọc trước khi làm bất cứ điều gì

| Deploy type | Ai approve | Điều kiện |
|-------------|-----------|---------|
| Staging | @Director-Tech (tự quyết) | QG-2 passed |
| Production | @CEO-Winston | QG-2 passed + CEO approval |

**KHÔNG BAO GIỜ deploy production mà không có CEO approval.**
**KHÔNG BAO GIỜ deploy khi tests đang fail.**

---

## Bước 1: Pre-deploy Checklist

Trước khi bắt đầu bất kỳ deploy nào:

```
[TOL] Pre-deploy Assessment:
→ Target: staging / production
→ Sprint: S##
→ QG-2 status: PASS / FAIL (nếu FAIL → STOP)
→ Tests: ALL PASS / FAILING (nếu FAILING → STOP)
→ CEO approval: [Y/N] (nếu production và N → STOP)
→ Last successful deploy: [date]
→ Migration needed: [Y/N]
→ Environment variables changed: [Y/N]
→ Rollback plan: [mô tả nếu cần rollback]
```

---

## Bước 2: Database Migration (nếu cần)

**Staging:**
```bash
# SSH vào Railway staging hoặc chạy qua Railway CLI:
railway run alembic upgrade head

# Verify:
railway run python -c "from app.db.session import engine; print('DB OK')"
```

**Production:**
```bash
# LUÔN backup trước migration production:
# Railway dashboard → Database → Create snapshot

# Sau đó:
railway run --environment production alembic upgrade head
```

**Nếu migration fail:** Rollback ngay → `alembic downgrade -1` → báo @CEO-Winston.

---

## Bước 3: Deploy Backend (Railway)

**Staging:**
```bash
# Railway tự động deploy khi push lên branch staging
git push origin staging

# Hoặc manual trigger:
railway up --environment staging
```

**Production:**
```bash
# Chỉ sau khi CEO approve
git push origin main

# Railway tự động deploy từ main
# Hoặc: railway up --environment production
```

**Monitor deploy:**
```bash
railway logs --environment [staging/production] -f
# Chờ đến khi thấy: "Application started successfully"
# Timeout: 5 phút
```

---

## Bước 4: Deploy Frontend (Vercel)

**Staging:**
```bash
# Vercel tự động deploy preview khi push PR
# Hoặc manual:
vercel --env staging
```

**Production:**
```bash
# Chỉ sau CEO approve
vercel --prod
```

**Monitor:** Vercel dashboard → Deployments → Check build logs.

---

## Bước 5: Smoke Test sau Deploy

Với mỗi environment, chạy smoke test manual:

```
Smoke Test Checklist — [Env] Deploy — [Date]

Core flows:
- [ ] Trang chủ load (< 3 giây)
- [ ] Đăng ký account mới thành công
- [ ] Đăng nhập thành công
- [ ] Tạo chart cơ bản (Sun sign) → AI response trả về
- [ ] Xem profile page
- [ ] Không có console errors nghiêm trọng

API endpoints:
- [ ] GET /health → 200 OK
- [ ] POST /auth/login → 200 (test credentials)
- [ ] GET /user/profile → 200 (authenticated)

Performance:
- [ ] Core Web Vitals: LCP < 2.5s (check Vercel analytics)
- [ ] API response time: < 2s cho chart generation
```

**Nếu bất kỳ item nào FAIL:**
1. Ghi rõ lỗi
2. Rollback ngay (xem Bước 6)
3. Báo @CEO-Winston nếu production

---

## Bước 6: Rollback Plan (nếu cần)

**Backend rollback (Railway):**
```bash
# Railway dashboard → Deployments → Chọn deploy trước → Redeploy
# Hoặc:
git revert [commit-hash] && git push origin main
```

**Frontend rollback (Vercel):**
```bash
# Vercel dashboard → Deployments → Chọn deployment trước → Promote to production
```

**Database rollback:**
```bash
alembic downgrade -1  # Hoặc specific revision
```

---

## Bước 7: Environment Variables Check

Sau deploy mới, verify env vars đúng:

**Staging:**
```
DATABASE_URL → Neon staging database
ANTHROPIC_API_KEY → API key (check không hết quota)
SECRET_KEY → JWT secret
ENVIRONMENT → "staging"
```

**Production:**
```
DATABASE_URL → Neon production database
ANTHROPIC_API_KEY → Production API key
SECRET_KEY → Production JWT secret (khác staging!)
ENVIRONMENT → "production"
```

**KHÔNG BAO GIỜ** log env vars. **KHÔNG BAO GIỜ** commit .env file.

---

## Bước 8: Báo cáo Deploy + Gọi /flog

**Báo cáo lên @CEO-Winston:**
```
[DEPLOY REPORT] S## → [Environment]
✅ Status: SUCCESS / ❌ FAILED + lý do
🔗 URL: [staging/production URL]
🕐 Deploy time: [timestamp]
🧪 Smoke test: PASS / FAIL [items]
📊 Performance: LCP [X]s, API [Y]s
📝 Migration: [Y/N — nếu Y, tên migration]
```

```
/flog — Deploy S## to [env] complete. URL: [url]. Smoke test: PASS.
```

---

## Output cam kết

- App live tại URL đúng environment
- Smoke test PASS (hoặc rollback nếu fail)
- Deploy report gửi @CEO-Winston
- /flog logged

```
[QG-1] Tự kiểm:
- [ ] Pre-deploy checklist đầy đủ?
- [ ] Migration thành công (nếu có)?
- [ ] Smoke test PASS?
- [ ] Không có critical errors trong logs?
- [ ] CEO đã được báo cáo?
```
