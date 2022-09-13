
# coding: utf-8

# # Clustering Documentation Example
# 
# <h2 id="k-means">K-means</h2>
# 
# k-means is one of the
# most commonly used clustering algorithms that clusters the data points into a
# predefined number of clusters. The MLlib implementation includes a parallelized
# variant of the k-means++ method
# called kmeans||


#Cluster methods Example
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('cluster').getOrCreate()

from pyspark.ml.clustering import KMeans

# Loads data
dataset = spark.read.format("libsvm").load("sample_kmeans_data.txt")

# Trains a k-means model.
kmeans = KMeans().setK(2).setSeed(1)
model = kmeans.fit(dataset)

# Evaluate clustering by computing Within Set Sum of Squared Errors.
wssse = model.computeCost(dataset)
print("Within Set Sum of Squared Errors = " + str(wssse))

# Shows the result.
centers = model.clusterCenters()
print("Cluster Centers: ")
for center in centers:
    print(center)
