# MongoDB - Hands on

- Hortonworks doesn't come with MongoDB.
- MongoDB-Ambari connector is available.

## Installation

1. Switch to root if necessary.
2. CMD> `cd /var/lib/ambari-server/resources/stacks/HDP`
3. CMD> `cd [Hadoop version]` <!-- [Hadoop version] is supposed to be the one that you have installed, in this case it is 2.5 -->
4. CMD> `cd services`
5. CMD> `git clone https://github.com/nikunjness/mongo-ambari.git`
6. Open Ambari and sign in as `admin`.
7. Goto 'Actions -> Services'.
8. Install MongoDB via 'Add Service Wizard'.
9. CMD> `pip install pymongo`

NOTE: If MongoDB doesn't start, deleting and reinstalling the virtual machine might be the only solution forward.
Note: In Hortonworks, you have to stop MongoDB from Ambari.

Have `u.user` file available on HDFS for the hands on activities.

## Using Spark to work on `users` table in MongoDB

1. CMD> `wget http://media.sundog-soft.com/hadoop/MongoSpark.py`
2. CMD> `export SPARK_MAJOR_VERSION=2` <!-- Only necessary when SPARK_MAJOR_VERSION is set to 1 i.e. Hortonworks Sandbox etc. -->
3. CMD> `spark-submit --packages org.mongodb.spark:mongo-spark-connector_2.11:2.0.0 MongoSpark.py` <!-- mongo-spark-connector_2.11:2.0.0 / 2.11 is Scala version and 2.0.0 is Spark Version, fix them accordingly.-->

## Using the MongoDB shell

### Creating an index

1. CMD> `mongo`
2. mongo> `use movielens`
3. mongo> `db.users.createIndex( {user_id: 1} )` <!-- createIndex( {col1: -1|1, col2: -1|1} ) | col1: column that you want to index, -1|1 for DESC or ASC -->
4. mongo> `db.users.explain().find( {user_id: 100})` <!-- explain() | Shows what it's going to do. -->
5. mongo> `db.users.find( {user_id: 100} )` <!-- find() | Shows the record with user_id equals to 100 -->

NOTE: You have to create 'index' yourself, unlike Cassandra, MongoDB doesn't create indecies.

### Using aggregation functions of MongoDB: Finding average age by occupation

Aggregation function expressions:

|Expression | Description                                                           |
|:---------:|:----------------------------------------------------------------------|
|$sum       | Summates the defined values from all the documents in a collection    |
|$avg       | Calculates the average values from all the documents in a collection  |
|$min       | Return the minimum of all values of documents in a collection         |
|$max       | Return the maximum of all values of documents in a collection         |
|$addToSet  | Inserts values to an array but no duplicates in the resulting document|
|$push      | Inserts values to an array in the resulting document                  |
|$first     | Returns the first document from the source document                   |
|$last      | Returns the last document from the source document                    |

```mjs
use movielens

/*
aggregate() :- This function is used to perform aggregation
$group { _id : { field_to_group_by: "$field_to_group_by" } } :- This is a GROUP BY function.
occupation: "$occupation" :- Return grouped field occupation as 'occupation'.
avgAge: { $avg: "$age" } :- Return average of column age, grouped by field occupation as 'avgAge'.
*/
db.users.aggregate( [ { $group: { _id: { occupation: "$occupation"} , avgAge: { $avg: "$age" } } } ] )

/* Counts of records in `users` collection */
db.users.count()

/* Get information about collections */
db.getCollectionInfos()

/* Drop a collection */
db.user.drop()
```
