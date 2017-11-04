'''
Created on May 22, 2017

Quick look at our Data: Machine learning for Stocks and Forex Technical Analysis 
based on https://www.youtube.com/watch?v=cExOVprMlQg&index=2&list=PLQVvvaa0QuDe6ZBtkCNWNUbdaBo2vA4RO

@author: ubuntu
'''
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import numpy as np
from matplotlib import style
style.use("ggplot")

def graphRawFx(): 
    date,bid,ask = np.loadtxt('./GBPUSD/GBPUSD1d.txt', unpack=True, delimiter=',', converters={0:mdates.bytespdate2num('%Y%m%d%H%M%S')}) 
    
    fig = plt.figure(figsize=(10,7)) 
    ax1= plt.subplot2grid((40,40), (0,0), rowspan=40, colspan=40) 
    ax1.plot(date,bid) 
    ax1.plot(date,ask) 
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%y-%m-%d %H:%M:%S')) 
    plt.grid(True) 
    plt.show() 

graphRawFx()