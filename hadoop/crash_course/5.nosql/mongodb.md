# MongoDB

- A non relational, NoSQL, document based data model, perfers consistency and partion tolerance over availability.
- Looks like JSON.
- `_id` field is always added to every document which makes having a PRIMARY/UNIQUE KEY unnecessary.

## No Real Schema Is Enforced

- You can have different fields in every document.
- No single `key` as in other databases.
  - Indices can be created on any fields or combination of fields.
  - `Shard`ing requires indexes. <!-- Sharding: Horizontal partitioning -->
- A lot of flexibility. <!-- Although you can shove anything, doesn't mean you should. -->
- Since being a NoSQL, joins have a cost.

## Terminology

- Databases / Has collections
- Collections / Has documents - Similar to tables
- Documents / Unit of storing data

Data can't be moved between collections of different databases.

*Aimed at corporate environments.*

## Replication Sets

- Single master.
- Maintains backup copies of your database instance.
  - Secondaries can elect a new primary within seconds if your primary goes down.
  - But make sure your operation log is long enough to give you time to recover the primary when it comes back.
  - If operation log runs out of memory when primary instance is down, it can result in lost operations.

### Replication Sets Quirks

- A majority of the servers in your set must agree on the primary.
  - Even number of servers (like 2) don't work well.
- If you don't want to set up more servers, then setup an 'arbiter' node but there can only be one.
- Application must know about enough servers in the replica set to be able to reach one to learn who's primary.
- Replicas only address durability, not your ability to scale.
  - Although not recommended, secondaries can be read from.
  - Database will go in read-only if primary is down and secondaries are being read from.
- Delayed secondaries can be set up as insurance against people doing dumb things.
  - For example; if a table is dropped accidently, delayed secondary can be used to recover from the mistake.

## Sharding

- Finally - "big data"
- Ranges of some indexes value you specify are assigned to different replica sets.

[App Server Process | MongoS]* -> [Primary] -> [Secondary] -> [Secondary] RS1: users min -> 100
                                  [Primary] -> [Secondary] -> [Secondary] RS2: users 100 -> 500
                                  [Primary] -> [Secondary] -> [Secondary] RS3: users 500 -> max
    [Config Server] <!-- Knows what node has what data and stuff -->
    [Config Server]
    [Config Server]

- Many app servers are running using `MongoS` which has **three** `Config Server`.
- These `Config Server` tells which replica set to talk to for the given data.
- The replica set has primary and secondaries.
- MongoS has a balancer running so all replica sets get equal load and ensure equal distribution.

### Sharding Quirks

- Auto-sharding sometimes doesn't work.
  - Split storms / can't split stuff fast enough.
  - MongoS process restart too often / things won't be balanced evenly.
- Must have exactly three `Config Server`.
  - If one of them goes down, whole database goes down.
  - This is on top of single-master design of replica sets.
- MongoDB's loose document model can be at odds with effective sharding.
  - Needs to stratgize about how to structure the keys across documents to effectively shard the data.
  
## Neat Things About MongoDB

- Not just another NoSQL data, has a very flexible document model.
- Shell is a full JavaScript interpreter.
  - JavaScript can be run on the shell.
- Supports many indices.
  - Only one can be used for sharding.
  - More than 2-3 are discouraged.
  - Full-text indices for text searches.
  - Spatial indices.
- Built-in aggregation capabilities, MapReduce, GridFS (file-system).
  - For some applications, Hadoop might not be required.
  - Integrates with Hadoop, Spark, and most languages.
  - In some cases for example; if Spark dataset is supposed to perform a MapReduce task, it might get passed down to MongoDB.
- A SQL connector is available.
  - Still isn't designed for efficient joins and normalized data.
