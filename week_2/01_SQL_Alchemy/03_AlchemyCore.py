from sqlalchemy import create_engine
from sqlalchemy import (
    Integer, String, MetaData, Table, Column, insert, select, update, delete, func)

engine = create_engine('sqlite:///myLearningDB.db')

# Creating of table called 'products'
metadata = MetaData()

products = Table(
    "products", 
    metadata, 
    Column('id', Integer, primary_key= True),
    Column('name', String),
    Column('price', Integer)
)

# Creates table (only if not exists)
metadata.create_all(engine)

# Inserting of values in table called 'products'

with engine.connect() as conn:
    
    conn.execute(insert(products), 
        [
            {'id': 1, 'name': 'laptop', 'price': 1000},
            {'id': 2, 'name': 'Phone', 'price': 500 },
            {'id': 3, 'name': 'Tablet', 'price': 800},
            {'id': 4, 'name': 'Monitor', 'price': 400},
            {'id': 5, 'name': 'Keyboard', 'price': 200}
        ]
    )
    conn.commit()

# Filtering and more  (Practice 3)
# Get all the products

with engine.connect() as conn:
    slt = select(products)
    result = conn.execute(slt)
    
    for row in result:
        print(row)


# Get products where price > 600
with engine.connect() as conn:
    stmt =  (select(products).where(products.c.price > 600))
    result = conn.execute(stmt)
    for row in result:
        print(row)


# Get products where price < 600
with engine.connect() as conn:
     stmt = (select(products).where(products.c.price < 600))
     result = conn.execute(stmt)
     for row in result:
         print(row)

# (Practice 4)
# Select only specific columns ie productname
with engine.connect() as conn:
    stmt = select(products.c.name).where(products.c.price > 1000)
    result = conn.execute(stmt)
    for item in result:
        print(item)

# (Practice 5)
# Change the price of "phone" from 500 -> 550

with engine.connect() as conn:
    stmt = update(products).where(products.c.name == 'Phone').values(price = 550)
    conn.execute(stmt)
    conn.commit()
    
# (Practice 6)
# Delete the product with name "Monitor"
with engine.connect() as conn:
    stmt = delete(products).where(products.c.name == 'Monitor')
    conn.execute(stmt)
    conn.commit()
    

# (Practice 7)
# Products with price BETWEEN 300 and 900

with engine.connect() as conn:
    stmt = select(products).where(products.c.price.between(300, 900))
    result = conn.execute(stmt)
    for item in result:
        print(item)

    
# Practice 8
# specific columsn and filter (name and price, price > 400)

with engine.connect() as conn:
    stmt = select(products.c.name, products.c.price).where(products.c.price > 400)
    result = conn.execute(stmt)
    for item in result:
        print(item)

# Update of multiple rows
with engine.connect() as conn:
    stmt = update(products).values(price=products.c.price + 100)
    conn.execute(stmt)
    conn.commit()

# Insert of more data 
# ADD 2 new products using batch insert

with engine.connect() as conn:
    conn.execute(insert(products),
                 [
                     {'id': 6 , 'name':'Earphone', 'price': 150},
                     {'id': 7,  'name': 'Speaker', 'price': 200 }
                 ])
    conn.commit()


# Aggreate Task
with engine.connect()as conn:
    statement = select(func.max(products.c.price))
    result = conn.execute(statement)
    print(result.scalar())