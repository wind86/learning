'''
Created on May 20, 2017

Rolling Apply and Mapping Functions - p.15 Data Analysis with Python and Pandas Tutorial
based on https://www.youtube.com/watch?v=uLqmM6ExPvo&index=15&list=PLQVvvaa0QuDc-3szzjeP6N6b0aDrrKyL-

@author: ubuntu
'''
import quandl as qdl
import pandas as pd
import pickle as pkl
import numpy as np
import os
from statistics import mean
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

# locally stored file with credentials
from quandl_api_key import *

housing_data = pd.read_pickle('HPI.pickle')
housing_data = housing_data.pct_change()

housing_data.replace([np.inf, -np.inf], np.nan, inplace=True)
housing_data['US_HPI_future'] = housing_data['Value'].shift(-1)
housing_data.dropna(inplace=True)

def create_labels(cur_hpi, fut_hpi):
    if fut_hpi > cur_hpi:
        return 1
    else:
        return 0

def moving_average(values):
    return mean(values)

housing_data['label'] = list(map(create_labels,housing_data['Value'], housing_data['US_HPI_future']))
print(housing_data.head())

housing_data['ma_apply_example'] = pd.rolling_apply(housing_data['M30'], 10, moving_average)
print(housing_data.tail())