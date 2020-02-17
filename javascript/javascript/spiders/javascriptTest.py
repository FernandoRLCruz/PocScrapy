# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class JavascripttestSpider(CrawlSpider):
    name = 'javascriptTest'
    allowed_domains = ['https://www.w3schools.com']
    start_urls = ['https://www.w3schools.com/js/tryit.asp?filename=tryjs_myfirst']
    rules = (   
        Rule(
            LinkExtractor(allow='/js/tryit.asp?filename=tryjs_myfirst')
        ),     
        Rule(
            LinkExtractor(
                allow='/js/tryit.asp?filename=tryjs_myfirst/',
            ), process_request='splash_request'
        )
    )
        
        
    

def splash_request(self, request):
    return SplashRequest(
        url = request.url,
        callback=self.parse_details,
        args={'wait': 2}
    )

def parse_details(self, response):
    self.log(teste)