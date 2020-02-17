# -*- coding: utf-8 -*-
import scrapy


class UdacitySpider(scrapy.Spider):
    name = 'udacity'
    start_urls = ['https://www.udacity.com/courses/all/']

    def parse(self, response):
        divs = response.xpath('//*[@class="card__inner card mb-0"]')
        for div in divs:
            link = div.xpath('.//h3/a')
            href = link.xpath('./@href').extract_first()
            yield scrapy.Request(
                url= 'https://www.udacity.com%s' % href,
                callback=self.parse_detail
            )


    def parse_detail(self, response):
        instructor = []
        title = response.xpath('//title/text()').extract_first()
        headline = response.xpath('//p[contains(@class, "legible center hidden-xs-down ng-star-inserted")]/text()').extract_first()
        image = response.xpath('(//div[contains(@style, "background-image")])[2]/@style').extract_first()
        for div in response.xpath('//div[contains(@class, "card ng-star-inserted")]'):
            instructor.append(
                {
                  'name': div.xpath('.//h5[contains(@class, "name")]/text()').extract_first(),
                  'image': div.xpath('//div[contains(@class, "card ng-star-inserted")]/img[contains(@class, "image")]/@src').extract_first()
                }   
            )
        yield{
            'title': title,
            'headline': headline,
            'image': image,
            'instructor': instructor
        }

#1 parte do spider udacity
# for div in divs:
#             link = div.xpath('.//h3/a')
#             title = link.xpath('./text()').extract_first()
#             href = link.xpath('./@href').extract_first()
#             image = div.xpath('.//div[contains(@class,"image-container ng-star-inserted")]/@style').extract_first()
#             description = div.xpath('.//h4[contains(@class, "category ng-star-inserted")]/text()').extract_first()
#             yield{
#                 'title': title,
#                 'url': href,
#                 'image': image,
#                 'description': description

#             }