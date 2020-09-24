import scrapy


class LeroymerlinItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    product_article = scrapy.Field()
    product_link = scrapy.Field()
    product_description = scrapy.Field()
    product_characters_name = scrapy.Field()
    product_characters_def = scrapy.Field()
    photo = scrapy.Field()
    product_characters_total = scrapy.Field()

    _id = scrapy.Field()


