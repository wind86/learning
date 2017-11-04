# -*- coding: utf-8 -*-
'''
Created on Nov 04, 2017

Scraping Details Pages from Listings
based on https://www.youtube.com/watch?v=JW_FxkSohkA&list=PLZyvi_9gamL-EE3zQJbU5N3nzJcfNeFHU&index=5

@author: ubuntu
'''
import scrapy


class AuthorsSpider(scrapy.Spider):
    name = 'authors'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        for url in response.css('div.quote > span > a::attr(href)').extract():
            yield scrapy.Request(url=response.urljoin(url), callback=self.parse_details)

        next_page_url = response.css('li.next > a::attr(href)').extract_first()
        if next_page_url:
            yield scrapy.Request(url=response.urljoin(next_page_url), callback=self.parse)
            
    def parse_details(self, response):
        yield {
            'name': response.css('h3.author-title::text').extract_first(),
            'birth_date': response.css('span.author-born-date::text').extract_first()
        }