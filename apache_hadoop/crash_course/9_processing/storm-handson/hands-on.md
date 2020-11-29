# Storm - Hands on

Start HDP Sandbox and login via SSH.

## Setting up Storm

- Open Ambari and log in as `admin`.
- Start `Storm` service.
- Start `Kafka` service.

## Count words with Storm

```sh
# Open Storm folder where all the tutorial scripts are present.
cd /usr/hdp/current/storm-client/contrib/storm-starter/src/jvm/org/apache/storm/starter

# Look at WordCountTopology.java
less WordCountTopology.java

# Execute the code.
storm jar /usr/hdp/current/storm-client/contrib/storm-starter/src/jvm/org/apache/storm/starter/storm-starter-topologies-*.jar org.apache.storm.starter.WordCountTopology wordcount

# Check logs
cd /usr/hdp/current/storm-client/logs/workers-artifacts
ls

# Navigate as you see fit.
```

- Go to `127.0.0.1:8744` to open Storm console on browser.
- Under `Topology Summary`, the job can be visualized.
- Click on the job for more in-depth visualization.
