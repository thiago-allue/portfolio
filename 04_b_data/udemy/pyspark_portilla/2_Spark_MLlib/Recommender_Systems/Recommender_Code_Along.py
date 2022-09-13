
# coding: utf-8

# # Recommender Code Along
# 
# The classic recommender tutorial uses the [movielens data set]
# (https://grouplens.org/datasets/movielens/).
# It is similar to using the iris or MNIST data set for other algorithms.
# Let's do a code along to get an idea of how this all works!
# 
# Looking for more datasets? Check out: https://gist.github.com/entaroadun/1653794


from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('rec').getOrCreate()


# With Collaborative filtering we make predictions (filtering)
# about the interests of a user by collecting preferences or taste
# information from many users (collaborating).
# The underlying assumption is that if a user A has the same opinion as a user B on an issue,
# A is more likely to have B's opinion on a different issue x than to have the opinion on x
# of a user chosen randomly.
# 
# The image below (from Wikipedia) shows an example of collaborative filtering.
# At first, people rate different items (like videos, images, games).
# Then, the system makes predictions about a user's rating for an item
# not rated yet. The new predictions are built upon the existing ratings
# of other users with similar ratings with the active user. In the image,
# the system predicts that the user will not like the video.


# Spark MLlib library for Machine Learning provides a
# Collaborative Filtering implementation by using Alternating
# Least Squares. The implementation in MLlib has these parameters:
# 
# * numBlocks is the number of blocks used to parallelize
#  computation (set to -1 to auto-configure).
# * rank is the number of latent factors in the model.
# * iterations is the number of iterations to run.
# * lambda specifies the regularization parameter in ALS.
# * implicitPrefs specifies whether to use the explicit feedback ALS variant or one adapted for implicit feedback data.
# * alpha is a parameter applicable to the implicit feedback variant of ALS that governs the baseline confidence in preference observations.
# 
# Let's see this all in action!

from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS


data = spark.read.csv('movielens_ratings.csv',inferSchema=True,header=True)

data.head()

data.describe().show()


# We can do a split to evaluate how well our model performed,
# but keep in mind that it is very hard to know conclusively
# how well a recommender system is truly working for some topics.
# Especially if subjectivity is involved, for example not everyone
# that loves star wars is going to love star trek, even though a
# recommendation system may suggest otherwise.


# Smaller dataset so we will use 0.8 / 0.2
(training, test) = data.randomSplit([0.8, 0.2])


# Build the recommendation model using ALS on the training data
als = ALS(maxIter=5, regParam=0.01, userCol="userId", itemCol="movieId", ratingCol="rating")
model = als.fit(training)


# Now let's see hwo the model performed!
# Evaluate the model by computing the RMSE on the test data
predictions = model.transform(test)
predictions.show()

evaluator = RegressionEvaluator(metricName="rmse", labelCol="rating",predictionCol="prediction")
rmse = evaluator.evaluate(predictions)
print("Root-mean-square error = " + str(rmse))


# The RMSE described our error in terms of the stars rating column.
# So now that we have the model, how would you actually supply a
# recommendation to a user?
# 
# The same way we did with the test data! For example:

single_user = test.filter(test['userId']==11).select(['movieId', 'userId'])

# User had 10 ratings in the test data set 
# Realistically this should be some sort of hold out set!
single_user.show()

reccomendations = model.transform(single_user)


reccomendations.orderBy('prediction',ascending=False).show()


# # Great Job!
