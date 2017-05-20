'''
Created on May 20, 2017

Scikit Learn Incorporation - p.16 Data Analysis with Python and Pandas Tutorial
based on https://www.youtube.com/watch?v=t4319ffzRg0&list=PLQVvvaa0QuDc-3szzjeP6N6b0aDrrKyL-&index=16

@author: ubuntu
'''
import pandas as pd
#import pickle as pkl
import numpy as np
#import os
from statistics import mean
from sklearn import svm, preprocessing, cross_validation

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

housing_data['label'] = list(map(create_labels,housing_data['Value'], housing_data['US_HPI_future']))
print(housing_data.head())

X = np.array(housing_data.drop(['label','US_HPI_future'], 1))
X = preprocessing.scale(X)

y = np.array(housing_data['label'])
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)

clf = svm.SVC(kernel='linear')
clf.fit(X_train, y_train)

print(clf.score(X_test, y_test))
# 0.603773584906