
# coding: utf-8

# # GroupBy and Aggregate Functions
# 
# Let's learn how to use GroupBy and Aggregate methods on a DataFrame. GroupBy allows you to group rows together
# based off some column value, for example, you could group together sales data by the day the sale occured,
# or group repeast customer data based off the name of the customer. Once you've performed the GroupBy operation you
# can use an aggregate function off that data. An aggregate function aggregates multiple rows of data into a single
# output, such as taking the sum of inputs, or counting the number of inputs.


from pyspark.sql import SparkSession

# May take a little while on a local computer
spark = SparkSession.builder.appName("groupbyagg").getOrCreate()


# Read in the customer sales data
df = spark.read.csv('sales_info.csv',inferSchema=True,header=True)
df.printSchema()
df.show()


# Let's group together by company!
df.groupBy("Company")


# This returns a GroupedData object, off of which you can all various methods
# Mean
df.groupBy("Company").mean().show()


# Count
df.groupBy("Company").count().show()


# Max
df.groupBy("Company").max().show()


# Min
df.groupBy("Company").min().show()

# Sum
df.groupBy("Company").sum().show()


# Check out this link for more info on other methods:
# http://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark-sql-module
# 
# Not all methods need a groupby call, instead you can just call the generalized .agg() method,
# that will call the aggregate across all rows in the dataframe column specified. It can take
# in arguments as a single column, or create multiple aggregate calls all at once using
# dictionary notation.
# 
# For example:

# Max sales across everything
df.agg({'Sales':'max'}).show()


# Could have done this on the group by object as well:
grouped = df.groupBy("Company")


grouped.agg({"Sales":'max'}).show()


# ## Functions
# There are a variety of functions you can import from pyspark.sql.functions.
# Check out the documentation for the full list available:
# http://spark.apache.org/docs/latest/api/python/pyspark.sql.html#module-pyspark.sql.functions


from pyspark.sql.functions import countDistinct, avg,stddev

df.select(countDistinct("Sales")).show()


# Often you will want to change the name, use the .alias() method for this:
df.select(countDistinct("Sales").alias("Distinct Sales")).show()
df.select(avg('Sales')).show()


df.select(stddev("Sales")).show()


# That is a lot of precision for digits! Let's use the format_number to fix that!
from pyspark.sql.functions import format_number


sales_std = df.select(stddev("Sales").alias('std'))
sales_std.show()


# format_number("col_name",decimal places)
sales_std.select(format_number('std',2)).show()



# ## Order By
# 
# You can easily sort with the orderBy method:


# OrderBy
# Ascending
df.orderBy("Sales").show()


# Descending call off the column itself.
df.orderBy(df["Sales"].desc()).show()


# Most basic functions you would expect to be available are, so make sure to check out the documentation!
