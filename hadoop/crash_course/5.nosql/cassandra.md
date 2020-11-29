# Cassandra

A distributed NoSQL database with no master node. Engineered to have no single point of failure.

## NoSQL with a twist

- Unlike HBase, there is no master node at all - every node runs exactly the same software and performs the same functions.
- Data model is similar to BigTable / HBase
- It's non-relational, but has a limited CQL query langage as its language.
- Can only do non-relational queries using CQL.

### CAP Theorem

- Consistency, availability, and parition tolerance.
- Proven to only be able to two out of there of these features.
- `Parition tolerance` is a requirement of 'big data' so only get to choose from consistency and availability.
- Cassandra favours availability over consistency.
- It is eventually consistent.
- This consistency can be modified based on your specifications which makes it `tunable consistency`.
- `Availability` is based on reliability and redundancy.
- Partition tolerance means that data can be partitioned easily and distributed across a cluster.
- Partition tolerance is not really a feature of massive databases like Oracle databases etc.
- Partition tolerance is non-negotiable in Big Data.

### Gossip protocol

- Nodes talk each other to know what data is present on what nodes.
- Node data is backed up on different nodes depending on backup configuration.
- Automatically manage each other and keep track of data and changes.
- Consistency can be traded off for speed and availability.

## Cassandra and your cluster

- Great for fast access to rows of information.
- Replicate Cassandra to another ring that is used for analytics and Spark integration.
  - One ring is reponsible for handling transaction queries from online requests and stuff.
  - First ring query data can be copied to another ring that can be used to analyze the data using Spark or Hive and use it in more batch-oriented way.
  - Meaning big data queries can be executed on Cassandra data without any performance hit to the transactional side of the database.

## CQL

- Cassandra's API.
- CQL is like SQL but with limitations.
  - **NO JOINS**
    - The data must be de-normalized.
    - Can't do look-ups between two tables.
  - All queries must be on some primary key.
    - Every tables must have a primary key.
    - Secondary indices have limited supported.
- CQLSH, aka CQL Shell, which provides command line to create tables, etc.
- All the tables must be in `keyspace` - keyspaces are like databases.
  - Basically, similar to databases but different temrinology.

## Cassandra and Spark

- DataStax offers a Spark-Cassandra connector.
- Allows you to read and write Cassandra tables as DataFrames.
- Smart about passing queries on those DataFrames down to the appropriate level.
- Use cases:
  - Use Spark for analytics on data stored in Cassandra.
    - Should use separate cluster.
  - Use Spark to transform data and store it into Cassandra for transactional use.
