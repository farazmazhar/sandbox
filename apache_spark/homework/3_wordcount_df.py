'''
author: faraz mazhar
descri: A PySpark script.

Word count using DataFrame and writing it to file with tab separator.
'''

# Disabling pylint false positive on PySpark import.
# pylint: disable=E0401
from pyspark.sql import SparkSession, Row
import pyspark.sql.functions as f
import pandas as pd

# Boiler plate code.
spark = SparkSession.builder \
    .config("spark.sql.warehouse.dir", "file:///C:/temp") \
    .appName("JoinMovieRatingsApp") \
    .getOrCreate()

spark.sparkContext.setLogLevel('ERROR')

# Reading a csv file.
rows = spark.sparkContext.textFile('1_i_will_flat_you.py')

toBeDf = rows.map(lambda x: x.split()) \
    .map(lambda x: Row(words=x))

df = spark.createDataFrame(toBeDf)

wordcountDF = df.withColumn('word', f.explode(f.col('words'))) \
    .groupBy('word') \
    .count() \
    .sort('count', ascending=False)

wordcountDF.show()
wordcountDF.repartition(1).write.csv("cc_out.csv", sep='\t')

spark.stop()
