# -*- coding: utf-8 -*-
import scrapy


class JieshaoSpider(scrapy.Spider):
	# TODO 爬虫脚本的名字，唯一
	name = 'jieshao'
	# TODO 允许爬虫访问的域名列表，可选
	allowed_domains = ['scrapy-chs.readthedocs.io']
	# TODO 初始URL，当没有设定URL，从此列表开始爬取
	start_urls = ['http://scrapy-chs.readthedocs.io/']

	# TODO 默认爬取到结果返回的函数，可以通过callback，调用其他函数
	def parse(self, response):
		# TODO 打印网页源代码
		print(response.body.decode('utf-8'))
		pass
