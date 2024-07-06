import scrapy
from ..items import Pblsem4Item


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    page_number = 2
    start_urls = ['https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_nav_0']

    def parse(self, response):
        items = Pblsem4Item()

        product_name = response.css('.a-link-normal ._cDEzb_p13n-sc-css-line-clamp-1_1Fn1y').css('::text').extract()
        product_author = response.css('.a-link-child ._cDEzb_p13n-sc-css-line-clamp-1_1Fn1y').css('::text').extract()
        product_price = response.css('._cDEzb_p13n-sc-price_3mJ9Z::text').extract()
        product_imagelink = response.css('.p13n-product-image::attr(src)').extract()

        items['product_name'] = product_name
        items['product_author'] = product_author
        items['product_price'] = product_price
        items['product_imagelink'] = product_imagelink

        yield items

        next_page = 'https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_pg_2?ie=UTF8&pg=' + str(AmazonSpiderSpider.page_number)
        if AmazonSpiderSpider.page_number < 2:
            AmazonSpiderSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
