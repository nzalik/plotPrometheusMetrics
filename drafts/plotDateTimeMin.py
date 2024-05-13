import matplotlib.pyplot as plt
from datetime import datetime

# Example data
dates = [datetime(2024, 4, 30, 7, 24), datetime(2024, 4, 30, 7, 25), datetime(2024, 4, 30, 7, 26)]
values = [10, 15, 20]

# Plot the data
plt.plot(dates, values)

# Set the minimum date for the x-axis
plt.xlim(datetime(2024, 4, 30, 7, 24))

# Display the plot
plt.show()