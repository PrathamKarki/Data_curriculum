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


# Grade system implementation using tha apply()

def grades(marks):
    if (marks >= 90):
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "F"
    

student_df["Math_Grade"] = student_df["Math"].apply(grades)


# apply() with lambda

student_df["Science_Result"] = student_df["Science"].apply(
    lambda x: "Pass" if x >= 60 else "Fail"
)

# apply() on Multiple columns 
# Example: Create Overall Average

student_df["Average"] = student_df[["Math", "Science", "English"]].apply(
    lambda row: (row["Math"] + row["Science"] + row["English"])/3,
    axis= 1
)

print(student_df.head())


# apply() for CONDITIONAL LOGIC (row-wise)
student_df["Result"] = student_df[["Math", "Science", "English"]].apply(
    lambda row: "Pass" if row["Math"] >= 50 and row["Science"] >= 50 and 
    row["English"] >= 50 else "Fail",
    axis=1
)
print(student_df.head())


# apply() on COLUMNS (axis = 0)
# Example: Get max of each subject

print(student_df[["Math", "Science", "English"]].apply(max, axis=0))



student_df["Result"] = student_df[["Math", "Science", "English"]].apply(
    lambda x: "Pass" if x["Math"] >= 60 and x["Science"] >= 60 and x["English"] >= 60 else "Fail",
    axis= 0
)

print(student_df.head())