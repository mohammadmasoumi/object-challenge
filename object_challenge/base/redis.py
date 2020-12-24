from redis import Redis

from app import app

__all__ = ('RedisService',)


class RedisService:

    @property
    def connect(self, **conf):
        if not conf:
            conf = app.config['REDIS_SETTINGS']

        return Redis(**conf)
