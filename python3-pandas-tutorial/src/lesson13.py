'''
Created on May 20, 2017

Joining 30 year mortgage rate - p.13 Data Analysis with Python and Pandas Tutorial
based on https://www.youtube.com/watch?v=FvamL5oA_EE&index=13&list=PLQVvvaa0QuDc-3szzjeP6N6b0aDrrKyL-

@author: ubuntu
'''
import quandl as qdl
import pandas as pd
import pickle as pkl
import os
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

# locally stored file with credentials
from quandl_api_key import *

file_name = 'fiddy_states.pickle'
percent_change_file_name = 'fiddy_states2.pickle'
percent_change_from_base_file_name = 'fiddy_states3.pickle'

def state_list():
    fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fiddy_states[0][0][1:]

def load_hpi_df(state):
    df = qdl.get("FMAC/HPI_" + state, authtoken = auth_token)
    df.columns = [state]
    return df

def get_hpi_data():
    if not os.path.isfile('./' + file_name):
        grab_initial_hpi_state_data()
    
    with open(file_name, 'rb') as pickle_in:
        return pkl.load(pickle_in)
    
def cache_hpi_data(data, filename):
    with open(filename,'wb') as pickle_out:
        pkl.dump(data, pickle_out)

def grab_hpi_data():
    main_df = pd.DataFrame()
    for state in state_list():
        print(state)
        df = load_hpi_df(str(state))

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)
    
    return main_df

def grab_initial_hpi_state_data():
    cache_hpi_data(grab_hpi_data(), file_name)

def grab_percent_change_hpi_state_data():
    main_df = pd.DataFrame()
    for df in grab_hpi_data():
        d = df.pct_change()

        if main_df.empty:
            main_df = d
        else:
            main_df = main_df.join(d)
    
    cache_hpi_data(main_df, percent_change_file_name)

def grab_percent_change_from_base_hpi_state_data():
    main_df = pd.DataFrame()
    for state in state_list():
        print(state)
        df = load_hpi_df(str(state))
        df[state] = (df[state] - df[state][0]) / df[state][0] * 100.0
        
        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)
    
    cache_hpi_data(main_df, percent_change_from_base_file_name)

def HPI_Benchmark():
    lbl = "Value"
    df = qdl.get("FMAC/HPI_USA", authtoken = auth_token)
    df[lbl] = (df[lbl] - df[lbl][0]) / df[lbl][0] * 100.0
    return df

def mortgage_30y():
    lbl = "Value"
    df = qdl.get("FMAC/MORTG", trim_start="1975-01-01", authtoken=auth_token)
    df[lbl] = (df[lbl] - df[lbl][0]) / df[lbl][0] * 100.0
    df=df.resample('1D')
    df=df.resample('M')
    #print(df.head())
    return df

#mortgage_30y()


HPI_data = pd.read_pickle(percent_change_from_base_file_name)
m30 = mortgage_30y()
HPI_Bench = HPI_Benchmark()
m30.columns=['M30']
HPI = HPI_Bench.join(m30)
#print(HPI.head())
#print(HPI.corr())

state_HPI_M30 = HPI_data.join(m30)
#print(state_HPI_M30.corr())
#print(state_HPI_M30.corr()['M30'])
print(state_HPI_M30.corr()['M30'].describe())