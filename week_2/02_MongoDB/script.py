from pymongo import MongoClient

client = MongoClient("mongodb+srv://<username>:<password>@cluster0.vs6kqin.mongodb.net/?appName=Cluster0")

# Creating the database
db = client["LearningDB"]

# Creating the collection 
products = db["products"]

print("Connected to the mongoDB")


# Inserting of first data into one document
products.insert_one({
    "name": "Laptop",
    "price": 120000, 
    "category": "Electronics"
})

print("Data is inserted to the products\n")

# Viewing of the inserted data
print("Displaying of the inserted Data in our document called products\n")
for document in products.find():
    print(document)