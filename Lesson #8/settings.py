# -*- coding: utf-8 -*-
BOT_NAME = 'instaparser'

SPIDER_MODULES = ['instaparser.spiders']
NEWSPIDER_MODULE = 'instaparser.spiders'


USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'

ROBOTSTXT_OBEY = False
LOG_ENABLED = True
LOG_LEVEL = 'DEBUG'

DOWNLOAD_DELAY = 1.25

DOWNLOADER_MIDDLEWARES = {
   'instaparser.middlewares.TooManyRequestsRetryMiddleware': 543,
}

ITEM_PIPELINES = {
   'instaparser.pipelines.InstaparserPipeline': 300,
}

AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 5
AUTOTHROTTLE_MAX_DELAY = 60
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
AUTOTHROTTLE_DEBUG = True