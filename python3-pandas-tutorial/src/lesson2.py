'''
Created on May 15, 2017

Pandas Basics - p.2 Data Analysis with Python and Pandas Tutorial
based on https://www.youtube.com/watch?v=0UA49Ds1XXo&list=PLQVvvaa0QuDc-3szzjeP6N6b0aDrrKyL-&index=2

@author: ubuntu
'''
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

web_stats = {'Day':[1,2,3,4,5,6],
             'Visitors':[43,34,65,56,29,76],
             'Bounce Rate':[65,67,78,65,45,52]}

df = pd.DataFrame(web_stats)

#print(df.head())
#print(df.tail())
#print(df.tail(2))

df.set_index('Day', inplace=True)
#df = df.set_index('Day')
#print(df)

#print(df['Visitors'])
#print(df.Visitors)

#df['Visitors'].plot()
#plt.show()

#df.plot()
#plt.show()

print(df[['Visitors','Bounce Rate']])