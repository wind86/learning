'''
Created on Apr 08, 2017

Headless Error Handling Python Tutorial
https://www.youtube.com/watch?v=7-2rNHi9EfU&list=PLQVvvaa0QuDfju7ADVp5W1GF9jVhjbX-_&index=23

@author: ubuntu
'''

import sys
import logging

def error_handling():
    return 'Error: {}. {}, line: {}'.format(sys.exc_info()[0],
                                         sys.exc_info()[1],
                                         sys.exc_info()[2].tb_lineno)
try:
    a+b
except:
    logging.error(error_handling())