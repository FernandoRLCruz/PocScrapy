# -*- coding: utf-8 -*-
import scrapy


class CourseraSpider(scrapy.Spider):
    name = 'coursera'
    
    category = None

    def start_requests(self):
        if self.category is None:
            yield scrapy.Request(
                url = 'https://pt.coursera.org/browse/computer-science',
                callback = self.parse
            )
        else:
            yield scrapy.Request(
                url = 'https://pt.coursera.org/browse/%s' % self.category,
                callback = self.parse
            )


    def parse(self, response):
        self.log(self.category)
        categories = response.xpath('//a[contains(@class, "nostyle degree-card-anchor-link")]')
        for item in categories:
            item_url = item.xpath('./@href').extract_first()
            self.log('Category: %s' % item_url)
            yield scrapy.Request(
                url='https://pt.coursera.org%s' % item_url,
                callback=self.parse_category
            )

    def parse_category(self, response):
        self.log(response.xpath("//title/text()").extract_first())