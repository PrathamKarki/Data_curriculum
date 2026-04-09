import pandas as pd

employees = pd.DataFrame(
    {
    "emp_id": [1, 2, 3, 4, 5, 6],
    "name": ["Ram", "Sita", "Hari", "Gita", "Nabin", "Laxmi"],
    "department": ["IT", "HR", "IT", "Finance", "HR", "IT"],
    "city": ["Kathmandu", "Pokhara", "Kathmandu", "Lalitpur", "Pokhara", "Kathmandu"]
    })


salaries = pd.DataFrame({
    "emp_id": [1,2,3,4,4, 7],
    "salary": [50000, 60000, 55000, 5000, 70000, 45000]
})


print(employees)
print("\n\n")
print(salaries)
print("\n")

# Q1) Get all employees from Kathmandu working in IT
print(employees[employees["department"] == 'IT'].sort_values(by="name",ascending=False))

# Q2) Get employees whose name starts with "S"

print(employees[employees["name"].str.startswith('S')])


# q3) Select only name and department for employees in HR

result = employees[employees["department"] == 'HR'][["name", "department"]]
print(result)


# q4) get last 3 rows , only first 2 columns

employees.iloc[-3: , 0:2]


# SECTION B -- MERGE
# Q5) Perform inner join between employees and salaries
emp_and_salaries = pd.merge(employees, salaries, on="emp_id")
print(emp_and_salaries)

# Q6) Perform left join 
emp_salaries = pd.merge(employees, salaries, on="emp_id", how="left")
print(emp_salaries)

# Q7) which employees have no salary record
no_salary = emp_salaries[emp_salaries["salary"].isna()]
print(no_salary)


# Section C -> GROUPBY
# Q8) Total salary per employee (emp_id)

totalSal_per_emp = pd.merge(employees, salaries, on="emp_id").groupby("emp_id")["salary"].sum()
print(totalSal_per_emp)

# Q9) Total salary per department
totalSal_per_depart = pd.merge(employees, salaries, on="emp_id").groupby("department")["salary"].sum()
print(totalSal_per_depart)


# Q10) Average salary per city
avg_salary_per_c = pd.merge(employees, salaries, on="emp_id").groupby("city")["salary"].mean()
print(avg_salary_per_c)


# Q11) Which department has the highest total salary
merged = pd.merge(employees, salaries, on="emp_id")

dept_salary = merged.groupby("department")["salary"].sum()

result = dept.salary.idxmax()

print(result)


# SECTION D
# get name | department | total_salary
mergeing = pd.merge(employees, salaries, on="emp_id")

result = mergeing.groupby(["name", "department"])["salary"].sum().reset_index(name = "total_salary")