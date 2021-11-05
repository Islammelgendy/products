import scrapy


class ProductsSpider(scrapy.Spider):
    name = 'products'
    start_urls = [
        "https://2b.com.eg/en/computers.html",
        "https://2b.com.eg/en/mobile-tablet.html",
        "https://2b.com.eg/en/gaming.html",
        "https://2b.com.eg/en/home-appliances.html",
        "https://2b.com.eg/en/accessories.html"


    ]

    def parse(self, response):
        Cat = response.css(
            'div.block-category-list').css('strong::text').get()
        for prod in response.css('div.product-item-info.type1'):

            yield {

                'title': prod.css('a.product-item-link::text').get(),
                'url': prod.css('a.product-item-link').attrib['href'],
                'category': Cat

            }

        next_page = response.css('a.action.next').attrib['href']
        if next_page is not None:

            yield response.follow(next_page, callback=self.parse)
