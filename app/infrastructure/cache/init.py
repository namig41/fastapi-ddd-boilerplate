import aioredis

from infrastructure.cache.config import CacheConfig


def init_redis(cache_config: CacheConfig) -> aioredis.Redis:
    return aioredis.from_url(cache_config.get_url("redis"))
