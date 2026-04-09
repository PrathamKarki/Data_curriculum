# Concatenation of the dataframes 
import pandas as pd
import numpy as np

# df1 and df2
data1 = {
    'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
    'Age': [27, 24, 22, 32],
    'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
    'Qualification': ['Msc', 'MA', 'MCA', 'Phd'],
    'Mobile No': [97, 91, 58, 76]
}

data2 = {
    'Name': ['Abhi', 'Ayushi', 'Dhiraj', 'Hitesh'],
    'Age': [17, 14, 12, 52],
    'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
    'Qualification': ['Btech', 'B.A', 'Bcom', 'B.hons'],
    'Salary': [1000, 2000, 3000, 4000]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

concatDoc = pd.concat([df1, df2])

# print(concatDoc)

# Merge() in Pandas
# Merge is used to combine two or more data frames based on common columns, indicies just like similar to sql joins

customers = pd.DataFrame({
    "customer_id" : [1,2,3],
    "name": ["Ram", "Sita", "Hari"]
})

orders = pd.DataFrame({
    "customer_id" : [1, 1, 2],
    "order_amount": [500, 300, 700]
})

print(customers)
print(orders)

# merge() them based on common column called 'customer_id'
print(pd.merge(customers, orders, on='customer_id'))


# left join using the merge()
print(pd.merge(customers, orders , on="customer_id", how='left'))


# right join using the merge()
print(pd.merge(customers, orders, on="customer_id", how="right"))


# full outer join using the merge()
print(pd.merge(customers, orders, on="customer_id", how="outer"))


# implementation of the right join 
print(pd.merge(customers, orders, on="customer_id", how="right"))
