# Flume

Made from start with Hadoop in mind.

## Introduction

- Another way to stream data into your cluster.
- Built-in sinks for HDFS and HBase.
- Originally made to handle log aggregation.
- It is like a buffer between the stream data and HDFS.

## Anatomy Of A Flume Agent And Flow

```txt
[ Webserver ] -> [ source ] -> [ Channel ] -> [ Sink ] -> [ HBase ]
```

## Componenets Of An Agent

- Source
  - Where the data is coming from?
  - Can optionally have channel selectors and interceptors.
  - Selectors can add logic.
  - Interceptors can modify the data.
- Channel
  - How the data is transferred. (via memory or files)
- Sink
  - Where the data is going?
  - Multiple sinks an be organized into Sink groups.
  - A sink can connect to only one channel.
    - Channel is notified to delete a message once the sink processes it.

## Built-in Source Types

- Spooling directory
- Avro
- Kafka
- Exec
- Thrift
- Netcat
- HTTP
- Custom

etc...

## Built-in Sink Types

- HDFS
- Hive
- HBase
- Avro
- Thrift
- ElasticSearch
- Kafka
- Custom

etc...

## Using Avro, Agents Can Connect To Other Agents As Well

- Create a multi-tier fan-in structure.

```txt

[ App Server ]      Avro Sink ->                        [        ]
[ App Server ]    [ Flume Agent ]   <- Avro Source      [        ]
[ App Server ] -> [ Flume Agent ] -> [ Flume Agent ] -> [  HDFS  ]
[ App Server ]    [ Flume Agent ]      Avro Sink ->     [        ]
[ App Server ]                                          [        ]

```
