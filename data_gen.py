# creating a practice artificial dataset
# with supposedly 3 clear clusters
# for k-means clustering

import numpy as np
import random
import json
# import matplotlib.pyplot as plt

# three sets of manually crafted (x1, x2) coordinates
x1_1 = np.random.rand(25) * 2 + 1
x2_1 = np.random.rand(25) * 2.5 + 1.5
x1_2 = np.random.rand(25) * 1.5 + 2
x2_2 = np.random.rand(25) * 1.5 + 4
x1_3 = np.random.rand(25) - 1
x2_3 = np.random.rand(25) * 2 + 2

# plt.plot(x1_1, x2_1, "ro", x1_2, x2_2, "bo", x1_3, x2_3, "go")
# plt.show()

x1 = x1_1.tolist() + x1_2.tolist() + x1_3.tolist()
x2 = x2_1.tolist() + x2_2.tolist() + x2_3.tolist()

x_tuples = []
for i in range(len(x1)):
    x_tuples.append((x1[i], x2[i]))
random.shuffle(x_tuples)

x1, x2, X = 0, 0, []
for x1, x2 in x_tuples:
    X.append([x1, x2])

# X is the final data set
filename = "datapoints.json"
with open(filename, "w") as f:
    json.dump(X, f)
