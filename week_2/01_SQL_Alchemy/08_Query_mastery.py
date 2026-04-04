# here we cover about :  filter(), filter_by(), AND, OR, order_by, limit, and some aggregations

from sqlalchemy import create_engine, Column, Integer, Float, String
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy  import or_ , and_, desc, func

engine = create_engine("sqlite:///queryDB.db")
Base = declarative_base()

# Creating of the model
class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    category = Column(String)

Base.metadata.create_all(engine)

# Creating of the session 
Session = sessionmaker(bind=engine)
session = Session()

# Inserting of the sample datas (first we create object and add them to session)
products = [
    Product(name = "Laptop", price = 1000, category = 'Electronics'),
    Product(name="Phone", price=500, category="Electronics"),
    Product(name="Tablet", price=800, category="Electronics"),
    Product(name="Shoes", price=150, category="Fashion"),
    Product(name="Shirt", price=80, category="Fashion"),
    Product(name="Watch", price=300, category="Accessories"),
]
session.add_all(products)
session.commit()

# Step 3: Understanding filter() vs filter_by()
# filter_by()
ElectronicProducts = session.query(Product).filter_by(category = 'Electronics').all()

print("\n---- Displaying only the products whose category is Electronics-------\n")
for elc in ElectronicProducts:
    print(elc.name, elc.price, elc.category)

# filter()
# Displaying all the products whose price is greater than 800 
ExpensiveProducts = session.query(Product).filter(Product.price >= 800).all()

print("\n--- Displaying the products whose price is greater than 800-----\n")
for elec in ExpensiveProducts:
    print(elec.name, elec.price, elec.category)


# Multiple Conditions (AND) : display proudcts whose price is less than 800 and catgory IS Fashion
multiCondition = session.query(Product).filter(and_(Product.price < 800, Product.category == "Fashion")).all()

print("\n-- Displaying the products whose price is less than 800 and category is Fashion\n")
for multi in multiCondition:
    print(multi.name, multi.price, multi.category)


# Multiple condition using the OR operator
# display products for either category is fashion or electronics
orOperation = session.query(Product).filter(or_(Product.category == 'Fashion', Product.category == 'Electronics')).all()

print("\n -- Displaying the product whose category is either Electronics or Fashion\n")
for item in orOperation:
    print(item.name, item.price, item.category)


# Ordering in the sqlalchemy
orderingItems = session.query(Product).filter(Product.price > 200).order_by(desc(Product.price)).all()

print("\n-- Displaying all the products greater than 200 and ordering them by descending order\n")

for orderItm in orderingItems:
    print(orderItm.name, orderItm.price, orderItm.category)


# Limit in the sqlalchemy
limitingItems = session.query(Product).filter(Product.price > 500).order_by(desc(Product.price)).limit(2).all()

print("\n---Limiting the products greater than 500 by 3\n")

for itm in limitingItems:
    print(itm.name, itm.price, itm.category)


# aggreations in the sqlalchemy
# display  the maximum price 
max_price = session.query(func.max(Product.price)).scalar()
print("\n Displaying the maximum product based on their price")
print(max_price)

# display the avgerage price
avg_price = session.query(func.avg(Product.price)).scalar()
print("Average price of the product:", avg_price)


# Doing other tasks 
# Task 1
# Get all products where price is greater than 200 and category = "Electronics"
task1 = session.query(Product).filter(and_(Product.price > 200, Product.category == 'Electronics')).all()

print("\n Displaying all the products\n")
for t1 in task1:
    print(t1.name, t1.price, t1.category)

# Task 2 
# Get products where price < 100 or category = 'Accessories'
task2 = session.query(Product).filter(or_(Product.price < 100, Product.category == 'Accessories')).all()

print("\n Displaying the products where price is less than 100 or category is equal to Accessories\n")

for t2 in task2:
    print(t2.name, t2.price, t2.category)

# Task 3
# Sort all the products by price descending
task3 = session.query(Product).order_by(desc(Product.price)).all()

print("\n Displaying all the products where the price is in descending order")
for t3 in task3:
    print(t3.name, t3.price, t3.category)


# Task 4
# Get the top 2 most expensive products
task4 = session.query(Product).order_by(desc(Product.price)).limit(2).all()

print("\n Displaying top 2 most expensive products ")
for t4 in task4:
    print(t4.name, t4.price, t4.category)


# Task 5
# Finding the minimum price and total number of products

task5 = session.query(func.min(Product.price), func.count(Product.id)).all()
print(task5)



# Task 6
# Finding the top 2 most cheapest products
task6 = session.query(Product).order_by(Product.price).limit(2).all()

print("\n Displaying top 2 most cheapest products")
for t6 in task6:
    print(t6.name, t6.price, t6.category)


# Sort all products by price in the descending order

task7 = session.query(Product).order_by(desc(Product.price)).all()

print("\n Displaying all the products sorted in the descending order based on price")

for t7 in task7:
    print(t7.name, t7.price, t7.category)