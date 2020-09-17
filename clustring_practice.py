# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 19:30:36 2020

@author: madha
"""


import pandas as pd
import numpy as np
import random as rd
import matplotlib.pyplot as plt
from pydataset import data
import seaborn as sns
df = data('iris')
df.head()

df1= df.select_dtypes(exclude=['object'])
df1.head()

from sklearn.preprocessing import StandardScaler
scalar = StandardScaler()
df1_scaled = scalar.fit_transform(df1)

df1_scaled.describe() #it converts to different format
pd.DataFrame(df1_scaled).describe()


     
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3)  #hyper parameters

kmeans.fit(df1_scaled)
kmeans.inertia_  #sum of sq distances of samples to their centeroid
kmeans.cluster_centers_
kmeans.labels_
kmeans.n_iter_  #iterations to stabilise the clusters
kmeans.predict(df1_scaled)

clusterNos = kmeans.labels_
clusterNos
type(clusterNos)

df1.groupby([clusterNos]).mean()
pd.options.display.max_columns =None
df.groupby(['Species']).mean()

import scipy.cluster.hierarchy as shc
dend = shc.dendrogram(shc.linkage(data2_scaled, method='ward'))

plt.figure(figsize = (10,7))
plt.title("Dendrogram")
dend = shc.dendrogram(shc.linkage(data2_scaled, method='ward'))
plt.axhline(y=6, color='r', linestyle='--')
plt.show();

#another method for Hcluster from sklearn
from sklearn.cluster import AgglomerativeClustering
aggCluster = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='ward')
aggCluster.fit_predict(data2_scaled)
aggCluster
aggCluster.labels_

#compare
compare = pd.DataFrame({'kmCluster': kmeans.labels_, 'HCaggl': aggCluster.labels_, 'Diff': kmeans.labels_ - aggCluster.labels_})
compare
compare.Diff.sum()
compare.kmCluster.value_counts()
compare.HCaggl.value_counts()
