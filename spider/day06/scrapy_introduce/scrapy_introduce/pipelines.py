# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# TODO 对获取到的数据进行处理，保存数据库，本地等
class ScrapyIntroducePipeline(object):
    def process_item(self, item, spider):
        return item
