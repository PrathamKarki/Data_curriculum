# Learning about the groupby in pandas
import pandas as pd
import numpy as np

information = {
    "Name": ["A", "B", "C", "D", "E"],
    "city": ["Kathmandu", "Pokhara", "Kathmandu", "Pokhara", "Kathmandu"],
    "sales": [100, 200, 150, 300, 250]
}

# creation of the dataframe
df = pd.DataFrame(information)


# Group by city based on their sales
# here we split dataframe based on "city" column, perform transformation/ aggregation as sum and combine 

sales_based_on_cities = df.groupby("city")["sales"].sum()

print(sales_based_on_cities.head())


# Working with the multiple aggregations
multipleAggregations = df.groupby("city")["sales"].agg(["sum", "mean", "count", "max", "min"])

print(multipleAggregations.head())



# group by with multiple columns ie. city and product

df2 = pd.DataFrame({
    "City" : ["Kathmandu", "Kathmandu", "Pokhara", "Pokhara"],
    "Product" : ["A", "B", "A", "B"],
    "Sales": [100, 200, 300, 400]
})


# grouping by based on city and product and then sales

multiGroup = df2.groupby(["City", "Product"])["Sales"].sum().reset_index()

print(multiGroup.head())


# Group entire dataframe

entireDf = df.groupby("city").sum()

print(entireDf.head())