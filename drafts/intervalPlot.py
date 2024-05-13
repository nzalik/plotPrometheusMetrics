import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime

# Assuming 'dates' is a list of datetime objects
dates = [datetime.datetime(0, 4, 30, 12, 30, 15),
         datetime.datetime(0, 4, 30, 12, 30, 16),
         datetime.datetime(0, 4, 30, 12, 30, 17)]
values = [10, 20, 30]

# Convert datetime objects to matplotlib dates
mpl_dates = mdates.date2num(dates)

plt.plot_date(mpl_dates, values, '-')

plt.xlabel('Time')
plt.ylabel('Values')
plt.show()