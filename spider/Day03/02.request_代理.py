# -*- coding: utf-8 -*-
# @Time    : 18-2-28 下午12:40
# @Author  : Zwl
# @Email   : 944951481@qq.com
# @File    : 02.request_代理.py
# @Software: PyCharm

import requests
import random

url = 'https://www.douban.com/note/657718689/'

# proxy = [
#     {'https':'https://113.128.28.36:45769'},
#     {'https':'https://121.226.168.124:43820'},
#     {'https':'https://120.38.103.88:27102'},
# ]
proxy = {"http":"http://103.78.213.147:80"}

try:
    resp = requests.get(url,proxies=proxy)
    print (resp.text)
except requests.HTTPError as e:
    if hasattr(e,'code'):
        print (e.code)
    if hasattr(e,'reason'):
        print (e.reason)