# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader.processors import TakeFirst


class JobparserItem(scrapy.Item):
    _id = scrapy.Field()
    name = scrapy.Field(output_processor=TakeFirst())
    salary = scrapy.Field()
    link = scrapy.Field(output_processor=TakeFirst())
    site = scrapy.Field()
    min_salary = scrapy.Field()
    max_salary = scrapy.Field()
    currency = scrapy.Field()

