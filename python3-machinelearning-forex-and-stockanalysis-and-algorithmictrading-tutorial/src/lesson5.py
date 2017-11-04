'''
Created on May 27, 2017

Finding Patterns: Machine Learning for Automated Trading in Forex and Stocks Part 5 
based on https://www.youtube.com/watch?v=Yf-P9w36Q1s&list=PLQVvvaa0QuDe6ZBtkCNWNUbdaBo2vA4RO&index=5

@author: ubuntu
'''
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import numpy as np
from functools import reduce 
import time
from matplotlib import style
style.use("ggplot")

date,bid,ask = np.loadtxt('./GBPUSD/GBPUSD1d.txt', unpack=True, delimiter=',', converters={0:mdates.bytespdate2num('%Y%m%d%H%M%S')})

def percentChange(startPoint,currentPoint):
    return ((currentPoint-startPoint)/startPoint)*100.00

def patternFinder():
    avgLine = ((bid+ask)/2)
    x = len(avgLine)-30
    y = 11

    currentStance = 'none'
    while y < x:
        p1 = percentChange(avgLine[y-10], avgLine[y-9])
        p2 = percentChange(avgLine[y-10], avgLine[y-8])
        p3 = percentChange(avgLine[y-10], avgLine[y-7])
        p4 = percentChange(avgLine[y-10], avgLine[y-6])
        p5 = percentChange(avgLine[y-10], avgLine[y-5])
        p6 = percentChange(avgLine[y-10], avgLine[y-4])
        p7 = percentChange(avgLine[y-10], avgLine[y-3])
        p8 = percentChange(avgLine[y-10], avgLine[y-2])
        p9 = percentChange(avgLine[y-10], avgLine[y-1])
        p10= percentChange(avgLine[y-10], avgLine[y])

        outcomeRange = avgLine[y+20:y+30]
        currentPoint = avgLine[y]

        print(reduce(lambda x, y: x + y, outcomeRange) / len(outcomeRange))

        print(currentPoint)
        print('_______')
        print(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10)
        time.sleep(55)

        y+=1

def graphRawFx(): 
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

#graphRawFx()

patternFinder()