# Phoenix - Hands on

HBase must be running before installing and using Phoenix.

## Installation

1. Login into Ambari as 'admin'.
2. Start HBase service.
3. Login into HDP Sandbox.
4. CMD> `yum install phoenix`
5. Location: `/usr/hdp/current/phoenix-client/`
6. CMD> `python /usr/hdp/currnet/phoenix-client/bin/sqlline.py` <!-- Starts Phoenix CLI -->

## Working with HBase: creating a table and 'UPSERTING' in the data

1. jdbc:phoenix:>

```sql
/* Create a table called 'us_population'. */
CREATE TABLE IF NOT EXISTS us_population(
    state CHAR(2) NOT NULL,
    city VARCHAR() NOT NULL,
    population BIGINT,
    CONSTRAINT my_pk PRIMARY KEY (state, city)
);

/* List tables to verify newly created table. */
!tables

/* UPSERT command is the INSERT command with a twist i.e. it will update the row if it already exists. */
UPSERT INTO us_population VALUES ('NY', 'New York City', 8143197);
UPSERT INTO us_population VALUES ('CA', 'Los Angeles', 3844829);

/* Verify newly ~inserted~ upserted rows. */
SELECT * FROM us_population;

/* Slightly complex SELECT command for scientific purposes. */
SELECT * FROM us_population WHERE STATE='CA';

/* DROP the table. */
DROP TABLE us_population;

/* List tables to verify newly dropped table. */
!tables

/* Quit from CLI */
!quit
```

## Integrating Phoenix with Pig

### 1. Create the 'users' table

- jdbc:phoenix:>

```sql
/* Create a 'users' table. */
CREATE TABLE users (
    USERID INTEGER NOT NULL,
    AGE INTEGER,
    GENDER CHAR(1),
    OCCUPATION VARCHAR,
    ZIP VARCHAR
    CONSTRAINT pk PRIMARY KEY (USERID)
);

/* List tables to verify newly created table. */
!tables

/* Quit from CLI */
!quit
```

### 2. Insert data

1. CMD> `mkdir ml-100k`
2. CMD> `cd ml-100k`
3. CMD> `wget http://media.sundog-soft.com/hadoop/ml-100k/u.user`
4. CMD> `cd ..`
5. CMD> `wget http://media.sundog-soft.com/hadoop/phoenix.pig`
6. CMD> `pig phoenix.pig`
7. Location: `/usr/hdp/current/phoenix-client/`
8. CMD> `python /usr/hdp/currnet/phoenix-client/bin/sqlline.py` <!-- Starts Phoenix CLI -->
9. jdbc:phoenix:>

```sql
/* List existing tables. */
!tables

/* Select ten rows from table 'users'. */
SELECT * FROM users LIMIT 10;
```

NOTE: Don't forget to stop HBase bfeore closing everything.
