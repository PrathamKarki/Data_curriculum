# Coloring and stying in the matplotlib
# Creating of the simple bar chart
import matplotlib.pyplot as plt
import numpy as np

products = ["A", "B", "C"]
sales = [100, 150, 90]


plt.figure(figsize=(5, 3))

# coloring and styling
plt.bar(products, sales, color = ["red", "blue", "green"])

plt.title("Styled Bar Chart")
plt.xlabel("Products")
plt.ylabel("Sales")

plt.grid(False)
plt.show()

# understanding of the fig, ax 
# fig are like an entire window or canvas
# ax is the actual plot area where your graph is drawn (think of one chart inside the page)

items = ["rice", 'milk', 'curd', 'oranges', 'pineapple']
price = [130, 80, 110, 120, 140]

fig, ax = plt.subplots()
ax.plot(items, price)
plt.show()

# Multiple subplots (Example 1: 1 Row, 2 Columns)

fig, ax = plt.subplots(1,2)

ax[0].plot([1,2,3], [10,20,30])
ax[0].set_title("Plot 1")

ax[1].plot([1,2,3], [30,20,10])
ax[1].set_title("Plot 2")

plt.show()


# Example 2: Working with the 2x2 grid (2 rows 2 columns)

fig, ax = plt.subplots(2, 2)

ax[0,0].plot([1,2,3], [15, 25, 50])
ax[0,1].plot([1,2,3], [15, 10, 5])
ax[1,0].plot([1,2,3], [30,40,20])
ax[1,1].plot([1,2,3], [40, 30 , 50])

fig.suptitle("My Line charts Dashboard") # overall title
plt.show()

