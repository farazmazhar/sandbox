'''
author: faraz mazhar
descri: A PySpark script.

This will take a file of following format:
+---+---+---+-------+
|"a"|"b"|"c"|"1|2|3"|
|...|...|...|...    |

Into:
+---+---+---+---+
|"a"|"b"|"c"|"1"|
|"a"|"b"|"c"|"2"|
|"a"|"b"|"c"|"3"|
|...|...|...|...|
'''

# Disabling pylint false positive on PySpark import.
# pylint: disable=E0401
from pyspark.sql import Column, Row, SparkSession
from pyspark.sql.functions import \
    explode  # Returns a new for each element in given array or map.
from pyspark.sql.functions import col, split

# Creating a Spark session.
spark = SparkSession.builder.config("spark.sql.warehouse.dir", "file:///C:/temp").appName("FlatterApp").getOrCreate()

# Setting log level to 'ERROR' for more specific logs.
spark.sparkContext.setLogLevel("ERROR")

# Input file to flat.
lines = spark.sparkContext.textFile('flat_me.txt')

# Converting lines into RDD of Row objects.
rows = lines.map(lambda x: Row(col1=str(x.split()[0]), col2=str(x.split()[1]), col3=str(x.split()[2]), col4=str(x.split()[3])))

# Converting RDD to DataFrame.
rowDF = spark.createDataFrame(rows)

# Selecting all rows and caching the DataFrame to presist with the default storage level.
table = rowDF.select('*').cache()

# Showing top results.
table.show()

# Exploding.
explodedDF = rowDF.withColumn('col4', explode(split(col('col4'), '\\|')))
explodedTable = explodedDF.select('*').cache()
explodedTable.show()

# Stopping Spark session.
spark.stop()
