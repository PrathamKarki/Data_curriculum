from neo4j import GraphDatabase

url = 'bolt://localhost:7687'
username = "neo4j"
password = "password"

driver = GraphDatabase.driver(url, auth=(username, password))

# First test query
def test_query():
    with driver.session() as session:
        result = session.run("RETURN 'Hello welcome to Neo4j' as message")
        for record in result:
            print(record["message"])
test_query()


# Create node from python 
def create_person(name):
    with driver.session() as session:
        session.run(
            "CREATE (p:Person {name: $name})",
            name=name
        )

create_person('Alice')
create_person("Bob")
create_person('Jason')


# Reading of the data 
def get_people():
    with driver.session() as session:
        result = session.run("MATCH (p:Person) RETURN p.name as name")
        for record in result:
            print(record["name"])

get_people()


# Creating the relationship

def create_relationship(person1, person2, person3):
    with driver.session() as session:
        result = session.run("""
                            MATCH (a:Person {name: $p1})
                            MATCH (b:Person {name: $p2})
                            MATCH (c:Person {name: $p3})
                            CREATE (a)-[:KNOWS]->(b)
                            CREATE (a)-[:KNOWS]->(c)
                            """, p1=person1, p2=person2, p3=person3)

create_relationship("Alice", "Bob", "Jason")