'''
Created on May 21, 2017

Monte Carlo Simulation and Python 18 - 2D charting monte carlo variables 
based on https://www.youtube.com/watch?v=p3WLN1-SohU&list=PLQVvvaa0QuDdhOnp-FnVStDsALpYk2hk0&index=18

@author: ubuntu
'''
import matplotlib
import matplotlib.pyplot as plt
import csv

def graph():
    with open('monteCarlo.csv','r') as montecarlo:
        datas = csv.reader(montecarlo, delimiter=',')
        for eachLine in datas:
            percentROI = float(eachLine[0])
            wagerSizePercent = float(eachLine[1])
            wagerCount = float(eachLine[2])
            pcolor = eachLine[3]

            plt.scatter(wagerSizePercent,wagerCount,color=pcolor)

    plt.show()

graph()