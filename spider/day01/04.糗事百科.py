# -*- coding: utf-8 -*-
# @Time    : 18-2-26 下午11:44
# @Author  : Zwl
# @Email   : 944951481@qq.com
# @File    : 04.糗事百科.py
# @Software: PyCharm
import urllib2
import re
import pymongo

header = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

def main():
	for i in range(1,11):
		url = 'http://www.qiushibaike.com/hot/page/' + str(i)
		# print '正在请求%s页' % i
		# 请求网页
		html = get_page(url)
		# 解析网页
		parse_html(html)


def get_page(url):
	try:
		resq = urllib2.Request(url, headers=header)
		resp = urllib2.urlopen(resq)
		return resp.read()
	except urllib2.URLError as e:
		if hasattr(e,'code'):
			print(e.code)
		if hasattr(e,'reason'):
			print(e.reason)


def parse_html(html):
	# 解码
	html = html.decode('utf-8')
	# 正则匹配
	reg = re.compile(r'<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<span>(.*?)</span>'
					 r'.*?<span class="stats-vote"><i class="number">(\d+)</i>.*?<i class="number">(\d+)</i>', re.S)
	# findall.返回【】
	items = re.findall(reg,html)
	# print(len(items))
	for item in items:
		# 拼装数据写入数据库
		data = {
			'author': item[0].strip(),
			'content': item[1].strip(),
			'laugh': item[2].strip(),
			'comment_num': item[3].strip()
		}
		# print(data)
		print item[0].strip(), item[1].strip(), item[2].strip(), item[3].strip()
		# # 保存到数据库
		# save_mongo(data)


def save_mongo(data):
	try:
		# 链接数据库
		client = pymongo.MongoClient('127.0.0.1', 27017)
		# 链接数据库
		db = client.qsbk
		# 链接集合
		coll = db.hot
		# 插入数据
		if coll.insert(data):
			print('插入数据成功')
	except:
		print('数据库链接失败')


if __name__ == '__main__':
	main()