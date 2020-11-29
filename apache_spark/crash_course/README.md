# Apache Spark

This is based on Frank Kane's Udemy course on Spark and Python.

Note: This work was done in 2018 so things might have changed by the time you are reading this. Also, if you are using Spark on Python only, you can install PySpark using Pip or Conda.


## Setting Up Env For Spark
    - Canopy (ignored in favour of VSCode)
    - winutils
    - Copy winutils.exe to:
        - C:\winutils\bin\
        - Create folder:
            - C:\tmp\hive
            - CMD> winutils.exe chmod 777 \tmp\hive
    - Java 8
    - PySpark 2.3.2
    - Environment variables
        - SPARK_HOME : C:\spark 
        - HADOOP_HOME : C:\winutils
        - JAVA_HOME : C:\Java\jdk
        - JRE_HOME : C:\Java\jre
        - PATH -> new -> 
            - {SPARK_HOME}\bin

## Testing The Env For Spark

    - cd C:\spark
    - pyspark 
        - pyspark> sc.textFile('README.md').count()
