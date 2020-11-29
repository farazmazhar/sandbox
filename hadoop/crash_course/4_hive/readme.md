# Hive

## Why

- Let's you query stuff on distributed cluster.
- Similar to SQL.
- Highly extensible via UDF, Thrift servers and JDBC/ODBC drivers.
- Easy to OLAP queries as compared to MapReduce in Java.

## Why not

- Not for OLTP queries.
- Not for transactions or record-level updates, inserts, and deletes.
- Limited because of SQL as compared to Pig, Spark etc.
- Stores data in de-normalized form.

## HiveQL

- Similar to MySQL with some extensions. For example, views.
- Allows you to specify how structed data is stored and partioned.
