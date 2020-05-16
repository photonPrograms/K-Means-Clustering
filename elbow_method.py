# plot cost function for different values of K
# to get the optimum K with elbow method

import numpy as np
import matplotlib.pyplot as plt

from kmeans import cluster

J = [] # list to hold the costs for various K

low, high = 1, 10 # bounds on K to analyze

for K in range(low, high):
    result = cluster(K)
    cost, length = 0, 0
    for i in range(K):
        cl = np.array(result[i])
        mu = np.mean(cl, axis = 0)
        cost += np.sum((cl - mu) ** 2)
        length += np.size(cl, axis = 0)
    J.append(cost / length)

plt.figure()
plt.style.use("seaborn")
plt.plot(range(low, high), J, "r--")
plt.show()
