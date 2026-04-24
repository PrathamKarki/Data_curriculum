# Learning about intermediate ORM concepts such as group by, having, joins and relationships
from sqlalchemy import create_engine, Column, func, Integer, String, Float, and_, or_, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine("sqlite:///IntermediateORM.db")
Base = declarative_base()

# Creating of the model
class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    # One to Many relationship: category has many products
    # what this means is "euta category can have multiple products"
    products = relationship("Product", back_populates = "category")


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float)
    category_id = Column(Integer, ForeignKey('categories.id'))
    
    # Relationship to Category
    category = relationship("Category", back_populates="products")

# Create all the tables 
Base.metadata.create_all(engine)

# Creating a session
Session = sessionmaker(bind= engine)
session = Session()

# Inserting of the data into the Category Table
cat1 = Category(name = "Electronics")
cat2 = Category(name = 'Fashion')
cat3 = Category(name = "Accessories")

# Insrting of the data into the Product Table
products = [
    Product(name = 'Laptop', price = 120000, category = cat1),
    Product(name = 'Monitor', price = 15000, category = cat1),
    Product(name = 'Shirt', price = 1200, category = cat2),
    Product(name = 'Tennis Ball', price = 100, category = cat3),
    Product(name = 'Pant', price = 1567, category = cat2),
    Product(name = 'Printer', price = 1200, category = cat1)
]

session.add_all([cat1, cat2, cat3])
session.add_all(products)
session.commit()


# Understanding GROUP BY in ORM with joins

result = session.query(Category.name, func.count(Product.id)).join(Product).group_by(Category.id).all()

print("\n Showing the name of the proudct and how many of them are there\n")
for name, count in result:
    print(f"{name} has {count} products")

print("\n")

# Understanding the Having in ORM
output = session.query(Category.name, func.count(Product.id).label("Product count")).join(Product).group_by(Category.id).having(func.count(Product.id) > 2).all()

for name, count in output:
    print(f"{name} has {count} products")

print("\n")

# Working on some practice problems

# Count how many products are in each category

task1 = session.query(Category.name, func.count(Product.id).label("Product count")).join(Product).group_by(Category.id).all()

for name, count in task1:
    print(f"{name} has {count} products")

print("\n")


# List categories that have more than 2 products (use HAVING)
task2 = (
        session.query(Category.name, func.count(Product.id)
           .label("Product count"))
           .join(Product).
           group_by(Category.id).having(func.count(Product.id) > 2).all()
        )

for name, count in task2:
    print(f"{name} has {count} products ")


# Find all the products in the "Fashion" Category using a join
task3 = (
    session.query(Product.name).join(Category).filter(Category.name == 'Fashion').all()
)

print("\n")
for item in task3:
    print(f"{item}")

print()

# Get the average price of products per category
task4 = (
    session.query(Category.name, func.avg(Product.price)
            .label("Average price"))
            .join(Product)
            .group_by(Category.id)
            .all()
      )

for name, price in task4:
    print(f"{name} has an average price of {price}")

