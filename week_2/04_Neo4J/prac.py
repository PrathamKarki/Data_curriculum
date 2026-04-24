from neo4j import GraphDatabase

url = 'bolt://localhost:7687'
username = 'neo4j'
password = 'password'

driver = GraphDatabase.driver(url, auth=(username, password))

# Testing for the initial connection 
def test_connection():
    with driver.session() as session:
        result = session.run("RETURN 'hello welcome to neo4j' as message")
        for record in result:
            print(record["message"])

test_connection()

# Creation of the basic node
def create_people(name):
    with driver.session() as session:
        session.run("CREATE (p:Person {name: $name})", 
                    name=name)

create_people("jack")
create_people("jill")
create_people("shaun")


# Displaying of all the people
def get_people():
    with driver.session() as session:
        result = session.run("MATCH (p:Person) RETURN p.name as name")


        