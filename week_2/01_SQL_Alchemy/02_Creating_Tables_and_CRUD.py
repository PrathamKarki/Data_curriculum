from sqlalchemy import create_engine
from sqlalchemy import Table, MetaData, Integer, String, Column, text
from sqlalchemy import insert, select

engine = create_engine('sqlite:///operationDB.db')

metadata = MetaData()

employees = Table(
        "employees",
        metadata,
        Column("id",  Integer, primary_key= True),
        Column("emp_name", String),
        Column("age", Integer),
        Column("address", String)
    )

metadata.create_all(engine)

# Inserting of Data 

with engine.connect() as conn:
    insertValues = insert(employees)
    
    conn.execute(insertValues, [
       {'id': 1, 'emp_name': "Charly", "age": 25, "address": "Kathmandu" },
       {'id': 2, 'emp_name': 'James', 'age': 19, "address": 'teku'},
       {'id': 3, 'emp_name': 'Gordon', 'age': 32, 'address': 'Manhattan'},
       {'id': 4, 'emp_name': "Keneddy", 'age': 38, 'address': 'Jamaica'}
    ])
    conn.commit()

# Selecting of the data

with engine.connect() as conn:
    selectStat = select(employees) 
    result = conn.execute(selectStat)

    for row in result:
        print(row)
    
    lessThan30 = select(employees).where(employees.c.age > 30)
    
    print(lessThan30)