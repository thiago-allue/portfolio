
# coding: utf-8

# # Tools for NLP
# 
# There are lots of feature transformations that need to be done on text data to get it
# to a point that machine learning algorithms can understand. Luckily, Spark has placed
# the most important ones in convienent Feature Transformer calls.
# 

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('nlp').getOrCreate()


# ## Tokenizer
from pyspark.ml.feature import Tokenizer, RegexTokenizer
from pyspark.sql.functions import col, udf
from pyspark.sql.types import IntegerType

sentenceDataFrame = spark.createDataFrame([
    (0, "Hi I heard about Spark"),
    (1, "I wish Java could use case classes"),
    (2, "Logistic,regression,models,are,neat")
], ["id", "sentence"])


sentenceDataFrame.show()

tokenizer = Tokenizer(inputCol="sentence", outputCol="words")

regexTokenizer = RegexTokenizer(inputCol="sentence", outputCol="words", pattern="\\W")

# alternatively, pattern="\\w+", gaps(False)
countTokens = udf(lambda words: len(words), IntegerType())

tokenized = tokenizer.transform(sentenceDataFrame)
tokenized.select("sentence", "words")    .withColumn("tokens", countTokens(col("words"))).show(truncate=False)

regexTokenized = regexTokenizer.transform(sentenceDataFrame)
regexTokenized.select("sentence", "words")     .withColumn("tokens", countTokens(col("words"))).show(truncate=False)


# ## Stop Words Removal
from pyspark.ml.feature import StopWordsRemover

sentenceData = spark.createDataFrame([
    (0, ["I", "saw", "the", "red", "balloon"]),
    (1, ["Mary", "had", "a", "little", "lamb"])
], ["id", "raw"])

remover = StopWordsRemover(inputCol="raw", outputCol="filtered")
remover.transform(sentenceData).show(truncate=False)


# ## n-grams
from pyspark.ml.feature import NGram

wordDataFrame = spark.createDataFrame([
    (0, ["Hi", "I", "heard", "about", "Spark"]),
    (1, ["I", "wish", "Java", "could", "use", "case", "classes"]),
    (2, ["Logistic", "regression", "models", "are", "neat"])
], ["id", "words"])

ngram = NGram(n=2, inputCol="words", outputCol="ngrams")

ngramDataFrame = ngram.transform(wordDataFrame)
ngramDataFrame.select("ngrams").show(truncate=False)


# _______
# # Feature Extractors
# _______

# <h2 id="tf-idf">TF-IDF</h2>
# 
# <p><a href="http://en.wikipedia.org/wiki/Tf%E2%80%93idf">Term frequency-inverse document frequency (TF-IDF)</a> 
# is a feature vectorization method widely used in text mining to reflect the importance of a term 
# to a document in the corpus. Denote a term by <code>$t$</code>, a document by  d , and the corpus by D.
# Term frequency <code>$TF(t, d)$</code> is the number of times that term <code>$t$</code> appears in document <code>$d$</code>, while 
# document frequency <code>$DF(t, D)$</code> is the number of documents that contains term <code>$t$</code>. If we only use 
# term frequency to measure the importance, it is very easy to over-emphasize terms that appear very 
# often but carry little information about the document, e.g. &#8220;a&#8221;, &#8220;the&#8221;, and &#8220;of&#8221;. If a term appears 
# very often across the corpus, it means it doesn&#8217;t carry special information about a particular document.
# Inverse document frequency is a numerical measure of how much information a term provides:
# 
# $$ IDF(t, D) = \log \frac{|D| + 1}{DF(t, D) + 1} $$
# 
# where |D| is the total number of documents in the corpus. Since logarithm is used, if a term 
# appears in all documents, its IDF value becomes 0. Note that a smoothing term is applied to avoid 
# dividing by zero for terms outside the corpus. The TF-IDF measure is simply the product of TF and IDF:
# $$ TFIDF(t, d, D) = TF(t, d) \cdot IDF(t, D). $$
# 

from pyspark.ml.feature import HashingTF, IDF, Tokenizer

sentenceData = spark.createDataFrame([
    (0.0, "Hi I heard about Spark"),
    (0.0, "I wish Java could use case classes"),
    (1.0, "Logistic regression models are neat")
], ["label", "sentence"])

sentenceData.show()

tokenizer = Tokenizer(inputCol="sentence", outputCol="words")
wordsData = tokenizer.transform(sentenceData)
wordsData.show()


hashingTF = HashingTF(inputCol="words", outputCol="rawFeatures", numFeatures=20)
featurizedData = hashingTF.transform(wordsData)

# alternatively, CountVectorizer can also be used to get term frequency vectors
idf = IDF(inputCol="rawFeatures", outputCol="features")
idfModel = idf.fit(featurizedData)
rescaledData = idfModel.transform(featurizedData)

rescaledData.select("label", "features").show()


# ## CountVectorizer
# CountVectorizer and CountVectorizerModel aim to help convert a collection of text documents
# to vectors of token counts. When an a-priori dictionary is not available, CountVectorizer
# can be used as an Estimator to extract the vocabulary, and generates a CountVectorizerModel.
# The model produces sparse representations for the documents over the vocabulary, which can
# then be passed to other algorithms like LDA.

# During the fitting process, CountVectorizer will select the top vocabSize words ordered by
# term frequency across the corpus. An optional parameter minDF also affects the fitting
# process by specifying the minimum number (or fraction if < 1.0) of documents a term
# must appear in to be included in the vocabulary. Another optional binary toggle parameter
# controls the output vector. If set to true all nonzero counts are set to 1. This is especially
# useful for discrete probabilistic models that model binary, rather than integer, counts.

from pyspark.ml.feature import CountVectorizer

# Input data: Each row is a bag of words with a ID.
df = spark.createDataFrame([
    (0, "a b c".split(" ")),
    (1, "a b b c a".split(" "))
], ["id", "words"])

# fit a CountVectorizerModel from the corpus.
cv = CountVectorizer(inputCol="words", outputCol="features", vocabSize=3, minDF=2.0)

model = cv.fit(df)

result = model.transform(df)
result.show(truncate=False)