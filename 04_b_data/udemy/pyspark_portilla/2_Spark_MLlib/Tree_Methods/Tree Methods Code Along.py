
# coding: utf-8

# # Tree Methods Code Along
# 
# In this lecture we will code along with some data and test out 3 different tree methods:
# 
# * A single decision tree
# * A random forest
# * A gradient boosted tree classifier
#     
# We will be using a college dataset to try to classify colleges as Private or Public based off these features:
# 
#     Private A factor with levels No and Yes indicating private or public university
#     Apps Number of applications received
#     Accept Number of applications accepted
#     Enroll Number of new students enrolled
#     Top10perc Pct. new students from top 10% of H.S. class
#     Top25perc Pct. new students from top 25% of H.S. class
#     F.Undergrad Number of fulltime undergraduates
#     P.Undergrad Number of parttime undergraduates
#     Outstate Out-of-state tuition
#     Room.Board Room and board costs
#     Books Estimated book costs
#     Personal Estimated personal spending
#     PhD Pct. of faculty with Ph.D.’s
#     Terminal Pct. of faculty with terminal degree
#     S.F.Ratio Student/faculty ratio
#     perc.alumni Pct. alumni who donate
#     Expend Instructional expenditure per student
#     Grad.Rate Graduation rate

# In[79]:


#Tree methods Example
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('treecode').getOrCreate()


# In[80]:


# Load training data
data = spark.read.csv('College.csv',inferSchema=True,header=True)


# In[81]:


data.printSchema()


# In[82]:


data.head()


# ### Spark Formatting of Data

# In[83]:


# A few things we need to do before Spark can accept the data!
# It needs to be in the form of two columns
# ("label","features")

# Import VectorAssembler and Vectors
from pyspark.ml.linalg import Vectors
from pyspark.ml.feature import VectorAssembler


# In[84]:


data.columns


# In[85]:


assembler = VectorAssembler(
  inputCols=['Apps',
             'Accept',
             'Enroll',
             'Top10perc',
             'Top25perc',
             'F_Undergrad',
             'P_Undergrad',
             'Outstate',
             'Room_Board',
             'Books',
             'Personal',
             'PhD',
             'Terminal',
             'S_F_Ratio',
             'perc_alumni',
             'Expend',
             'Grad_Rate'],
              outputCol="features")


# In[86]:


output = assembler.transform(data)


# Deal with Private column being "yes" or "no"

# In[87]:


from pyspark.ml.feature import StringIndexer


# In[88]:


indexer = StringIndexer(inputCol="Private", outputCol="PrivateIndex")
output_fixed = indexer.fit(output).transform(output)


# In[89]:


final_data = output_fixed.select("features",'PrivateIndex')


# In[90]:


train_data,test_data = final_data.randomSplit([0.7,0.3])


# ### The Classifiers

# In[91]:


from pyspark.ml.classification import DecisionTreeClassifier,GBTClassifier,RandomForestClassifier
from pyspark.ml import Pipeline


# Create all three models:

# In[116]:


# Use mostly defaults to make this comparison "fair"

dtc = DecisionTreeClassifier(labelCol='PrivateIndex',featuresCol='features')
rfc = RandomForestClassifier(labelCol='PrivateIndex',featuresCol='features')
gbt = GBTClassifier(labelCol='PrivateIndex',featuresCol='features')


# Train all three models:

# In[117]:


# Train the models (its three models, so it might take some time)
dtc_model = dtc.fit(train_data)
rfc_model = rfc.fit(train_data)
gbt_model = gbt.fit(train_data)


# ## Model Comparison
# 
# Let's compare each of these models!

# In[118]:


dtc_predictions = dtc_model.transform(test_data)
rfc_predictions = rfc_model.transform(test_data)
gbt_predictions = gbt_model.transform(test_data)


# **Evaluation Metrics:**

# In[119]:


from pyspark.ml.evaluation import MulticlassClassificationEvaluator


# In[120]:


# Select (prediction, true label) and compute test error
acc_evaluator = MulticlassClassificationEvaluator(labelCol="PrivateIndex", predictionCol="prediction", metricName="accuracy")


# In[121]:


dtc_acc = acc_evaluator.evaluate(dtc_predictions)
rfc_acc = acc_evaluator.evaluate(rfc_predictions)
gbt_acc = acc_evaluator.evaluate(gbt_predictions)


# In[122]:


print("Here are the results!")
print('-'*80)
print('A single decision tree had an accuracy of: {0:2.2f}%'.format(dtc_acc*100))
print('-'*80)
print('A random forest ensemble had an accuracy of: {0:2.2f}%'.format(rfc_acc*100))
print('-'*80)
print('A ensemble using GBT had an accuracy of: {0:2.2f}%'.format(gbt_acc*100))


# Interesting! Optional Assignment - play around with the parameters of each of these models, can you squeeze some more accuracy out of them? Or is the data the limiting factor?
