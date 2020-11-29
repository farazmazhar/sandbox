# Spark Streaming - Hands on

Start HDP Sandbox and login via SSH.

## Spark Streaming with Flume

### Analyzing web logs published with Flume using Spark Streaming

```sh Flume
# Get the Frank Kane's configuration file for Flume.
wget http://media.sundog-soft.com/hadoop/sparkstreamingflume.conf

# Open Flume folder where all the scripts are present.
cd /usr/hdp/current/flume-server/bin

# Start Flume agent.
./flume-ng agent --conf conf --conf-file ~/sparkstreamingflume.conf --name a1
```

```sh Spark Streaming
# Get the Spark Streaming script for this activity.
wget http://media.sundog-soft.com/hadoop/SparkFlume.py

# Create `checkpoint` directory.
mkdir checkpoint

# Select Spark 2.
export SPARK_MAJOR_VERSION=2

# Submit the Spark script.
spark-submit --packages org.apache.spark:spark-streaming-flume_2.11:2.0.0 SparkFlume.py

# Data recieved from Flume will show up here.
```

```sh spool dir
# Frank Kane's access logs.
wget http://media.sundog-soft.com/hadoop/access_log.txt

# Copy data in `spool` directory.
cp access_log.txt spool/log22.txt

# This should get you output in Spark Streaming shell.
```
