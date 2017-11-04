# -*- coding: utf-8 -*-
'''
Created on Nov 04, 2017

Scraping Infinite Scrolling Pages
based on https://www.youtube.com/watch?v=EelmnSzykyI&list=PLZyvi_9gamL-EE3zQJbU5N3nzJcfNeFHU&index=6

@author: ubuntu
'''
import scrapy
import json

class QuotesScrollSpider(scrapy.Spider):
    name = 'quotes-scroll'
    api_url = 'http://quotes.toscrape.com/api/quotes?page={}'
    start_urls = [api_url.format(1)]

    def parse(self, response):
        data = json.loads(response.text)
        for quote in data['quotes']:
            yield {
                'author_name': quote['author']['name'],
                'text': quote['text'],
                'tags': quote['tags']
            }
        
        if data['has_next']:
            next_page = data['page'] + 1
            yield scrapy.Request(url=self.api_url.format(next_page), callback=self.parse)