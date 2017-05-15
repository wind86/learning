'''
Created on May 15, 2017

Building dataset - p.4 Data Analysis with Python and Pandas Tutorial 
based on https://www.youtube.com/watch?v=3GpvWlVinf0&index=4&list=PLQVvvaa0QuDc-3szzjeP6N6b0aDrrKyL-

@author: ubuntu
'''
import quandl as qdl
import pandas as pd

# locally stored file with credentials
from quandl_api_key import *

#df = qdl.get("FMAC/HPI_TX", authtoken=auth_token)
#print(df.head())

fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
#print(fiddy_states)
#print(fiddy_states[0])

for abbv in fiddy_states[0][0][1:]:
    #print(abbv)
    print("FMAC/HPI_"+str(abbv))