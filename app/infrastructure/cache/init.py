from app.infrastructure.cache.config import CacheConfig
import aioredis

def init_redis(cache_config: CacheConfig) -> Redis:
    return aioredis.from_url(cache_config.get_url("redis"))