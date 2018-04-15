# -*- coding: utf-8 -*-
# @Time    : 18-3-2 下午6:15
# @Author  : Zwl
# @Email   : 944951481@qq.com
# @File    : 01.threading_斗图网.py
# @Software: PyCharm

import threading
import requests
from bs4 import BeautifulSoup
import time
import os

# TODO 确定数据
base_url = 'https://www.doutula.com/photo/list/?page='
header = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
	}
# 初始化存放url的容器
url_list = []
# 构造url,取三页
for i in range(1, 4):
	url = base_url + str(i)
	# 将拼接好的链接添加到url_list
	url_list.append(url)
# 初始化存档img_url的容器
img_url_list = []
# 初始化锁
glock = threading.Lock()


# TODO 定义生产者线程，用于请求网页和解析网页
class Producer(threading.Thread):
	# 重写run方法，start执行此方法
	def run(self):
		print('当前生产线程是%s' % threading.current_thread())
		# 当存放链接的列表存在数据时，进行此循环
		while len(url_list) > 0:
			# TODO 当一个线程取链接时，锁住
			glock.acquire()
			# 从url_list中拿出一个链接，并删除 [从末尾取出，并删除有返回值]
			request_url = url_list.pop()
			# TODO 当取完释放锁，方便其他线程
			glock.release()
			# 请求链接,并返回响应
			page = requests.get(request_url, headers=header)
			# 根据响应，得到源码
			html = page.text
			# 解析页面
			parse_html = BeautifulSoup(html, 'lxml')
			# 获取标签及图片的url
			img_urls = parse_html.select('.img-responsive.lazy.image_dta')
			# 上锁
			glock.acquire()
			# 遍历得到的图片列表
			for img_url_item in img_urls:
				# 获取图片的链接
				img_url = img_url_item.attrs['data-original']
				# 如果图片的链接不是以http开头，则构建图片链接数据
				if not img_url.startswith('http'):
					img_url = 'http:' + img_url
					img_url_list.append(img_url)
				else:
					img_url_list.append(img_url)
			# 释放锁
			glock.release()


# TODO 消费者线程，负责把图片写入本地
class Consumer(threading.Thread):
	# 重写父方法
	def run(self):
		print('当前消费线程是%s'%threading.current_thread())
		# TODO 设置休眠，当消费者等待生产者两秒，因为刚开始列表无数据，不能取出
		time.sleep(2)
		# 当img_url_list存在数据，执行此循环
		while len(img_url_list) > 0:
			glock.acquire()
			img_url = img_url_list.pop()
			glock.release()
			# 请求图片链接，并显示图片
			img = requests.get(img_url, headers=header).content
			# 定义图片存储目录
			dire = os.getcwd() + '/images/'
			# 如果路径不存在则创建目录
			if not os.path.exists(dire):
				os.mkdir('images')
			# 初始化图片的name
			img_name = img_url[-14:-4]
			# 构造图片路径
			path = dire + img_name
			# 打开路径
			with open(path, 'wb') as f:
				# 写入数据
				f.write(img)


if __name__ == '__main__':
	for i in range(1, 3):
		Producer().start()
	for i in range(1, 3):
		Consumer().start()
