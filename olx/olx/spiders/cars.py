# -*- coding: utf-8 -*-
import scrapy


class CarsSpider(scrapy.Spider):
    name = 'cars'
    allowed_domains = ['pe.olx.com.br']
    start_urls = ['http://pe.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios/']

    def parse(self, response):
        items = response.xpath('//ul[@id="main-ad-list"]/li[contains(@class, "item") and not(contains(@class, "list_native"))]')
        for item in items:
            url = item.xpath('./a/@href').extract_first()
            yield scrapy.Request(
                url = url,
                callback=self.parse_details
            )
        next_page = response.xpath('//div[contains(@class, "module_pagination")]//a[contains(@rel, "next")]/@href').extract_first()
        if next_page:
            self.log('PROXIMA PAGINA: {}'.format(next_page))
            yield scrapy.Request(
                url = next_page,
                callback=self.parse
            )

    def parse_details(self,response):
        title = response.xpath('//title/text()').extract_first()
        year =  response.xpath("//span[contains(text(), 'Ano')]/following-sibling::a/text()").extract_first()
        ports = response.xpath("//span[contains(text(), 'Portas')]/following-sibling::span/text()").extract_first()
        yield {
            'title': title,
            'year' : year,
            'ports': ports
        }


#//div[contains(@class, "module_pagination")]//a[contains(@rel, 'next')]




