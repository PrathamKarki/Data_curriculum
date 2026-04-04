from pymongo import MongoClient

client = MongoClient("mongodb+srv://<username>:<password>@cluster0.vs6kqin.mongodb.net/?appName=Cluster0")


db = client["aggregationDB"]
orders = db["orders"]

orders.insert_many([
    {"customer": "Aarav", "product": "Laptop", "price": 80000, "category": "Electronics"},
    {"customer": "Aarav", "product": "Mouse", "price": 1500, "category": "Electronics"},
    {"customer": "Sita", "product": "Shoes", "price": 3500, "category": "Fashion"},
    {"customer": "Sita", "product": "Bag", "price": 2500, "category": "Fashion"},
    {"customer": "Ramesh", "product": "Phone", "price": 50000, "category": "Electronics"},
    {"customer": "Ramesh", "product": "Watch", "price": 7000, "category": "Accessories"},
    {"customer": "Nita", "product": "Perfume", "price": 3000, "category": "Accessories"},
    {"customer": "Nita", "product": "Shoes", "price": 4000, "category": "Fashion"}
])

# Displaying all the products where price is greater than 5000
# Basic Filter (all orders where price > 5000)
print("\nDisplay all the products where price is greater than 5000\n")
for item in orders.find({"price" : {"$gt" : 5000} }):
    print(item)

# Task 2
# Find all orders by customer "Aarav"
print("\nFind all the orders by customers called Aarav\n")
for item in orders.find({"customer" : "Aarav"}):
    print(item)


# Task 3
# find orders where category is Electronics, Fashion 
print("\n Fina orders where category is Electronics and Fashion\n\n")
for item in orders.find({"category": {"$in" : ["Electronics", "Fashion"]}}):
    print(item)


# Task 4: Sort by price (descending)
print("\n Show most expensive orders first")
for item in orders.find().sort("price", -1):
    print(item)


# Task 5: Top 3 cheapest orders
print("\n Sort by the top 3 cheapest orders\n\n")
for item in orders.find().sort("price", 1).limit(3):
    print(item)

# Aggregation Section 
# Task 6: count orders per category

ordersPerCategory = [
    {
        "$group": {
            "_id" : "$category",
            "total_orders": {"$sum": 1 }
        }
    }
]

print("\n count the orders per category")
for item in orders.aggregate(ordersPerCategory):
    print(item)


# Task 7: Total spending per customer
spendingPerCustomer = [
    {
        "$group": {
            "_id": "$customer",
            "total_orders": {"$sum" : "$price"}
        }
    }
]
print("\n Total spending per customer is:")

for item in orders.aggregate(spendingPerCustomer):
    print(item)


# Task 8: Average order value per category
avgOrderPerCategory = [
    {
        "$group": {
            "_id": "$category",
            "total_orders": {"$avg" : "$price"}
        }
    }
]

print("\n Average order value per category")
for item in orders.aggregate(avgOrderPerCategory):
    print(item)


# Task 9: Filter BEFORE grouping
# only include orders where price > 3000 then group by category

filterBeforegroup  = [
    {
        "$match": {
            "price": {"$gt": 3000}
        }
    },

    {
        "$group": {
            "_id" : "$category",
            "count": {"$sum": 1}
        }
    }
]

print("\n Only include orders wehre price is greater than 500 and group by category\n\n")
for item in orders.aggregate(filterBeforegroup):
    print(item)


# Task 10: HAVING condition 
# Only show categories with total orders > 2
fitlerAftergroup = [
    {
        "$group": {
            "_id": "$category",
            "total_orders": {"$sum": 1}
        }
    },

    {
        "$match": {
            "total_orders": {"$gt" : 2}
        }
    }
]


# full pipeline
# filter price greater than 2000 , group by category, sum total revenu and sort by descending

fullPipeline = [
    {
        "$match": {
            "price": {"$gt": 2000}
        }
    },
    {
        "$group": {
            "_id" : "$category",
            "total_revenue": {"$sum" : "$price"}
        }
    },

    {
        "$sort": {
            "total_revenue" : -1
        }
    }
]

print("filter price greater than 2000, group by category, sum total revenue and sort by descending")
for item in orders.aggregate(fullPipeline):
    print(item)