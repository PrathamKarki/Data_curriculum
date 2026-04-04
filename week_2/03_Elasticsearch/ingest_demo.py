# Step 1: Create a connection 
from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

print(es.info())

# Step 2: Create an ingest pipeline
es.ingest.put_pipeline(
    id = "my_pipeline",
    body = {
        "description" : "Lowercase name field",
        "processors": [
            {
                "lowercase": {
                    "field": "name"
                }
            }
        ]
    }
)

# Inserting the data using pipeline

doc = {
    "name": "Football Shoes",
    "price": 5000,
    "category": "sports"
}

es.index(
    index= "products_pipeline",
    document=doc,
    pipeline="my_pipeline"
)

res = es.search(index="products_pipeline", body={"query" : {"match_all" : {}}})

print("\nStored Data:")
for item in res["hits"]["hits"]:
    print(item["_source"])
    