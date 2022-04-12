
# coding: utf-8

# # Dates and Timestamps
# 
# You will often find yourself working with Time and Date information,
# let's walk through some ways you can deal with it!

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("dates").getOrCreate()

df = spark.read.csv("appl_stock.csv", header=True, inferSchema=True)


# Let's walk through how to grab parts of the timestamp data
from pyspark.sql.functions import format_number, dayofmonth, hour, dayofyear, \
    month, year, weekofyear, date_format

# Extract day of month of timestamp
df.select(dayofmonth(df['Date'])).show()

# Extract (..) of timestamp
df.select(hour(df['Date'])).show()

# Extract (..) of timestamp
df.select(dayofyear(df['Date'])).show()

# Extract (..) of timestamp
df.select(month(df['Date'])).show()


# So for example, let's say we wanted to know the average closing price per year.
# Easy! With a groupby and the year() function call:

df.select(year(df['Date'])).show()


df.withColumn("Year",year(df['Date'])).show()


newdf = df.withColumn("Year",year(df['Date']))
newdf.groupBy("Year").mean()[['avg(Year)', 'avg(Close)']].show()


# Still not quite presentable! Let's use the .alias method as well as round() to clean this up!

result = newdf.groupBy("Year").mean()[['avg(Year)','avg(Close)']]
result = result.withColumnRenamed("avg(Year)", "Year")
result = result.select('Year',format_number('avg(Close)',2).alias("Mean Close")).show()



