# HBASE

- Non-relational, scalable database, built on top of HDFS.
- Implementation of Google's BigTable.
- It has built-in auto-sharding.

## CRUD

- CREATE
- READ
- UPDATE
- DELETE
- No query language but has CRUD API.

## HBase data model

- Fast access to an give ROW.
- A ROW is referenced by a unique KEY. (Similar to Primary Key)
- Each ROW has a small number of COLUMN FAMILIES.
- A COLUMN FAMILY may contain arbitrary COLUMNS.
- You can have a very large number of COLUMNS in a COLUMN FAMILY.
- Each CELL can have many VERSIONS with given timestamps.
- Sparse data is A-OK - missing columns in a row consume no storage.

## Accesing HBase

- HBase shell
- Java API
  - Wrappers for Python, Scala, etc.
- Spark, Hive, Pig
- REST service
- Thrift service
- Avro service
