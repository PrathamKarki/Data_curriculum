import pandas as pd
import numpy as np

# Creating of the dataframe
foods_df = pd.DataFrame({ "Food": [
        "Burger", "Pizza", "Pasta", "Fries", "Fried Chicken",
        "Salad", "Ice Cream", "Soda", "Steak", "Sandwich"
    ],
    "Calories": [295, 266, 131, 312, 320, 152, 207, 150, 271, 250],
    "Protein (g)": [17, 11, 5, 4, 25, 5, 3, 0, 26, 12],
    "Fat (g)": [14, 10, 1.1, 15, 20, 10, 11, 0, 19, 8],
    "Carbs (g)": [30, 33, 25, 41, 8, 12, 24, 39, 0, 30]
})

print(foods_df.head())


# INDEXING, SELECTING AND ASSIGNING 
# understanding of the Native accessors (access of property)
# eg
print("\n---Accessing of the property using the dot operatioon----\n")
print(foods_df.Food) # gives us all food but in series


print("\n--Accessing of the property using the [] operator----\n")
print(foods_df["Calories"]) # gives us all calories , in series


print("\n--Another way of using the [] operation with index---\n")
print(foods_df["Food"][2])


# INDEXING IN PANDAS: loc and iloc
# index-based selection: (iloc: selects data based on its numerical position)
print("\n-- Using iloc ----\n")
print(foods_df.iloc[0])

# using iloc to retrive all the rows but only the first column

print(foods_df.iloc[:, 0])


# Selecting of the first 3 food 

print(foods_df.iloc[:3, 0])
 #or   
print(foods_df.iloc[1:3, 0])


print(foods_df.iloc[:5])



# using the loc [Label-based selection ] 

print(foods_df.loc[0, 'Food'])


print(foods_df.loc[:, ['Calories', 'Protein (g)', 'Fat (g)']])



# Conditional selection 

print(foods_df.Food == 'Burger')



print(foods_df.loc[(foods_df.Food == 'Burger') & (foods_df.Calories >=200 )])



# Note: the and operation here is used as '&'  ,   the or operation as '|'




# creation of the dataframe

df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss Elizabeth"
        ]
    }
)


# print(df.loc[1, "Name"])


# print("\n")
# print(df.set_index("Name"))