import pandas as pd
import numpy as np

# using read csv
movies = pd.read_csv("../Datasets/movies.csv")
 
ipl = pd.read_csv("../Datasets/ipl-matches.csv")


# Some of the attributes used in DataFrame
# shape, dtype, index, columns, head and tail, sample, info

print(movies.head())

print(movies.dtypes)

print(movies.index) # gives us entire index

print(movies.columns) # give us all the columns present in the movies dataframe
print(ipl.columns)

print(movies.values) # give us all the values 
print(ipl.values)


# Head and tail 
print(movies.head())
print(ipl.tail())


# info 
print(movies.info())
print(ipl.info())

# describe() provide the statistical information for the numerical columns
print(movies.describe())


# is null
movies.isnull().sum()


# sum
movies.sum(axis=1) # does row wise sum if axis = 1