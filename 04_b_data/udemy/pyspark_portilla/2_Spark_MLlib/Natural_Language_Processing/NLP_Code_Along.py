
# coding: utf-8

# # NLP Code Along
# 
# For this code along we will build a spam filter!
# We'll use the various NLP tools we learned about
# as well as a new classifier, Naive Bayes.
# 
# We'll use a classic dataset for this - UCI
# Repository SMS Spam Detection:
# https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection

from pyspark.sql import SparkSession


spark = SparkSession.builder.appName('nlp').getOrCreate()


data = spark.read.csv("smsspamcollection/SMSSpamCollection",inferSchema=True,sep='\t')

data = data.withColumnRenamed('_c0','class').withColumnRenamed('_c1','text')

data.show()


# ## Clean and Prepare the Data

# ** Create a new length feature: **

from pyspark.sql.functions import length

data = data.withColumn('length',length(data['text']))

data.show()

# Pretty Clear Difference
data.groupby('class').mean().show()


# ## Feature Transformations


from pyspark.ml.feature import Tokenizer,StopWordsRemover, CountVectorizer,IDF,StringIndexer

tokenizer = Tokenizer(inputCol="text", outputCol="token_text")
stopremove = StopWordsRemover(inputCol='token_text',outputCol='stop_tokens')
count_vec = CountVectorizer(inputCol='stop_tokens',outputCol='c_vec')
idf = IDF(inputCol="c_vec", outputCol="tf_idf")
ham_spam_to_num = StringIndexer(inputCol='class',outputCol='label')


from pyspark.ml.feature import VectorAssembler
from pyspark.ml.linalg import Vector



clean_up = VectorAssembler(inputCols=['tf_idf','length'],outputCol='features')


# ### The Model
# 
# We'll use Naive Bayes, but feel
# free to play around with this choice!

from pyspark.ml.classification import NaiveBayes


# Use defaults
nb = NaiveBayes()


# ### Pipeline
from pyspark.ml import Pipeline


data_prep_pipe = Pipeline(stages=[ham_spam_to_num,tokenizer,stopremove,count_vec,idf,clean_up])

cleaner = data_prep_pipe.fit(data)

clean_data = cleaner.transform(data)



# ### Training and Evaluation!

clean_data = clean_data.select(['label','features'])
clean_data.show()

(training,testing) = clean_data.randomSplit([0.7,0.3])

spam_predictor = nb.fit(training)

data.printSchema()

test_results = spam_predictor.transform(testing)

test_results.show()


from pyspark.ml.evaluation import MulticlassClassificationEvaluator

acc_eval = MulticlassClassificationEvaluator()
acc = acc_eval.evaluate(test_results)
print("Accuracy of model at predicting spam was: {}".format(acc))


# Not bad considering we're using straight math on text data!
# Try switching out the classification models!
# Or even try to come up with other engineered features!
# 
# ## Great Job!
