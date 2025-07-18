import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans


iris = load_iris()
X = iris.data

K = 3


kmeans = KMeans(n_clusters=K, random_state=0)
labels = kmeans.fit_predict(X)
centroids = kmeans.cluster_centers_


print("K-means Labels:", labels)
print("K-means Centroids:", centroids)

plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', color='red', s=200)
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('K-means Clustering of Iris Dataset')
plt.show()