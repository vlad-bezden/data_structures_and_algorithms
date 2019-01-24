"""Simple K-Mean example of unsupervised machine learning algorithm"""

import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

original_set = -2 * np.random.rand(100, 2)
second_set = 1 + 2 * np.random.rand(50, 2)
original_set[50:100, :] = second_set

kmean = KMeans(n_clusters=2)
kmean.fit(original_set)

print(kmean.cluster_centers_)
print(kmean.labels_)

# chart points of each group
# index = kmean.labels_ == i is a nifty way by which we select all points that
# correspond to group i.
# When i=0, all points belonging to group zero are returned to the variable index.
for i in set(kmean.labels_):
    index = kmean.labels_ == i
    plt.plot(original_set[index, 0], original_set[index, 1], "o")

# plot centoids or mean values around which the clusters haveformed
plt.plot(kmean.cluster_centers_[0][0], kmean.cluster_centers_[0][1], "*", c="r", ms=10)
plt.plot(kmean.cluster_centers_[1][0], kmean.cluster_centers_[1][1], "*", c="r", ms=10)
plt.show()

# prediction:
sample = np.array([[-1.4, -14.0]])
print(f"Predict: {kmean.predict(sample)}")
another_sample = np.array([[2.5, 2.5]])
print(f"Predict: {kmean.predict(another_sample)}")
