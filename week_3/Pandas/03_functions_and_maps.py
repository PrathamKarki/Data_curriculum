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


# Understanding of the Functions and Maps
# describe() function in pandas

print(student_df.Math.describe())

# Seeing the average marks obtained in English subject
print(student_df["English"].mean())


# checking if there is a unique name or not
print(student_df["Math"].unique())


# To see the list of unique values and how often they occur we use value_count()
print(student_df["English"].value_counts())


# Maps in Pandas
# Maps are used to transform values into a series, it works only on one column

def grade(marks):
   if marks >= 90:
        return "A+"
   elif marks >= 80  and marks <=80:
        return "A"
   elif marks >=70 and marks <= 79:
        return "B"
   else:
        return "C"

student_df["Math Grades"] = student_df["Math"].map(grade)

print(student_df.head(5))

# Using of map with dictionary

name_to_id = {
    "Aaarva": 101,
    "Sita": 102,
    "Ram": 103,
    "Gita": 104,
    "Krishna": 105, 
    "Maya": 106,
    "Arjun": 107,
    "Laxmi": 108
}

student_df["Student_ID"] = student_df["Name"].map(name_to_id)


# Using of the map() with LAMBDA

student_df["Attendance_Stauts"] = student_df["Attendance (%)"].map(
    lambda x: "Present" if x>= 75 else "Low Attendance"
)


# Practice problems
# Creating a new column "Science_Grade" using map() 

def science_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80  and marks <=80:
        return "A"
    elif marks >=70 and marks <= 79:
        return "B"
    else:
        return "C"


student_df["Science Grade"] = student_df["Science"].map(science_grade)
print(student_df.head())


# Creating a dictionary that maps "name" to "city

name_to_city = {
    "Aaarva": "Kathmandu",
    "Sita":  "Lalitpur",
    "Ram":  "Bhaktapur",
    "Gita": "Pokhara",
    "Krishna": "Butwal", 
    "Maya": "Biratnagar",
    "Arjun": "Dharan",
    "Laxmi": "Nepalgunj"
}


student_df["City"] = student_df["Name"].map(name_to_city)


# Creat "Attendance_Flag" with map + lambda

student_df["Attendance_Flag"] = student_df["Attendance (%)"].map(
    lambda x: "Excellent" if x >= 90 
    else "Good" if x >= 80
    else "Average" if x >= 70
    else "Poor" 
)


print(student_df.head())

