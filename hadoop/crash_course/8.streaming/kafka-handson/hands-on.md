# Kafka - Hands on

Start HDP Sandbox and login via SSH.

## Spinning up Kafka

- Open Ambari and login as Admin.
- Select `Kafka` from service list on the left.
- Click on `Service Actions` on the top right hand side.
- Select start.

## Creating a topic

```sh Producer
# Open Kafka folder where all the scripts are present.
cd /usr/hdp/current/kafka-broker/bin

# Create a topic.
./kafka-topic.sh --create --zookeeper sandbox.hortonworks.com:2181 --replication-factor 1 --partitions 1 --topic very_cool_topic

# List the newly created topic
./kafka-topic.sh --list --zookeeper sandbox.hortonworks.com:2181

# Publish data to the topic.
./kafka-console-producer.sh --broker-list sandbox.hortonworks.com:6667 --topic very_cool_topic

# Following line are being sent to the Kafka topic
This is a line of data.
I am sending this on very_cool_topic.
```

```sh Consumer
# Open Kafka folder where all the scripts are present.
cd /usr/hdp/current/kafka-broker/bin

# Consume data from the topic.
./kakfa-console-consumer.sh --bootstrap-server sandbox.hortonworks.com:6667 --zookeeper localhost:2181 --topic very_cool_topic --from-beginning

# Should recieve data on this terminal.
```

## Publishing web logs

```sh Producer
# Open Kafka folder where all the configurations are present.
cd /usr/hdp/current/kafka-broker/conf

# Make copies of certain properties files.
cp connect-file-source.properties ~/
cp connect-standalone.properties ~/
cp connect-file-sink.properties ~/
cd ~

# Edit connect-standalone.properties
nano connect-standalone.properties

# Change bootstrap.server
bootstrap.server=sandbox.hortonworks.com:6667

# Edit connect-file-sink.properties
nano connect-file-sink.properties

# Change name, file, and topic
name=local-file-sink
file=/home/maria_dev/logout.txt
topic=very_cool_log

# Edit connect-file-source.properties
nano connect-file-source.properties

# Change name, file, and topic
name=local-file-source
file=/home/maria_dev/access_log_small.txt
topic=very_cool_log

# Get the `access_log_small.txt` file.
wget http://media.sundog-soft.com/hadoop/access_log_small.txt

# Open Kafka folder where all the scripts are present.
cd /usr/hdp/current/kafka-broker/bin

# Spin up the connector.
./connect-standalone.sh ~/connect-standalone.properties ~/connect-file-source.properties ~/connect-file-sink.properties
```

```sh Consumer-console
# Open Kafka folder where all the scripts are present.
cd /usr/hdp/current/kafka-broker/bin


# Consume data from the topic.
./kakfa-console-consumer.sh --bootstrap-server sandbox.hortonworks.com:6667 --zookeeper localhost:2181 --topic very_cool_log --from-beginning

# Should recieve data on this terminal.
```

```sh Consumer-file
# Switch to home directory.
cd ~ # maria_dev's home directory.

# List all the files.
ls

# Check out the data.
less logout.txt

# Doing the following should add a new line to the logout.txt and Consumer-console.
echo "This is a new line." >> access_log_small.txt
```

NOTE: Stop the Kafka service after the work is done.
