# -*- coding: utf-8 -*-
# @Time    : 18-2-26 下午8:27
# @Author  : Zwl
# @Email   : 944951481@qq.com
# @File    : 02.urllib2.py
# @Software: PyCharm
# TODO 解决某些网站对https请求不会响应，引入urllib2
import urllib2, urllib

# 定义一个URL
url = 'https://www.zhihu.com/question/49144687 '

header = {
	# 向服务器提供身份
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
	# 对付反爬虫，写本身链接
'Referrer':'https://www.zhihu.com/question/49144687',
}

# req = urllib2.Request(url, headers=header)
# resp = urllib2.urlopen(req)
# print resp.read()
# # 打印请求方式
# print req.get_method()  # GET 因为没有传入参数data


# TODO Request传入参数data,请求方式会变成post
data = urllib.urlencode({'key':'环境'})
# 创建request实例
req1 = urllib2.Request(url, data=data, headers=header)
resp1 = urllib2.urlopen(req1)

print resp1.read()
print req1.get_method()  # POST 传入参数改变请求方式

