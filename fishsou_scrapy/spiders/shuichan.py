# -*- coding: utf-8 -*-
import scrapy


class ShuichanSpider(scrapy.Spider):
    name = 'shuichan'
    allowed_domains = ['shuichan.cc']
    start_urls = ['http://shuichan.cc/']

    def parse(self, response):
        pass
