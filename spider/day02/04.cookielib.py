# -*- coding: utf-8 -*-
# @Time    : 18-2-27 下午2:17
# @Author  : Zwl
# @Email   : 944951481@qq.com
# @File    : 04.cookielib.py
# @Software: PyCharm

import urllib2
import cookielib

# TODO 创建cookieJar对象
cookie= cookielib.CookieJar()

# TODO 创建处理器对象
cookie_handler = urllib2.HTTPCookieProcessor(cookie)

# TODO  创建opener
opener = urllib2.build_opener(cookie_handler, urllib2.HTTPHandler(debuglevel=1))

# TODO 打开链接
resp = opener.open('http://www.baidu.com')

# TODO 关闭链接
resp.close()

# TODO 验证是否保存cookie--字典形式
print('--------------%s' % cookie._cookies)

# TODO 验证是否携带cookie请求(头会带有cookie信息)
resp = opener.open('http://www.baidu.com')