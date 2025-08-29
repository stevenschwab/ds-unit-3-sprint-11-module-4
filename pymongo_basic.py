import os
from pymongo import MongoClient
from dotenv import load_dotenv

# load the environment variables from the .env file
load_dotenv()

# create a MongoClient to interact with your MongoDB instance
db_url = os.getenv("MONGODB_URL")
client = MongoClient(db_url)

# get a reference to your database
db = client['mydatabase']

# get a reference to your collection
collection = db['mycollection']

# insert a document into the collection
collection.insert_one({
    "name": "John Smith", 
    "age": 30, 
    "job": "developer",
    "favorite_language": "Python",
})

# find a document in the collection
document = collection.find_one({"favorite_language": "Python"})

print(document)