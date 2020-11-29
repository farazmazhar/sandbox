# Zookeeper - Hands on

On HDP Sandbox, Zookeeper runs automatically when it boots up since a lot of services are dependant on it.

## Simulating a failing master

```sh
# Go to Zookeeper folder.
cd /usr/hdp/current/zookeeper-client/bin

# In real scenarios C++, Java, or Python is used to interact with Zookeeper; following script can be used to get the command line interface.
./zkCli.sh

# Although Zookeeper opens its own shell, it is similar to bash.
# These commands with replicate on all the nodes.

# List files.
ls /

# Create an ephemeral znode and some "data" in it.
create -e /testmaster "127.0.0.1:2223"

# Get the znode.
get /testmaster

# Exit from the Zookeeper CLI to simulate crashing.
quit

# Go into Zookeeper shell again to check the znode.
./zkCli.sh

# Get the znode.
get /testmaster

# Create the master znode.
create -e /testmaster "127.0.0.1:2225"

# Recreating the testmaster, this should fail.
create -e /testmaster "127.0.0.1:2225"

# Exit from the Zookeeper CLI.
quit
```

Once one node crashes, other nodes will try to become the master.
