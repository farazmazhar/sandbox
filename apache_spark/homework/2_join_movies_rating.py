'''
author: faraz mazhar
descri: A PySpark script.

> Joins data of two csv files.
> movies.csv and ratings.csv based on movieId.
'''

# Disabling pylint false positive on PySpark import.
# pylint: disable=E0401
from pyspark.sql import Row, SparkSession
from pyspark.sql.functions import col, split

# Boiler plate code.
spark = SparkSession.builder \
    .config("spark.sql.warehouse.dir", "file:///C:/temp") \
    .appName("JoinMovieRatingsApp") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")
# ratingDF = spark.createDataFrame(ratingRow)

# Reading CSV files.
movieDF = spark.read.csv('movies.csv', header=True)
ratingDF = spark.read.csv('ratings.csv', header=True)

# Creating tables.
movieTable = movieDF.select('*').cache()
ratingTable = ratingDF.select('*').cache()

# Creating table aliases.
movie_x = movieDF.alias('mDF')
ratings_x = ratingDF.alias('rDF')

movie_x.join(ratings_x, col('mDF.movieId') == col('rDF.movieId'), 'full') \
    .drop(col('rDF.movieId')) \
    .select(col('mDF.*'), col('rDF.*')) \
    .show()

# Displaying tables.
movieTable.show()
ratingTable.show()

# Stopping Spark session.
spark.stop()
