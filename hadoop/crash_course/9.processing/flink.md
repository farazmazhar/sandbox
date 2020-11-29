# Flink

- German for quick and nimble.

## Introduction

- Stream processing engine, similar to Storm.
- Can run on Standalone cluster, or on top of YARN or Mesos.
- Highly scalable.
- Fault-tolerant.
  - Can surive failures while still guaranteeing exactly-once processing.
  - Uses 'state snapshot' to achieve this.
- Up and coming quickly.

# Flink vs. Spark Streaming vs. Storm

- Flink is faster than Storm.
- Flink offers 'real streaming' like Storm. (Storm's Trident API uses micro-batches)
- Flink offers higher-level API like Trident and Spark but still doing real-time streaming.
- Flink has good scala support.
- Flink has its own ecosystem with ML libraries etc.
- Flink can process data based on event times, not when data was recieved.
  - Impressive windowing system.
  - This plus real-time streaming and exactly-once semantics is important for financial applications.
- Flink is the youngest of the technologies.

## All three are converging it seems.

- Spark Streaming's 'Structured Streaming' paves the way for real event-based streaming in Spark.
- Becomes more a question of what fits best in your existing evnironment.

## Architecture

[ CEP ][ Table ]                [ FlinkML ][ Gelly ][ Table ]
[ Data Stream API              ][ DataSet API               ]
[                     Flink Runtime                         ]
[ Standalone Cluster ][ YARN / Hadoop ][ AWS ][    Local    ]

## Connectors

- HDFS
- Cassandra
- Kafka
- ElastiCache
- NiFi
- Redis
- RabbitMQ
