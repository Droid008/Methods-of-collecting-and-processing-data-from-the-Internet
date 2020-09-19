# -*- coding: utf-8 -*-
BOT_NAME = 'jobparser'

SPIDER_MODULES = ['scrapy_2.jobparser.spiders']
NEWSPIDER_MODULE = 'scrapy_2.jobparser.spiders'


USER_AGENT = 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0'

ROBOTSTXT_OBEY = False

LOG_ENABLED = True
LOG_LABEL = 'DEBUG'

COOKIES_ENABLED = True


ITEM_PIPELINES = {
    'scrapy_2.jobparser.pipelines.JobparserPipeline': 300,
    'scrapy_2.jobparser.pipelines.JobparserItemAdjustmentsPipeline': 200,
}