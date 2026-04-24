# Initial connection for the elasticsearch
from elasticsearch import Elasticsearch
from elasticsearch import helpers

es = Elasticsearch("http://localhost:9200")

print(es.info())

# creation of the index and inserting of the values in the document
es.indices.create(index="products", ignore = 400)

docs = [
    {"name": "basketball", "price": 4500, "category": "sports"},
    {"name": "football", "price": 3000, "category": "sports"},
    {"name": "tennis racket", "price": 7000, "category": "sports"},
    {"name": "chair", "price": 2000, "category": "furniture"}
]

actions = [
    {
        "_index": "products",
        "_source": doc
    }
    for doc in docs
]

helpers.bulk(es, actions)

# q1: Return the producsts where price is between 1000 to 5000\
query1 = {
    "query": {
        "range": {
            "price": {
                "gte": 1000,
                "lte": 5000
            }
        }
    }
}

result = es.search(index="products", body=query1)

print("\n Result for the product where price is between 1000 and 5000\n\n")
for item in result["hits"]["hits"]:
    print(item["_source"])



# q2: Return products where price is greater than 3000
query2 = {
    "query": {
        "range": {
            "price": {
                "gt": 3000
            }
        }
    }
}

result2 = es.search(index="products", body=query2)

print("\n Result for the product where price is greater than 3000")
for item in result2["hits"]["hits"]:
    print(item["_source"])


#q3: Return products where price is less than 3000

query3 = {
    "query": {
        "range": {
            "price": {
                "lt": 3000
            }
        }
    }
}

result3 = es.search(index="products", body=query3)

print("\n Result for the product where price is less than 3000")
for item in result3["hits"]["hits"]:
    print(item["_source"])



# Using of the boolean query and multiple condition

query4 = {
    "query": {
        "bool": {
            "must": [
                {"match" :{"category" : "sports"}}
            ],
          "filter": [
              {
                  "range": {
                      "price": {
                          "gte": 3000,
                          "lte": 5000
                      }
                  }
              }
          ]  
        }
    }
}
result4 = es.search(index="products", body=query4)

print("\n Result for the products where category is sports and price must be between 3k to 5k\n")
for item in result4["hits"]["hits"]:
    print(item["_source"]);


# Task 1: Category = sports , price between 3000 and 5000

query5 = {
    "query": {
        "bool" : {
            "must" : [
                {
                    "match": {
                        "category": "sports"
                    }
                }
            ],
            "filter" : [
                {
                    "range": {
                        "price": {
                            "gte": 3000,
                            "lte": 5000
                        }
                    }
                }
            ]
        }
    }
}


result5 = es.search(index="products", body=query5)

print("\n Result for the products where category is sports and price is between 3000 and 5000")
for item in result5["hits"]["hits"]:
    print(item["_source"]);

# Task 2: find products name = football OR basketball, price > 3000

query6 = {
    "query": {
        "bool": {
            "should": [
                {"match": {"name": "football"}},
                {"match": {"name": "basketball"}}
            ],
            "filter": [
                {
                    "range": {
                        "price": {
                            "gt": 3000
                        }
                    }
                }
            ], 
            "minimum_should_match" : 1
        }
    }
}

result6 = es.search(index="products", body=query6)

print("\n Result for the products where product name is football or basketball, where price is greater than 3000")
for item in result6["hits"]["hits"]:
    print(item["_source"]);

# Task 3: Exclude furniture category and price less than 5000

query7 = {
    "query": {
        "bool": {
            "must_not" :[
                {"match": {"category" : "furniture"}}
            ],
        "filter": [
            {
                "range": {
                    "price" : {
                        "lt": 5000
                    }
                }
            }
        ]
        }
    }
}

result7 = es.search(index="products", body=query7)

print("\n Result for the products where product category not in furniture and price less than 5000")
for item in result7["hits"]["hits"]:
    print(item["_source"])