import pandas as pd

"""
    Series are the sequence of values or data, in pandas it can be considered as a list, 
    if a dataframe is considered as a table.
"""

# Creating of the country series as well as giving the name to series as "nations"
countries = ["Japan", "India", "Germany", "Ghana", "Sweden"]

country = pd.Series(countries, index= ["Asia", "Asia", "Europe", "Africa", "Europe"],
name = "Nations")

print(country)


# Creating of series using the dictionaries
marks = {
    "maths": 77,
    "science": 88, 
    "social studies": 54,
    "English": 89
}

series_s = pd.Series(marks, name="marks of a student")
print(series_s)


# Some of the attributes in Series
# size
print(series_s.size)

#dtype
print(series_s.dtype)

# name
print(series_s.name)

# is_unique
print(series_s.is_unique)


# index
print(series_s.index)

