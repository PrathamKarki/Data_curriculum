# STEP 1: basic ORM setup and import

from sqlalchemy import (
    create_engine, Column, insert, delete, Integer, String, update, 
)
from sqlalchemy.orm import declarative_base, sessionmaker
engine = create_engine('sqlite:///ormDB.db')
# Create a Base class
Base = declarative_base()


# Step 2: Creating a model (table as class)

class Employees(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key= True)
    name = Column(String)
    age = Column(Integer)
    address = Column(String)


# Step 3: Create Table in the DB

Base.metadata.create_all(engine)


# Step 4: Create a session 
Session = sessionmaker(bind=engine)
session = Session()

# Step 5: Inserting data in the ORM way

emp1 = Employees(id = 1, name = 'Jason', age = 24, address = 'kathmandu')
emp2 = Employees(id = 2, name = 'Jackson', age = 32, address = 'Biratnagar')
emp3 = Employees(id = 3, name = 'Shawn', age = 27, address = 'damak')


session.add(emp1)
session.add(emp2)
session.add(emp3)


# Step 6: Querying of the data 

users = session.query(Employees).all()

for user in users:
    print(user.id, user.name, user.age)


# filtering of data

ageLessthan20 = session.query(Employees).filter(Employees.age > 25).all()

for item in ageLessthan20:
    print(item.name, item.age)




# PRACTICE ON BASIC ORM

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///productsDB.db')

Base = declarative_base()

# creating model called product

class Products(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

# This creates the table
Base.metadata.create_all(engine)

# Creating of the session 
Session = sessionmaker(bind=engine)
session = Session()


# Inserting of the products 

produc1 = Products(id = 1, name = 'Burger', price = 550)
produc2 = Products(id = 2, name = 'Pizza', price=  730)
produc3 = Products(id = 3, name = 'Chicken', price = 1200)
produc4 = Products(id = 4, name = 'Mo:Mo', price = 130)


session.add(produc1)
session.add(produc2)
session.add(produc3)
session.add(produc4)

session.commit()


# Fetching all products

fetchProducts = session.query(Products).all()

for item in fetchProducts:
    print(item.id, item.name, item.price)


# filter product where price > 500
filteredProduct = session.query(Products).filter(Products.price > 500).all()

for items in fetchProducts:
    print(items.id, items.name, items.price)


# Adding two more products

product5 = Products(id = 5, name = 'Carrot', price = 50)
product6 = Products(id = 6, name = 'Onion',   price = 120)

session.add(product5)
session.add(product6)
session.commit()


# Product with name = "Pizza"

queryProduct = session.query(Products).filter_by(name = 'Pizza')
print(queryProduct.id, queryProduct.name, queryProduct.price)

# Update : Change "Burger" price to 600

burger = session.query(Products).filter_by(name='Burger').first()
burger.price = 600
session.commit()

# Delete Mo:Mo
momo = session.query(Products).filter_by(name='Mo:Mo').first()
session.delete(momo)
session.commit()