from neo4j import GraphDatabase

url = "bolt://localhost:7687"
username = "neo4j"
password = "password"

driver = GraphDatabase.driver(url, auth=(username, password))


def test_connection():
    with driver.session() as session:
        result = session.run("RETURN 'Hello Neo4j' AS message")
        for record in result:
            print(record["message"])

test_connection()

# Creating of the nodes
def create_person(tx, name, age):
    query = """
            CREATE (p: Person {name : $name, age: $age})
            """
    tx.run(query, name=name, age=age)

with driver.session() as session:
    session.execute_write(create_person, "Pratham", 22)
    session.execute_write(create_person, "Ram", 25)
    session.execute_write(create_person, "Hari", 32)

# Creating of relationship
def create_friendship(tx):
    query = """
            MATCH (a:Person {name: "Pratham"}), (b:Person {name: "Ram"})
            CREATE (a)-[:FRIEND]->(b)
            """
    tx.run(query)

with driver.session() as session:
    session.execute_write(create_friendship)

