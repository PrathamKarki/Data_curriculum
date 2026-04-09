# Filtering in the dataframe
import pandas as pd
import numpy as np

ipl_data = pd.read_csv('../Datasets/ipl-matches.csv')

# displaying of the first 5 rows
print(ipl_data.head())


# how many matches has csk won in kolkata
ipl_data[(ipl_data['city'] == 'Kolkata') & (ipl_data['winningTeam'] == 'Chennai Super Kings')]


# toss winner is match winner in percentage
(ipl_data[ipl_data['Tosswinner'] == ipl_data['winningTeam']].shape[0] / ipl_data.shape[0]) *100


# Movies Dataset
movies = pd.read_csv("../Datasets/movies.csv")


print(movies.head())


# find movies where the country is india

movies["Country"] = "India"
movies.head()

movies['actors'].str.split('|').apply(lambda x: x[0])
