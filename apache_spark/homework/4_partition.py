'''
author: faraz mazhar
descri: A PySpark script.

Dabbling with mapPartition and mapPartitionWithIndex.
'''
import pandas as pd

# Disabling pylint false positive on PySpark import.
# pylint: disable=E0401
from pyspark import SparkConf, SparkContext

# Boiler plate code.
conf = SparkConf().setMaster("local").setAppName("partitionRDD")
sc = SparkContext(conf=conf)

sc.setLogLevel("ERROR")

# An example function for mapPartition.
def f(iterator): 
    yield sum(iterator)

# An example function for mapPartitionWithIndex.
def f2(splitIndex, iterator):
    yield splitIndex

rdd = sc.parallelize([1, 2, 3, 4], 2)

res = rdd.mapPartitions(f).collect()                        # [3, 7]
resWithIndex = rdd.mapPartitionsWithIndex(f2).collect()     # [0, 1]

print(res)
print(resWithIndex)
