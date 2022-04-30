# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobparserItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    salary = scrapy.Field()
    url = scrapy.Field()
    company = scrapy.Field()
    min_salary = scrapy.Field()
    max_salary = scrapy.Field()
    currency = scrapy.Field()
    comment = scrapy.Field()
    pass
