from dataclasses import dataclass

from settings.config import settings


@dataclass
class CacheConfig:
    host: str = settings.CACHE_HOST
    port: int = settings.CACHE_PORT
    provider: str = settings.CACHE_PROVIDER

    @property
    def get_url(self) -> str:
        return f"{self.provider}://{self.host}:{self.port}"
