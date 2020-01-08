# -*- coding: utf-8 -*-
import scrapy


class UsServiceProvidersSpider(scrapy.Spider):
    name = 'us_service_providers'
    allowed_domains = ['www.globaltrade.net']
    start_urls = ['https://www.globaltrade.net/United-States/expert-service-provider.html?pageSize=10&orderBy=1&filterByPost=false&filterByRef=false&topicClear=false&industryClear=false&currentPage=%s'  % page for page in range(1,3)]

    def parse(self, response):
        provider_url = response.xpath('//li[@class="sp-id"]/p[@class="sp-name"]/a[@class="profileNavigator"]/@href').extract()
        print(provider_url)
        pass
