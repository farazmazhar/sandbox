# Tez - Hands on

## Querying in Hive using Tez against MapReduce

1. Login to the Ambari.
2. Open Hive view.
3. Upload required tables, for this demostration `u.ratings` and `u.item` in ml-100k from `movielens`.
4. Query in Hive.
5. Click the gear icon on the right hand side.
6. Change a property.
7. `hive.execution.engine = tez|mapreduce` <!-- This option lets you select an exection engine on which the Hive executes its queries. -->

```sql
/* This query takes a bit of time so this would be a nice test to compare performance between Tez and MapReduce. */
/* Create show name of top movie ids by rating count. */
DROP VIEW IF EXISTS topMovieIDs;

CREATE VIEW topMovieIDs AS
SELECT movie_id, count(movie_id) as ratingCount
FROM movielens.ratings
GROUP BY movie_id
ORDER BY ratingCount DESC;

SELECT n.name, ratingCount
FROM topMovieIDs t
JOIN movielens.names n
ON t.movie_id = n.movie_id;
```

HDP Sandbox has a `Tez view` to show you the visualizations in terms of analytics, DAG detals, tasks, graphs etc.
