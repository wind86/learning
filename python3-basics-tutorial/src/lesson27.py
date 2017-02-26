'''
Created on Jan 22, 2017

@author: ubuntu
'''
import csv

with open('example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    #print(readCSV)
    
    #for row in readCSV:
    #    print(row)
    
    dates = []
    colors = []
    
    for row in readCSV:
        dates.append(row[0])
        colors.append(row[3])
        
    print(dates)
    print(colors)
    
    whatColor = input('what color to find? ')
    coldex = colors.index(whatColor.lower())
    print(whatColor, dates[coldex])