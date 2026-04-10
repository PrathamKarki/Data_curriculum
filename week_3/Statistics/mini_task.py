import pandas as pd
import statistics as stat

student_data = pd.DataFrame({
    "Name": ["Ram", "Sita", "Hari", "Gita", "Ram", "Sita", "Hari"],
    "Department": ["IT", "HR", "IT", "Finance", "HR", "IT", "IT"],
    "Level": ["Low", "Medium", "High", "Medium", "Low", "High", "Medium"]
})

print(student_data)

# Count how many students in each department
no_of_students =student_data["Department"].value_counts()
print(no_of_students)

# find the % distribution of the department
department_percentage_distribution = student_data["Department"].value_counts(normalize=True) * 100
print(department_percentage_distribution)

# find most common departments
print("Most common department:", no_of_students.idxmax())


# Convert "Level" into ordered categorical

level = student_data["Level"].astype(
    pd.CategoricalDtype(categories=["Low", "Medium", "High"], ordered=True)
)

print(level)

# find highest level
highest_level = level.max()
print(highest_level)

# find mode of level
mode_level = level.mode()
print(mode_level)


# Mixture of Numeric variables and Categorical varialbes

df = pd.DataFrame({
    "Name": ["Ram", "Sita", "Hari", "Gita", "Nabin", "Laxmi"],
    "Department": ["IT", "HR", "IT", "Finance", "HR", "IT"],
    "Age": [21, 23, 22, 24, 25, 22],
    "Salary": [50000, 60000, 55000, 65000, 62000, 58000]
})

print(df)

# Basic: numerical variable analysis
print(df["Age"].mean())
print(df["Age"].median())
print(df["Age"].std())
print(df["Age"].min(),  df["Age"].max())

# full summary of the statistical numerical information using the describe()

print(df[["Age", "Salary"]].describe())

# finding the average salary, highest salary and lowest salary

average_salary = df["Salary"].mean()
print("The average salary of all employees is", average_salary)

highest_salary = df["Salary"].max()
print("The Highest salary of all employees is", highest_salary)

lowest_salary = df["Salary"].min()
print("The lowest salary of the employee is:",lowest_salary)

# Categorical variable analysis 
# Count the departments
print(df["Department"].value_counts())


# Percentage distribution
print(df["Department"].value_counts(normalize=True) * 100)

# Average salary per department
print(df.groupby("Department")["Salary"].mean())
