'''
Counts ratings in given dataset.
'''


import collections
from pyspark import SparkConf, SparkContext

CONF = SparkConf().setMaster("local").setAppName("RatingsHistogram")
SC = SparkContext(conf=CONF)

LINES = SC.textFile("ml-100k/u.data")
RATINGS = LINES.map(lambda x: x.split()[2])
RESULT = RATINGS.countByValue()

SORTEDRESULTS = collections.OrderedDict(sorted(RESULT.items()))
for key, value in SORTEDRESULTS.items():
    print("%s %i" % (key, value))
