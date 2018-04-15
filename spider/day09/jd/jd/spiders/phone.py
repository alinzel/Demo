# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
a = 1
class PhoneSpider(CrawlSpider):

	name = 'phone'
	allowed_domains = ['jd.com']
	start_urls = ['https://list.jd.com/list.html?cat=9987,653,655&page=1']

	rules = (
		Rule(LinkExtractor(allow=r'page=[1-7]{1,3}'),
			 				callback='parse_item',
			 				follow=True,),
	)


	def parse_item(self, response):
		global a
		print('当前链接' + response.url)

		# print(response.text)
		# 解析商品列表页
		# items = response.xpath('//div[@class="gl-i-wrap j-sku-item"]').extract_first()
		# print(items)

		print(a)
		a += 1