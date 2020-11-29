# Drill - Hands on

## Setting up Drill

It is not a part of HDP so needs to be installed.

### Installing Drill on HDP

1. CMD> `wget http://archive.apache.org/dist/drill/drill-1.12.0/apache-drill-1.12.0.tar.gz`
2. CMD> `tar -xvf apache-drill-1.12.0.tar.gz`
3. CMD> `apache-drill-1.12.0/bin/drillbit.sh start -Ddrill.exec.port=8765`
4. CMD> `apache-drill-1.12.0/bin/drillbit.sh stop`

## Quering movielens data on MongoDB and Hive

1. Login to Ambari as 'admin'.
2. Spin up a database, in this case MongoDB.
3. Go to Hive view and import `u.ratings` data into Hive.
4. hive> `CREATE DATABSE movielens;`
5. Upload data `u.ratings` into `movielens` database using 'Upload Table' option at the top of Hive view.
6. SSH into HDP sandbox.
7. Switch to root.
8. Make sure `u.user` is present in HDFS.
9. CMD> `export SPARK_MAJOR_VERSION=2`
10. CMD> `spark-submit --packages org.mongodb.spark:mongo-spark-connector_2.11:2.0.0 MongoSpark.py`
11. Open `http://127.0.0.1:8765` in browser.
12. Enable 'MongoDB', and 'Hive' plugins.
13. Update 'Hive' plugin by changing `"hive.metastore.uris": "thrift://localhost:9083"`.
14. Select 'Query' tab to query the data.

```sql
-- Show all the available databases.
-- Naming convention [datastore.database] i.e. 'hive.movielens'.
SHOW DATABASES;

-- Select 10 results from hive.movielens.ratings table.
SELECT * FROM hive.movielens.ratings LIMIT 10;

-- Select 10 results from mongo.movielens.users table.
SELECt * FROM mongo.movielens.users LIMIT 10;

-- Grouping cross-technologies to get number of ratings for each occupation.
SELECT u.occupation, COUNT(*),
FROM hive.movielens.ratings r
JOIN mongo.moivelens.users u
ON r.user_id = u.user_id
GROUP BY u.occupation;
```

NOTE: Stop MongoDB from Ambari after completing the task.
