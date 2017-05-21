'''
Created on May 21, 2017

Monte Carlo Simulation and Python 
based on https://www.youtube.com/watch?v=uY3ZHfnFjJc&list=PLQVvvaa0QuDdhOnp-FnVStDsALpYk2hk0&index=19

@author: ubuntu
'''
import matplotlib
import matplotlib.pyplot as plt
import csv
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

def graph():
    with open('monteCarlo.csv','r') as montecarlo:
        datas = csv.reader(montecarlo, delimiter=',')
        for eachLine in datas:
            percentROI = float(eachLine[0])
            wagerSizePercent = float(eachLine[1])
            wagerCount = float(eachLine[2])
            pcolor = eachLine[3]

            ax.scatter(wagerSizePercent,wagerCount,percentROI,color=pcolor)

            ax.set_xlabel('wager percent size')
            ax.set_ylabel('wager count')
            ax.set_zlabel('percent ROI')

    plt.show()

graph()