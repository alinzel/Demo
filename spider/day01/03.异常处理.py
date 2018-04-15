# -*- coding: utf-8 -*-
# @Time    : 18-2-26 下午8:48
# @Author  : Zwl
# @Email   : 944951481@qq.com
# @File    : 03.异常处理.py
# @Software: PyCharmurl
import urllib2
url = 'hhtp://www.baidu.com'

# resp = urllib2.urlopen(url)  # urllib2.URLError: <urlopen error unknown url type: hhtp>

# TODO 捕获异常
try:
	resp = urllib2.urlopen(url)
	print resp.read()
# TODO HTTPError 是 URLError的子类，应该写在前边
except urllib2.HTTPError as e:
	print e.code
	print e.msg
except urllib2.URLError as e:
	print e.message
	print e.reason
	print e.errno

# TODO 改写捕获异常
try:
	urllib2.urlopen(url)
except urllib2.URLError as e:
	# TODO 判断有没有属性
	if hasattr(e,'code'):
		print e.code
	if hasattr(e,'msg'):
		print e.msg
	if hasattr(e,'reason'):
		print e.reason


