# Presto

- Made and partially maintained by Facebook.
- Open source.
- Very similar to drill.
- Unlike drill, it can talk to Cassandra but can't talk to MongoDB.

## Facebook's Presto

- Can connect to many different 'big data' databases and data stores at once, and can query across them.
- It acts like a layer between different data stores.
- Provides SQL syntax.
- Optimized for OLAP i.e. analytical queries, data warehousing.
- Exposes JDBC, Command-Line, and Tableau interfaces.

## Reasons to use Presto

- Use Presto, instead of Drill, because it can connect to Cassandra.
- Used by Facebook, Dropbox, AirBNB etc.
- A single Presto query can combine data from multiple sources, allowing for analytics across your entire organization.
- Presto breaks the false choice between having fast analytics using an expensive commercial solution or using a slow 'free' solution that requires excessive hardware.

## Can connect to

- Cassandra
- Hive
- MongoDB
- MySQL
- Local files
- Kafka
- Redis
    etc...

## Links:

- [Presto documentation](http://prestodb.github.io/)
