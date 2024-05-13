import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import numpy as np
import json
import re

json_files = [
    '../data3/cpu/teastore-persistence-7d6bcb6b96-jcl4d.json',
    '../data3/cpu/teastore-webui-59f448d7f5-8z9cs.json',

]


def plot_json(file_name):
    with open(file_name, 'r') as file:
        json_data = json.load(file)

    datas = json_data['data']['result'][0]['values']

    return datas


for file_name in json_files:
    print(len(json_files))
    file_parts = file_name.split("/")
    last_part = (file_parts[-1]).split(".")[0]
    result = re.split(r'-\d+', last_part)[0]
    data = plot_json(file_name)

    # Vos données

    # Convert timestamps to numpy datetime64 objects
    timestamps = np.array([np.datetime64(datetime.fromtimestamp(ts)) for ts, _ in data])
    # Extract values
    values = [float(value) for _, value in data]

    # Plot the graph
    plt.figure(figsize=(10, 6))
    plt.plot(timestamps, values)

    # Calculate the start and end times
    start_time = timestamps[0]
    end_time = timestamps[-1]

    # Calculate the nearest 20-second intervals for start and end times
    start_time = start_time - np.timedelta64(start_time.astype('datetime64[s]').astype(int) % 20, 's')
    end_time = end_time + np.timedelta64(20 - end_time.astype('datetime64[s]').astype(int) % 20, 's')

    # Generate a list of ticks every 20 seconds
    ticks = np.arange(start_time, end_time + np.timedelta64(1, 's'), np.timedelta64(20, 's'))

    # Set ticks on the x-axis
    plt.gca().set_xticks(ticks)

    # Format the ticks as HH:MM:SS
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))

plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Plot with Timestamps every 20 seconds (starting at 20s)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
