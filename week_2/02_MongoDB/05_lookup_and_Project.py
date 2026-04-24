from pymongo import MongoClient

client = MongoClient("mongodb+srv://<username>:<password>@cluster0.vs6kqin.mongodb.net/?appName=Cluster0")
# creating of the database
database = ['advancedDB']

# creation of the collection 
orders = database["orders"]
customers = database["customers"]

# Inserting data into the customers and orders

customers.insert_many([
    {"_id": 1, "name": "Aarav", "city": "Kathmandu"},
    {"_id": 2, "name": "Sita", "city": "Pokhara"},
    {"_id": 3, "name": "Ramesh", "city": "Lalitpur"}
])


orders.insert_many([
    {"product": "Laptop", "price": 80000, "customer_id": 1},
    {"product": "Mouse", "price": 1500, "customer_id": 1},
    {"product": "Shoes", "price": 3500, "customer_id": 2},
    {"product": "Phone", "price": 50000, "customer_id": 3}
])


# Show only product and price (hid _id)

pipeline = [
    {
        "$project": {
            "product": 1, 
            "price": 1, 
            "_id" : 0
        }
    }
]

# displaying the output
print("\n -- Using $project ---")
for item in orders.aggregate(pipeline):
    print(item)



# PART 2: $lookup (JOIN)

lookupPipeline = [
    {
        "$lookup" : {
            "from": "customers", # collection to join
            "localField": "customer_id", # field in orders
            "foreignField": "_id",
            "as": "customer_info"

        }
    }
]

print("\n -- Using $lookup (JOIN) --- ")
for item in orders.aggregate(pipeline):
    print(item)