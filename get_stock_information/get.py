#coding=utf8

import requests
from pyquery import PyQuery as pq

url="http://www.cmoney.tw/follow/channel/stock-2498"
r = requests.get(url)
print r.text

data = open('data.html', 'w')
data.write(r.text.encode('utf-8'))
data.close()

url_index = pq(r.text)
print "Title:" + url_index('title').text()

#table_item = url_index('td')
#for i in table_item:
#	print table_item(i).text()
