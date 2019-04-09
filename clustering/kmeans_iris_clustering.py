#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import numpy as np
import math

from sklearn.datasets import make_moons, make_circles, make_blobs
from sklearn.datasets import make_gaussian_quantiles

from sklearn.cluster import KMeans, DBSCAN, SpectralClustering, AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage

import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

from sklearn.datasets import load_iris


# setting up iris data

fp = pd.read_csv('iris.csv')
fp = fp.drop(['id'], axis=1)
iris_arr = np.array(fp.iloc[:,:-1])


# # Kmeans Clustering

# returns list of pairs of k and its ssd
def find_opt_k(data):
    k_list = range(1,10)
    ssd = [KMeans(n_clusters=i, random_state=None, max_iter=1000).fit(arr).inertia_ for i in k_list]
    plt.plot(k_list, ssd, 'X-')
    plt.xlabel('k')
    plt.ylabel('Sum_of_squared_distances')
    plt.title('Elbow Method For Optimal k')
    return [i for i in zip(k_list, ssd)]


find_opt_k(iris_arr)


def sse_funct(points, centroid):
    d = 0
    for point in points:
        n = len(point)
        d += sum(math.pow(point[i] - centroid[i], 2) for i in range(n))
    return d

def kmeans_funct(k, data):
    km = KMeans(n_clusters=k, random_state=None).fit(data)
    return km.cluster_centers_, km.labels_, km.inertia_

# returns amount of clusters made and the sum squared error of every point from its cluster center
def bisecting_kmeans(k, data):
    clusters = [data] # list of clusters with cluster of all pts
    all_sse = [0]
    final_centers = [[0]] # list of their centers
    
    while len(clusters[:]) < k:
        idx = all_sse.index(max(all_sse))
        all_sse.pop(idx)
        cluster = clusters.pop(idx)
        center = final_centers.pop(idx)

        # pick lowest SSE bisection
        low_sse = float('inf')
        opt_labels = []
        for i in range(1000):
            centers, labels, inertia = kmeans_funct(2, cluster)
            if inertia < low_sse:
                low_sse = inertia
                opt_labels = labels
                center = centers 
        
        # separate out data points into their 2-means clusters
        cluster1, cluster2 = [], []
        for i, point in enumerate(cluster):
            if opt_labels[i] == 0:
                cluster1.append(point)
            else:
                cluster2.append(point)
        
        # add the two clusters (and their centers) to the list
        clusters.append(cluster1)
        clusters.append(cluster2)
        final_centers.append(center[0])
        final_centers.append(center[1])
        all_sse.append(sse_funct(cluster1, center[0]))
        all_sse.append(sse_funct(cluster2, center[1]))
        
    return len(clusters), sum(sse_funct(points, center) for points,center in zip(clusters, final_centers))


bisecting_kmeans(3, iris_arr)
bisecting_kmeans(4, iris_arr)
bisecting_kmeans(2, iris_arr)


