'''
Created on Nov 03, 2017

Getting Started with Web Scraping using Scrapy
based on https://www.youtube.com/watch?v=vkA1cWN4DEc&list=PLZyvi_9gamL-EE3zQJbU5N3nzJcfNeFHU

@author: ubuntu
'''

# type in console 
# scrapy shell http://quotes.toscrape.com/random

# print(response.text)

# response.css('small.author')

# response.css('small.author').extract()

# response.css('small.author::text').extract()

# response.css('small.author::text')[0].extract()

# response.css('small.author::text').extract_first()

# response.css('span.text::text').extract_first()

# response.css('a.tag::text').extract()
