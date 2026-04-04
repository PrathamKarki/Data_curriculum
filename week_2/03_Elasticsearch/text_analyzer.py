from elasticsearch import Elasticsearch
from elasticsearch import helpers

es = Elasticsearch("http://localhost:9200")

print(es.info())

# Use of the analyze api 
response = es.indices.analyze(
    body={
        "analyzer": "standard",
        "text": "Football Shoes"
    }
)

print("\nTokens:")
for token in response["tokens"]:
    print(token["token"])


# trying with another example
res = es.indices.analyze(
    body={
        "analyzer": "standard",
        "text": "Mo Salah is playing football"
    }
)

print("\nTokens are:")
for token in res["tokens"]:
    print(token["token"])


# Trying different analyzers
resp = es.indices.analyze(
    body={
        "analyzer": "whitespace",
        "text": "football-shoes"
    }
)

print("\n The tokens for the analyzers as whitespace is given as:")
for token in resp["tokens"]:
    print(token["token"])  # output:  football-shoes


# Trying and testing with the standard analyzer
r = es.indices.analyze(
    body = {
        "analyzer": "standard",
        "text": "football-shoes"
    }
)

print("\n The token for the analyzer is given as:")
for token in r['tokens']:
    print(token["token"]) # Output as : football, shoes


# testing with the whitespace analyzer

ressponse = es.indices.analyze(
    body = {
        "analyzer": "whitespace",
        "text": "Mo salah is the-best-player in the world"
    }
)


print("\nThe token for the analyzer is given as:")
for token in ressponse['tokens']:
    print(token["token"]) 