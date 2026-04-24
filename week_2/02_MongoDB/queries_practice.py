# Solidfying my knowledge of some queries in mongoDB such LIMIT, ORDER BY, and more

from pymongo import MongoClient

client = MongoClient("mongodb+srv://<username>:<password>@cluster0.vs6kqin.mongodb.net/?appName=Cluster0")

# Creating the database
database = client['queriesPracDB']

# Creating of the collection 
products = database["products"]


# Inserting some values in the collection called products

products.insert_many([
      { "name": "Phone",  "price": 1200, "category": "Electronics"},
      { "name": "Shirt", "price": 2400, "category": "Fashion" },
      { "name": "Shoes", "price": 3500,"category": "Fashion" },
      { "name": "Laptop","price": 1345000,"category": "Electronics" },
      { "name": "Watch",  "price": 8000, "category": "Accessories" },
      { "name": "Headphones", "price": 4500, "category": "Electronics"  }
])

# Reading of the inserted values
print("\n\nDisplaying of the inserted data\n\n")
for item in products.find():
    print(item)

# Task 1: Products where price is greater than 2000 and category is Fashion 
print("\n Displaying of the product whose price is greater than 2000 and category is Fashion")
for item in products.find({"category": "Fashion", "price" : {"$gt": 2000}}):
    print(item)

# Task 2: Products where price is greater than 3000 or category is "Electronics"
print("\n Displaying of the product whose price is less than 3000 or category is Electronics\n\n")
for item in products.find({"$or": [
    {"category": "Electronics"},
    {"price": {"$lt": 3000}}
]}):
    print(item)

#Task 3: Sort all the products by their price in descending 
print("\nSorting all the products based on their price in the descending\n\n")
for item in products.find().sort("price", -1):
    print(item)


# Task 4: Get the top 3 cheapest products 
print("\nDisplay the top 3 cheapest products\n\n")
for item in products.find().sort("price", 1).limit(3):
    print(item)

# Task 5: Find products whose category is "Fashion" OR "Electronics" using in
print("\nDisplay the product whose category is Fashion or electronics\n\n")
for item in products.find({"category": {"$in": ["Fashion", "Electronics"]}}):
    print(item)


# Task 6: Products where price is greater than 3000 or category is "Electronics"
print("\n Displaying of the products whose price is less then 3000 or category is Electronics\n\n")
for item in products.find({"$or": [
    {"category": "Electronics"},
    {"price": {"$lt": 3000}}
]}):
    print(item)


# Task 7: Find products whose category is "Fashion" and "Electronics"
print("\nDisplaying of the products whose category is Fashion and Electronics\n")
for item in products.find({"Category" : {"$in": ["Fashion", "Electronics"]}}):
    print(item)

