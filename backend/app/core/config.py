from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # App
    APP_ENV: str = "development"
    APP_DEBUG: bool = True
    FRONTEND_URL: str = "http://localhost:3000"
    SENTRY_DSN: str = ""

    # Database
    DATABASE_URL: str

    # Redis
    REDIS_URL: str = "redis://redis:6379/0"

    # Auth
    JWT_SECRET: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_DAYS: int = 30

    # AI
    ANTHROPIC_API_KEY: str = ""

    # External
    ASTROLOGY_API_KEY: str = ""
    ASTROLOGY_API_BASE_URL: str = "https://astrology-api.io/api/v1"

    # VietQR / Payment
    BANK_BIN: str = "970436"          # Vietcombank default
    BANK_ACCOUNT_NUMBER: str = ""
    BANK_ACCOUNT_NAME: str = "360HUMAN"
    WEBHOOK_SECRET: str = "change-me-in-prod"
    PRICE_PRO: int = 199000
    PRICE_MAX: int = 499000


settings = Settings()
