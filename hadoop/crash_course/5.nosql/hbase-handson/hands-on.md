# HBase - Hands on

## Task: Import movies ratings in HBase using Python API

- Create a HBase table for movie ratings by user.
- Then show we can quickly query it for individual users.
- Good example of sparse data.
- Dataset: Movielens

### Structure

Python client -> [REST service -> HBase|HDFS]

### Steps task 1

1. Have port visible to the Python client machine.
   - HBase REST
   - HBase Master
   - HBase Region
2. Go to Ambari.
3. Start HBase service.
4. Launch REST service on top of HBase.
   - CMD> `/usr/hdp/current/hbase-master/bin/hbase-daemon.sh start rest -p 8000 --infoport 8001`
5. Create the Python script to access HBase.
6. Stop REST service on top of HBase.
   - CMD> `/usr/hdp/current/hbase-master/bin/hbase-daemon.sh stop rest`

## Task: HBase / Pig integration - Populating HBase at scale

- Must create HBase table ahead of time.
- Your relation must have a unique key as its first column, followed by subsequent columns as you want them saved in HBase.
- USING clause allows you to STORE into an HBase table.
- Can work at scale - HBase is transactional on rows.

### Steps task 2

1. Upload `u.user` file into HDFS.
2. Open hbase shell.
   1. hbase> `create 'users','userinfo'`
        - Translation: Create a users table with column family userinfo.
   2. hbase> exit
3. CMD> `wget http://media.sundog-soft.com/hadoop/hbase.pig`
4. CMD> `less hbase.pig`
5. CMD> `pig hbase.pig`
6. Open hbase shell.
   1. hbase> `scan 'users'`
   2. hbase> `disable 'users'`
   3. hbase> `drop 'users'`

Note:

- `timestamp` column gets added by default.
- It also supports versioning by default.
- Table must be disabled to be dropped.
