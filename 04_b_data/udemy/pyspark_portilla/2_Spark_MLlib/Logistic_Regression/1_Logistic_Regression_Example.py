
# coding: utf-8

# # Logistic Regression
# 
# Let's see an example of how to run a logistic regression with Python and Spark! This is documentation example, we will quickly run through this and then show a more realistic example, afterwards, you will have another consulting project!

# In[69]:


from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('logregdoc').getOrCreate()


# In[70]:


from pyspark.ml.classification import LogisticRegression


# In[86]:


# Load training data
training = spark.read.format("libsvm").load("sample_libsvm_data.txt")

lr = LogisticRegression()

# Fit the model
lrModel = lr.fit(training)

trainingSummary = lrModel.summary


# In[87]:


trainingSummary.predictions.show()


# In[73]:


# May change soon!
from pyspark.mllib.evaluation import MulticlassMetrics


# In[74]:


lrModel.evaluate(training)


# In[75]:


# Usually would do this on a separate test set!
predictionAndLabels = lrModel.evaluate(training)


# In[76]:


predictionAndLabels.predictions.show()


# In[77]:


predictionAndLabels = predictionAndLabels.predictions.select('label','prediction')


# In[78]:


predictionAndLabels.show()


# ## Evaluators
# 
# Evaluators will be a very important part of our pipline when working with Machine Learning, let's see some basics for Logistic Regression, useful links:
# 
# https://spark.apache.org/docs/latest/api/python/pyspark.ml.html#pyspark.ml.evaluation.BinaryClassificationEvaluator
# 
# https://spark.apache.org/docs/latest/api/python/pyspark.ml.html#pyspark.ml.evaluation.MulticlassClassificationEvaluator

# In[79]:


from pyspark.ml.evaluation import BinaryClassificationEvaluator,MulticlassClassificationEvaluator


# In[89]:


evaluator = BinaryClassificationEvaluator(rawPredictionCol='prediction', labelCol='label')


# In[83]:


# For multiclass
evaluator = MulticlassClassificationEvaluator(predictionCol='prediction', labelCol='label',
                                             metricName='accuracy')


# In[90]:


acc = evaluator.evaluate(predictionAndLabels)


# In[91]:


acc


# Okay let's move on see some more examples!
