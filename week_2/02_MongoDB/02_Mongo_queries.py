# Here we learn about quering in mongoDB
# such as =, less than, greater than, IN, OR, AND, ORDER BY, LIMIT
from pymongo import MongoClient

client = MongoClient("mongodb+srv://<username>:<password>@cluster0.vs6kqin.mongodb.net/?appName=Cluster0")

# creating of the database
db = client["queriesDB"]

# Creating the collection 
products = db["products"]

# Inserting the values into collection products
products.insert_many(
    [
        { "name": "Phone",  "price": 1200, "category": "Electronics"},

        { "name": "Shirt", "price": 2400, "category": "Fashion" },

        { "name": "Shoes", "price": 3500,"category": "Fashion" },

        { "name": "Laptop","price": 1345000,"category": "Electronics" },

        { "name": "Watch",  "price": 8000, "category": "Accessories" },

        { "name": "Headphones", "price": 4500, "category": "Electronics"  }
    ]
)

# Reading all the values inserted inside the product
print("Displaying all the products present in the product collection\n")
for doc in products.find():
    print(doc)


# Products whose price is greater than 3000
print("Displaying the product whose price is greater than 3000\n")
for item in products.find({"price": {"$gt": 3000}}):
    print(item)


# Products whose price is less than 5000
print("Displaying the product whose price is less than 5000\n")
for items in products.find({"price": {"$lt" : 5000}}):
    print(items)

# Products whose category is Fashion
print("Displaying those products whose category is Fashion\n")
for items in products.find({"category": "Fashion"}):
    print(items)

# Multiple Condition (AND)
print("Displaying the products whose category is fashion and price is less than 2000")
for items in products.find({"category": "Fashion",
                            "price": {"$gt": 2000}
                            }):
    print(items)

# Working with the OR condtion 
print("Displaying the products whose category is electronics or price is less than 3000")
for item in products.find({
    "$or": [
        {"Category": "Electronics"},
        {"price": {"$lt": 3000}}
    ]
}):
    print(item)

# Working with IN operator 
print("Displaying the products whose category is in fashion and electronics\n")
for item in products.find({
    "category": {"$in": ["Fashion", "Electronics"]}
}):
    print(item)

# Sorting (using the order by)
# Displaying the products in the ascending order 
print("Displaying the products in the ascending order\n")
for item in products.find().sort("price", 1):
    print(item)

print("Displaying the products in the descending order\n")
for item in products.find().sort("price", -1):
    print(item)

# Limit like in sql 
print("Displaying the products in the descending order and top 3 products\n")
for item in products.find().sort("price", -1).limit(3):
    print(item)