# -*- coding: utf-8 -*-
# @Time    : 18-3-1 上午9:47
# @Author  : Zwl
# @Email   : 944951481@qq.com
# @File    : 01.bs4_css.py
# @Software: PyCharm
from bs4 import BeautifulSoup
import requests
import pymongo


# 主程序入口
def main():
	# 确定准备数据
	url = 'https://www.douban.com/doulist/45004834/'
	header = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
	}
	# 请求页面
	html = get_page(url, header)
	# 解析页面
	parse_html(html)


# 解析页面
def parse_html(html):
	page = BeautifulSoup(html, 'lxml')

	# 获取数据--TODO CSS选择器的使用
	divs = page.select('.bd.doulist-subject')
	for div in divs:
		# TODO 属性选择器span[title="2016-08-19 11:57:01"]
		# time = parse_html.select('span[title="2016-08-19 11:57:01"]')[0].get_text()
		# 图片
		img = div.select('.post a img')[0].attrs['src']
		# 标题
		title = div.select('.title a')[0].get_text().strip()
		# 评分
		score = div.select('.rating .rating_nums')[0].get_text()
		# 评价
		comment = div.select('.rating > span')[2].get_text()[1:-4]

		# 构造数据
		mongo_data = {
			'img_url': img,
			'title': title,
			'score': score,
			'comment': comment,
		}

		# 作者级出版社信息
		infos = div.select('.abstract')[0].stripped_strings  # 返回生成器

		for i in infos:
			if '作者' in i:
				author = i.replace('作者: ', '')
				mongo_data['author'] = author
			elif '出版社' in i:
				publisher = i.replace('出版社: ', '')
				mongo_data['publisher'] = publisher
			elif '出版年' in i:
				year = i.replace('出版年: ', '')
				mongo_data['year'] = year
		print(mongo_data)
		# 保存到数据库
		# save_mongo(mongo_data)


# 保存数据
def save_mongo(data):
	# 链接数据库客户端
	client = pymongo.MongoClient('127.0.0.1', 27017)
	# 链接数据库
	db = client.DB_book
	# 链接集合
	coll = db.info
	# 插入数据
	if coll.insert(data):
		print('数据插入成功')


# 请求页面
def get_page(url, header):
	resp = requests.get(url, headers=header)
	return resp.text


if __name__ == '__main__':
	main()
