# 配置文件：RedisConfig
from fastapi_plus.utils.redis import RedisConfig

redis_config = RedisConfig()
redis_config.host = 'redis'
redis_config.port = '6379'
redis_config.username = 'root'
redis_config.password = '1q2w3e4R'
redis_config.database = 1
