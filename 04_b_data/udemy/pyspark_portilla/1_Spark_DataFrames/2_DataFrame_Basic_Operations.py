
# coding: utf-8

# # Basic Operations
# 
# This lecture will cover some basic operations with Spark DataFrames.
# 
# We will play around with some stock data from Apple.

from pyspark.sql import SparkSession

# May take awhile locally
spark = SparkSession.builder.appName("Operations").getOrCreate()


# Let Spark know about the header and infer the Schema types!
df = spark.read.csv('appl_stock.csv',inferSchema=True,header=True)

df.printSchema()


# ## Filtering Data
# 
# A large part of working with DataFrames is the ability to quickly filter out data based on conditions. Spark
# DataFrames are built on top of the Spark SQL platform, which means that is you already know SQL, you can quickly
# and easily grab that data using SQL commands, or using the DataFram methods (which is what we focus on in this
# course).


# Using SQL
df.filter("Close < 500").show()  # Where Close is a column


# Using SQL with .select()
df.filter("Close < 500").select('Open').show()  # Where Open is a columns

# Using SQL with .select()
df.filter("Close<500").select(['Open','Close']).show()


# Using normal python comparison operators
df.filter(df["Close"] < 200).show()
df.filter( (df["Close"] < 200) & (df['Open'] > 200) ).show()

# Make sure to add in the parenthesis separating the statements!
df.filter( (df["Close"] < 200) | (df['Open'] > 200) ).show()


# Make sure to add in the parenthesis separating the statements!
df.filter( (df["Close"] < 200) & ~(df['Open'] < 200) ).show()


# In[46]:


df.filter(df["Low"] == 197.16).show()


# Collecting results as Python objects
df.filter(df["Low"] == 197.16).collect()


result = df.filter(df["Low"] == 197.16).collect()


# In[62]:


# Note the nested structure returns a nested row object
type(result[0])


# In[65]:


row = result[0]


# Rows can be called to turn into dictionaries

# In[64]:


row.asDict()


# In[59]:


for item in result[0]:
    print(item)


# That is all for now Great Job!
