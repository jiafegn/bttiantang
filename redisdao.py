# -*- coding: utf-8 -*-

import sys
import redis
from config import Config

reload(sys)
sys.setdefaultencoding('utf-8')


class RedisDao():
    _redis = {}

    def __init__(self):
        self._init_redis()

    def _init_redis(self):
        try:
            self._redis['conn'] = redis.Redis(host=Config.redis_host, port=Config.redis_port, db=0)
        except:
            print ('Redis Connect Error!')
            sys.exit()

    def redisLpop(self, key):
        return self._redis['conn'].lpop(key)

    def redisLpush(self, key, data):
        return self._redis['conn'].lpush(key, data)

    def redisRpush(self, key, data):
        return self._redis['conn'].rpush(key, data)

    def redisHget(self, key, name):
        # key = Config.redis_key_category_hash
        # self._redis['conn'].hset(key,name,111)
        return self._redis['conn'].hget(key, name)

    def redisHset(self, key, name, value):
        # key = Config.redis_key_category_hash
        return self._redis['conn'].hset(key, name, value)

    def redisHdel(self, key, name):
        # key = Config.redis_key_category_hash
        return self._redis['conn'].hdel(key, name)
