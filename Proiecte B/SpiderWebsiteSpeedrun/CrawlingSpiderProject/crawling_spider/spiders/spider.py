import scrapy
from crawling_spider.items import CrawlingSpiderItem
import time 
import logging
import sys


logger = logging.getLogger(__name__)
handler = logging.FileHandler('logger.log')
formatter = logging.Formatter('%(asctime)s - %(message)s - %(levelname)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

class SpidermanSpider(scrapy.Spider):

    name='spiderman'
    start_urls = []

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback = self.parse)

    def __init__(self, url:str='', tag:str='', maxDepth=None, *args, **kwargs):
        super(SpidermanSpider, self).__init__(*args, **kwargs)
        self.start_urls.append(url)
        self.tag = tag
        self.history = {}
        self.parent = {}
        self.maxDepth = int(maxDepth)
        
    def parse(self, response, traseu=[], depth=0):
        self.history.setdefault(response.url, True)
        size = round(len(response.body) / (2 ** 20), 2)
        traseu.append((response.url, f'{size}MB'))
        tag=self.tag
        links = list(filter(lambda x: True if x not in self.history else self.history[x], response.xpath(f'//a[@{tag}][starts-with(@href, "https")]/@href').getall()))
        if len(links) == 0 or depth == self.maxDepth:
            print('Traseu', traseu, end = '\n', sep = ' ')
            item = CrawlingSpiderItem()
            traseu2 = traseu.copy()
            traseu2 = list(map(lambda x: '(' + ','.join(x) + ')', traseu))
            item['traseu'] = '->'.join(traseu2)
            yield item
            return None

        for link in links:
            logger.info(f'Am accesat linkul {link} dupa ce am plecat de la {response.url}\n')
            yield scrapy.Request(link, callback=self.parse, cb_kwargs={'traseu':traseu.copy(), 'depth':depth+1})
        logger.info(f'Am terminat de trimis request-urile din link-ul {response.url}')

        return None
        