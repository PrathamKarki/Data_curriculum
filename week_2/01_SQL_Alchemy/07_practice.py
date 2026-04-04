from sqlalchemy import(
     create_engine, text, Column, Integer, Float, String, insert, inspect
)
from sqlalchemy.orm import (
    declarative_base, sessionmaker
)
engine = create_engine("sqlite:///practicesDB.db")

Base = declarative_base()

# Creating of an model called Item
class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key= True)
    name = Column(String)
    price = Column(Float)
    deliveryAddress = Column(String)

Base.metadata.create_all(engine)

# Creating of the session 
Session = sessionmaker(bind=engine)
session = Session()

# Creating of the Object States
item1 = Item(name = "Pen", price = 50, deliveryAddress = 'Chabahil')

# Inspecting if item1 is a transient
print("Item1 is a transient: ", inspect(item1).transient)


#Addubg the item1 into the session 
session.add(item1)
# Checking if the item1 is pending or not
print("Inspecting the Item1 if it is pending or not :", inspect(item1).pending )

# Commiting the item1 into the session 
session.commit()
#checking if the item1 is persistent or not
print("Insepcting if item1 is persistent or not: ", inspect(item1).persistent )


# Inserting of the 3 more items
item2 = Item(name = "Book", price = 300, deliveryAddress = 'boudha')
item3 = Item(name = "Bag", price = 800, deliveryAddress = 'jorpati' )
item4 = Item(name = "Bottle", price = 150, deliveryAddress = 'Bansbari' )

session.add_all([item2, item3, item4])
session.commit()

# Quering all the items and displaying them 
stationaryItems = session.query(Item).all()

print('------- Displaying of all the stationary Items ------------\n\n')
for i in stationaryItems:
    print(i.name, i.price, i.deliveryAddress)


# Rollback()
item5 = Item(name = "TempItem", price = 999, deliveryAddress = 'JPN')

session.add(item5)

session.rollback()

print("\n\n------- Displaying of all the items to see if TempItem is present or not\n")
statItem = session.query(Item).all()
for i in statItem:
    print(i.name, i.price, i.deliveryAddress)


# Section 5: Flush vs Commit
item6 = Item(name = 'FlushItem', price= 500)

session.add(item6)
session.flush()

print("after flush id for item6 is", item6.id)

session.rollback()

print("IS the flushItem present: ", item6.id)



# Task 10 : Fetch item "Book" and change price to 350 and commit
fetchBook = session.query(Item).filter_by(name='Book').first()

if fetchBook:
    fetchBook.price = 350
    session.commit()

# fetching the item book and changing its price to 350 and commiting
print("\n\n Fetching the item book and changing the price to 350")
print(fetchBook.name, fetchBook.price, fetchBook.deliveryAddress)


# Task 11 : Delete the item "bottle" and commit and query all items and confirm deletion

fetchItems = session.query(Item).filter_by(name = 'Bottle').first()

if fetchItems:
    session.delete(fetchItems)
    session.commit()

allItems  = session.query(Item).all()

for item in allItems:
    print(item.name, item.price, item.deliveryAddress)