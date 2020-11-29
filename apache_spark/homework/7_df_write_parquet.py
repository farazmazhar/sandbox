'''
author: faraz mazhar
descri: A PySpark script.

Writing a DF in parquet.

Follow 6_s3_etl_s3.py for better comments.
'''

# Disabling pylint false positive on PySpark import.
# pylint: disable=E0401
import pyspark.sql.functions as f
from pyspark.sql import Row, SparkSession# Boiler plate code.

spark = SparkSession.builder \
    .config("spark.sql.warehouse.dir", "file:///C:/temp") \
    .appName("toParquet") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

df = spark.read.csv('salary.csv', header=True)
df.show(n=5)

df.coalesce(1).write.parquet('salary_in_parquet')

spark.stop()
