# -*- coding: utf-8 -*-
'''
Created on Nov 04, 2017

Following Pagination Links with Scrapy
based on https://www.youtube.com/watch?v=G9Nni6G-iOc&list=PLZyvi_9gamL-EE3zQJbU5N3nzJcfNeFHU&index=4

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

        # relative url
        next_page_url = response.css('li.next > a::attr(href)').extract_first()
        if next_page_url:
            # full url
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)