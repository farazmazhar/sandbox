# Apache Phoenix

- Sits on top of HBase.
- Part of Hadoop ecosystem.

## SQL for HBase

- A SQL driver for HBase that supports transactions.
- Fast, low-latency - OLTP support.
- Originally developed by Salesforce, but is now open-sourced.
- Exposes JDBC connector for HBase.
- Supports secondary indices and user-defiend functions.
- Integrates with MapReduce, Spark, Hive, Pig, and Flume.
- Supports 'User Defined Functions'.
- If queries are designed carefully, it can be even faster than native HBase connectors.

## Reasons to use

- It's fast.
- No significant performance cost for having it as an extra top layer on HBase.
- Use Pheonix instead of Drill when you know you are only going to use HBase.
- Reason to use Pheonix over native clients is the fact that:
  - It provides SQL interface.
  - Provides JDBC connector.
  - Can optimize complex queries.

## Architecture

- Basically similar to HBase architecture.
- Phoenix client sits on top of HBase API.
- Pheonix Co-Processor sits next to HBase Region Server which sits on top of HDFS.
- Zookeeper keeps track of everything.

## Using Phoenix

- Command-Line Interface (comes with Phoenix installation)
- Phoenix API for Java
- JDBC driver (thick client - most of the logic exists on client side)
- Phoenix Query Server (PQS) (thin client - separate server that handles queries, eventually allowing non-JVM access)
- JARs for MapReduce, Hive, Pig, Flume, and Spark.
