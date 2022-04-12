# coding: utf-8

# # Spark DataFrame Basics

# Spark DataFrames are the workhouse and main way of working with Spark and Python post Spark 2.0. DataFrames act as powerful versions of tables, with rows and columns, easily handling large datasets. The shift to DataFrames provides many advantages:

# * A much simpler syntax
# * Ability to use SQL directly in the dataframe
# * Operations are automatically distributed across RDDs

# If you've used R or even the pandas library with Python you are probably already familiar with the concept of DataFrames. Spark DataFrame expand on a lot of these concepts, allowing you to transfer that knowledge easily by understanding the simple syntax of Spark DataFrames.


# Remember that the main advantage to using Spark DataFrames vs those other programs is that Spark can handle data across many RDDs, huge data sets that would never fit on a single computer. That comes at a slight cost of some "peculiar" syntax choices, but after this course you will feel very comfortable with all those topics!
# Let's get started!

# ## Creating a DataFrame

# First we need to start a SparkSession:
from pyspark.sql import SparkSession

# Then start the SparkSession

# May take a little while on a local computer
spark = SparkSession.builder.appName("Basics").getOrCreate()


# You will first need to get the data from a file (or connect to a large distributed file like HDFS, we'll talk about this later once we move to larger datasets on AWS EC2).

df = spark.read.json('people.json')


# #### Showing the data
# Note how data is missing!
df.show()

df.printSchema()

df.columns

df.describe()

# Some data types make it easier to infer schema (like tabular formats such as csv which we will show later). 

# However you often have to set the schema yourself if you aren't dealing with a .read method that doesn't have inferSchema() built-in.

# Spark has all the tools you need for this, it just requires a very specific structure:

# In[8]:


from pyspark.sql.types import StructField,StringType,IntegerType,StructType


# Next we need to create the list of Structure fields
# name: string, name of the field.
# dataType: :class:`DataType` of the field.
# nullable: boolean, whether the field can be null (None) or not.


data_schema = [StructField("age", IntegerType(), True),
               StructField("name", StringType(), True)]

final_struc = StructType(fields=data_schema)


df = spark.read.json('people.json', schema=final_struc)


# ### Grabbing the data
# Get a column
df['age']


# Get a dataframe with a single column
df.select('age')

# Get and return visually it
df.select('age').show()


# Returns list of Row objects
df.head(2)

df.select(['age', 'name'])
df.select(['age', 'name']).show()



### Creating new columns

# Adding 'newage' with a simple copy of 'age'
df.withColumn('newage',df['age']).show()
df.show()


# Simple Rename
df.withColumnRenamed('age','supernewage').show()


# More complicated operations to create new columns

# Multiplying
df.withColumn('doubleage', df['age']*2).show()

# Summing
df.withColumn('add_one_age', df['age']+1).show()

# Dividing
df.withColumn('half_age', df['age']/2).show()


# ### Using SQL


# To use SQL queries directly with the dataframe, you will need to register it to a temporary view:


# Register the DataFrame as a SQL temporary view
df.createOrReplaceTempView("people")


# In[29]:
sql_results = spark.sql("SELECT * FROM people WHERE age=30").show()
sql_results
sql_results.show()


# It's not the  focus of the course, but it is there!

