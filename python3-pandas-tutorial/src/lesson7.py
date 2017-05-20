'''
Created on May 20, 2017

Pickling - p.7 Data Analysis with Python and Pandas Tutorial
based on https://www.youtube.com/watch?v=WkIW0YLoQEE&list=PLQVvvaa0QuDc-3szzjeP6N6b0aDrrKyL-&index=7

@author: ubuntu
'''
import quandl as qdl
import pandas as pd
import pickle as pkl
import os
# locally stored file with credentials
from quandl_api_key import *

file_name = 'fiddy_states.pickle'

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

def grab_initial_hpi_state_data():
    main_df = pd.DataFrame()
    for state in state_list():
        print(state)
        df = load_hpi_df(str(state))

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)
    
    with open(file_name,'wb') as pickle_out:
        pkl.dump(main_df, pickle_out)


print(get_hpi_data())