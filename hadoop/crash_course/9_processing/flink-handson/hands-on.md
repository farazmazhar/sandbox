# Flink - Hands on

Start HDP Sandbox and login via SSH.

## Setting up Flink

1. Go to [Flink website](https://flink.apache.org).
2. Download Flink.
3. Run following commands.

```sh
# Extract the flink package.
tar xvfz flink-1.2.0.tar.gz

# Modify configurations to make it work on HDP Sandbox.
# Change `jobmanager.web.port` to `8082`
cd flink-1.2.0/conf
nano flink-conf.yaml

# Start Flink
../bin/start-local.sh

# Stop Flink
../bin/stop-local.sh
```

## Counting words with Flink

- Pull-up Flink console on `127.0.0.1:8082`.

```sh netcat
# Open a port using netcat to broadcast on TCP port 9000.
nc -l 9000

# Type here for netcat to boardcast the message.
```

```sh Flink
# Execute the Flink WordCount code.
./flink-1.2.0/bin/flink run ./flink-1.2.0/examples/streaming/SocketWindowWordCount.jar --port 9000
```

```sh View logs
cd flink-1.2.0/log/

less flink-*-jobmanager-0-sandbox-*.out

# Messages broadcasted to TCP port 9000 will show up here in a form of WordCount log file.
```
