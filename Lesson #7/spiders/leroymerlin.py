import scrapy
from scrapy.http import HtmlResponse
from leroymerlin.items import LeroymerlinItem

class LeroymerlSpider(scrapy.Spider):
    name = 'leroymerl'
    allowed_domains = ['leroymerlin.ru']
    main_site = 'https://leroymerlin.ru'
    start_urls = ['https://leroymerlin.ru/search/?q=%D0%BA%D0%BE%D0%B2%D0%B5%D1%80']

    def parse(self, response:HtmlResponse):
        products = response.xpath("//product-card//@data-product-url").extract()
        for product in products:
            product = 'https://leroymerlin.ru' + product

            yield response.follow(product, callback=self.product_parse)

        next_page = response.css("div.next-paginator-button-wrapper a::attr(href)").extract_first()
        if next_page:
            yield response.follow(next_page, callback=self.parse)


    def product_parse(self, response:HtmlResponse):

        name = response.xpath("//h1/text()").extract_first()
        price = response.xpath("//@product-price").extract_first()
        product_article = response.xpath("//@product-id").extract_first()
        product_link = response.url
        product_characters_name = response.xpath("(//uc-pdp-section-layout)[2]//dt/text()").extract()
        product_characters_def = response.xpath("(//uc-pdp-section-layout)[2]//dd/text()").extract()
        product_description = response.xpath("//uc-pdp-section-vlimited//div//p/text()").extract()
        photo = response.xpath("//uc-pdp-media-carousel//picture//@src").extract()
        #photo = response.xpath("//uc-pdp-section-vlimited//div//p/text()").extract()
        #photo = response.xpath("//img[@alt='product image']/@src").extract()

        yield LeroymerlinItem(name=name, price=price, product_article=product_article, photo=photo, product_link=product_link, product_description=product_description, product_characters_name=product_characters_name, product_characters_def=product_characters_def)
        print()

