# -*- coding: utf-8 -*-
'''
Created on Nov 04, 2017

Scraping JavaScript pages with Scrapy and Splash
based on https://www.youtube.com/watch?v=VvFC93vAB7U&index=8&list=PLZyvi_9gamL-EE3zQJbU5N3nzJcfNeFHU

@author: ubuntu
'''
import scrapy
from scrapy_splash import SplashRequest

class QuotesJSSpider(scrapy.Spider):
    name = 'quotes-js'
    
    def start_requests(self):
        yield SplashRequest(
                url='http://quotes.toscrape.com/js',
                callback=self.parse
            )
    
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'author': quote.css('small.author::text').extract_first(),
                'text': quote.css('span.text::text').extract_first(),
                'tags': quote.css('div.tags > a.tag::text').extract()
            }