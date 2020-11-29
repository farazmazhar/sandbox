# NoSQL

- Give up rich query language like SQL for a fast and scalable solution.
- Random access to planet-size data.

## Why NoSQL

Scaling up MySQL etc to massive loads requires extreme measures.

- Denormalization
- Caching layer
- Master/Slave setups
- Sharding
- Materialized views
- Removing stored procedures

## When You Should Go For NoSQL

- Your high-transaction queries are probably pretty simple once de-normalized.
- A simple get / put API may meet your needs.
- Looking up values for given key is simple, fast, and scalable.
- Both can be used in combination e.g. Hive/Pig and HBase etc.

## Choosing Your Database

Following things should be considered when choosing a database:

- Systems that needs to be integrated.
  - Things that needs to talk together can talk to each other or not.
- Scaling requirments.
  - Do you need horizontal scalability?
  - Are the systems going to generate big enough data to warrant a distributed system?
- Support consideration.
  - Is in-house expertise available for security and optimizations?
  - Is professional support available that is affordable?
- Budget considerations.
  - Mostly not a problem for most of the software cases but hardware cost needs to be considered.
  - Not a big concern.
- CAP theorem
  - Which of the two do you prefer?
  - What type of application is being built?
  - Consistency and Availabilty; use MySQL - Partition tolerance is required in big data so might not be a good solution.
  - Partition Tolerance and Consistency; use HBase or MongoDB
  - Availability and Partition Tolerance; use Cassandra
- Simplicity
  - Keep it as simple as possible.
  - Don't do what is not required.
