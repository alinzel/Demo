# -*- coding: utf-8 -*-
# @Time    : 18-3-3 上午11:34
# @Author  : Zwl
# @Email   : 944951481@qq.com
# @File    : 01.Pool_爬小说.py
# @Software: PyCharm
from multiprocessing.dummy import Pool
import requests
from bs4 import BeautifulSoup


# 主程序入口
def main():
	# 确定数据
	url = 'http://www.quanshuwang.com/book/9/9055/'
	header = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
	}
	# 请求页面
	page = get_page(url, headers=header)
	# 解析页面
	html = parse_page(page)
	# 抽取数据
	get_data(html)


# 请求页面
def get_page(url, headers):
	resp = requests.get(url, headers)
	return resp.content.decode('gbk')


# 解析页面
def parse_page(page):
	html = BeautifulSoup(page, 'lxml')
	return html


# 抓取页面数据
def get_data(html):
	book_infos = html.select('.clearfix.dirconone > li a')
	book_list = []
	for book_info in book_infos:
		book_data = {}
		book_url = book_info['href']
		book_title = book_info['title']
		book_data['book_url'] = book_url
		book_data['book_title'] = book_title
		book_list.append(book_data)
	print(len(book_list))


if __name__ == '__main__':
	main()
