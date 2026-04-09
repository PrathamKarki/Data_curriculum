import pandas as pd
import numpy as np

# Creating of the dataframe customers and orders
customers = pd.DataFrame({
    "customer_id": [1,2,3,4],
    "name": ["Ram", "Sita", "Hari", "Gita"]
})

orders = pd.DataFrame({
    "customer_id": [1,1,2,5],
    "order_amount": [500, 300, 700, 1000]
})


# looking at the initial table for customer and orders
print(customers)
print(orders)


# Question 1: Perform the inner join 
innerJoing = pd.merge(customers, orders, on="customer_id", how='inner')
print(innerJoing)


# Question 2: Perform left join
leftJoing = pd.merge(customers, orders, on='customer_id', how='left')
print(leftJoing)


# Question 3: Perform the outer join 
outerJoin = pd.merge(customers, orders, on='customer_id', how='outer')
print(outerJoin)


# Question 4: which customers have no orders
performJOin = pd.merge(customers, orders, on='customer_id', how='left')
no_orders = performJOin[performJOin["order_amount"].isnull()]
print(no_orders)


# Question 5: Get total order amount per customer name
info = pd.merge(customers, orders, on="customer_id") \
          .groupby("name")["order_amount"].sum()

print(info)