# Learning about the categorical varaiables in statistics
# Types of categorical varaiables
# 1. Nominal (doesn't have order)
# 2. Ordinal (has order)
import statistics as stats
import pandas as pd

# mode with categorical variable
datas = ["Red", "Blue", "Red", "Green", "Blue", "Red"]

# what type of variable is it?
# it's a nominal  as it has no order, and isn't comparable like red > green


# Creating of categorical data
data = pd.Series(["Red", "Blue", "Red", "Green", "Blue", "Red"])
print(data)

# Count for the categorical data
# frequency distribution 
print(data.value_counts())

# find the mode for the given categorical data
mode_val = data.mode()
print(mode_val)

# find the percentage (convert the categorical data into percentage)
percentage = data.value_counts(normalize=True) * 100
print(percentage)

# finding of the unique categories
uniqueCat = data.unique()
print(uniqueCat)

# Converting to the "category" type
data = data.astype("category")
print(data.dtype)

# Understanding Nominal vs ordinal 
# Nominal 
foods = pd.Series(["Red", "Green", "Blue"])
# doesn't have any order so it's nominal

# Ordinal (with order)
levels = pd.Series(["Low", "Medium", "High"])
order = pd.Categorical(levels, categories=["Low", "Medium", "High"], ordered=True)