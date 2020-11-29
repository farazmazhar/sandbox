# Pig Latin Scripting

## Introduction

- Sit on MapReduce.
- Scripting language that looks like SQL.
- Highly extensible.
- Can have UDF (User-Defined Functions).

## Pig hierarchy

1. HDFS
2. YARN
3. MapReduce/TEZ
4. Pig

## Running

- Grunt
- Script
- Ambari/Hue (interactive UI)


### Selecting the enviornment

    - MapReduce (Converts the script into MapReduce before execution).
    - TEZ (Directed Acyclic Graphs to find for optimized execution).

## Pig Latin commands

Following are some of the useful scripting commands.

- LOAD
- STORE (Ex: STORE ratings INTO 'outRatings' USING PigStorage(':');)
- DUMP
- Filter
- DISTINCT
- FOREACH/GENERATE
- MAPREDUCE
- STREAM
- SAMPLE
- JOIN
- COGROUP (Like join but creates different tuples for each key)
- GROUP
- CROSS (Cartesian product)
- CUBE (like CROSS but can do more than two columns)
- ORDER
- RANK (Ranks the rows based on the order they are in)
- LIMIT
- UNION
- SPLIT

Diagnostic commands.

- DESCRIBE (Pretty much like printSchema of Spark)
- EXPLAIN (Gives insight into what Pig intends to do)
- ILLUSTRATE (Takes a sample from each relation and shows exactly what it's doing with each piece of data)

UDF commands.

_NOTE: Unlike Spark UDFs need to be written in JAVA and packaged as a JAR file._

- REGISTER (Used to register the JAR file with UDF)
- DEFINE (Assigns names to the UDFs that are registered)
- IMPORT (Used for importing macros)

Other functions and loaders.

- AVG
- CONCAT
- COUNT
- MAX
- MIN
- SIZE
- SUM

- PigStorage
- TextLoader
- JsonLoader
- AvroStorage
- ParquetLoader
- OrcStorage
- HBaseStorage

## Example

### Find the oldest 5-star movies (MovieLens dataset)

_Following datasets are present in HDFS..._
_General convention of HDFS path in HDP sandbox: /user/username/folder/filename_

- Loading `u.data`.

            ratings = LOAD 'path/to/u.data' AS
                    (userID:int, movieID:int, rating:int, ratingTime:int);

- Loading `u.item`.

            metadata = LOAD 'path/to/u.item' USING
                    PigStorage('|') AS (moveiID:in, movieTitle:chararray,
                    releaseDate:chararray, videoRelease:chararray,
                    imdbLink:chararray);

- View the loaded data.

            DUMP metadata

    _Note: DUMP a subset of data as to not get flooded with output._

- Creating a relation.

            nameLookup = FOREACH metadata GENERATE movieID, movieTitle,
                    ToUnixTime(ToDate(releaseDate, 'dd-MMM-yyyy')) AS releaseTime;

- GroupBy.

            ratingsByMovie = GROUP ratings By movieID;

- Averaging ratings.

            avgRatings = FOREACH ratingsByMovie GENERATE group AS movieID,
                    AVG(ratings.rating) AS avgRating;

- Show schema.

            DESCRIBE ratings;
            DESCRIBE ratingsByMovie;
            DESCRIBE avgRatings;

- Applying filter.

            fiveStarMovies = FILTER avgRatings BY avgRating > 4.0;

- Joining datasets.

            fiverStarsWithData = JOIN fiveStarMovies BY movieID, nameLookup BY movieID;

- OrderBy.

            oldestFiveStarMovies = ORDER fiveStarsWithData BY
                    nameLookup::releaseTime;

### Most rated one star movies

Only * points of scripts, from fiveStarMovies, would change for this example.

- Averaging ratings.*

            avgRatings = FOREACH ratingsByMovie GENERATE group AS movieID,
                    AVG(ratings.rating) AS avgRating, COUNT(ratings.rating) AS numRatings;

- Applying filter.*

            badMovies = FILTER avgRatings BY avgRating < 2.0;

- Final Result.

            finalResults = FOREACH namedBadMovies GENERATE nameLookup::movieTitle AS movieName,
                    badMovies::avgRating AS avgRating, badMovies::numRatings AS numRatings;

- OrderBy.*

            finalResultsSorted = ORDER finalResults BY numRatings DESC; 
