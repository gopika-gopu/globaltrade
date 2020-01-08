# -*- coding: utf-8 -*-
import scrapy


class UsServiceprovidersSpider(scrapy.Spider):
    name = 'us_serviceproviders'
    allowed_domains = ['www.globaltrade.net']
    start_urls = ['http://www.globaltrade.net/']

    def parse(self, response):
        pass
