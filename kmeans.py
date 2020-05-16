import json
import numpy as np
import random

def cluster(K):
    """
    the K means clustering algorithm
    K = the number of clusters
    returns list of datapoints seggregated into clusters
    """

    # loading the matrix of data points
    filename = "datapoints.json"
    with open(filename) as f:
        X = np.array(json.load(f))

    m = np.size(X, axis = 0) # number of datapoints

    # random initialization of mu
    # the array of centroids
    mu = np.zeros((K, 2))
    init_index = random.sample(range(m), K)
    j = 0
    for i in init_index:
        mu[j, :] = X[i, :].copy()
        j += 1
    
    NITER = 500 # number of passes for clustering
    dist, c = np.zeros(K), np.zeros(m)

    for i in range(NITER):
        for j in range(m):
            dist = np.sum((mu - X[j, :]) ** 2, axis = 1)
            c[j] = np.argmin(dist)

        for j in range(K):
            mu[j, :] = np.mean(X[np.where(c == j)], axis = 0)

    # datapoints seggregated into clusters
    result = []
    for i in range(K):
        result.append(X[np.where(c == i)].tolist())
    
    return result
