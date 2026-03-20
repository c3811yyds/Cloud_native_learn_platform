from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from redis import Redis
from redis.exceptions import RedisError

# 全局扩展对象：在 app.py 中初始化，在各业务模块中复用。
db = SQLAlchemy()
jwt = JWTManager()
redis_client = None


def init_redis(app):
    """初始化 Redis；如果当前环境不可用，则以禁用缓存模式继续运行。"""
    global redis_client
    try:
        client = Redis.from_url(
            app.config["REDIS_URL"],
            decode_responses=True,
            socket_connect_timeout=1,
            socket_timeout=1,
        )
        client.ping()
        redis_client = client
    except RedisError:
        redis_client = None
        app.logger.warning("Redis unavailable, continuing with cache disabled.")