# -*- coding: utf-8 -*-
import scrapy


class InstaparserItem(scrapy.Item):
    user_id = scrapy.Field()
    _id = scrapy.Field()

    subscription_id = scrapy.Field()
    subscription_photo = scrapy.Field()
    subscription_name = scrapy.Field()
    subscription = scrapy.Field()

    subscriber_id = scrapy.Field()
    subscriber_photo = scrapy.Field()
    subscriber_name = scrapy.Field()
    subscriber = scrapy.Field()