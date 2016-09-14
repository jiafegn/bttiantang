# -*- coding: utf-8 -*-

from mysqlpooldao import MysqlDao
import threading
import random


class Tt(threading.Thread):
    def run(self):
        mysqlDao = MysqlDao()
        for one in xrange(0, 1000):
            v = random.randint(1, 10000)
            sql = 'insert into yingshi_test (`name`) values (%s)'
            print(sql)
            mysqlDao.executeValues(sql, v)
        mysqlDao.close()


if __name__ == '__main__':
    worker_num = 15
    threads = []
    for x in xrange(0, worker_num):
        threads.append(Tt())
    for t in threads:
        t.start()
    for t in threads:
        t.join()
