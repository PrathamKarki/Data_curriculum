# practicing on categorical variables 
import pandas as pd
import numpy as np

info = pd.Series(["Python", "Java", "Python", "C++", "Java", "Python"])

# Tasks
# Count each language
count = info.value_counts()
print(count)

# find percentage distribution for each 
percentage_distribution =  info.value_counts(normalize=True) * 100
print("The percentage distribution is\n", percentage_distribution)

# find the mode
mode_info = info.mode()
print("The mode of given data is :", mode_info)

# Number of unique values

no_of_values = info.nunique()
print(no_of_values)


# Convert the data into the ordered categorical
ratings = pd.Series(["Low", "High", "Medium", "Medium", "Low", "High", "Medium"])

ratings = ratings.astype(
    pd.CategoricalDtype(categories=["Low", "Medium", "High"], ordered=True)
)

print(ratings)

# Count each category
print(ratings.value_counts())

# Find mode
print(ratings.mode())

# which is highest category?
print(ratings.max())
