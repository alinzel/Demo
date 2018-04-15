# -*- coding: utf-8 -*-
# @Time    : 18-2-27 下午3:28
# @Author  : Zwl
# @Email   : 944951481@qq.com
# @File    : 06.py3下的urllib.py
# @Software: PyCharm
from urllib import request

url = 'https://www.douban.com/'

# urlopen(url,data,timeout)
resp = request.urlopen(url)
print(resp.getcode())

# Request(url,headers,data)
header = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
req = request.Request(url, headers=header)
resp = request.urlopen(req)
print(resp.getcode())

# urlencode()--post