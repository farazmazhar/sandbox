'''
author: faraz mazhar
descri: A PySpark script.

Gets a file from S3, performs ETL (term is used loosely here), and then uploads it back to S3.

Note: When using this sort of script on EMR, the files on S3 can be accessed directly using something like:
    # sprkCntx.textFile('s3://s3-bucket-name/file_key')
    # sprkSsin.read.csv('s3://s3-bucket-name/file_key')
    ...
    - To use above, EMR must have a proper role to access S3 which means use of boto3 is not required.
'''
# Some important import to glob files.
import glob as g

# AWS Python API
import boto3

# Disabling pylint false positive on PySpark import.
# pylint: disable=E0401
import pyspark.sql.functions as f
from pyspark.sql import Row, SparkSession

# Boiler plate code.
spark = SparkSession.builder \
    .config("spark.sql.warehouse.dir", "file:///C:/temp") \
    .appName("S3etlS3") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

'''COMMENTED TO READ ONLY
# Getting the file from S3 bucket.
s3 = boto3.client('s3')                 # Creating a S3 client.
s3.download_file('faraz-raw-bucket',    # Bucket name.
                 'salary.csv',          # Key name.
                 'salary_from_s3.csv')  # Write-as filename.
'''

# Reading the file retrieved from S3.
df = spark.read.csv('salary_from_s3.csv', header=True)

# Displaying DataFrame.
df.show(n=5)

'''COMMENTED TO READ ONLY
# Writing the file into a file changing separator.
df.coalesce(1).write.csv('salary_from_s3_new', sep='\t')
'''

# Spark job is done here.
spark.stop()

# Getting filename.
filenames = g.glob('.\\salary_from_s3_new\\*.csv')

# Printing content of newly created files.
for filename in filenames:
    print(filename)

    with open(filename, 'r') as file:
        count = 0

        for lines in file.readlines():
            print(lines.strip())
            count += 1

            if (count == 5):
                break
    print('only showing top 5 rows',)

'''COMMENT TO READ ONLY
    # Uploading file to S3.
    print('Uploading to S3...')
    s3.upload_file(filename,                                        # Read-as filename.
                  'faraz-raw-bucket',                               # Bucket name
                  'salary_from_s3_' + filename.split('\\')[-1])     # Key name.
    print('Upload complete.',)
'''