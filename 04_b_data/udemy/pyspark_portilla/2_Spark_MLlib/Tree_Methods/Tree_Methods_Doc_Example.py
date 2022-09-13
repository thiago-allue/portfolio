
# coding: utf-8

# # Random Forest Example
# 
# This is just a quick walkthrough of the Documentation's Example of Random Forest:

# In[3]:


from pyspark.ml import Pipeline
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator


# In[4]:


from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('rf').getOrCreate()


# In[17]:


# Load and parse the data file, converting it to a DataFrame.
data = spark.read.format("libsvm").load("sample_libsvm_data.txt")


# In[18]:


data.show()


# In[19]:


data.head()


# In[21]:


# Split the data into training and test sets (30% held out for testing)
(trainingData, testData) = data.randomSplit([0.7, 0.3])


# In[22]:


trainingData.printSchema()


# In[23]:


# Train a RandomForest model.
rf = RandomForestClassifier(labelCol="label", featuresCol="features", numTrees=20)


# In[26]:


# Train model.  This also runs the indexers.
model = rf.fit(trainingData)


# In[29]:


# Make predictions.
predictions = model.transform(testData)


# In[30]:


predictions.printSchema()


# In[31]:


# Select example rows to display.
predictions.select("prediction", "label", "features").show(5)


# In[32]:


# Select (prediction, true label) and compute test error
evaluator = MulticlassClassificationEvaluator(labelCol="label", predictionCol="prediction", metricName="accuracy")


# In[33]:


accuracy = evaluator.evaluate(predictions)
print("Test Error = %g" % (1.0 - accuracy))


# In[37]:


# Not a very good example to show this!
model.featureImportances


# ## Gradient Boosted Trees
# 
# Gradient-boosted trees (GBTs) are a popular classification and regression method using ensembles of decision trees. More information about the spark.ml implementation can be found further in the section on [GBTs.](http://spark.apache.org/docs/latest/ml-classification-regression.html#gradient-boosted-trees-gbts). For more information on the algorithm itself, please see the [spark.mllib documentation on GBTs.](http://spark.apache.org/docs/latest/mllib-ensembles.html#gradient-boosted-trees-gbts)
# 
# Luckily Spark makes very easy to use, basically just an import switch:

# In[41]:


from pyspark.ml.classification import GBTClassifier

# Load and parse the data file, converting it to a DataFrame.
data = spark.read.format("libsvm").load("sample_libsvm_data.txt")


# Split the data into training and test sets (30% held out for testing)
(trainingData, testData) = data.randomSplit([0.7, 0.3])

# Train a GBT model.
gbt = GBTClassifier(labelCol="label", featuresCol="features", maxIter=10)

# Train model.  This also runs the indexers.
model = gbt.fit(trainingData)

# Make predictions.
predictions = model.transform(testData)

# Select example rows to display.
predictions.select("prediction", "label", "features").show(5)


# In[42]:


# Select (prediction, true label) and compute test error
evaluator = MulticlassClassificationEvaluator(labelCol="label", predictionCol="prediction", metricName="accuracy")
accuracy = evaluator.evaluate(predictions)
print("Test Error = %g" % (1.0 - accuracy))


# So this data isn't really realistic enough to really judge to effectiveness of GBT models, this data makes it seem like they are perfection, instead of just an improvement on normal Random Forests.

# Let's move on to a more realistic example!
