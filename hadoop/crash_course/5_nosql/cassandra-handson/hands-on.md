# Cassandra - Hands on

- Hortonworks Sandbox doesn't come with Cassandra so it needs to be installed.
- EMR doesn't come with an option to install Cassandra.

## Installation

### Prerequisites

1. Go as root, if enough permissions are not available.
2. Install `scl-utils`, if your enviornment requires switching Python versions. (important for Hortonworks 2.5)
3. Cassandra requires Python 2.7 or greater. (install it if not available already / important for Hortonworks 2.5)
4. Switch to Python 2.7: `scl enable python27 bash`.

### Installation steps

1. CMD> `cd /etc/yum.repos.d`.
2. CMD> `nano datastax.repo`
   - Use file:///datastax.repo
3. CMD> `yum install dsc30`
4. CMD> `pip install cqlsh`
5. CMD> `service cassandra start`
6. CMD> `cqlsh [--cqlversion="3.4.0"]` <!-- [--cqlversion="3.4.0"] is optional in case there is a verion related issues. -->

## Hands on work

### Post-installation: setting up a users table for movielens dataset.

REMEMBER... NO JOINS!

1. CMD> `cqlsh`
2. cqlsh> `CREATE KEYSPACE movielens WITH replication = {'class': 'SimpleStrategy', 'replication_factor':'1'} AND durable_writes = true;`
3. cqlsh> `USE movielens;`
4. csqlsh:movielens> `CREATE TABLE users (user_id int, age int, gender text, occupation text, zip text, PRIMARY KEY (user_id));`
5. csqlsh:movielens> `DESCRIBE TABLE users`
6. csqlsh:movielens> `SELECT * users;`

### Using Spark to work on `users` table in Cassandra

1. CMD> `wget http://media.sundog-soft.com/hadoop/CassandraSpark.py`
2. CMD> `export SPARK_MAJOR_VERSION=2` <!-- Only necessary when SPARK_MAJOR_VERSION is set to 1 i.e. Hortonworks Sandbox etc. -->
3. CMD> `spark-submit --packages datastax:spark-cassandra-connector:2.0.0-M2-s_2.11 CassandraSpark.py` <!-- spark-cassandra-connector:2.0.0-M2-s_2.11 / 2.0.0 is Spark Version and 2.11 is Scala version, fix them accordingly. -->
4. CMD> `cqlsh [--cqlversion="3.4.0"]`
5. cqlsh> `USE movielens;`
6. csqlsh:movielens> `SELECT * FROM users LIMIT 10;`
7. csqlsh:movielens> `exit`
8. CMD> `service cassandra stop`
