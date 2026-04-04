# Here we will learn about the Mongodb aggreations such as group by and aggregation

from pymongo import MongoClient

client = MongoClient("mongodb+srv://<username>:<password>@cluster0.vs6kqin.mongodb.net/?appName=Cluster0")

# Creating of the database
db = client["aggregationDB"]

# Creating the collection 
products = db["products"]

# Inserting the items into the products 

products.insert_many([
    {"name": "Phone",  "price": 1200, "category": "Electronics"},
    {"name": "Shirt", "price": 2400, "category": "Fashion" },
    {"name": "Shoes", "price": 3500,"category": "Fashion" },
    {"name": "Laptop","price": 1345000,"category": "Electronics" },
    {"name": "Watch",  "price": 8000, "category": "Accessories" },
    {"name": "Headphones", "price": 4500, "category": "Electronics"  }
])

# Displaying of all the products
print("\nDisplaying of all the products in the product collection")
for doc in products.find():
    print(doc)

# Find all the electronic category products
print("\n Displaying all the electronic category product")
for doc in products.find({"category": "Electronics"}):
    print(doc)


# Aggreagtion in mongodb
# Basics

# Creating the pipeline 
# Group by concept
# STEP 1:
pipeline = [
    {
        "$group" : {
            "_id": "$category",
            "total_products" : {"$sum": 1}
        }
    }
]
for result in products.aggregate(pipeline):
    print(result)

# STEP 2: SUM     (total price per category)

pricePerCat = [
    {
        "$group": {
            "_id": "$category",
            "total_price" : {"$sum" : "$price"}
        }
    }
]


# Displaying Total price per category
print("\n Displaying the total price per category")
for result in products.aggregate(pricePerCat):
    print(result)


# STEP 3: Average
# Average price per category

avgPricePerCat = [
    {
        "$group": {
            "_id": "$category",
            "average_price": {"$avg": "$price"}
        }
    }
]
# Average price per category
print("\n Displaying the average price per category\n\n")
for result in products.aggregate(avgPricePerCat):
    print(result)


# STEP 4: MAX/MIN

max_and_min = [
    {
        "$group": {
            "_id": "$category",
            "max_price": {"$max", "$price"},
            "min_price": {"$min", "$price"}
        }
    }
]
# Max and min in mongodb
for result in products.aggregate(max_and_min):
    print(result)


# STEP 5: Filter before grouping ($match)

filterBeforeGroup = [
    {
        "$match":{
            "category" : "Electronics"
        }
    },

    {
        "$group" : {
            "_id" : "$category",
            "total": {"$sum": 1}
        }
    }
]

# for filter before grouping 
for item in products.aggregate(filterBeforeGroup):
    print(item)


# STEP 6: Filter after grouping ($match)

filterAfterGroup = [
    {
        "$group": {
            "_id" : "$category",
            "total": {"$sum": 1}
        }
    },

    {
        "$match": {
            "total": {"$gt": 2}
        }
    }
]

for item in products.aggregate(filterAfterGroup):
    print(item)