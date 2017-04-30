'''
Created on Apr 30, 2017

Scikit Learn Machine Learning Tutorial for investing with Python p. 5 
based on https://www.youtube.com/watch?v=2vQfMAEu670&index=5&list=PLQVvvaa0QuDd0flgGphKCej-9jp-QdzZ3

More Parsing

@author: ubuntu
'''
import pandas as pd
import os
import time
from datetime import datetime

path = "/home/ubuntu/workspace/project/learning/python3-scikit-machinelearning-tutorial/src/intraQuarter"

def Key_Stats(gather="Total Debt/Equity (mrq)"):
    statspath = path+'/_KeyStats'
    stock_list = [x[0] for x in os.walk(statspath)]

    for each_dir in stock_list[1:]:
        each_file = os.listdir(each_dir)
        data = each_dir.split("/")
        ticker = data[len(data) - 1]
        if len(each_file) > 0:
            for file in each_file:
                date_stamp = datetime.strptime(file, '%Y%m%d%H%M%S.html')
                unix_time = time.mktime(date_stamp.timetuple())
                #print(date_stamp, unix_time)
                full_file_path = each_dir+'/'+file
                print(full_file_path)
                source = open(full_file_path,'r').read()
                #print(source)
                value = source.split(gather+':</td><td class="yfnc_tabledata1">')[1].split('</td>')[0]
                print(ticker+":",value)
            
            time.sleep(15)
Key_Stats()