# Initial connection for the graphdatabase

from neo4j import GraphDatabase

url = "bolt://localhost:7687"
username = 'neo4j'
password = 'password'

driver = GraphDatabase.driver(url, auth=(username, password))


# running the engine

def test_connection():
    with driver.session() as session:
        result = session.run("RETURN 'THIS IS neo4j' as message")
        for record in result:
            print(record["message"])
        
# STEP 1: Creating of the basic node
def create_peoples(name):
    with driver.session() as session:
        session.run("CREATE (p.Person {name: $name})",
        name=name )

create_peoples("Ram")
create_peoples("Hari")
create_peoples("Iyer")


# Displaying of the people
print("\n---------Displaying of the people -------")

def get_some_people():
    with driver.session as session:
        result = session.run("MATCH (p:Person) RETURN p.name AS name")
        for record in result:
            print(record["name"])

get_some_people()


