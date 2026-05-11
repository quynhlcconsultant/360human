from contextlib import asynccontextmanager

import redis.asyncio as aioredis
import sentry_sdk
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text

from app.core.config import settings
from app.core.database import engine
from app.core.redis import connect_redis, disconnect_redis, get_redis
from app.routers import auth, interpret, payments, profiles, users

# ─── Sentry Initialization ────────────────────────────────
if settings.SENTRY_DSN:
    sentry_sdk.init(
        dsn=settings.SENTRY_DSN,
        traces_sample_rate=1.0,
        profiles_sample_rate=1.0,
    )


@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_redis()
    yield
    await disconnect_redis()


app = FastAPI(
    title="360Human API",
    version="0.1.0",
    description="Personal intelligence platform — 5 systems × 10 topics",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth.router)
app.include_router(users.router)
app.include_router(profiles.router)
app.include_router(interpret.router)
app.include_router(payments.router)


@app.get("/health", tags=["System"])
async def health_check():
    status = {"status": "ok", "services": {}}

    # Check DB
    try:
        async with engine.connect() as conn:
            await conn.execute(text("SELECT 1"))
        status["services"]["database"] = "ok"
    except Exception as e:
        status["services"]["database"] = f"error: {e}"
        status["status"] = "degraded"

    # Check Redis
    try:
        r = await get_redis()
        await r.ping()
        status["services"]["redis"] = "ok"
    except Exception as e:
        status["services"]["redis"] = f"error: {e}"
        status["status"] = "degraded"

    return status


@app.get("/", tags=["System"])
async def root():
    return {"message": "360Human API", "docs": "/docs"}
