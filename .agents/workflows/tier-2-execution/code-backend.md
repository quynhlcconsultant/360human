---
description: Viết code backend FastAPI — endpoint, model, logic, migration, test
tier: execution
version: v1.0
owner: "@Specialist-Backend"
calls:
  - /qg-check (Tier 3)
  - /flog (Tier 3)
called_by:
  - /build-sprint (@Director-Tech)
input: "Task description + relevant ARCH files + existing code path cần modify/tạo"
output: "File code Python hoàn chỉnh (endpoint, model, hoặc service) + unit test"
---

# Workflow: /code-backend

> **Tier 2 — EXECUTION**
> Ai chạy: @Specialist-Backend (hoặc @Director-Tech khi không có specialist)
> Khi nào: Được gọi từ /build-sprint để implement backend task

---

## Bước 1: Load Tech Context

Đọc bắt buộc trước khi viết 1 dòng code:
1. `02_Production/Architecture/ARCH-001_*.md` — tech stack (FastAPI, PostgreSQL, Docker)
2. `02_Production/Architecture/ARCH-002_api-design.md` — API conventions
3. File code liên quan trong `backend/` — hiểu existing patterns

Tech stack 360Human (KHÔNG tự ý thay đổi):
- **Backend:** Python 3.11, FastAPI, SQLAlchemy, Alembic
- **Database:** PostgreSQL (Neon serverless)
- **AI:** Anthropic Claude API (`claude-sonnet-4-6` hoặc mới nhất)
- **Auth:** JWT + bcrypt
- **Deploy:** Railway hoặc Docker

---

## Bước 2: Phân tích Task

Xác định rõ trước khi code:

```
[TOL] Task Analysis:
→ Task: [Tên task]
→ Type: New endpoint / Modify existing / Data model / Service logic / Migration
→ Files cần tạo: [list]
→ Files cần sửa: [list]
→ Dependencies: [external libs mới cần? → phải hỏi @Director-Tech nếu cần thêm dep]
→ Database changes?: [Y/N — nếu Y, cần Alembic migration]
→ Confidence: X%
```

**Gate:** Nếu task yêu cầu thêm dependency mới (pip install X) → escalate @Director-Tech approval trước.

---

## Bước 3: Viết Code

### Conventions bắt buộc:

**File structure:**
```
backend/
├── app/
│   ├── api/v1/         ← Routes/Endpoints
│   ├── models/         ← SQLAlchemy models
│   ├── schemas/        ← Pydantic schemas
│   ├── services/       ← Business logic
│   ├── core/           ← Config, security, deps
│   └── db/             ← Database session, base
└── alembic/            ← Migrations
```

**Naming conventions:**
- Endpoints: `snake_case` (GET /user_profile, POST /chart_generate)
- Models: `PascalCase` (class UserProfile, class AstrologyChart)
- Functions: `snake_case` với verb đầu (get_user, create_chart, validate_token)
- Variables: `snake_case`

**Code quality checklist khi viết:**
```python
# ✅ Mọi endpoint phải có:
@router.post("/endpoint", response_model=Schema, status_code=201)
async def create_something(
    data: InputSchema,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)  # nếu auth required
) -> Schema:
    """Docstring ngắn mô tả endpoint."""
    ...

# ✅ Error handling rõ ràng:
raise HTTPException(status_code=404, detail="Resource not found")

# ✅ Logging cho mọi action quan trọng:
import logging
logger = logging.getLogger(__name__)
logger.info(f"User {user_id} created chart for {target_date}")
```

**Với Claude AI calls:**
```python
# Dùng đúng model ID:
client = anthropic.Anthropic()
response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=2048,
    messages=[{"role": "user", "content": prompt}]
)
```

---

## Bước 4: Viết Alembic Migration (nếu có DB change)

```bash
# Tạo migration file:
alembic revision --autogenerate -m "add_table_xxx_or_column_yyy"

# Review migration file trước khi commit
# Không bao giờ chạy alembic upgrade trực tiếp trên production
```

---

## Bước 5: Viết Unit Test

Với mỗi function/endpoint mới, viết test tương ứng:

```python
# tests/test_[module].py
import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_create_endpoint_success(client: AsyncClient, auth_headers: dict):
    response = await client.post(
        "/api/v1/endpoint",
        json={"field": "value"},
        headers=auth_headers
    )
    assert response.status_code == 201
    assert response.json()["field"] == "value"

@pytest.mark.asyncio
async def test_create_endpoint_unauthorized(client: AsyncClient):
    response = await client.post("/api/v1/endpoint", json={})
    assert response.status_code == 401
```

Minimum test coverage cho mỗi endpoint:
- Happy path (success)
- Unauthorized (401)
- Not found (404) nếu applicable
- Validation error (422) nếu applicable

---

## Bước 6: Self QG-check — Gọi /qg-check

```
/qg-check
Level: QG-1
Scope: Backend task — [tên task]
```

Checklist cụ thể:
- [ ] Code follow conventions (naming, structure)?
- [ ] Error handling đầy đủ?
- [ ] Không có hardcoded secrets / credentials?
- [ ] Logging đã thêm cho actions quan trọng?
- [ ] Unit tests viết xong và pass?
- [ ] Migration file (nếu có) reviewed và safe?
- [ ] Không có SQL injection risk (dùng parameterized queries / ORM)?

---

## Bước 7: Báo cáo lên @Director-Tech + Gọi /flog

```
[CODE-BACKEND DONE] [Tên task]
✅ Files created/modified: [list]
✅ Tests: [N] tests, all pass
⚠️ Deferred/Notes: [nếu có]
🔗 Migration: [Y/N — tên migration nếu có]
```

```
/flog — Backend task [Tên] done. Files: [list]. Tests: N pass.
```

---

## Output cam kết

- File(s) code Python tại đúng vị trí trong `backend/`
- Unit tests pass
- Alembic migration (nếu có DB changes)
- QG-1 self-check passed
- @Director-Tech đã được báo cáo

```
[QG-1] Tự kiểm:
- [ ] Code chạy không có error?
- [ ] Tests pass?
- [ ] Conventions đúng?
- [ ] Không có secrets hardcoded?
- [ ] Logging đầy đủ?
```
