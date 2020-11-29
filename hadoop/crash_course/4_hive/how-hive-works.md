# How Hive works

## Schema On Read

- Hive maintans a "metastore" that imparts a structure you define on the unstructured data that is stored on HDFS etc.

```SQL
CREATE TABLE (
    userID INT,
    movieID INT,
    rating INT,
    time INT
)
ROW FORMAT DELIMTED
FIELDS TERMINATED BY '\t'
STORED AS TEXTFILE;

LOAD DATA LOCAL INPATH `${env:HOME}/ml-100k/u.data`
OVERWRITE INTO TABLE ratings;
```

## Where Is The Data

- LOAD DATA
  - MOVES data from a distributed filesystem into Hive.
- LOAD DATA LOCAL
  - COPIES data from your local filesystem into Hive.
- Managed vs. External tables

```SQL
CREATE EXTERNAL TABLE IF NOT EXISTS ratings (
    userID INT,
    movieID INT,
    rating INT,
    time INT
)
ROW FORMAT DELIMITED FIELDS TERMIANTED BY '\t'
LOCATION '/path/to/u.data';
```

## Partitioning

- You can store your data in partitioned subdirectories.
  - Huge optimization if oyur queries are only on certain partitions.

```SQL
CREATE TABLE customers (
    name STRING
    address STRUCT<stree:STRING, city:STRING, state:STRING, zip:INT>
)
PARTITIONED BY (country STRING)
```

## Ways To Use Hive

- Interactive via `hive>` prompt / Command line interface (CLI)
- Save query files
  - CMD> `hive -f /path/to/queries.hql`
- Through Ambari / Hive
- Through JDBC / ODBC server
- Through Thrift service
  - But remember, Hive is suitable for OLTP
- Via Oozie (managmenet tool for clusters)
