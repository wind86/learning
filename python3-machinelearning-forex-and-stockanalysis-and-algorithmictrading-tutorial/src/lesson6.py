'''
Created on May 27, 2017

Pattern Finding and Storing: Machine Learning for Algorithmic Trading in Forex and Stocks Part 6 
based on https://www.youtube.com/watch?v=vEu9OvHj8QE&index=6&list=PLQVvvaa0QuDe6ZBtkCNWNUbdaBo2vA4RO

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

patternAr = []
performanceAr = []


def percentChange(startPoint,currentPoint):
    return ((currentPoint-startPoint)/startPoint)*100.00

def patternStorage():
    startTime = time.time()
    
    avgLine = ((bid+ask)/2)
    x = len(avgLine)-30
    y = 11
    currentStance = 'none'
    
    while y < x:
        pattern = []
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

        try:
            avgOutcome = reduce(lambda x, y: x + y, outcomeRange) / len(outcomeRange)
        except Exception as e:
            print(str(e))
            avgOutcome = 0

        futureOutcome = percentChange(currentPoint, avgOutcome)

        pattern.append(p1)
        pattern.append(p2)
        pattern.append(p3)
        pattern.append(p4)
        pattern.append(p5)
        pattern.append(p6)
        pattern.append(p7)
        pattern.append(p8)
        pattern.append(p9)
        pattern.append(p10)

        patternAr.append(pattern)
        performanceAr.append(futureOutcome)
        
        y+=1

    endTime = time.time()
    print(len(patternAr))
    print(len(performanceAr))
    print('Pattern storing took:', endTime-startTime)

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

patternStorage()