# -*- coding: utf-8 -*-
import scrapy
from fishsou_scrapy.items import FishsouScrapyItem

class ShuichanSpider(scrapy.Spider):
    name = 'shuichan'
    allowed_domains = ['shuichan.cc']

    url = "http://www.shuichan.cc/news_list.asp?action=&c_id=91&s_id=101&page="
    offset = 0

    start_urls = [url + str(offset)]

    def parse(self, response):
        #for each in response.css("a[href*=news_view]::attr(href)").extract():

        html = response.xpath('//td[contains(@width, "672")]')

        for each in response.xpath('//td[contains(@width, "672")]'):

            item = FishsouScrapyItem()
            item['like'] = str(each.css("a[href*=news_view]::attr(href)"))

            yield item

        if self.offset < 10:
            self.offset += 1

        # 每次处理完一页的数据之后，重新发送下一页页面请求
        # self.offset自增10，同时拼接为新的url，并调用回调函数self.parse处理Response
        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)
