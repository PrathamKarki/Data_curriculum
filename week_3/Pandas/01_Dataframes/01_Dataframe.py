import pandas as pd
import numpy as np

# Creation of the dataframe
# using lists
# using dicts
# using read_csv

# using lists
student_data = [
    [100, 80, 10],
    [90, 70, 7],
    [120, 100, 14],
    [80, 50, 2]
]

list_df = pd.DataFrame(student_data, columns=["IQ", "Marks", "Package"])

print(list_df.head())


# using a dictionaary

student_dict = {
    "iq" : [100, 90, 120, 80],
    "marks": [80, 70, 100, 50],
    "package": [10, 7, 14, 2]
}


dict_dataframe = pd.DataFrame(student_dict)

print(dict_dataframe.head())


# using read csv

movies = pd.read_csv("../Datasets/movies.csv")
 
ipl = pd.read_csv("../Datasets/ipl-matches.csv")
