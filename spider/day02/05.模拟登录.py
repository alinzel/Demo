# -*- coding: utf-8 -*-
# @Time    : 18-2-27 下午2:18
# @Author  : Zwl
# @Email   : 944951481@qq.com
# @File    : 05.模拟登录.py
# @Software: PyCharm
import urllib2, urllib, cookielib

# 创建cookie
cookies = cookielib.CookieJar()
cookis_handler = urllib2.HTTPCookieProcessor(cookies)
opener = urllib2.build_opener(cookis_handler, urllib2.HTTPHandler(debuglevel=1))
opener.addheaders = [
	('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36')
]

data = {
	'email': '18698035693',
	'password': 'qiulei1314'
}

url = 'http://www.renren.com/PLogin.do'

data = urllib.urlencode(data)

requset = urllib2.Request(url, data)
resp = opener.open(requset)
if resp:
	print('success')
else:
	print('error')

# 再次登录
resp = opener.open('http://zhibo.renren.com/top')
print(resp.read())
