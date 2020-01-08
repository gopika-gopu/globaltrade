# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urljoin
from w3lib.html import remove_tags

class UsServiceProvidersSpider(scrapy.Spider):
    name = 'us_service_providers'
    allowed_domains = ['www.globaltrade.net']
    start_urls = ['https://www.globaltrade.net/United-States/expert-service-provider.html?pageSize=10&orderBy=1&filterByPost=false&filterByRef=false&topicClear=false&industryClear=false&currentPage=%s'  % page for page in range(1,413)]
    custom_settings = {
        'FEED_URI' : 'json/globaltrade_us.json',
        'FEED_FORMAT': 'json'
    }

    def parse(self, response):
        provider_urls = response.xpath('//li[@class="sp-id"]/p[@class="sp-name"]/a[@class="profileNavigator"]/@href').extract()
        for provider in provider_urls:
            new_page_url  = 'https://www.globaltrade.net' + provider
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'}
            url = urljoin(response.url, new_page_url)
            yield scrapy.Request(url,headers=headers, callback=self.parse_details)

    def parse_details(self, response):
        logo = response.css('div.image img::attr(data-original)').get()
        title = response.css('h1.sp-title span::text').get()
        sub_title = response.css('h1.sp-title span::text').get()
        primary_location = response.css('.profile-details [itemprop=addressLocality]::text').get()
        primary_location = primary_location.replace("\n", " ").replace("  ", " ").strip() if primary_location != None else None
        area_of_expertise = response.css('a.mainExp').get()
        area_of_expertise = remove_tags(area_of_expertise) if area_of_expertise != None else None
        about = None
        website = None
        languages_spoken = None
        page_url = response.request.url

        for overview in response.css('div.profile-content div.details tr'):
            if(overview.css('td:nth-child(1)::text').get() == "About:"):
                about = remove_tags(overview.css('td:nth-child(2)').get()).replace("\n", " ").replace("  ", " ").strip()
            if(overview.css('td:nth-child(1)::text').get() == "Website:"):
                website = remove_tags(overview.css('td:nth-child(2)').get()).replace("\n", " ").replace("  ", " ").strip()
            if(overview.css('td:nth-child(1)::text').get() == "Languages spoken:"):
                languages_spoken = remove_tags(overview.css('td:nth-child(2)').get()).replace("\n", " ").replace("  ", " ").strip()

        scraped_info = {
            'logo_url':logo,
            'title':title,
            'sub_title':sub_title,
            'primary_location':primary_location,
            'area_of_expertise':area_of_expertise,
            'about':about,
            'website':website,
            'languages_spoken':languages_spoken, 
            'page_url':page_url
        }
        yield scraped_info 