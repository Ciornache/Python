import scrapy
from scrapy.spiders import CrawlSpider , Rule
from scrapy.linkextractors import LinkExtractor
class MySpider(CrawlSpider):

    name = "spider1"
    start_urls = ["https://www.autovit.ro/"]
    allowed_domains = ["autovit.ro"]

    rules=Rule(link_extractor=LinkExtractor(allow="promoted\w*"), callback="parse_item", follow = True),

    def parse_item(self, response):
        lista_link = response.xpath('//a[@class="ooa-1mrywk9"]/@href').getall()
        for url in lista_link:
            yield scrapy.Request(url, callback=self.parse_item2)
    
    def parse_item2(self, response):
        name_attributes=response.xpath('//p[@class="e130ulp54 ooa-12b2ph5"]/text()').getall()
        cnt=len([x for x in name_attributes if x == 'Km'])
        if cnt == 0:
            return None
        nume=response.xpath('//h3[@class="offer-title big-text e1aecrfb2 ooa-ebtemw er34gjf0"]/text()').get()
        pret=' '.join([response.xpath('//h3[@class="offer-price__number e1mlrgts4 ooa-1jtct0k er34gjf0"]/text()').get(), response.xpath('//p[@class="offer-price__currency e1mlrgts5 ooa-1h7cehh er34gjf0"]/text()').get()])
        attributes=response.xpath('//p[@class="e4cq37s0 ooa-1pe3502 er34gjf0"]/text()').getall()
        an, km = attributes[1:3]
        yield {
                'nume':nume,
                'pret':pret,
                'an':an,
                'km':km
              }
    
        