# record the results of k-means clustering
# using the optimum value of K as obtained by elbow method

import json
from kmeans import cluster

# user inputs K after assessing the elbow plot
K = int(input())
results = cluster(K)

filename = "results.json"
with open(filename, "w") as f:
    json.dump(results, f) # store clustering results
