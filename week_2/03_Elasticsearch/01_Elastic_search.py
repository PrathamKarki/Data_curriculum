# Connection to the Elasticsearch
from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

print(es.info())

# Creating of the index and insertion of the data 

es.indices.create(index="items", ignore=400)

docs = {
    "name": "Football", 
    "price": 4500,
    "category": "sports"
}

es.index(index="items", document=docs)


# Range query for the price greater than or equal to 1000 and less than equal to 5000
query = {
    "query": {
        "range": {
            "price": {
                "gte": 1000,
                "lte": 5000
            }
        }
    }
} 

result = es.search(index="items", body=query)

print("RESULT:")

for item in result["hits"]["hits"]:
    print(item["_source"])


# Range query for price gretaer than 2000 and lTe 4500

query2 = {
    "query": {
        "range" : {
            "price" : {
                "gt": 1000,
                "lte": 4500
            }
        }
    }
}

result2 = es.search(index="items", body=query2)

for item in result["hits"]["hits"]:
    print(item["_source"])


# Range query for price greater than 2000 and lte 4500

query3 = {
    "query":{
        "range": {
            "price": {
                "gt": 1000,
                "lte": 4500
            }
        }
    }
}


result3 = es.search(index="items", body=query3)

for item in result["hits"]["hits"]:
    print(item["_source"])