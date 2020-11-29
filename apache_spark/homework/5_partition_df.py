'''
author: faraz mazhar
descri: A PySpark script.

MapPartition on DataFrame.

DataFrame structure:
+-------+----------+
| years |  salary  |
+-------+----------+
|  1.1  | 39343.00 |
|  1.3  | 46205.00 |
|  1.5  | 37731.00 |
| ...   | ...      |
+-------+----------+

Answer on 'salary_mini.csv':
+-----+--------+
|years|  salary|
+-----+--------+
|  5.9|166804.0|
| 14.5|275573.0|
+-----+--------+
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


# An example function for mapPartition.
def func(iterator): 
    yield sum(iterator)

# Partition logic for df.
salarydf = spark.read.csv('salary_mini.csv', header=True)

years = spark.sparkContext.parallelize(
    salarydf.rdd.map(lambda x: float(x['years'])).collect(),
    2
    ) \
    .mapPartitions(func) \
    .collect() 

salary = spark.sparkContext.parallelize(
    salarydf.rdd.map(lambda x: float(x['salary'])).collect(),
    2
    ) \
    .mapPartitions(func) \
    .collect() 

df = spark.createDataFrame(list(zip(years, salary)), schema=['years', 'salary'])
df.show()

spark.stop()