'''
Created on Apr 30, 2017

Scikit Learn Machine Learning SVM Tutorial with Python p. 2 - Example 
based on https://www.youtube.com/watch?v=KTeVOb8gaD4&list=PLQVvvaa0QuDd0flgGphKCej-9jp-QdzZ3&index=2

Simple Support Vector Machine (SVM) example with character recognition

@author: ubuntu
'''
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm

digits = datasets.load_digits()

print(digits.data)
print(digits.target)

clf = svm.SVC(gamma=0.001, C=100)

x,y = digits.data[:-10], digits.target[:-10]
clf.fit(x,y)

print('Prediction', clf.predict(digits.data[-6]))

plt.imshow(digits.images[-6], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()