# YARN

- Yet Another Resource Negotiator.
- A fundamental part of Hadoop.

## Introduction

- Introduced in Hadoop 2.
- Spearates the problem of managing resources on your cluster from MapReduce.
- Enables development of MapReduce alternatives like Spark and Tez on top of YARN.
- It sits under the hood, managing the cluster.
- Although it is possible to develop applications for YARN; but given the resoruces available, there is no need for it.

## Architectural position of YARN in Hadoop

[(MapReduce), (Spark), (Tez) ] - YARN Appliocations
[            YARN            ] - Cluster Compute Layer
[            HDFS            ] - Cluster Storage Layer

YARN is managing compute resources verses the HDFS which manages the storage resources.

## YARN generalizes the steps

- A client node initiate the request which triggers YARN.
- YARN initates an 'Applicaiton Master' on a 'node manager'.
- The node manager spins up 'nodes' to run multiple 'Application Process'.
- So on

## Running and scheduling of applications

- An application talks to the resource manager to distribute the work to the cluster.
- Locality of the data can be specified i.e. which HDFS block(s) do you want to process?
  - YARN then in turn will try to get the process on the same node that has your HDFS blocks.
- You can specify different scheduling options for applicaitons.
  - Can run more than one application at once on your cluster.
  - Schedulers
    - FIFO - First In First Out
    - Capacity - May run jobs in parallel, if resources are available
    - Fair - May cut into a larger running job to squeeze in a small one

## Building applications on YARN

- Unless it's an aboslute necessity, Spark or Tez can be used to create DAG based applications.
- If you have to...
  - Use frameworks like Apache Slider, Apache Twill
