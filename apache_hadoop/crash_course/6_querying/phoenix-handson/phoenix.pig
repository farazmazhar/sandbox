/* Registers where the JAR dependency for Phoenix is present. */
REGISTER /usr/hdp/current/phoenix-client/phoenix-client.jar

/* Loads the pipe delimited 'u.user' data with proper metadata. */
users = LOAD '/user/maria_dev/ml-100k/u.user' 
USING PigStorage('|') 
AS (USERID:int, AGE:int, GENDER:chararray, OCCUPATION:chararray, ZIP:chararray);

/* Stores the 'users' table into HBase in a table called 'users'. */
STORE users into 'hbase://users' using
    org.apache.phoenix.pig.PhoenixHBaseStorage('localhost','-batchSize 5000');

/* Loads 'USERID' and 'OCCUPATION' columns from the HBase table using Phoenix connector. */
occupations = load 'hbase://table/users/USERID,OCCUPATION' using org.apache.phoenix.pig.PhoenixHBaseLoader('localhost');

/* Groups the data by OCCUPATION column, counts the rows, and dumps the data.  */
grpd = GROUP occupations BY OCCUPATION; 
cnt = FOREACH grpd GENERATE group AS OCCUPATION,COUNT(occupations);
DUMP cnt;  
