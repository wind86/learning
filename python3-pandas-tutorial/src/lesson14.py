'''
Created on May 20, 2017

Adding other economic indicators - p.14 Data Analysis with Python and Pandas Tutorial
based on https://www.youtube.com/watch?v=pxZy5jHID_A&list=PLQVvvaa0QuDc-3szzjeP6N6b0aDrrKyL-&index=14

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
    return df

#mortgage_30y()
def sp500_data():
    df = qdl.get("YAHOO/INDEX_GSPC", trim_start="1975-01-01", authtoken=auth_token)
    df["Adjusted Close"] = (df["Adjusted Close"]-df["Adjusted Close"][0]) / df["Adjusted Close"][0] * 100.0
    df = df.resample('M')#.mean()
    df.rename(columns={'Adjusted Close':'sp500'}, inplace=True)
    df = df["sp500"]
    return df

def gdp_data():
    df = qdl.get("BCB/4385", trim_start="1975-01-01", authtoken=auth_token)
    df["Value"] = (df["Value"]-df["Value"][0]) / df["Value"][0] * 100.0
    df = df.resample('M')
    df.rename(columns = {'Value':'GDP'}, inplace=True)
    df = df['GDP']
    return df

def us_unemployment():
    df = qdl.get("ECPI/JOB_G", trim_start="1975-01-01", authtoken=auth_token)
    df["Unemployment Rate"] = (df["Unemployment Rate"]-df["Unemployment Rate"][0]) / df["Unemployment Rate"][0] * 100.0
    df = df.resample('1D').resample('M')
    return df


HPI_data = pd.read_pickle(percent_change_file_name)
m30 = mortgage_30y()
sp500 = sp500_data()
gdp = gdp_data()
HPI_Bench = HPI_Benchmark()
unemployment = us_unemployment()
m30.columns=['M30']
HPI = HPI_data.join([
    HPI_Bench,
    m30,
    sp500,
    gdp,
    unemployment
    ])
HPI.dropna(inplace=True)
print(HPI.corr())

HPI.to_pickle('HPI.pickle')