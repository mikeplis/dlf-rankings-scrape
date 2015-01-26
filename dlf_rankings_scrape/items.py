# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class DlfRanking(scrapy.Item):
    rank = scrapy.Field(serializer=int)
    position = scrapy.Field()
    player = scrapy.Field()
    age = scrapy.Field(serializer=int)
    adp = scrapy.Field(serializer=float)
    # max = scrapy.Field()
    # min = scrapy.Field()
