'''
Created on May 27, 2017

Percent Change: Machine Learning for Automated Trading in Forex and Stocks Part 4 
based on https://www.youtube.com/watch?v=fL4lGl5CoTM&list=PLQVvvaa0QuDe6ZBtkCNWNUbdaBo2vA4RO&index=4

@author: ubuntu
'''
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import numpy as np
from matplotlib import style
style.use("ggplot")

def percentChange(startPoint,currentPoint):
    return ((currentPoint-startPoint)/startPoint)*100.00

def graphRawFx(): 
    date,bid,ask = np.loadtxt('./GBPUSD/GBPUSD1d.txt', unpack=True, delimiter=',', converters={0:mdates.bytespdate2num('%Y%m%d%H%M%S')}) 
    
    fig=plt.figure(figsize=(10,7))

    ax1 = plt.subplot2grid((40,40), (0,0), rowspan=40, colspan=40)
    ax1.plot(date,bid)
    ax1.plot(date,ask)
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))

    plt.grid(True)
    for label in ax1.xaxis.get_ticklabels():
            label.set_rotation(45)
    plt.gca().get_yaxis().get_major_formatter().set_useOffset(False)

    ax1_2 = ax1.twinx()
    ax1_2.fill_between(date, 0, (ask-bid), facecolor='g',alpha=.3)
    plt.subplots_adjust(bottom=.23)
    
    plt.show()

graphRawFx()