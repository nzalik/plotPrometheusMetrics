import matplotlib.pyplot as plt

# Sample data for the first column
x1 = [1, 2, 3, 4, 5]
y1 = [10, 15, 20, 25, 30]

# Sample data for the second column
x2 = [1, 2, 3, 4, 5]
y2 = [5, 10, 15, 20, 25]

# Plotting the first column
plt.plot(x1, y1, label='Column 1')

# Plotting the second column
#plt.plot(x2, y2, label='Column 2')

# Adding titles and labels
plt.title('Two Columns Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Adding legend
plt.legend()

# Displaying the plot
plt.show()
