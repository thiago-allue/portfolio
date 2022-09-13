
# coding: utf-8

# # Missing Data
# 
# Often data sources are incomplete, which means you will have missing data, you have 3 basic options
# for filling in missing data (you will personally have to make the decision for what is the right approach:
# 
# * Just keep the missing data points.
# * Drop them missing data points (including the entire row)
# * Fill them in with some other value.
# 
# Let's cover examples of each of these methods!

# ## Keeping the missing data
# A few machine learning algorithms can easily deal with missing data, let's see what it looks like:

from pyspark.sql import SparkSession
# May take a little while on a local computer
spark = SparkSession.builder.appName("missingdata").getOrCreate()


df = spark.read.csv("ContainsNull.csv",header=True,inferSchema=True)
df.show()


# Notice how the data remains as a null.

# ## Drop the missing data
# 
# You can use the .na functions for missing data. The drop command has the following parameters:
# 
#     df.na.drop(how='any', thresh=None, subset=None)
#     
#     * param how: 'any' or 'all'.
#     
#         If 'any', drop a row if it contains any nulls.
#         If 'all', drop a row only if all its values are null.
#     
#     * param thresh: int, default None
#     
#         at least 2 NON-null values
#         
#     * param subset: 
#         optional list of column names to consider.

# In[6]:


# Drop any row that contains missing data
df.na.drop().show()


# Has to have at least 2 NON-null values
df.na.drop(thresh=2).show()
df.na.drop(subset=["Sales"]).show()
df.na.drop(how='any').show()
df.na.drop(how='all').show()


# ## Fill the missing values with values

df.na.fill('NEW VALUE').show()
df.na.fill(0).show()


# Usually you should specify what columns you want to fill with the subset parameter
df.na.fill('No Name',subset=['Name']).show()


# A very common practice is to fill values with the mean value for the column, for example:

from pyspark.sql.functions import mean
mean_val = df.select(mean(df['Sales'])).collect()

# Spark has a weird nested formatting of Row object!
mean_val[0][0]


# In[24]:
mean_sales = mean_val[0][0]
df.na.fill(mean_sales, ["Sales"]).show()


# One (very ugly) one-liner
df.na.fill(df.select(mean(df['Sales'])).collect()[0][0],['Sales']).show()