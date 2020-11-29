# Oozie - Hands on

Spin up HDP Sandbox and login into it via SSH.

## Analyze and extract movies released before 1940s

- Sandbox bash shell

```sh
# Log into MySQL shell. Passoword is `hadoop`.
mysql -u root -p
```

- MySQL shell

```sql MySQL
/* List all the databases to see if movielens exists or not. */
SHOW databases;

/* Quit from the shell. */
quit
```

- Sandbox bash shell

```sh
# Download movielens script to populate MySQL database.
wget http://media.sundog-soft.com/hadoop/movielens.sql
```

- MySQL shell

```sql MySQL
/* Fix encoding to utf8. */
SET names 'utf8';
SET character SET utf8;

/* Create `movielens` database. */
CREATE DATABASE movielens;

/* Change to movielens. */
USE movielens;

/* Execute the script. */
SOURCE movielens.sql

/* Show tables. */
SHOW tables

/* Select from movies table. */
SELECT * FROM movies LIMIT 10;

/* Grant premissions for Sqoop. */
GRANT ALL PRIVILEGES ON movielens.* to ''@'localhost';

/* Quit from MySQL shell */
quit
```

- Sandbox bash shell

```sh
# Get hive script to create old movies table.
wget http://media.sundog-soft.com/hadoop/oldmovies.sql

# Read the file to see what it does and if the paths are correct or not.
less oldmovies.sql

# Setting up Oozie - getting the workflow script.
wget http://media.sundog-soft.com/hadoop/workflow.xml

# Setting up Oozie - getting the properties file.
wget http://media.sundog-soft.com/hadoop/job.properties

# Setting up Oozie - moving files to HDFS.
hadoop fs -put workflow.xml /user/maria_dev
hadoop fs -put oldmovies.sql /user/maria_dev
hadoop fs -put /usr/share/java/mysql-connector-java.jar /user/oozie/share/lib/lib_20161025075203/sqoop # Make sure the path to sqoop is correct.
```

- Setting up Oozie - restart Oozie
- Ambari > Services > Oozie > Services Actions > Restart All

```sh
# Run the job.
oozie job -oozie http://localhost:11000/oozie -config /home/maria_dev/job.properties -run

# Exit out of the shell
exit
```

- Go to `http://localhost:11000/oozie` for read-only visualization.
- Go to Ambari > Files View.
- Go to `/user/maria_dev/oldmovies`
- The output should be present here.
