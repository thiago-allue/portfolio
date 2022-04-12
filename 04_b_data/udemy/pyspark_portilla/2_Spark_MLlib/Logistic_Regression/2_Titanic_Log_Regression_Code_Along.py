
# coding: utf-8

# # Logistic Regression Code Along
# This is a code along of the famous titanic dataset, its always nice to start off with this dataset because it is an example you will find across pretty much every data analysis language.

# In[1]:


from pyspark.sql import SparkSession


# In[2]:


spark = SparkSession.builder.appName('myproj').getOrCreate()


# In[3]:


data = spark.read.csv('titanic.csv',inferSchema=True,header=True)


# In[4]:


data.printSchema()


# In[7]:


data.columns


# In[8]:


my_cols = data.select(['Survived',
 'Pclass',
 'Sex',
 'Age',
 'SibSp',
 'Parch',
 'Fare',
 'Embarked'])


# In[29]:


my_final_data = my_cols.na.drop()


# ### Working with Categorical Columns
# 
# Let's break this down into multiple steps to make it all clear.

# In[12]:


from pyspark.ml.feature import (VectorAssembler,VectorIndexer,
                                OneHotEncoder,StringIndexer)


# In[13]:


gender_indexer = StringIndexer(inputCol='Sex',outputCol='SexIndex')
gender_encoder = OneHotEncoder(inputCol='SexIndex',outputCol='SexVec')


# In[14]:


embark_indexer = StringIndexer(inputCol='Embarked',outputCol='EmbarkIndex')
embark_encoder = OneHotEncoder(inputCol='EmbarkIndex',outputCol='EmbarkVec')


# In[15]:


assembler = VectorAssembler(inputCols=['Pclass',
 'SexVec',
 'Age',
 'SibSp',
 'Parch',
 'Fare',
 'EmbarkVec'],outputCol='features')


# In[30]:


from pyspark.ml.classification import LogisticRegression


# ## Pipelines 
# 
# Let's see an example of how to use pipelines (we'll get a lot more practice with these later!)

# In[17]:


from pyspark.ml import Pipeline


# In[18]:


log_reg_titanic = LogisticRegression(featuresCol='features',labelCol='Survived')


# In[19]:


pipeline = Pipeline(stages=[gender_indexer,embark_indexer,
                           gender_encoder,embark_encoder,
                           assembler,log_reg_titanic])


# In[20]:


train_titanic_data, test_titanic_data = my_final_data.randomSplit([0.7,.3])


# In[21]:


fit_model = pipeline.fit(train_titanic_data)


# In[22]:


results = fit_model.transform(test_titanic_data)


# In[23]:


from pyspark.ml.evaluation import BinaryClassificationEvaluator


# In[24]:


my_eval = BinaryClassificationEvaluator(rawPredictionCol='prediction',
                                       labelCol='Survived')


# In[26]:


results.select('Survived','prediction').show()


# In[27]:


AUC = my_eval.evaluate(results)


# In[28]:


AUC


# ## Great Job!
