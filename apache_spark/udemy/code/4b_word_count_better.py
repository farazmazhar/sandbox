'''
Word count but doesn't count punctuations and stuff.
'''

import re
from pyspark import SparkConf, SparkContext

def normalize_words(text):
    '''
    Normalizes words and turns them in all lowercase.
    '''
    return re.compile(r'\W+', re.UNICODE).split(text.lower())

conf = SparkConf().setMaster("local").setAppName("WordCount")
sc = SparkContext(conf=conf)

input_rdd = sc.textFile("book.txt")
words = input_rdd.flatMap(normalize_words)
wordCounts = words.countByValue()

for word, count in wordCounts.items():
    clean_word = word.encode('ascii', 'ignore')
    if clean_word:
        print(clean_word.decode() + " " + str(count))
