from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PYTHONPATH: str

    SERVICE_API_HOST: str
    SERVICE_API_PORT: int

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_TEST_DB: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str

    PGADMIN_EMAIL: str
    PGADMIN_PASSWORD: str

    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str

    WEATHER_API_KEY: str
    WEATHER_API_URL: str

    CACHE_HOST: str
    CACHE_PORT: str

    SMTP_HOST: str
    SMTP_PORT: int
    SMTP_USERNAME: str
    SMTP_PASSWORD: str

    MESSAGE_BROKER_HOST: str
    MESSAGE_BROKER_PORT: int
    MESSAGE_BROKER_UI_PORT: int
    MESSAGE_BROKER_USER: str
    MESSAGE_BROKER_PASSWORD: str

    TELEGRAM_TOKEN: str


config: Settings = Settings()
