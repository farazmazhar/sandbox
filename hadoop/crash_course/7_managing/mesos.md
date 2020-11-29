# Mesos

- Resource negotiator.
- More broad than YARN.
- Made by Twitter.

## Introduction

- Can manage resources for tasks other than big data, including tasks related to web servers, small scripts etc.
- It's goal is to be more general purpose than YARN in terms of problem solving.
- It's really a general container management system.
- Mesos isn't technically a part of Hadoop.
- YARN can talk to Mesos using Myriad.
  - Meaning no need to partition data centers between both of these managers.
- Spark and Storm can use both YARN and Mesos.

## Difference between YARN and Mesos

- YARN is a monolithic scheduler, you give it job a and it figures it out.
- Mesos is a two-tiered system.
  - Makes offeres of resources to your application ("framework").
  - Your framework decisdes whether to accept or reject them.
  - You also decide your own scheduling algorithm.
- YARN is optimized for long, analytical jobs like in Hadoop.
- Mesos is built to handle stuff that YARN can handle as well as long and short lived processes.

## Fitting in

- If all of your organization's cluster application needs to be managed then Mesos can handle that.
  - Alternatives that can used are Kuberentes and Docker.
- YARN is although a better choice for Spark and Storm, Mesos can be used.
- Spark on Mesos is limited to one executor per slave (node).
- If data is on HDFS, YARN is a beter choice.
- If you are using both YARN and Mesos, you can either give both of them their own resources or you can use Myriad for them to talk and share resources.

## Usage

- If your organization as a whole has chose to use Mesos to manage its computing resources in general.
- There is a `Hadoop on Mesos` package on Cloudera that bypasses YARN entirely.
- If your whole system is just Hadoop based, then YARN is a better option.
