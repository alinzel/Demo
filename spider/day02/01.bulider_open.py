# -*- coding: utf-8 -*-
# @Time    : 18-2-27 上午10:04
# @Author  : Zwl
# @Email   : 944951481@qq.com
# @File    : 01.bulider_open.py
# @Software: PyCharm
import urllib2

url = 'http://www.douban.com/'

# 实例一个HTTPHandler对象,TODO debuglevel=0默认
http_handler = urllib2.HTTPHandler(debuglevel=1)
# 打开实例的HTTPHandler对象
opener = urllib2.build_opener(http_handler)
# 添加头部
opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36')]

# resp = opener.open(url)  # TODO 打开链接 同URLopen（）
# print resp.read()

# install_opener将opener添加到urllib2库中，供以后在别处使用
def install_handler():
	urllib2.install_opener(opener)
	resp = opener.open(url)
	print resp.read()

if __name__ == '__main__':
	install_handler()