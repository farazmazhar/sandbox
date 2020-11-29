# Spark

## Introduction

- A fast and general engine for large-scale data processing.
- Can be written in programming langauges in Java, Scala or Python.
- It's scalable.
- It can run on YARN or can run stand-alone using its built-in cluster manager.
- Memory based solution.
- DAG engine (Directed Acyclic Graph) optimizes the workflow.
- Can be 100x faster in memory or 10x faster on disk than MapReduce.
- Very popular technology.
- It's not very hard.
- Built around one main concept: the Resilient Distributed Dataset (RDD).
  
## Componenets of Spark

- Spark Streaming (realtime ingestion and analysis)
- Spark SQL
- MLLib
- GraphX (Graph as in Graph Theory)

These components sit on top of Spark core.

## Lazy Execution

- Nothion actually happens in your driver progam until an action is called like show, count, collect etc.

## RDD

- Resilient
- Distributed
- Dataset

### Creating a RDD

- Using SparkContext which is a driver program.
- `nums = sc.parallelize([1, 2, 3, 4])`
- `sc.textFile('file:///path/to/file')`

### Transforming RDD

- map
- flatmap
- filter
- distinct
- sample
- union, intersection, subtract, cartesian

### RDD actions

- collect (returns a Python object, usually a list)
- count
- countByValue
- take (top X rows)
- top
- reduce

## SparkSQL

- Extends RDD to a 'DataFrame' object.

### Dataframes

- Contains Row objects.
- Is a DataSet of Row objects.
- Can run SQL queries.
- Has a schema.
- Read and write to sturctured data formats like JSON, Hive, Parquet etc.
- Communicates with JDBC/ODBC, Tableau etc.

### Using SparkSQL in Python

- Get a Spark session by:
  - `from pyspark.sql import SparkSession`
  - `spark = SparkSession.builder.appName("localsandbox07102019").getOrCreate()` 
- Get a Spark context by:
  - `from pyspark.sql import SparkContext`

_Consult docs of PySpark tutorial._
