# -*- coding: utf-8 -*-

import sys
import pymysql
import redis
from config import Config
from time import sleep

reload(sys)
sys.setdefaultencoding('utf-8')


class Database():
    _mysql = {}
    _redis = {}

    def __init__(self):
        self._init_mysql()
        # self._init_redis()

    def _init_mysql(self):
        try:
            self._mysql['conn'] = pymysql.connect(host=Config.mysql_host, port=Config.mysql_port,
                                                  password=Config.mysql_password,
                                                  user=Config.mysql_user, db=Config.mysql_dbname,
                                                  charset=Config.mysql_charset)
            self._mysql["cur"] = self._mysql["conn"].cursor()
        except:
            print ('Mysql Connect Error,sleep 100!')
            sleep(100)
            try:
                print('retry mysql connect')
                self._mysql['conn'] = pymysql.connect(host=Config.mysql_host, port=Config.mysql_port,
                                                      password=Config.mysql_password,
                                                      user=Config.mysql_user, db=Config.mysql_dbname,
                                                      charset=Config.mysql_charset)
                self._mysql["cur"] = self._mysql["conn"].cursor()
            except:
                print ('Mysql Connect Error!')
                sys.exit()

    def _init_redis(self):
        try:
            self._redis['conn'] = redis.Redis(host=Config.redis_host, port=Config.redis_port, db=0)
        except:
            print ('Redis Connect Error!')
            sys.exit()

    def mysqlExecute(self, sql):
        self._mysql['cur'].execute(sql)
        self._mysql['conn'].commit()
        return self._mysql['cur']

    def mysqlExecuteValues(self, sql, values):
        self._mysql['cur'].execute(sql, values)
        self._mysql['conn'].commit()
        return self._mysql['cur']

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

    def getBaseRootId(self, name):
        sql = 'select * FROM base_root WHERE name = "' + name + '"'
        self.mysqlExecute(sql)
        result = []
        for one in self._mysql['cur']:
            result.append(one)
        if len(result) == 0:
            ret = 0
        else:
            if len(result[0]) == 0:
                ret = 0
            else:
                ret = result[0][0]
        return ret

    def getCategoryId(self, name):
        sql = 'select * FROM meishichina_category WHERE name = "' + name + '"'
        self.mysqlExecute(sql)
        result = []
        for one in self._mysql['cur']:
            result.append(one)
        if len(result) == 0:
            ret = 0
        else:
            if len(result[0]) == 0:
                ret = 0
            else:
                ret = result[0][0]
        return ret

    def getIdBySql(self, sql):
        self.mysqlExecute(sql)
        for r in self._mysql['cur']:
            if len(r) >= 0:
                ret = r[0]
            else:
                ret = 0
        return ret

    def mysqlClose(self):
        self._mysql["cur"].close()
        self._mysql['conn'].close()
