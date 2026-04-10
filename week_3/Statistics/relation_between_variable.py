import pandas as pd

df = pd.DataFrame({
    "Age": [21, 23, 22, 24, 25, 22],
    "Department": ["IT", "HR", "IT", "HR", "Finance", "Finance"],
    "Salary": [50000, 60000, 55000, 65000, 62000, 58000]
})


# Categorical vs Numerical 
print(df.groupby("Department")["Salary"].mean())