'''
Created on Apr 30, 2017

Scikit Learn Machine Learning Tutorial with Python p. 7 
based on https://www.youtube.com/watch?v=PMAwBh0nrds&index=7&list=PLQVvvaa0QuDd0flgGphKCej-9jp-QdzZ3

Getting more data and meshing data sets

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

    for each_dir in stock_list[1:25]:
        each_file = os.listdir(each_dir)
        data = each_dir.split("/")
        ticker = data[len(data) - 1]
        df = pd.DataFrame(columns = ['Date','Unix','Ticker','DE Ratio','Price','SP500'])
        sp500_df = pd.DataFrame.from_csv('/home/ubuntu/workspace/project/learning/python3-scikit-machinelearning-tutorial/src/sp500.csv')
        if len(each_file) > 0:
            for file in each_file:
                date_stamp = datetime.strptime(file, '%Y%m%d%H%M%S.html')
                unix_time = time.mktime(date_stamp.timetuple())
                full_file_path = each_dir+'/'+file
                source = open(full_file_path,'r').read()
                try:
                    value = float(source.split(gather+':</td><td class="yfnc_tabledata1">')[1].split('</td>')[0])
                    
                    try:
                        sp500_date = datetime.fromtimestamp(unix_time).strftime('%Y-%m-%d')
                        row = sp500_df[(sp500_df.index == sp500_date)]
                        sp500_value = float(row["Adj Close"])
                    except:
                        # 259200 is 3 days in seconds
                        sp500_date = datetime.fromtimestamp(unix_time-259200).strftime('%Y-%m-%d')
                        row = sp500_df[(sp500_df.index == sp500_date)]
                        sp500_value = float(row["Adj Close"])
                    
                    stock_price = float(source.split('</small><big><b>')[1].split('</b></big>')[0])
                    #print("stock_price:",stock_price,"ticker:", ticker, "sp500:", sp500_value)
                    
                    df = df.append({
                        'Date':date_stamp,
                        'Unix':unix_time,
                        'Ticker':ticker,
                        'DE Ratio':value,
                        'Price':stock_price,
                        'SP500':sp500_value}, ignore_index = True)
                except Exception as e:
                    pass
            
    save = gather.replace(' ','').replace(')','').replace('(','').replace('/','')+('.csv')
    print(save)
    df.to_csv(save)
    

    
Key_Stats()