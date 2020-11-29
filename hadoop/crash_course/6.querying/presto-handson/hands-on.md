# Presto - Hands on

Connect to HDP Sandbox via SSH and spin up Cassandra (for this activity).

## Installation

1. Switch to root, if required permissions are not available.
2. Go to docs on [Presto documentation: Deploying](http://prestodb.github.io/docs/current/installation/deployment.html) website.
3. Get the link address to the tar ball.
4. CMD> `wget https://repo1.maven.org/maven2/com/facebook/presto/presto-server/0.226/presto-server-0.226.tar.gz`
5. CMD> `tar -xvfz presto-server-0.226`
6. CMD> `cd presto-server-0.226`
7. Create configuration files following the Presto documentation file.
8. CMD> `wget http://media.sundog-soft.com/hadoop/presto-hdp-config.tgz` <!-- Getting Frank Kane's configs for HDP 2.5 -->
9. CMD> `tar -xvfz presto-hdp-config`
10. CMD> `cd etc`
11. CMD> `less config.properties` <!-- This is from Frank Kane for HDP 2.5. Don't use this for actual setup. -->
12. CMD> `less node.properties` <!-- This is from Frank Kane for HDP 2.5. Don't use this for actual setup. -->
13. CMD> `less hive.properties` <!-- This is from Frank Kane for HDP 2.5. Don't use this for actual setup. -->
14. CMD> `cd presto-server-0.226/bin`
15. Go to docs on [Presto documentation: Deploying](http://prestodb.github.io/docs/current/installation/cli.html) website.
16. Get the link address to the jar file.
17. CMD> `wget https://repo1.maven.org/maven2/com/facebook/presto/presto-cli/0.226/presto-cli-0.226-executable.jar`
18. CMD> `mv presto-cli-0.226-executable.jar presto`
19. CMD> `chmod +x presto`
20. CMD> `cd ..`
21. CMD> `bin/launcher start` <!-- Start the daemon to spin up the Presto. -->
22. After it spins up, open the web interface via browser. <!-- localhost:8090 for HDP 2.5 with Frank Kane's config files. -->
23. CMD> `bin/presto --server 127.0.0.1:8090 --catalog hive` <!-- Start Command Line Interface. -->

## Querying data in Hive

1. presto> `SHOW TABLES FROM default;` <!-- 'default' is like a userspace -->
2. presto> `SELECT * FROM default.ratings LIMIT 10;`
3. Resource and log visualization of queries can be seen in the web interface.
4. presto> `SELECT * FROM default.ratings where rating = 5 LIMIT 10;`
5. presto> `SELECT COUNT(*) FROM default.ratings WHERE rating = 1;`

## Querying data in Cassandra and Hive

1. CMD> `scl enable python27 bash`
2. CMD> `service cassandra start`
3. CMD> `nodetool enablethrift` <!-- Nodetool is a Cassandra tool. -->
4. CMD> `cqlsh --cqlversion="3.4.0"
5. cqlsh> `DESCRIBE keyspaces;`
6. cqlsh> `USE movielens;`
7. cqlsh:movielens> `DESCRIBE tables;`
8. cqlsh:movielens> `SELECT * FROM users LIMIT 10;`
9. cqlsh:movielens> `quit`
10. CMD> `cd presto-server-0.226/etc/catalog`
11. CMD> `nano cassandra.properties`
12. Use file: 'file:///cassandra.properties'.
13. CMD> `cd ../..`
14. CMD> `bin/launcher start`
15. CMD> `bin/presto --server 127.0.0.1:8090 --catalog hive,cassandra`
16. After the work stop everything.
17. CMD> `bin/launcher stop` <!-- Stop Presto service. (Path is assuming you are in Presto server directory) -->
18. CMD> `service cassandra stop` <!-- Stop Cassandra service. -->

```sql
/* Show tables in Cassandra's movielens database. */
SHOW TABLES FROM cassandra.movielens;

/* Describe that Cassandra's movielens database. */
DESCRIBE cassandra.movielens;

/* Select 10 rows from Cassandra's movielens database's user table. */
SELECT * FROM cassandra.movielens.users LIMIT 10;

/* Select 10 rows from Hive's default keyspace's rating table. */
SELECT * FROM hive.default.ratings LIMIT 10;

/* Counting number of ratings by occupation using 'ratings' table in Hive and 'users' table in Cassandra. */
SELECT u.occupation, COUNT(*)
FROM hive.default.ratings r
JOIN cassandra.movielens.users u
ON r.user_id = u.user_id
GROUP BY u.occupation;

/* Quit out of Presto. */
quit
```

NOTE: Study the Presto documentation to read for all the databases that Presto can connect to and their connectors.
