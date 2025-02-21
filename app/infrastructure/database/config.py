from dataclasses import dataclass

from settings.config import settings


@dataclass
class DBConfig:
    user: str = settings.DATABASE_USER
    password: str = settings.DATABASE_PASSWORD
    host: str = settings.DATABASE_HOST
    port: int = settings.DATABASE_PORT
    name: str = settings.DATABASE_NAME
    provider: str = settings.DATABASE_PROVIDER

    @property
    def database_url(self):
        return f"{self.provider}://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"
