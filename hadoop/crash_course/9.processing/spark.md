# Spark Streaming

## Introduction

- Processes data in real-time.
- Analyze data streams in real time, instead of in huge batch jobs daiy.
- Analyzing streams of web logs data to react to user behaviour.
- Analyze streams of real-time sensor data for IOT stuff.
- Processing of RDD's can happen in parallel on different worker nodes.

## Architecture

```txt

Data Streams   | Micro Batches of data | Transform and output to other systems
-> [ Recievers ] [      DStream      ]  ->
-> [ Recievers ] [ RDD ][ RDD ][ RDD ] ->
-> [ Recievers ]                       ->

```

## DStreams (Discretized Streams)

- Generates the RDDs for each time step, and can produce output at each time step.
- Can be transformed and acted on in much the same way as RDDs.
- Can access their underlying RDDs if you need them.

## Common Stateless Tranformations On DStreams

- Map
- FlatMap
- Filter
- ReduceByKey

## Stateful Data

- You can also maintain a long-lived state on a DStream.
- Example: running totals, broken down by keys.
- Example: aggregating session data in web activity.

## Windowing

- Looking at a data within specific parameters.

### Windowed Transformations

- Allow you to compute results across a longer time period than your batch interval.
- Example: top-sellers from the past hour.
  - You might process data every one second (the batch interval)
  - But maintian a window of one hour.
- The window 'slides' as time goes on, to represent batches within the window interval.

### Intervals

- Batch intervals: how often data is captured into a DStream.
- Slide intervals: how often a windowed transformation is computed.
- Window interval: is how far back in time the windowed tranformation goes.

### In code

- The batch interval is set up with your SparkContext:
  - `ssc = StreamingContext(sc, 1)`
- You can use `reduceByWindow()` or `reduceByKeyAndWindow()` to aggregate data across a longer period of time.
  - `hashtagCounts = hashtagKeyValues.reduceByKeyAndWindow(lambda x, y: x + y, lambda x, y: x - y, 300, 1)`

## Example

- Every batch contains one second of data (the batch interval)
- We setup a window interval of 3 seconds and slide interval of 2 seconds.

```txt
TIME ------------------------------------------------------------------------>
[  2 sec  ][  2 sec  ][  2 sec  ][  2 sec  ][  2 sec  ][  2 sec  ][  2 sec  ] (Window Interval) {Batch}
         [   3 sec   ]              [   3 sec   ]               [   3 sec   ] (Slide interval)  {Compute result}
```

## Structured Streaming

- Uses DataSets.
- New data just keeps getting appended to it.
- Continous application keeps querying updated datasets.

### Advantages

- Looks a lot like non-streaming code.
- Is more efficient.
- SQL style queries are optimized.
- Interoperability with other Spark componenets.
- DataSets in general is the direction Spark is taking.
