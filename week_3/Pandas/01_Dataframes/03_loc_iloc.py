import pandas as pd
import numpy as np



student_dict = {
    "name": ['nitish', 'ankit', 'rupesh', 'rishabh'],
    "iq" : [100, 90, 120, 80],
    "marks": [80, 70, 100, 50],
    "package": [10, 7, 14, 2]
}


students = pd.DataFrame(student_dict)


# set_index() -> used to make specific column to act as an index
students.set_index('name', inplace=True)
print(students.head())


movies = pd.read_csv('../Datasets/movies.csv')

# SELECTING COLS FROM THE DATAFRAME
# fetching of the single column (will be a series)
print(movies["title_x"])

# fetching of the multiple column (willl be a dataframe)
print(movies[["title_x", "year_of_release", "actors"]].head())


# SELECTING OF ROWS FROM A DATAFRAME
# iloc and loc method
# iloc searches using index position,  loc search using index label

movies.iloc[0:5:2] 
movies.iloc[5:] # 5 onwards other movies will be generated
movies.iloc[:5] 


# fancy indexing 
movies.iloc[[0,4,5]]


# loc: fetches based on index label
students.loc["nitish"]

# fancy indexing
students.loc[['nitish', 'rishabh', 'rupesh']]



# SELECTING OF BOTH ROWS AND COLS
movies.loc[0:2, 'title_x' : 'poster_path' ]