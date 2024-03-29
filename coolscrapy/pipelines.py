# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class CoolscrapyPipeline(object):
    def process_item(self, item, spider):
        return item

import json
import codecs

class JsonWithEncodingPipeline(object):

    def __init__(self):
        self.file = codecs.open('scraped_data_utf8.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()


class Zufang58Pipeline(object):
    def __init__(self):
        self.file = open('zufang58.json', mode='w', encoding='utf-8')

    def process_item(self, item, spider):
        jsondata = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(jsondata)
        return item

    def close_spider(self, spider):
        self.file.close()

