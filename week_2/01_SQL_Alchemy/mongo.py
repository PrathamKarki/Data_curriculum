from pymongo import Mongoclient

client = Mongoclient

# create/use of a database

db = client["my_database"]

# Create/use a collection like a table
collection = db["products"]


# Inserting into the documents
collection.inser_one({
    "name": "laptop",
    "price": 1200,
    "category": "Electronics"
})


# multiple documents
collection.insert_many([
    {"name": "phone", "price": 600, "category": "Electronics"},
    {"name": "Shirt", "price": 50, "category": "Fashion"}
])