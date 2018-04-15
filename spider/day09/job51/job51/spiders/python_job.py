# -*- coding: utf-8 -*-
import scrapy


class PythonJobSpider(scrapy.Spider):
    name = 'python_job'
    allowed_domains = ['51job.com']
    start_urls = ['http://51job.com/']

    def parse(self, response):
        pass
