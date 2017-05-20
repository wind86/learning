'''
Created on May 20, 2017

Rolling statistics - p.11 Data Analysis with Python and Pandas Tutorial
based on https://www.youtube.com/watch?v=FRzfD1FtrsQ&index=11&list=PLQVvvaa0QuDc-3szzjeP6N6b0aDrrKyL-

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

#HPI_data = get_hpi_data()
#HPI_data['TX2'] = HPI_data['TX'] * 2
#print(HPI_data[['TX','TX2']].head())

#HPI_data.plot()
#plt.legend().remove()
#plt.show()
#----------------------------

#grab_percent_change_hpi_state_data()
#HPI_data = pd.read_pickle(percent_change_file_name)

#HPI_data.plot()
#plt.legend().remove()
#plt.show()
#----------------------------
# grab_percent_change_from_base_hpi_state_data();
# HPI_data = pd.read_pickle(percent_change_from_base_file_name)
# 
# HPI_data.plot()
# plt.legend().remove()
# plt.show()

def HPI_Benchmark():
    lbl = "Value"
    df = qdl.get("FMAC/HPI_USA", authtoken = auth_token)
    df[lbl] = (df[lbl] - df[lbl][0]) / df[lbl][0] * 100.0
    return df

# fig = plt.figure()
# ax1 = plt.subplot2grid((2,1), (0,0))
# ax2 = plt.subplot2grid((2,1), (1,0), sharex=ax1)
# HPI_data = pd.read_pickle(percent_change_from_base_file_name)
# HPI_data['TX12MA'] = pd.rolling_mean(HPI_data['TX'], 12)
# HPI_data['TX12STD'] = pd.rolling_std(HPI_data['TX'], 12)
# 
# HPI_data['TX'].plot(ax=ax1)
# HPI_data['TX12MA'].plot(ax=ax1)
# HPI_data['TX12STD'].plot(ax=ax2)
# 
# plt.show()

fig = plt.figure()
ax1 = plt.subplot2grid((2,1), (0,0))
ax2 = plt.subplot2grid((2,1), (1,0), sharex=ax1)
HPI_data = pd.read_pickle(percent_change_from_base_file_name)

TX_AK_12corr = pd.rolling_corr(HPI_data['TX'], HPI_data['AK'], 12)

HPI_data['TX'].plot(ax=ax1, label="TX HPI")
HPI_data['AK'].plot(ax=ax1, label="AK HPI")
HPI_data.dropna(inplace=True)
ax1.legend(loc=4)

TX_AK_12corr.plot(ax=ax2)

plt.show()
