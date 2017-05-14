'''
Created on May 14, 2017

Scikit Learn Machine Learning Tutorial for investing with Python p. 27
based on https://www.youtube.com/watch?v=ZS-IM9C3eFg&list=PLQVvvaa0QuDd0flgGphKCej-9jp-QdzZ3&index=27

Unsupervised Machine Learning: Flat Clustering
K-Means clusternig example with Python and Scikit-learn

@author: ubuntu
'''
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from sklearn.cluster import KMeans


# x = [1, 5, 1.5, 8, 1, 9]
# y = [2, 8, 1.8, 8, 0.6, 11]
# 
# plt.scatter(x,y)
# plt.show()

X = np.array([[1, 2],
              [5, 8],
              [1.5, 1.8],
              [8, 8],
              [1, 0.6],
              [9, 11]])

kmeans = KMeans(n_clusters=4)
kmeans.fit(X)

centroids = kmeans.cluster_centers_
labels = kmeans.labels_

print(centroids)
print(labels)

colors = ["g.","r.","c.","y."]

for i in range(len(X)):
    print("coordinate:",X[i], "label:", labels[i])
    plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize = 10)


plt.scatter(centroids[:, 0],centroids[:, 1], marker = "x", s=150, linewidths = 5, zorder = 10)

plt.show()