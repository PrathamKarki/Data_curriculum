import pandas as pd
import numpy as np

# Creating of the dataframe 

df = pd.DataFrame({
    "Name": ["Ram", "Sita", "Gita", "Hari", "Shyam", "Krishna"],
    "City": ["Kathmandu", "Kathmandu", "Pokhara", "Pokhara", "Kathmandu", "Pokhara"],
    "Department": ["IT", "HR", "IT", "HR", "IT", "IT"],
    "Salary": [50000, 60000, 55000, 52000, 70000, 65000]
})


# Task_1: Total salary per city
salaryPerCity = df.groupby("City")["Salary"].mean()
print(salaryPerCity.head())


# Task_2: Average salary per department
salaryPerDepartment = df.groupby("Department")["Salary"].sum()
print(salaryPerDepartment.head())


# Task_3 : Count of employees per city
employeesPerCity = df.groupby("City")["Name"].count()
print(employeesPerCity.head())


# Task_4 : Total salary per City and Department
cityNDepartment = df.groupby(["City", "Department"])["Salary"].sum().reset_index()
print(cityNDepartment.head())

# Task_5 : get this output  city, total_salary , Avg_Salary

solution = df.groupby("City")["Salary"].agg(
    Total_salary = "sum",
    Avg_Salary = "mean"
).reset_index()


print(solution.head())


# Task_6: Which city has the highest total salary?
task_6 = df.groupby("City")["Salary"].sum()

task_6.idxmax()


print(task_6.head())