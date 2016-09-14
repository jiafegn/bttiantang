# -*- coding: utf-8 -*-

import sys
import requests
from lxml import etree
from headers import Headers
from config import Config
from mysqldao import MysqlDao
import time
from proxies import Proxies

url_main = 'http://www.bttiantang.com/movie.php?/order/id/'

page_count = 10
# 1367为总页数,需要定期修改
for one in xrange(1, page_count):
    url = url_main + str(one)
    print(url)
    headers = Headers.getHeaders()
    try:
        proxies = Proxies.get_proxies()
        req = requests.get(url, headers=headers, timeout=30, proxies=proxies)
        code = req.status_code
        print(code)
        if code == 200:
            html = req.content
            selector = etree.HTML(html)
            content_urls = selector.xpath('//*[contains(@class,"litpic")]/a[1]/@href')
            for content_url in content_urls:
                content_url = Config.url_main + content_url
                created_at = time.strftime('%Y-%m-%d %H:%M:%S')
                insert_value = '"' + content_url + '",0,"' + created_at + '"'
                mysqlDao = MysqlDao()
                sql = 'select url from bttiantang_url ORDER BY id desc limit 0,1 '
                ret = mysqlDao.execute(sql)
                for r in ret:
                    res = r
                if r[0] == content_url:
                    print('game over')
                    sys.exit()
                sql = 'insert ignore into bttiantang_url (`url`,`status`,`created_at`) values(' + insert_value + ')'
                print(sql)
                mysqlDao.execute(sql)
                mysqlDao.close()
    except Exception, e:
        print Exception, ":", e
        time.sleep(10)
