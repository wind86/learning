'''
Created on Apr 30, 2017

Scikit Learn Machine Learning Tutorial for investing with Python p. 6 
based on https://www.youtube.com/watch?v=cdaMWZIy5vA&index=6&list=PLQVvvaa0QuDd0flgGphKCej-9jp-QdzZ3

Structuring data with Pandas

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
        df = pd.DataFrame(columns = ['Date','Unix','Ticker','DE Ratio'])
        if len(each_file) > 0:
            for file in each_file:
                date_stamp = datetime.strptime(file, '%Y%m%d%H%M%S.html')
                unix_time = time.mktime(date_stamp.timetuple())
                full_file_path = each_dir+'/'+file
                source = open(full_file_path,'r').read()
                try:
                    value = source.split(gather+':</td><td class="yfnc_tabledata1">')[1].split('</td>')[0]
                    df = df.append({
                        'Date':date_stamp,
                        'Unix':unix_time,
                        'Ticker':ticker,
                        'DE Ratio': float(value),
                        }, ignore_index = True)
                except Exception as e:
                    pass
            
    save = gather.replace(' ','').replace(')','').replace('(','').replace('/','')+('.csv')
    print(save)
    df.to_csv(save)
    
Key_Stats()