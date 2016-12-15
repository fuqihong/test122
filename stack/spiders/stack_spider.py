#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'qihong.fu'
__mtime__ = '2016/12/15'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""



from scrapy import Spider
from scrapy.selector import Selector

from stack.items import StackItem


class StackSpider(Spider):
    name = "stack"
    allowed_domains = ["stackoverflow.com"]
    start_urls = [
        "http://stackoverflow.com/questions?pagesize=50&sort=newest",
    ]

    def parse(self, response):
        questions = Selector(response).xpath('//div[@class="summary"]')
        for question in questions:
            item = StackItem()
            item['title'] = question.xpath(
                'h3/a[@class="question-hyperlink"]/text()').extract()[0]
            item['url'] = question.xpath(
                'h3/a[@class="question-hyperlink"]/@href').extract()[0]
            item['desc'] = question.xpath(
				'div[@class = "excerpt"]/text()').extract()[0]
            item['nameAsk'] = question.xpath(
				'div[@class = "excerpt"]/text()').extract()[0]
            yield item