from neo4j import GraphDatabase

url = "bolt://localhost:7687"
username = "neo4j"
password = "password"

driver = GraphDatabase.driver(url, auth=(username, password))

# Testing for the initial connection 
def test_connection():
    with driver.session() as session:
        result = session.run("RETURN 'Hello welcome to neo4j' as message")
        for record in result:
            print(record["message"])

test_connection()


# Creation of the basic node
def create_people(name):
    with driver.session() as session:
        session.run("CREATE (p:Person {name: $name})",
        name=name
        )

create_people("Ram")
create_people("Sita")
create_people("Hari")


# Displaying all the people
def get_people():
    with driver.session() as session:
        result = session.run("MATCH (p:Person) RETURN p.name AS name")
        for record in result:
            print(record["name"])


get_people()

# Creation of the relationship
def create_relationship(person1, person2, person3):
    with driver.session() as session:
        result = session.run("""
                              MATCH (a:Person {name: $p1})
                              MATCH (b:Person {name: $p2})
                              MATCH (c:Person {name: $p3})
                              CREATE (a)-[:KNOWS]->(b)
                              CREATE (b)-[:KNOWS]->(c)
                              CREATE (c)-[:KNOWS]->(a)
                            """, p1=person1, p2=person2, p3=person3)
        
create_relationship('Ram', 'Sita', 'Hari')


# Task 1: Find out who sita knows
def she_knows():
    with driver.session() as session:
        result = session.run("MATCH (p:Person {name:'Sita'})-[:KNOWS]->(friend)" \
        " RETURN friend.name AS name")
        for record in result:
            print(record["name"])

she_knows()

# Task 2: Find who knows sita
def who_knows_sita():
    with driver.session() as session:
        result = session.run("MATCH (person.Person)-[:KNOWS]->(s:Person {name: 'Sita'}) " \
        "RETURN person.name AS name")
    for record in result:
        print(record["name"])


who_knows_sita()


# Task 3: Find mutual friends
def mutual_friends(p1, p2):
    with driver.session() as session:
        result = session.run("""
                            MATCH (a:Person {name: $p1})-[:KNOWS]->(mutual:Person)<-[:KNOWS]-(b:Person {name: $p2})
                            RETURN mutual.name AS name
                            """, p1=p1, p2=p2)
        for record in result:
            print(record["name"])


mutual_friends("Ram", "Sita")


# Task 4: 
def knows_ram():
    with driver.session() as session:
        result = session.run("MATCH (person.Person)-[:KNOWS]->(s.Person {name: 'Ram'})" \
        "RETURN person.name as name")
    for record in result:
        print(record["name"])
    

knows_ram()


