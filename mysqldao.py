# -*- coding: utf-8 -*-

import sys
import pymysql
from config import Config
from time import sleep

reload(sys)
sys.setdefaultencoding('utf-8')


class MysqlDao():
    _mysql = {}

    def __init__(self):
        self._init_mysql()

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

    def execute(self, sql):
        self._mysql['cur'].execute(sql)
        self._mysql['conn'].commit()
        return self._mysql['cur']

    def executeValues(self, sql, values):
        self._mysql['cur'].execute(sql, values)
        self._mysql['conn'].commit()
        return self._mysql['cur']

    def close(self):
        self._mysql["cur"].close()
        self._mysql['conn'].close()
