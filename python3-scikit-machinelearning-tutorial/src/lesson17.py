'''
Created on May 07, 2017

Scikit Learn Machine Learning Tutorial for investing with Python p. 17
based on https://www.youtube.com/watch?v=oRwPwTbrNuk&list=PLQVvvaa0QuDd0flgGphKCej-9jp-QdzZ3&index=17

Improving our Analysis with a more accurate measure of performance in relation to fundamentals

@author: ubuntu
'''
import pandas as pd
import os
import quandl as ql
import time
 
# locally stored file with credentials
from quandl_api_key import *

path = "/home/ubuntu/workspace/project/learning/python3-scikit-machinelearning-tutorial/src/intraQuarter"

def Stock_Prices():
    df = pd.DataFrame()

    statspath = path+'/_KeyStats'
    stock_list = [x[0] for x in os.walk(statspath)]

    print(stock_list)

    for each_dir in stock_list[1:]:
        try:
            data = each_dir.split("/")
            ticker = data[len(data) - 1]
            print(ticker)
            name = "WIKI/"+ticker.upper()
            data = ql.get(name,
                              trim_start = "2000-12-12",
                              trim_end = "2017-05-01",
                              authtoken=auth_token)
            
            data[ticker.upper()] = data["Adj. Close"]
            df = pd.concat([df, data[ticker.upper()]], axis = 1)

        except Exception as e:
            print(str(e))
            time.sleep(10)
            
            try:
                data = each_dir.split("/")
                ticker = data[len(data) - 1]
                print(ticker)
                name = "WIKI/"+ticker.upper()
                data = ql.get(name,
                                  trim_start = "2000-12-12",
                                  trim_end = "2017-05-01",
                                  authtoken=auth_token)
                data[ticker.upper()] = data["Adj. Close"]
                df = pd.concat([df, data[ticker.upper()]], axis = 1)

            except Exception as e:
                print(str(e))

    df.to_csv("stock_prices.csv")
                
Stock_Prices()