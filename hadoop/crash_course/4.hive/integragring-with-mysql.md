# Integrating MySQL and Hadoop

Using a tool called Sqoop.

## What is MySQL

- Popular, free, relational database.
- Generally monolithic in nature.
- Can be used for OLTP - so exporting data into MySQL can be useful.
- Existing data may exist in MySQL that you want to import to Hadoop.

## Sqoop

- Sqoop can handle big data
- Actually kicks off MapReduce job to handle importing or exporting your data.
- Using only Mappers since no calucations are being done.
- Might not be the most efficient on smaller datasets.
- Can be used using simple terminal commands.

```sh
# Copies data from your source to distributed HDFS
sqoop import --connect jdbc:mysql://path/to/movielens --driver com.mysql.jdbc.Driver --table movies

# Importing directly to Hive, skipping HDFS
sqoop import --connect jdbc:mysql://path/to/movielens --driver com.mysql.jdbc.Driver --table movies --hive-import
```

- Incremental imports
  - --check-column and --last-value arguments to keep track of where you left off last time.
- Export data from Hive to MySQL

```sh
# -m is not required in cluster size >1. Confirm this before using.
# REQUIREMENT: TARGET TABLE MUST ALREADY EXIST IN MySQL, WITH COLUMNS IN EXPECTED ORDER.
sqoop export --connect jdbc:mysql://path/to/movielens -m 1 --driver com.mysql.jdbc.Driver --table exported_movies --export-dir /path/to/hive/movies --input-fields-terminated-by '\0001'
```
