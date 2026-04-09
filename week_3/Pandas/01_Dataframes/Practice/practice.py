import pandas as pd

customers = pd.DataFrame({
    "customer_id": [1,2,3,4,5],
    "name": ["Ram", "Sita", "Hari", "Gita", "Nabin"],
    "city": ["Kathmandu", "Pokhara", "Kathmandu", "Lalitpur", "Pokhara"]
})


orders = pd.DataFrame({
    "order_id": [101, 102, 103, 104, 105, 106],
    "customer_id": [1,1,2,3,3,6],
    "amount": [500, 300, 700, 200, 400, 900]
})


# Section a: basic dataframe and filtering
# Show all customers from kathmandu
kathmandu_customers =  customers[customers["city"] == 'Kathmandu']
print(kathmandu_customers)

# Show all orders where amount > 400
orders = [orders['amount'] > 400]
print(orders)

# Select only name and city
values = customers[["name", "city"]]
print(values)

# Get the first 3 rows of orders
firstThree = orders.iloc[:3]
print(firstThree)

# get row 2 to 4 from customers , and all columns
output = customers.iloc[2:5, :]
print(output)

# Practice on Groupby 
# Find total order amount per customer_id

total_amount_per = pd.merge(customers, orders, on="customer_id").groupby('customer_id')["amount"].sum()
print(total_amount_per)


# Average order amount per customer_id
avg_amt_customer_id = pd.merge(customers, orders, on="customer_id").groupby("customer_id")["amount"].mean()
print(avg_amt_customer_id)


# Which customer_id has the highest total order amount
highest_order_amount = pd.merge(customers, orders, on="customer_id").groupby("customer_id")["amount"].sum()

highest_customer_id = highest_order_amount.idxmax()

print(higheest_customer_id)



# Merge
# Inner join customers + orders
innerJoin = pd.merge(customers, orders, on="customer_id")
print(innerJoin)

# left join customers + orders
leftJoin = pd.merge(customers, orders, on="customer_id", how="left")
print(leftJoin)

# Find customers who have no orders

leftJoins = pd.merge(customers, orders, on="customer_id", how="left")
no_orders = leftJoins[leftJoins["amount"].isna()]
print(no_orders)


# Display and show name, city , amount
information = pd.merge(customers, orders, on="customer_id")
display = information[["name", "city", "amount"]]
print(display)



# Section D: Pipeline
# Find total spending per customer by name

inf = pd.merge(customers, orders, on="customer_id")
grouping  = inf.groupby("name")["amount"].sum()

print(grouping)


# Find total spending per city
merging= pd.merge(customers, orders, on="customer_id")
city = merging.groupby("city")["amount"].sum()

print(city)


# Find customers whose total spending > 600
merged = pd.merge(customers, orders, on="customer_id")
spending = merged.groupby("customer_id")["amount"].sum()
filtered = spending[spending > 600]
print(filtered)

