import matplotlib.pyplot as plt

# Implementing of the basic line plot 
x = [1,2,3,4]
y = [10,20,30,40]

plt.plot(x,y)
plt.title("Basic line plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()


# Bar Graph
# Used for comparing quantities across categories
# Real use case/ example: sales per product, studests per class, 
names = ["milk", 'eggs', 'omelette', 'bacon', 'cheese', 'butter']
price = [120, 220, 100, 180, 130, 145 ]

# constructing of the bar chart
plt.bar(names, price)
plt.title("Comparison of products with their price")
plt.xlabel("Products")
plt.ylabel("Price")
plt.show()


# Scatter plot
# Used for finding the relationship and correlation 
#
x = [1,2,3,4,5]
y = [5,7,9,11,13]

plt.scatter(x,y)
plt.title("Scatter plot")
plt.show()

# Histogram
# used for understanding of the distribution(single numerical varaiable by frequency)
# example: salary distribution, age distribution
data = [10, 20, 20, 30, 30, 30, 40]

plt.hist(data, bins = 4)
plt.title("Histogram")
plt.show()


# 3.4 Box Plot
# used for finding the outliers and spread
# It helps to show median, quartiles and outliers
data = [10,20,30,40,100]

plt.boxplot(data)
plt.title("Box plot")
plt.show()


# 3.5 Pie Chart
# Used for showing proportions

labels = ['A', 'B', 'C']
sizes = [40, 35, 25]

plt.pie(sizes, labels=labels, autopct='%1.1f%%' )
plt.title("Pie Chart")
plt.figure(figsize=(6,4))
plt.show()