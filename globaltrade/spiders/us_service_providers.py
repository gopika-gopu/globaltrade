# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urljoin


class UsServiceProvidersSpider(scrapy.Spider):
    name = 'us_service_providers'
    allowed_domains = ['www.globaltrade.net']
    start_urls = ['https://www.globaltrade.net/United-States/expert-service-provider.html?pageSize=10&orderBy=1&filterByPost=false&filterByRef=false&topicClear=false&industryClear=false&currentPage=%s'  % page for page in range(1,3)]

    def parse(self, response):
        provider_urls = response.xpath('//li[@class="sp-id"]/p[@class="sp-name"]/a[@class="profileNavigator"]/@href').extract()
        for provider in provider_urls:
            new_page_url  = 'https://www.globaltrade.net' + provider
            url = urljoin(response.url, new_page_url)
            print(url)
        pass