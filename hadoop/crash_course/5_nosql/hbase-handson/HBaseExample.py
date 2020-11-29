# starbase is a REST client for HBase.
from starbase import Connection

c = Connection(host='127.0.0.1', port='8000')

# Initializes a table instance.
ratings = c.table('ratings')

# Drops the table, if it exists.
if (ratings.exists()):
    print("Dropping existing ratings table.")
    ratings.drop()

# Creating a column family.
ratings.create('rating')

# Parsing the file to insert into HBase.
print("Parsing the ml-100k ratings data...")
ratingFile = open("path/to/ml-100k/u.data", "r")

# Initialize batch instance to work with which will insert the data as a batch into the table.
batch = ratings.batch()

for line in ratingFile:
    (userID, movieID, rating, timestable) = line.split()
    # 'userID' is a unique key.
    # 'rating' is a column family in which 'movieID' is a column and its 'rating' is the value.
    batch.update(userID, {'rating': {movieID: rating}})

ratingFile.close()

print("Committing ratings data to HBase via REST service.")
# Commits the queued batched items into HBase.
batch.commit(finalize=True)

print("Get back ratings for some users...")
print("Ratings for userID 1: ")
# Fetches the data from the table based on the Unique key.
print(ratings.fetch(row="1"))
print("Ratings for userID 33: ")
print(ratings.fetch(row="33"))
