# Step-by-step implemetation of data preprocessing

# Step_1: Import Libraries 
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "dataset", "diabetes.csv")

# Step_2: Load dataset
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

df = pd.read_csv(file_path)
print(df.head())

# Step 3: Inspect data strcutre and check missing values
print(df.shape)
print("\n")
print(df.info())
print("\n")
print(df.isnull().sum())


# Step 4: Statistical Summary and Visualizing outliers
print("\n")
print(df.describe())

fig, ax = plt.subplots(len(df.columns), 1,  figsize=(7,18), dpi=95)

for i, col  in enumerate(df.columns):
    sns.boxplot(x=df[col], ax=ax[i])
    ax[i].set_title(col)

plt.tight_layout()
plt.show()