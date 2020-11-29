# Flume - Hands on

Start HDP Sandbox and login via SSH.

## Netcat to logs using Flume

```txt Example architecture
             [ Source: Spooldir ]
[ Files ] -> [    Timestamp     ] -> [ Channel: Memory ] -> [ Sink: HDFS ] -> [ HDFS ]
             [   interceptor    ]
```

```sh telnet
# Use `telnet` to open a communication line on localhost:44444.
telnet localhost 44444

# Type in content to and see it in the Flume server
Hello there. General Kenobi!
Fourscore and seven years ago.
```

```sh Flume server
# Get the example file.
wget http://media.sundog-soft.com/hadoop/example.conf

# Open Flume folder where all the scripts are present.
cd /usr/hdp/current/flume-server/bin

# Start the Flume agent
./flume-ng agent --conf conf --conf-file ~/example.conf --name a1 -Dflume.root.logger=INFO,console
```

## Set Up Flume To Monitor A Directory And Store Its Data In HDFS

### Set Up Flume For Second Activity

1. Login to Ambari.
2. Open `HDFS View`.
3. Go to `/user/maria_dev`
4. Create a new folder called `flume`.
5. After the Flume has consumed the data, it should become available on HDFS in the `/user/maria_dev/flume` directory.

```sh
# Create directory in maria_dev home for the spool sink folder.
mkdir spool

# Add data to spool/ directory.
cp access_log_small.txt spool/fred.txt

# When flume is done with the file, it will append '.COMPLETE' to the name.
```

```sh Flume Server
# Get the conf file.
wget http://media.sundog-soft.com/hadoop/flumelogs.conf

# Open Flume folder where all the scripts are present.
cd /usr/hdp/current/flume-server/bin

# Start the Flume agent
./flume-ng agent --conf conf --conf-file ~/flumelogs.conf --name a1 -Dflume.root.logger=INFO,console

# When change is made in spool/ directory it should show up here.
```
