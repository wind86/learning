'''
Created on May 08, 2017

Scikit Learn Machine Learning Tutorial for investing with Python p. 21
based on https://www.youtube.com/watch?v=ocgvXbv2iHs&index=21&list=PLQVvvaa0QuDd0flgGphKCej-9jp-QdzZ3

Pulling current data from Yahoo

@author: ubuntu
'''
import urllib.request
import os
import time

path = "/home/ubuntu/workspace/project/learning/python3-scikit-machinelearning-tutorial/src/intraQuarter"

def Check_Yahoo():
    statspath = path+"/_KeyStats"
    stock_list = [x[0] for x in os.walk(statspath)]

    for e in stock_list[1:]:
        try:
            e = e.replace("/home/ubuntu/workspace/project/learning/python3-scikit-machinelearning-tutorial/src/intraQuarter/_KeyStats/","")
            print("loading", e.upper())
            link = "https://finance.yahoo.com/quote/"+e.upper()+"/key-statistics"
            
            resp = urllib.request.urlopen(link).read()
 
            save = "forward/"+str(e)+".html"
            store = open(save,"w")
            store.write(str(resp))
            store.close()

        except Exception as e:
            print(str(e))
            time.sleep(2)

Check_Yahoo()
