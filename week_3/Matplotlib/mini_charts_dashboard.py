import matplotlib.pyplot as plt
import numpy as np

movies = ['Gone girl', 'Charades', 'Psycho', 'Rear window', 'Silence of a lamb', 'Pulp fiction']
ratings = [9.8, 7.8, 8.1, 5.6, 6.5, 8.2]

fig, ax = plt.subplots(2,2, figsize=(12, 10))
fig.suptitle("Different Charts showcasing Movies and their ratings")

# Line plots
ax[0,0].plot(movies, ratings)
ax[0,0].set_title("Line chart of movies vs ratings")

# Bar plot
ax[0,1].bar(movies, ratings)
ax[0,1].set_title("Bar chart of movies vs ratings")


# Scatter
ax[1,0].scatter(movies, ratings)
ax[1,0].set_title("Scatter chart of movies vs ratings")

# Histogram
ax[1,1].hist([9.8, 7.8, 8.1, 5.6, 6.5, 6.5, 9.8, 7.8,9.8,6.5,6.5,6.5])
ax[1,1].set_title("Histogram of the rating")

# Rotate x labels for all the plots
for row in ax:
    for col in row:
        col.tick_params(axis='x', rotation=45)



plt.tight_layout()
plt.show()
