import json
import logging

from django.conf import settings

from redis.client import StrictRedis
from redis.exceptions import ConnectionError, TimeoutError

from apps.core.services.statsd import statsd

logger = logging.getLogger(__name__)

QUEUE_REMOVE_LIMIT = 10000


class Redis(object):

    QUEUE_PREFIX = "redis-queue"

    def __init__(self):
        self.client = None

    def init_app(self, connection: str = None):
        self.client = StrictRedis.from_url(
            connection or settings.REDIS_CONNECTION_QUEUE_BASE,
            socket_timeout=settings.REDIS_SOCKET_TIMEOUT,
            socket_connect_timeout=settings.REDIS_SOCKET_CONNECT_TIMEOUT,
        )

    def delete_queue(self, key):
        queue_key = "%s:%s" % (self.QUEUE_PREFIX, key)
        for _ in range(self.get_queue_length(key) // QUEUE_REMOVE_LIMIT):
            self.client.ltrim(queue_key, 0, -QUEUE_REMOVE_LIMIT - 1)
        self.client.delete(queue_key)

    def queue_append(self, key, *values, **kwargs):
        client = kwargs.get("pipeline", self.client)
        values = [json.dumps(value, separators=(",", ":")) for value in values]
        redis_key = "%s:%s" % (self.QUEUE_PREFIX, key)
        limit = kwargs.get("limit")

        if limit:
            cur_size = self.client.llen(redis_key)
            if limit - cur_size < len(values):
                statsd.increment_counter("redis_queue_over_limit", redis_key)
            if cur_size >= limit:
                return
            values = values[: limit - cur_size]

        try:
            client.rpush(redis_key, *values)
        except (ConnectionError, TimeoutError) as e:
            logger.exception(e)
            statsd.increment_counter("queue_append(%s)" % str(e), "redis_fail")

    def queue_pop(self, key, limit):
        queue_name = "%s:%s" % (self.QUEUE_PREFIX, key)
        with self.client.pipeline() as p:
            p.lrange(queue_name, 0, limit - 1)
            p.ltrim(queue_name, limit, -1)
            res = p.execute()
            values = [json.loads(value) for value in res[0]]
        return values

    def get_queue_length(self, key):
        return self.client.llen("%s:%s" % (self.QUEUE_PREFIX, key))


class RedisQueue(object):
    def __init__(self, redis_client):
        self._redis = redis_client

    def push(self, key, data, limit=None, pipeline=None):
        kwargs = {}
        if pipeline is not None:
            kwargs["pipeline"] = pipeline
        self._redis.queue_append(key, *data, limit=limit, **kwargs)

    def pop(self, key, limit):
        return self._redis.queue_pop(key, limit)

    def get_length(self, key):
        return self._redis.get_queue_length(key)

    def delete(self, key):
        self._redis.delete_queue(key)


redis = Redis()
queue = RedisQueue(redis)
