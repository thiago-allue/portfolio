
# coding: utf-8

# # Linear Regression Example
# 
# Let's walk through the steps of the official documentation example.
# Doing this will help your ability to read from the documentation,
# understand it, and then apply it to your own problems (the upcoming
# Consulting Project).

# In[3]:


from pyspark.sql import SparkSession


spark = SparkSession.builder.appName('lr_example').getOrCreate()


from pyspark.ml.regression import LinearRegression

# Load training data
training = spark.read.format("libsvm").load("sample_linear_regression_data.txt")

# Interesting! We haven't seen libsvm formats before.
# In fact the aren't very popular when working with datasets in Python,
# but the Spark Documentation makes use of them a lot because of their formatting.
# Let's see what the training data looks like:

training.show()


# This is the format that Spark expects. Two columns with the names "label" and "features". 
# 
# The "label" column then needs to have the numerical label, either a regression numerical value,
# or a numerical value that matches to a classification grouping. Later on we will talk about
# unsupervised learning algorithms that by their nature do not use or require a label.

# These are the default values for the featuresCol, labelCol, predictionCol
lr = LinearRegression(featuresCol='features', labelCol='label', predictionCol='prediction')

# Fit the model
lrModel = lr.fit(training)

# Print the coefficients and intercept for linear regression
print("Coefficients: {}".format(str(lrModel.coefficients))) # For each feature...
print('\n')
print("Intercept:{}".format(str(lrModel.intercept)))

# Summarize the model over the training set and print out some metrics
trainingSummary = lrModel.summary


# Lots of info, here are a few examples:
trainingSummary.residuals.show()
print("RMSE: {}".format(trainingSummary.rootMeanSquaredError))
print("r2: {}".format(trainingSummary.r2))


# Spark DataFrames have an almost too convienent method of splitting the data! Let's see it:

all_data = spark.read.format("libsvm").load("sample_linear_regression_data.txt")

# Pass in the split between training/test as a list.
# No correct, but generally 70/30 or 60/40 splits are used. 
# Depending on how much data you have and how unbalanced it is.
train_data,test_data = all_data.randomSplit([0.7,0.3])


train_data.show()

test_data.show()

unlabeled_data = test_data.select('features')

unlabeled_data.show()

correct_model = lr.fit(train_data)


# Now we can directly get a .summary object using the evaluate method:
test_results = correct_model.evaluate(test_data)


test_results.residuals.show()
print("RMSE: {}".format(test_results.rootMeanSquaredError))


# Well that is nice, but realistically we will eventually want to test
# this model against unlabeled data, after all, that is the whole point
# of building the model in the first place. We can again do this with a
# convenient method call, in this case, transform(). Which was actually
# being called within the evaluate() method. Let's see it in action:


predictions = correct_model.transform(unlabeled_data)


predictions.show()
