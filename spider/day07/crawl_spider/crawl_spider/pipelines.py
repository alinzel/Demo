# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.conf import settings
import json


class CrawlSpiderPipeline(object):
	def __init__(self):
		# TODO 初始化数据库信息,在这里初始化是为了只连接一次数据库，如果写在方法里每次都要链接，浪费时间，耗内存
		# self.client = pymongo.MongoClient('127.0.0.1', 27017)
		# 使用从settings中导入的配置
		self.client = pymongo.MongoClient(settings['MONGO_IP'], settings['MONGO_PORT'])
		self.db = self.client.bole_zhangzhan
		self.coll = self.db.bole

		# TODO 初始化要保存的文件，原因同上
		self.f = open('./bole_file.json', 'w+', encoding='utf-8')

	def process_item(self, item, spider):
		# print(type(item))  # TODO item为·爬虫类 <class 'crawl_spider.items.CrawlSpiderItem'>
		# print(type(dict(item)))  # <class 'dict'>

		# 插入到数据库
		# self.coll.insert(dict(item))

		# 保存为JSON文件
		line = json.dumps(dict(item), ensure_ascii=False) + '\n'
		self.f.write(line)
		return item  # 在控制台输出元数据，可以不写
