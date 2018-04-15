# -*- coding: utf-8 -*-
import scrapy


class JobSpider(scrapy.Spider):
    # 爬虫脚本名，不能重复
    name = 'job'
    # 允许的域名
    allowed_domains = ['python.jobbole.com/all-posts']
    # 要请求的链接
    start_urls = ['http://python.jobbole.com/all-posts/']

    def parse(self, response):
        # response.body-->查看网页源码，返回字节形式，decode进行解码，为字符串形式
        # print(response.body.decode('utf-8'))
        # TODO response为请求目标网页的响应结果[<200 http://python.jobbole.com/all-posts/>]，相当于resp
        # 解析页面
        items= response.xpath('//div[@class="post-thumb"]/a').extract()
        print(items)
