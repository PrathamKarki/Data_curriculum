# Diving deeper into the ORM  concept
# filter() vs filter_by()
# Multiple conditions
# Ordering (order_by)
# Limiting (limit)

from sqlalchemy import create_engine, Column, Integer, Float, String 
from sqlalchemy.orm import sessionmaker, declarative_base
engine = create_engine('sqlite:///DeepORMdb.db')

# Parents for all models
Base = declarative_base()

# Creating models 
class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

# Create Table

Base.metadata.create_all(engine)


# Creating of the session 
Session = sessionmaker(bind=engine)
session = Session()

product1 = Product(id= 1, name = 'Bagpack',   price = 1200)
product2 = Product(id= 2, name = 'Laptop',    price = 125000)
product3 = Product(id= 3, name =  'Monitor',   price = 300000)
product4 = Product(id= 4, name =  'Printer',   price = 12000)
product5 = Product(id= 5, name =  'Scanner',   price = 40000 )
product6 = Product(id = 6, name = 'Notebook', price = 250)
product7 = Product(id = 7, name = 'Carpet', price = 12000)
product8 = Product(id = 8, name = 'Bottle', price = 200)

session.add(product1)
session.add(product2)
session.add(product3)
session.add(product4)
session.add(product5)
session.add(product6)
session.add(product7)
session.add(product8)

session.commit()

# Displaying the content of the table
 
displayProducts = session.query(Product).all()

for item in displayProducts:
    print(item.id, item.name, item.price)

# Filtering of the data 

expensive = session.query(Product).filter(Product.price > 600).all()

for p in expensive:
    print(p.name)

session.commit()


# Filtering of the data where price is less than 300
cheapest = session.query(Product).filter(Product.price < 300).all()

for cheap in cheapest:
    print(cheap.name)

session.commit()


# Display the product called 'Scanner'

productScanner = session.query(Product).filter_by(Product.name == 'Scanner').first()

print(productScanner);