# -*- coding: utf-8 -*-
# @Time    : 18-3-4 下午1:38
# @Author  : Zwl
# @Email   : 944951481@qq.com
# @File    : 02.homework_拉勾网.py
# @Softwa
import requests
from bs4 import BeautifulSoup
import time
import pymongo


# 主程序入口
def main():
	# 全国站
	# base_url = 'https://www.lagou.com/jobs/list_Python?px=page&city=全国'
	base_url = 'https://www.lagou.com/zhaopin/Python/'
	header = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
	}
	for i in range(1, 11):
		url = base_url + str(i)
		# url = base_url.replace('page', str(i))
		page = get_page(url, header)
		position_url_list = parse_page(page)
		for position_url in position_url_list:
			parse_position_url(position_url, header)


# 解析职位链接，得到职位先关数据
def parse_position_url(position_url, header):
	mongo_data = {
		'position_url': position_url
	}
	# 请求
	position_page = get_page(position_url, header)
	# 解析
	position_html = BeautifulSoup(position_page, 'lxml')
	position_title = position_html.select('.position-content-l .job-name .name')
	# TODO 如果为空可以try,再请求一次
	for i in position_title:
		if i:
			position_title = i.text
			mongo_data['position_title'] = position_title
		else:
			mongo_data['position_title'] = position_title
	position_salary = position_html.select('.position-content-l .job_request .salary')
	for i in position_salary:
		if i:
			position_salary = i.text
			mongo_data['position_salary'] = position_salary
		else:
			mongo_data['position_salary'] = position_salary
	position_place = position_html.select('.position-content-l .job_request p > span')
	if position_place:
		position_place = position_place[1].text.replace('/', '').strip()
		mongo_data['position_place'] = position_place
	else:
		mongo_data['position_place'] = position_place
	position_experience = position_html.select('.position-content-l .job_request p > span')
	if position_experience:
		position_experience = position_experience[2].text.replace('/', '').strip()
		mongo_data['position_experience'] = position_experience
	else:
		mongo_data['position_experience'] = position_experience
	position_education = position_html.select('.position-content-l .job_request p > span')
	if position_education:
		position_education = position_education[3].text.replace('/', '').strip()
		mongo_data['position_education'] = position_education
	else:
		mongo_data['position_education'] = position_education
	position_descs = position_html.select('.job_bt')
	if position_descs:
		position_descs = position_descs[0].stripped_strings
		position_desc_list = []
		for position_desc in position_descs:
			position_desc_list.append(position_desc)
			mongo_data['position_desc'] = position_desc_list
	else:
		mongo_data['position_desc'] = position_descs
	print(mongo_data)
	time.sleep(15)
	# save_mongo(mongo_data)


def save_mongo(data):
	client = pymongo.MongoClient('127.0.0.1', 27017)
	db = client.LaGouWang
	coll = db.job
	coll.insert(data)


# 解析页面,取出position_url
def parse_page(page):
	html = BeautifulSoup(page, 'lxml')
	position_urls = html.select('.con_list_item.default_list .list_item_top .position .p_top a')
	position_url_list = []
	for position_url in position_urls:
		position_url = position_url.attrs['href']
		position_url_list.append(position_url)
	return position_url_list


# 请求页面
def get_page(url, header):
	page = requests.get(url, headers=header)
	return page.text


if __name__ == '__main__':
	main()
