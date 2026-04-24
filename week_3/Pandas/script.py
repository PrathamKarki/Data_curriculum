import pandas as pd

"""
    Dataframes are those 2D data datastructures, that contains array of individual entires
    each of which these entries have certain value 
"""


# creating of the dataframe
items = pd.DataFrame({
    "food" : ['Burger', 'fries', 'Chicken', 'pizza'],
    "Calories": [180, 120, 150, 1600]
}, index=[1, 2, 3, 4])


# Creating another dataframe for students and their marks
student_df = pd.DataFrame({
    "Students": ["Rami", "Cassidy", 'Madison', 'Max', 'Chloe'],
    "Marks": [87, 72, 45, 88, 92]
}, index=[1, 2, 3, 5, 6])


print(student_df.shape)




