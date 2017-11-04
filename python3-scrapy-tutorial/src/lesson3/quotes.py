# -*- coding: utf-8 -*-
'''
Created on Nov 04, 2017

Scraping Multiple Items from a Page 
based on https://www.youtube.com/watch?v=E6lOVwigsNA&list=PLZyvi_9gamL-EE3zQJbU5N3nzJcfNeFHU&index=3

@author: ubuntu
'''
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'author_name': quote.css('small.author::text').extract_first(),
                'text': quote.css('span.text::text').extract_first(),
                'tags': quote.css('a.tag::text').extract()
            }