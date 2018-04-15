# -*- coding: utf-8 -*-
# @Time    : 18-2-27 上午10:41
# @Author  : Zwl
# @Email   : 944951481@qq.com
# @File    : 03.代理.py
# @Software: PyCharm

import urllib2
import random

# 定义url
url = 'https://www.douban.com/'

# 定义代理IP
proxy_list = [
	{'http' : '61.135.217.7:80'},
	{'https' : '202.120.1.39:7777'},
	{'http' : '58.253.116.10:80'},
	{'https' : '117.95.199.86:44606'},
	{'http':'122.114.31.177:808'},
    {'http':'219.133.68.164:8081'},
    {'https':'114.232.80.185:26451'},
]

# 实例化代理处理器
proxy_handler = urllib2.ProxyHandler(random.choice(proxy_list))

# 打开代理器
opener = urllib2.build_opener(proxy_handler)

# 添加头部信息
opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36')]

# 打开链接
resp = opener.open(url)
print resp.read()
