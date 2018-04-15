# -*- coding: utf-8 -*-
import scrapy


class TianmaoSpider(scrapy.Spider):
    name = 'tianmao'
    allowed_domains = ['tmall.com']
    start_urls = ['https://list.tmall.com/search_product.htm?&cat=50025135&s=120&sort=d&style=g']

    def parse(self, response):
        print(response.body.decode('utf-8'))
