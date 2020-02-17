# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CoursesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    headline = scrapy.Field()
    url = scrapy.Field()
    instructors = scrapy.Field()
    lectures = scrapy.Field()
    image = scrapy.Field()


""" item['title'] = response.xpath('(//h2)[1]').extract_first()
item['headline'] = response.xpath('//div[contains(@class,"textoBanner")]//p[contains(@class, "mt-0 mb-0")]').extract_first() """