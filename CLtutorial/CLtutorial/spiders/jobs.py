# -*- coding: utf-8 -*-
import scrapy

#run in terminal, navigate to project directory, cmd "scrapy crawl jobs -o file.csv"
class JobsSpider(scrapy.Spider):
    name = 'jobs'
    allowed_domains = ['craigslist.org']
    start_urls = ['https://newyork.craigslist.org/d/software-qa-dba-etc/search/sof/']

    def parse(self, response):
        titles = response.xpath('//a[@class="result-title hdrlnk"]/text()').extract()

        for title in titles:
            yield {'Title': title}
    pass
