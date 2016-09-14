# -*- coding: utf-8 -*-

import requests
from lxml import etree
from headers import Headers

url = 'http://www.bttiantang.com/jumpto.php?aid=28306'
headers = Headers().getHeaders()
req = requests.get(url,headers=headers)
selector = etree.HTML(req.content)
url = selector.xpath('//script/text()')
print(url[0].split('"'))