import pandas as pd
import numpy as np


# Creating of the student dataframe
student_df = pd.DataFrame({
    "Name" : ["Aaarva", "Sita", "Ram", "Gita", "Krishna", "Maya", "Arjun", "Laxmi"],
    "Math" : [78, 92, 56, 81, 67, 88, 45, 73],
    "Science": [85, 79, 60, 90, 72, 95, 50, 68],
    "English": [80, 88, 58, 77, 69, 91, 55, 70],
    "Attendance (%)": [92,85,70,95,88,96, 65, 80]
})

# Select only the name column
print(student_df["Name"])

# Get the first 4 students
print(student_df.head())


# Get last 2 students using the iloc
print("\n--------\n")
print(student_df.iloc[-2:])


# Part 2 Column + Row Combination
print("\n-----Part 2: Columns and row combination-------\n")

# Select "Name" and "Math" columns for all students
print(student_df.loc[:, ["Name", "Math"]])

# Marks of "Gita" in all subjects using loc
print(student_df.loc[(student_df.Name == 'Gita'), ["Math", "Science", "English"] ])


# Using iloc , get row 2 , column 3 value
print(student_df.iloc[2, 3])


# Part C: Conditional Filtering 
# Find the students who scored more than 80 in Math
print(student_df.loc[student_df["Math"] > 80])


# Find students with attendance < 80
print(student_df.loc[student_df["Attendance (%)"] < 80])


# Find students who scored ( in math greater than 70 and science less than 80)
print(student_df.loc[(student_df["Math"] > 70) & (student_df["Science"] > 80)])


# Part D: Thinking and Logic
# Find students who are weak in studies
print(student_df.loc[(student_df["Math"] < 60) & (student_df["Science"] < 60) & (student_df["English"] < 60)])

# Find students who are excelletn in studies

print(student_df.loc[(student_df["Math"] > 85) & (student_df["Science"] > 85) & (student_df["English"] > 85)])