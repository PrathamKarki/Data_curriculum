# Task 1: Perform following activities: connect mongodb, create database
# Create collection, Insert documents and read the document

from pymongo import MongoClient

client = MongoClient("mongodb+srv://<username>:<password>@cluster0.vs6kqin.mongodb.net/?appName=Cluster0")

# Creating of the database
db = client['LearnDB']

# Creating of the collection 
products = db["products"]

# Inserting of the 3 products into our document 

products.insert_many([
    {
         "name": "Phone",
         "price": 12000,
         "category": "Electronics"
    },

    {
        "name": "Shirt", 
        "price": 2400, 
        "category": "Fashion"
    },

    {
        "name": "Shoes",
        "price": 3500,
        "category": "Fashion"
    }
]
)

# Reading of the created document
for item in products.find():
    print(item)