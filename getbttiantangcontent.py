# -*- coding: utf-8 -*-

import time
import threading
import requests
from lxml import etree
import simplejson
from mysqlpooldao import MysqlDao
from headers import Headers
import sys
from config import Config

reload(sys)
sys.setdefaultencoding('utf-8')


class Worker(threading.Thread):
    def getDetails(self, details):
        ret = []
        if len(details) > 0:
            detail = Config.url_main + details[0]
            headers = Headers().getHeaders()
            req = requests.get(detail, headers=headers)
            selector = etree.HTML(req.content)
            js = selector.xpath('//script/text()')
            if len(js) > 0:
                urls = js[0].split('"')
                if len(urls) > 0:
                    ret.append(urls[1])
        return ret

    def run(self):
        while True:
            print(self.name)
            mysqlDao = MysqlDao()
            sql = 'select * from bttiantang_url WHERE `status`=0 limit 0,1'
            ret = mysqlDao.execute(sql)
            res = []
            for r in ret:
                res = r
            print(res)
            if len(res) == 0:
                print('sleep')
                # sql = 'update yingshi_bttiantang_url set `status`=0 WHERE `status`=2'
                # database.mysqlExecute(sql)
                mysqlDao.close()
                # time.sleep(21600)
                # continue
                """
                不用睡眠直接退出等crontab唤醒
                """
                print('game over')
                sys.exit()
            else:
                id = res[0]
                url = res[1]
                sql = 'update bttiantang_url set `status`=2 where `id`=' + str(id)
                mysqlDao.execute(sql)
                headers = Headers.getHeaders()
                n = 0
                while n < 5:
                    req = requests.get(url, headers=headers)
                    if req.status_code == 200:
                        html = req.content
                        selector = etree.HTML(html)
                        contents = selector.xpath('//ul[contains(@class,"moviedteail_list")]')
                        if len(contents) > 0:
                            break
                    n = n + 1
                if len(contents) > 0:
                    content = contents[0]
                else:
                    continue
                names_chn = selector.xpath('//div[contains(@class,"moviedteail_tt")]/h1/text()')
                names_eng = selector.xpath('//div[contains(@class,"moviedteail_tt")]/span/text()')
                name_chn = ''
                name_eng = ''
                if len(names_chn) > 0:
                    name_chn = names_chn[0]
                if len(names_eng) > 0:
                    name_eng = names_eng[0]
                names_nick = content.xpath('li[contains(text(),"%s")]/a/text()' % (u'又名'))
                if len(names_nick) > 0:
                    names_nick_new = ",".join(names_nick)
                else:
                    names_nick_new = ""
                imgs = simplejson.dumps(selector.xpath('//div[contains(@class,"moviedteail_img")]/a/img/@src'))
                tags = content.xpath('li[contains(text(),"%s")]/a/text()' % (u'标签'))
                if len(tags) > 0:
                    tags_new = ",".join(tags)
                else:
                    tags_new = ""
                areas = content.xpath('li[contains(text(),"%s")]/a/text()' % (u'地区'))
                if len(areas) > 0:
                    areas_new = ",".join(areas)
                else:
                    areas_new = ""
                years = content.xpath('li[contains(text(),"%s")]/a/text()' % (u'年份'))
                if len(years) > 0:
                    years_new = ",".join(years)
                else:
                    years_new = ""
                directors = content.xpath('li[contains(text(),"%s")]/a/text()' % (u'导演'))
                if len(directors) > 0:
                    directors_new = ",".join(directors)
                else:
                    directors_new = ""
                writers = content.xpath('li[contains(text(),"%s")]/a/text()' % (u'编剧'))
                if len(writers) > 0:
                    writers_new = ",".join(writers)
                else:
                    writers_new = ""
                casts = content.xpath('li[contains(text(),"%s")]/a/text()' % (u'主演'))
                if len(casts) > 0:
                    casts_new = ",".join(casts)
                else:
                    casts_new = ""
                imdbs = content.xpath('li[contains(text(),"%s")]/a/text()' % (u'imdb'))
                if len(imdbs) > 0:
                    imdbs_new = ",".join(imdbs)
                else:
                    imdbs_new = ""
                details = self.getDetails(content.xpath('li[contains(text(),"%s")]/a/@href' % (u'详情')))
                if len(details) > 0:
                    details_new = details[0]
                else:
                    details_new = ""
                created_at = time.strftime('%Y-%m-%d %H:%M:%S')
                downloads = selector.xpath('//div[contains(@class,"tinfo")]')
                download = []
                for d in downloads:
                    try:
                        dn_text = d.xpath('a[1]/@title')[0]
                        dn_url = d.xpath('a[1]/@href')[0]
                        download.append({dn_text: dn_url})
                    except:
                        pass
                download_json = simplejson.dumps(download)
                sql_pattern = 'insert ignore INTO `bttiantang_content`(`names_chn`, `names_eng`,`names_nick`,`imgs`,`tags`, `areas`, `years`, `directors`, `writers`,`casts`, `imdbs`,`details`, `download`,`created_at`, `url`) VALUES(%s, %s, %s,%s,%s,%s, %s, %s,%s, %s,%s, %s,%s, %s, %s)'
                sql_values = (
                    name_chn, name_eng, names_nick_new, imgs, tags_new, areas_new, years_new, directors_new,
                    writers_new, casts_new, imdbs_new,
                    details_new, download_json, created_at, url)
                mysqlDao.executeValues(sql_pattern, sql_values)
                sql = 'update bttiantang_url set `status`=1 where `id`=' + str(id)
                mysqlDao.execute(sql)
                mysqlDao.close()


if __name__ == '__main__':
    worker_num = 10
    threads = []
    for x in xrange(0, worker_num):
        threads.append(Worker())
    for t in threads:
        t.start()
        time.sleep(5)
    for t in threads:
        t.join()
