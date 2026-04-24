# Part 1: Learning on creating engine and execution of the query 

# Task 1 : Creating of SQLite Engine and execution of query "SELECT 5 + 5"

from sqlalchemy import create_engine
from sqlalchemy import text

engine = create_engine('sqlite:///mainDB.db')

def simpleQueryExecution():
    with engine.connect() as conn:
        output = conn.execute(text("SELECT 5 + 5")).scalar()
        print(output)  # all() returns output as list of rows as tuples
        sqlite_versionResult = conn.execute(text("SELECT sqlite_version()"))
        print(sqlite_versionResult.all())



# Task 2: executes some of queries
''' 
"SELECT 10 * 3"
"SELECT 100 / 4"
"SELECT 'Hello SQLAlchemy'"
'''

def executeSomeQueries():
    with engine.connect() as conn:
        query1 = conn.execute(text("SELECT 10 * 3")).scalar()
        query2 = conn.execute(text("SELECT 'Hello SQLAlchemy'")).scalar()
        query3 = conn.execute(text("SELECT 100/4"))
        dateTime = conn.execute(text("SELECT datetime('now')"))
        print(query1)
        print(query2)
        print(query3.all())
        print(dateTime.all())

executeSomeQueries()

simpleQueryExecution()