'''
Created on May 07, 2017

Scikit Learn Machine Learning Tutorial for investing with Python p. 16 
based on https://www.youtube.com/watch?v=zZs2UE-yEMo&index=16&list=PLQVvvaa0QuDd0flgGphKCej-9jp-QdzZ3

Using Quandl for more data

@author: ubuntu
'''
import pandas as pd
import os
import quandl as ql
import time

# locally stored file with credentials
from quandl_api_key import *

data = ql.get("WIKI/KO", trim_start = "2000-12-12", trim_end = "2017-05-01", authtoken=auth_token)

print(data)