BOT_NAME = 'leroymerlin'

IMAGES_STORE = 'leroymerlin_images'
FILES_STORE = 'leroymerlin_files'

SPIDER_MODULES = ['leroymerlin.spiders']
NEWSPIDER_MODULE = 'leroymerlin.spiders'


USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'

ROBOTSTXT_OBEY = False

CONCURRENT_REQUESTS = 16
LOG_ENABLED = True
LOG_LEVEL = 'DEBUG'

ITEM_PIPELINES = {
    'leroymerlin.pipelines.LeroymerlinPipeline': 300,
    'leroymerlin.pipelines.LeroymerlinPhotosPipeline': 100
}