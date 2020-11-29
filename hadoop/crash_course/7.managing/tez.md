# Tez

Manages Directed Acycling Graphs.

## Introduction

- An alternative to MapReduce.
- Infrastructure against which code can be written.
  - Hive, Pig, MapReduce jobs.
- Constructrs Directed Acyclic Graphs (DAGs) for more efficient processing of distributed jobs.
  - Relies on holistic view of your job; eliminates unnecessary steps and dependencies.
- Optimizes phhysical data flow and resource usage.

## Working

Unlike MapReduce, Tez looks at the workflow and optimizes it removing any unnecessary steps and dependencies making it faster than MapReduce.

## Architectural position of Tez in Hadoop

[     (Hive),          (Pig) ] - Querying Layer
[(MapReduce), (Spark), (Tez) ] - YARN Appliocations
[            YARN            ] - Cluster Compute Layer
[            HDFS            ] - Cluster Storage Layer

- All the layers above Tez can use Tez (or MapReduce).
- It might be used by default but Hive and Pig can be explicitly told to utilize Tez.
