# Kafka

Publish / Subscribe messaging system.

## Introduction

- General-purpose.
- Kafka servers store all incoming messages from publishers for some period of time, and publishes them to a stream of data called a `topic`.
- Kafka consumers subscribe to one or more topics, and receives data as it's published.
- A stream / topic can have many different consumers, all with their own position in the stream maintained.
- It's not just for Hadoop.

## Architecture

```txt
                            (Producers)
             [ DB ]     [App] [App] [App]      [App]
(Connectors) [ DB ] ->  [ Kafka Cluster ] <->  [App] (Stream Processors)
             [ DB ]     [App] [App] [App]      [App]
                            (Consumers)
```

## Scaling

- Kafka itself may be distributed among many profcess on many servers.
  - Will distribute the storage of stream data as well.
- Consumers may also be distributed.
  - Consumers of the same group will ahve messages distributed amongst them.
  - Consumers of different groups will get their own copy of each message.
