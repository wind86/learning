'''
Created on May 15, 2017

Data Analysis with Python and Pandas Tutorial Introduction
based on https://www.youtube.com/watch?v=Iqjy9UqKKuo&list=PLQVvvaa0QuDc-3szzjeP6N6b0aDrrKyL-&index=1

@author: ubuntu
'''
import pandas as pd
import datetime
import pandas.io.data as web

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2015, 8, 22)

df = web.DataReader("XOM", "yahoo", start, end)
#print(df)
print(df.head())

import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

df['High'].plot()
plt.legend()
plt.show()