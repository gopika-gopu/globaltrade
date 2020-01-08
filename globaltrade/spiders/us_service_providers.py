# -*- coding: utf-8 -*-
import scrapy


class UsServiceProvidersSpider(scrapy.Spider):
    name = 'us_service_providers'
    allowed_domains = ['www.globaltrade.net']
    start_urls = ['https://www.globaltrade.net/United-States/expert-service-provider.html']

    def parse(self, response):
        provider_url = response.xpath('//li[@class="sp-id"]/p[@class="sp-name"]/a[@class="profileNavigator"]/@href').extract()
        print(provider_url)
        pass
