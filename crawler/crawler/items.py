# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item

class jobItem(Item):
    title = Field()
    company = Field()
    link = Field()
    date = Field()
    location = Field()
    interesting = Field()