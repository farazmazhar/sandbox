# Apache Drill

- A query engine that lets you issue SQL queries across wide range of stuff in a cluster like external database e.g. MongoDB, file systems e.g. HDFS or Google Cloud etc.
- It can communicate with Hive and HBase bringing them under one SQL flag.
- Can talk to MongoDB but not with Cassandra.

## SQL for NoSQL

- Sits on top of technologies that store data.
- Allows you to query variety of non-relational database and data files.
  - Hive, MongoDB, HBase
  - Flat JSON or Parquet files in HDFS, S3, Azure, Google cloud or any local file system.
- It is based on Google's Dremel.
- It is real SQL.
- It has ODBC / JDBC driver so other tools can connect to it like any relational database.
- Based on SQL 2003 standards.
- It can do similar stuff that Hive can do while providing real SQL interface.
- It is still non-relational under the hood so 'joins' and stuff are still going to have a cost.
- Allows SQL analysis disparate data sources without requiring to load and transform them.
- Joins can be between cross-technologies like JSON with Hive with HBase etc in your application ecosystem.
