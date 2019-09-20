# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CoolscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class HuxiuItem(scrapy.Item):
    title = scrapy.Field()    # 标题
    link = scrapy.Field()     # 链接
    desc = scrapy.Field()     # 简述
    posttime = scrapy.Field() # 发布时间


class Zufang58Item(scrapy.Item):
    # 标题
    title = scrapy.Field()
    # 房间
    room = scrapy.Field()
    # 区域
    zone = scrapy.Field()
    # 地址
    address = scrapy.Field()
    # 价格
    money = scrapy.Field()
    # 发布信息的类型，品牌公寓，经纪人，个人
    type = scrapy.Field()
