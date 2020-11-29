# Hive - hands on

## Finding the most popular movie in MovieLens dataset

1. Select 'Hive view' in Ambari.
2. Upload the data in Hive using 'Upload Table' option.
3. Add proper metadata. 
4. Click upload after giving the metadata.
   - Files used where `u.data` for the ratings and `u.item` for the names.
5. Create a view to find the most popular movieId.
6. Join the view with the names table to get the name of the most popular movie.

Following are the queries written during this activity.

```SQL
/* CREATE A VIEW WITH COUNTS OF `movieID` AND THEIR COUNTS `ratingCount` IN DESC ORDER */
/* IF NOT EXISTS - TO KEEP EVERYTHING CLEAN, USE THIS SO HIVE DOESN'T CREATE A VIEW ON EVERY EXECUTION */
CREATE VIEW IF NOT EXISTS topMovieIDs AS
SELECT movieID, count(movieID) as ratingCount
FROM ratings
GROUP BY movieID
ORDER BY ratingCount DESC;

/* JOIN THE VIEW WITH THE NAMES TABLE TO GET THE NAME OF THE MOST POPULAR MOVIE */
SELECT n.title, ratingCount
FROM topMovieIDs t JOIN names n ON t.movieID = n.movieID;

/* CLEAN UP */
DROP VIEW topMovieIDs
```

## Use Hive to Find The Movie With The Highest Average Rating

- Hint: AVG() can be used on aggregated data, like COUNT() does.
- Extra credit: only consider movies with more than 10 ratings.

```SQL
/* CREATE A VIEW WITH `movieID` AND THEIR AVERAGES `avgRating` */
/* IF NOT EXISTS - TO KEEP EVERYTHING CLEAN, USE THIS SO HIVE DOESN'T CREATE A VIEW ON EVERY EXECUTION */
CREATE VIEW IF NOT EXISTS avgRatings AS
SELECT movieID, avg(rating) as avgRating, count(movieID) as ratingCounts
FROM ratings
GROUP BY movieID
ORDER BY avgRating DESC;

/* JOIN THE VIEW WITH THE NAMES TABLE TO GET THE NAME OF THE HIGHLY RATED MOVIES WITH MORE THAN 10 VIEWS */
SELECT n.title, ratingCount
FROM topMovieIDs t JOIN names n ON t.movieID = n.movieID
WHERE ratingCount > 10;

/* CLEAN UP */
DROP VIEW avgRatings
```

## Import movie dataset from MySQL to HDFS/Hive

_. `-m` arg is for the numbers of mappers. Leave it out if you are a working on a large cluster.

1. Grant premissions to `localhost` for `movielens.*` on MySQL.
    - mysql> GRANT ALL PRIVILEGES ON movielens.* TO ''@'localhost';
2. Import using Sqoop.
   1. Into HDFS
       - sqoop import --connect jdbc:mysql://localhost/movielens --driver com.mysql.jdbc.Driver --table movies -m 1
   2. Directly into Hive warehouse
       - sqoop import --connect jdbc:mysql://localhost/movielens --driver com.mysql.jdbc.Driver --table movies -m 1 --hive-import

## Export movie dataset to MySQL from Hadoop

_. Might have to grant premission like it was done for 'Import...'.

1. Create table in `movielens.*` on MySQL for the dataset.
    - mysql> use movielens;
    - mysql> CREATE TABLE exported_movies (id INTEGER, title VARCHAR(255), releaseData DATE);
2. Export using Sqoop.
    - sqoop export --connect jdbc:mysql://path/to/movielens --driver com.mysql.jdbc.Driver --table exported_movies -m --export-dir /path/to/hive/warehouse/movies --input-fields-terminated-by '\0001'
