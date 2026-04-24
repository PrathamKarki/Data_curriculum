from sqlalchemy import create_engine, Column, Integer, Float, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///databaseDB.db")

Base = declarative_base()

# Creating a product Model 
class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)


Base.metadata.create_all(engine)

# Task 1: Creating session before inserting of the data
Session = sessionmaker(bind=engine)
session = Session()


p1 = Product(name = 'Book', price = 300)
p2 = Product(name = 'Pen', price = 50)
p3 = Product(name = 'Bag', price = 800)

session.add(p1)
session.add(p2)
session.add(p3)

# session.add_all([p1, p2, p3])  can be done like this also


# Task 2: print all products

allProducts = session.query(Product).all()

for p in allProducts:
    print(p.name, p.price)


# Task 3 Filter products where
filterProduct = session.query(Product).filter(Product.price > 200).all()

for fp in filterProduct:
    print(fp.name, fp.price)

# note: This query worked even though we didn't commit because 
# Session has pending objects and query is read form session cache and db

session.add(Product(name= "Test", price = 999))

session.rollback()

result = session.query(Product).all()

for res in result:
    print(res.name, res.price)

#-------------------- Important Concept ------------------------------------
# Understanding about 4 states of object, how does SQLAlchemy trakcs objects internally: 
'''
    1. Transient
        - object created but not in session 
        eg; p = Product(name = "aaron")

    2. Pending 
        - added to session but Not commited yet
        eg: session.add(p)
    
    3. Persistent
        - Saved in the database (after commit)
        eg: session.commit()
    
    4. Deleted
        - Marked for deletion
        eg: session.delete(p)

'''


# Task 1: Print the object states: (4 states: transient, pending , persistent)

from sqlalchemy import inspect

# Creating the object  but not in session (transient)
p = Product(name="Handicrafs", price = 1200)
print("Transient for the created object is :", inspect(p).transient)

# Adding the created object to the session (pending)
session.add(p)
print("Pending of the object after adding it to the session:", inspect(p).pending)

# Persistent : after being saved to the database
session.commit()
print("Persistent after the object is added to the session:", inspect(p).persistent)

# Deleted
session.delete(p)
print("After the deletion", inspect(p).persistent)


# Understanding of the rollback() in session 
# creating of the obj
obj1 = Product(name = "Salad", price = 175)

session.add(obj1)

session.rollback()

disResult = session.query(Product).filter_by(name = 'Salad').all()

print("after rollback: ", disResult)

for res in disResult:
    print(res.name, res.price)


# Flush and commit in the ORM 

