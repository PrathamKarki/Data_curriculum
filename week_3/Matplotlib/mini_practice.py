# Creating of the different charts
import matplotlib.pyplot as plt
import numpy as np

# Creating a bar chart 
androids = ["Alice", "Kara", "Markus", "North", "Connor", "Deviants"]
marks = [76, 82, 22, 45, 69, 78]

plt.title('Comparison of marks per androids')
plt.figure(figsize=(8, 4))

plt.bar(androids, marks)
plt.xlabel("Androids")
plt.ylabel("Marks Obtained")
plt.show()

# Task 1: Create bar chart of
# products: A,B, C
# Sales:  100, 150, 90

products = ["A" , "B", "C"]
sales = [100, 150, 90]

plt.title("Bar chart of products per sales")
plt.figure(figsize=(7,4))
plt.bar(products, sales)
plt.xlabel("Products")
plt.ylabel("Sales")
plt.show()


# Task 2
# Creation of the scatter plot: Hours studied vs marks

hours_studied = [2, 4, 8, 6, 12]
marks = [78, 62, 85, 92, 27]


plt.title("Scatter plot: Hours studied vs Marks obtained")
plt.figure(figsize=(6, 4))
plt.scatter(hours_studied, marks)
plt.xlabel("Hours Studied")
plt.ylabel("Marks obtained")
plt.show()


# Task 3
# Histogram
random = np.random.default_rng()
random_integer_array = random.integers(low=1, high= 15, size=5)

random_numbers = random_integer_array.tolist()

# plotting of the histogram
plt.title("Distribution of random number based on frequency")
plt.hist(random_numbers)
plt.show()