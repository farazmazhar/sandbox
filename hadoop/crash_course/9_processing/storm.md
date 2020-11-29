# Storm

- Real-time processing

## Introduction

- Another framework for processing continous stream of data on a cluster.
  -  Can run on top of YARN.
- Works on individual events, not micro-batches.
  - If you need sub-second latency, use Storm.

## Storm terminology.

- A stream consists of tuples that flow through.
- Spouts that are sources of stream data. (Kafka, Twitter, etc.)
- Bolts that process stream data as it's recieved.
  - Transform, aggregate, write to databases / HDFS.
- A topology is a graph of spouts and bots that process your stream.

```txt

[ Spout ] -> [ Bolt ] -> [ Bolt ]
[ Spout ] -> [ Bolt ] ->
[ Spout ] -> [ Bolt ]

```

## Architecture

```txt
                               [ Supervisor ]
              [ Zookeeper ] -> [ Supervisor ]
[ Nimbus ] -> [ Zookeeper ] -> [ Supervisor ]
              [ Zookeeper ] -> [ Supervisor ]
                               [ Supervisor ]
```

## Devleoping Storm applications

- Usually done with Java.
  - Alothough bolts may be directed through scripts in other langauges.
- Storm Core.
  - The lower-level API for Storm.
  - "At-least once" semantics.
- Trident
  - The higher-level API for Storm.
  - "Exaclty once" semantics.
- Storm runs your applications "forever" once submitted - until you explicitly stop them.

## Storm vs. Spark Streaming

- Spark having rest of your disposal with Spark Streaming.
- Turly real-time processing with Storm.
- Core Storm offers "tumbling windows" in addition to "sliding windows".
- Kafka + Storm seems to be a pretty popular combination.
