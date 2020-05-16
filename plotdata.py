# plot the data before and after classification
# for the special case of limited clusters and 2 features

import matplotlib.pyplot as plt
import json

plt.style.use("seaborn")

filename = "datapoints.json"
with open(filename) as f:
    unclustered = json.load(f)

# plotting unclustered data
x1, x2 = [], []
for i in range(len(unclustered)):
    x1.append(unclustered[i][0])
    x2.append(unclustered[i][1])

plt.subplot(121)
plt.scatter(x1, x2)

# plotting clustered data
filename = "results.json"
with open(filename) as f:
    clustered = json.load(f)

colors = ['r', 'g', 'b', 'c', 'y', 'm', 'w', 'k']
plt.subplot(122)

i = 0
for cluster in clustered:
    x1, x2 = [], []
    for j in range(len(cluster)):
        x1.append(cluster[j][0])
        x2.append(cluster[j][1])

    plt.scatter(x1, x2, color = colors[i])
    i+= 1

plt.show()
