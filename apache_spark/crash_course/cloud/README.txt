-- RUNNING ON EMR --
    1. Partition dataset
        - A very large dataset won't just work since Spark doesn't optimaly partition the data.
        - Solution is to use '.partitionBy(numberOfPartitions)' on RDD.
        - When using following methods, don't forget to partition since they would benefit from it.
            a. join()
            b. cogroup()
            c. groupWith()
            d. join()
            e. leftOuterJoin()
            f. rightOuterJoin()
            g. groupByKey()
            h. reduceByKey()
            i. combineByKey()
            j. lookup()
        - Right number to partition by.
            a. Too few won't take full advantage while too many would be too much overhead.
            b. Minimum number of partition should number of cores, or executors that fit within available memory.
            c. Suggested in course '.partitionBy(100)'.

    2. Running a job on EMR.
        - file    : 11_EMR_movie_similarities_1m.py
        - dataset : Movielens' one million dataset.
        - Preferably keep dataset in S3 bucket.
        - 'SparkConf()' is empty for EMR since it would be passed as an argument to take advantage of built-in configurations.
        - Creating cluster:
            a. Use 10 clusters for reliability, though course example has 5.
        - Execute following:
            a. aws s3 cp s3://{spark_script}.py ./
            b. aws s3 cp s3://{dataset}/movies.dat ./
            c. spark-submit --executor-memory 1g {spark_script}.py 260
                # Movie id 260 is 'Star Wars'.
                # Default 'executor-memory' is 512MB.

    3. Troubleshooting Spark jobs.
        - Dark art.
        - Locally, console with GUI at 4040.
        - Collect logs on Yarn:
            a. yarn logs -applicationID {appid}
        // Watch Section 4, Lecture 36 again.
            # Network issue.
            
            