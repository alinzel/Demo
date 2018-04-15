# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request
from scrapy.loader import ItemLoader
# TODO 导入定义字段的类
from ..items import CrawlSpiderItem
import re
# TODO 默认的日志方法
from scrapy.conf import settings
# TODO 自定义日志方法
import logging
my_logger = logging.getLogger('日志以此来开头')


# TODO 类名：脚本名Spider
class CrawlspiderSpider(CrawlSpider):
    # TODO spider脚本的名字，唯一
    name = 'crawlspider'
    # TODO 可选，spider可爬取的域名的列表
    allowed_domains = ['python.jobbole.com', 'baidu.com']
    # TODO 初始url列表， 当没有设置特定url时，spider将从此列表开始抓取
    start_urls = ['http://python.jobbole.com/all-posts/']
    # TODO 链接可匹配的规则
    rules = (
        Rule(LinkExtractor(allow=r'page/(\d+)'), callback='parse_item', follow=True),
    )

    # TODO spider的起循环点，当指定url访问指定的URL，没有指定，会访问初始URL列表
    '''
        def start_requests(self):
            url = 'http://www.baidu.com'
            # TODO 当指定回调函数，将请求后结果返回回调函数，没有指定回调函数，将将调用parse
            # TODO 返回值为一个生成器，当返回Request类型，将继续爬取请求，返回item将给管道进行处理
            yield Request(url, callback=self.parse_item)
    '''

    # 解析页面
    def parse_item(self, response):
        '''
            日志信息
        '''
        print(response.url)

        # TODO 使用默认的日志,一下是打印每一种信息类型，当出现对应信息，会显示在日志中（settings设置级别也相关）
        # self.logger.info('info' + response.url)
        # self.logger.debug('debug' + response.url)
        # self.logger.warning('warning' + response.url)
        # self.logger.error('error' + response.url)
        # TODO 使用自定义的日志--my_logger，自定义日志头部返回值
        my_logger.info('info' + response.url)
        my_logger.debug('debug' + response.url)
        my_logger.warning('warning' + response.url)
        my_logger.error('error' + response.url)

        # TODO 使用xpath解析页面，得到包含所有内容的a标签
        items = response.xpath('//div[@class="post floated-thumb"]/div[@class="post-thumb"]/a')
        for item in items:
            # 解析得到的a标签，TODO extract（）返回列表，extract_first()返回第一个值
            # 文章链接
            art_url = item.xpath('./@href').extract_first()
            # 文章标题
            art_title = item.xpath('./@title').extract_first()
            # 文章图片
            art_img = item.xpath('./img/@src').extract_first()

            # TODO 请求文章链接 yield
            yield Request(art_url, callback=self.parse_art_url, meta={'art_url': art_url, 'art_title': art_title, 'art_img': art_img})


    # 解析文章链接
    def parse_art_url(self, response):
        # TODO ItemLoaders提供的是填充容器(items字典形式)的机制
        items = ItemLoader(item=CrawlSpiderItem(), response=response)  # 返回 scrapy对象 <scrapy.loader.ItemLoader object at 0x7f3f1d459f28>
        # TODO 通过ItemLoader实例化返回的对象，进行页面解析
        # # TODO add_xpath会将匹配到的内容添加到指定字段
        # items.add_xpath('art_content', '//div[@class="entry"]/p/text()')
        # items.add_xpath('art_create_time', '//div[@class="entry-meta"]/p/text()')
        # TODO 解析页面，拿到文章内容
        art_content = response.xpath('//div[@class="entry"]')
        art_content_list = art_content.xpath('string(.)').extract()[0].strip().split('\r\n')
        art_contents = ''
        # TODO 对数据进行处理
        for i in art_content_list:
            art_contents += i
            art_contents = art_contents.strip().replace('\n','').replace(' ', '').replace('\t', '')
        # TODO 获取时间
        art_create_time = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()').extract_first()
        # TODO replace_value替代原来字段的值
        items.replace_value('art_img', response.meta['art_img'])
        items.replace_value('art_url', response.meta['art_url'])
        items.replace_value('art_title', response.meta['art_title'])
        items.replace_value('art_content', art_contents)
        items.replace_value('art_create_time', art_create_time.strip()[0:-2])
        # TODO return给管道
        return items.load_item()
