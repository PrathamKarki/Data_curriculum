import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Creating of the bar graph
names = ["ram", "hari", "gita", "sita", "shyam"]
marksObtained = [78, 47, 22, 49, 82]

# plt.bar(names, marksObtained)
plt.title("Marks obtained by the students")
plt.show()


# Scatter plot graph 
x = [1,2,3,4]
y = [10,20,25,30]

plt.scatter(x,y)
plt.title("Scatter plot graph")
plt.show()

# Learning about the histogram graph
# This graph generally shows distribution
data = [1,2,2,3,2,2,4,5,6,6,6,7,10, 15, 15]

plt.hist(data)
plt.title("Histogram")
plt.show()

# Learning about the box plot graph
# This kind of graph helps to detect outliers
info = [1,2,3,4,5,100]
plt.title("Box Plot")
plt.show()

# Learning about the pie chart
labels = ["A", "B", "C"]
sizes = [30,40,30]

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.show()


# Bar graph

countries = ['Japan', 'USA', 'Canada', 'Germany', 'Ireland', 'Switzerland']
population = [1390000000, 2567000000000,  12000000000, 15600000000, 456000000, 673000000000]

plt.bar(countries, population)
plt.title("Population based on the country")

plt.show()