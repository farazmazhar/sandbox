"""
This was created to find different rows between two dataframes.
"""

from pyspark.sql import SparkSession, functions as F
from pyspark.sql.types import *
from pyspark.context import SparkContext

spark = SparkSession.builder.appName("delta_lake") \
    .config("spark.jars.packages", "io.delta:delta-core_2.12:0.7.0") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .getOrCreate()

from delta.tables import *

table_name = ''
env = ''

print('TABLE NAME:', table_name)

rpath = f's3://{table_name}'
dpath = f's3a://{table_name}'


raw_df = spark.read.parquet(rpath)
transformed_df = spark.read.format('delta').load(dpath)

def hash_and_register_data_tables(data_df, table_name):
    data_df = data_df.withColumn("hash_value", F.sha2(F.concat_ws("||", *data_df.columns), 512))
    data_df.createOrReplaceTempView(table_name)
    
    print(f'row count for {table_name}: ' + str(data_df.count()))

drop_column_list = []
print('DROP COLUMN LIST:', drop_column_list)


filtered_column_raw_df = raw_df
filtered_column_transformed_df = transformed_df

for col, dtype in filtered_column_raw_df.dtypes:
    if 'decimal' in dtype:
        filtered_column_raw_df = filtered_column_raw_df.withColumn(col, F.col(col).cast(DecimalType(38, 10)))
        
for col, dtype in filtered_column_transformed_df.dtypes:
    if 'decimal' in dtype:
        filtered_column_transformed_df = filtered_column_transformed_df.withColumn(col, F.col(col).cast(DecimalType(38, 10)))

for column in drop_column_list:
    filtered_column_raw_df = filtered_column_raw_df.drop(column)
    filtered_column_transformed_df = filtered_column_transformed_df.drop(column)

hash_and_register_data_tables(filtered_column_raw_df, 'raw')
hash_and_register_data_tables(filtered_column_transformed_df, 'transformed')


df1 = spark.sql('''SELECT
    raw.hash_value AS raw_hash_value,
    tran.hash_value AS tran_hash_value
FROM
    raw AS raw FULL
    OUTER JOIN transformed AS tran ON raw.hash_value = tran.hash_value
WHERE
    raw.hash_value is NULL
    OR tran.hash_value is NULL''')
    
df1.createOrReplaceTempView('hmmm')
    
print('Number of different rows:', df1.count())


spark.sql('SELECT * FROM raw t, hmmm h WHERE t.hash_value = raw_hash_value').show(50)
print('#' * 50, '\n\n')
spark.sql('SELECT * FROM transformed t, hmmm h WHERE t.hash_value = tran_hash_value').show(50)






    


