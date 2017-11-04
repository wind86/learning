# -*- coding: utf-8 -*-
'''
Created on Nov 04, 2017

Submitting Forms in your Scrapy Spiders 
based on https://www.youtube.com/watch?v=Lo3aswJ7lzw&index=7&list=PLZyvi_9gamL-EE3zQJbU5N3nzJcfNeFHU

@author: ubuntu
'''
import scrapy
import json

class LoginSpider(scrapy.Spider):
    name = 'login-spider'
    login_url = 'http://quotes.toscrape.com/login'
    start_urls = [login_url]

    def parse(self, response):
        token = response.css('input[name="csrf_token"]::attr(value)').extract_first()
        data = {
            'csrf_token': token,
            'username': 'abc',
            'password': 'abc',
        }
        yield scrapy.FormRequest(url = self.login_url, formdata = data, callback = self.parse_quotes)

    def parse_quotes(self, response):
        for quote in response.css('div.quote'):
            yield {
                'author_name': quote.css('small.author::text').extract_first(),
                'author_url':  quote.css('small.author ~ a[href*="goodreads.com"]::attr(href)').extract_first()
            }