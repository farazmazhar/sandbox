# Oozie

Orchestrating your Hadoop jobs.

## Introduction

- Burmese for 'elephant keeper'.
- A system for running and scheduling Hadoop tasks.
- Organzie and schedule Hadoop tasks.

## Workflows

- A multi-stage Hadoop job
  - Might chain together MapReduce, Hive, Pig, Sqoop, and distcp tasks.
  - Other systems available via add-ons like Spark.
- A workflow is Directed Acyclic Graph of actions.
  - Specified via XML.
  - You can run as many actions you want in parallel that don't depend on each other.

### Workflow structure

```txt
                     [pig]
(start) -> [fork] ->       -> [join] -> [hive] -> (end)
                    [sqoop]
```

## Steps to set up a workflow in Oozie

- Make sure each action works on its own.
- Make a directory in HDFS for your job.
- Create `workflow.xml` file and put it in your HDFS folder.
- Create `job.properties` defining any variables for your `workflow.xml` needs.
  - This goes on your local filesystem where you'll launch the job from.
  - You could also set these properties within your XML.

## Running a workflow with Oozie

- CMD> `oozie job --oozie http://localhost:11000/oozie -config /home/maria_dve/job.properties -run`
- Monitor progress at `http://127.0.0.1:11000/oozie`.

## Oozie coordinators

- Schedules workflow exectuion.
- Launches workflows based on a given start time and frequency.
- Will also wait for required input data to become available.
- Run in exactly the same way as workflow.

## Oozie bundles

- New in Oozie 3.0.
- A bundle is a collection of coordinators that can be managed together.
- Example: you may have a bunch of coordinators for processing log data in various ways.
  - By grouping them in a handle, you could suspend them all if there were some problem with log collection.
- It can be a bit complex.
