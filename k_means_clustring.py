# -*- coding: utf-8 -*-
"""k_means_clustring.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YnmdGAHkmzl-kM6Pq0gVXDO9paEkXTvQ
"""

from google.colab import files
data=files.upload()

import pandas as pd
mall=pd.read_csv("Mall_Customers.csv")

mall.info()

mall.head()

x=mall[["Annual Income (k$)","Spending Score (1-100)"]]

import numpy as np

x=np.array(x)

x

x.dtype

res=np.array([[18,25],[25,65],[14,98],[65,26]])
res

from sklearn.cluster import KMeans

wcss=[]

for i in range(1,11):
  kmeans=KMeans(n_clusters=i,init='k-means++',random_state=42)
  kmeans.fit(x)
  wcss.append(kmeans.inertia_)

wcss

import matplotlib.pyplot as plt
import seaborn as sns

plt.plot(range(1,11),wcss)

kmeans=KMeans(n_clusters=5,init='k-means++',random_state=42)
y_means=kmeans.fit_predict(x)

y_means

x[y_means==1]

x[y_means==4,0],x[y_means==4,1]

plt.scatter(x[y_means==1,0],x[y_means==1,1],label="cluster1")
plt.scatter(x[y_means==2,0],x[y_means==2,1],label="cluster2")
plt.scatter(x[y_means==3,0],x[y_means==3,1],label="cluster3")
plt.scatter(x[y_means==4,0],x[y_means==4,1],label="cluster4")
plt.scatter(x[y_means==0,0],x[y_means==0,1],label="cluster0")
plt.legend()
plt.xlabel("Salary")
plt.ylabel("Expences")