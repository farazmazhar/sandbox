# Zookeeper

The man behind the man behind the man.

## Introduction

- Keeps track of information that must be synced across your cluster.
  - Who is the master node?
  - What tasks are assigned to which workers?
  - Which worker is currently available?
- It's a tool that application can use to recover from partial failures in your cluster.
- An intergral part of HBase, High-Availability(HA) MapReduce, Drill, Strom, Solr, etc.

## Failure modes

- Master crases, needs to fail over to a backup.
- Worker crashes, its work needs to be redistributed.
- Network trouble, part of your cluster can't see the rest of it.

## "Primitive" operations in a distributed system

- Master election
  - One node registers itself as a master, and holds a "lock" on that data.
  - Other nodes cannot become master until that lock is released.
  - One one node is allowed to hold the lock at a time.
- Crash detection
  - "Ephemeral" data on a node's availability automatically goes away if the node disconnects, or fails to refresh itself after some time-out period.
- Group management
- Metadata
  - List of outstanding tasks, task assignments.

## Zookeeper's API approach (not primitive)

- A more general approach.
- It is really a little distributed file system.
  - With strong conssitency guarantees.
  - Replace the concept of "file" with "znode" and you have pretty much got it.
- Zookeeper API:
  - create
  - delete
  - exists
  - setData
  - getData
  - getChildren

```txt
/
│
├──── /master `master1.foobar.com:2223`
|
└──── /workers
      │
      ├──── worker-1 `worker-2.foobar.com:2225`
      |
      └──── worker-2 `worker-5.foobar.com:2225`
```

## Notification

- Clients can register for notifications on a znode.
  - Avoids continuous polling.
  - Example: register for notification on /master - if it goes away, try to take over as the new master.

## Persistent and ephemeral znodes

- Presistent znodes remain stored until explicity deleted.
  - i.e., assignment of tasks to worker must presist even if master crashes.
- Ephemeral znode goes away if the client that created it crashes or loses its connection to Zookeeper.
  - i.e., if the master crashes, it should release its lock on the znode that indicates which node is the master.

## Zookeeper Architechture

```txt
              [  Master   ]                     [Zookeeper server]
              [ ZK client ]                     [Zookeeper server]
                                                [Zookeeper server] Zookeeper ensemble
[  Master   ] [  Master   ] [  Master   ]       [Zookeeper server]
[ ZK client ] [ ZK client ] [ ZK client ]       [Zookeeper server]
```

- Have to have more than 3 servers and at least have 5 servers.
- Having 2 servers quorum can cause split brain in a set of 5.
- Have 3 server quorum for the set of 5 having servers in different data centers for redundancy.
