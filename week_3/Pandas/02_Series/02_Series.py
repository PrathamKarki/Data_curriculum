# Series in Pandas
import pandas as pd
import numpy as np

# import the file with read csv and then convert to series
# Squeeze() converts its to series
subsfile = pd.read_csv('../Datasets/subs.csv')

# importing the file with reaad csv for file with 2 columns
cricketFile = pd.read_csv('../Datasets/kohli_ipl.csv', index_col= 'match_no').squeeze()

# Importing of the another file
bollywoodData = pd.read_csv("../Datasets/bollywood.csv", index_col='movie').squeeze()



# Learning about the series methods
# head and tail
# sample
# value_counts
# sort_values

# head: give preview of the data (first 5 rows)
print(bollywoodData.head())

# tail: give preview of the data (last 5 rows)
print(bollywoodData.tail())

# sample: give us randomly one row from our dataset
# also you can specify the number like sample(5) give random five rows
print(bollywoodData.sample())


# value_counts: checks for frequency count 
print(bollywoodData.value_counts())


# sort_values: sorts in ascending order
# doesn't peform change in original value: if wanna change in og then use inplace=True
print(cricketFile.sort_values())

print(cricketFile.sort_values(ascending=False)) # gives in descending


# sort_index : sorts the dataframe or series by its 
bollywoodData.sort_index()

# Some mathematical methods in Series
# count (it doesn't count missing values)
# sum
# mean , median, mode, std, var
# min/max
# describe

# count
print(cricketFile.count())

# sum 
print(subsfile.sum())

# mean : average subscriber


# Series Indexing
x = pd.Series([12, 13, 14, 35, 46, 57, 58, 79, 9])
print(x[1])


