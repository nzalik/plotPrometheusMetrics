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

fig, axs = plt.subplots(len(json_files), figsize=(10, 6 * len(json_files)))

def plot_json(file_name):
    with open(file_name, 'r') as file:
        json_data = json.load(file)

    datas = json_data['data']['result'][0]['values']

    return datas

for i, file_name in enumerate(json_files):
    file_parts = file_name.split("/")
    last_part = (file_parts[-1]).split(".")[0]
    result = re.split(r'-\d+', last_part)[0]
    data = plot_json(file_name)

    # Convert timestamps to numpy datetime64 objects
    timestamps = np.array([np.datetime64(datetime.fromtimestamp(ts)) for ts, _ in data])
    # Extract values
    values = [float(value) for _, value in data]

    # Plot the graph on the corresponding subplot
    axs[i].plot(timestamps, values)

    # Calculate the start and end times
    start_time = timestamps[0]
    end_time = timestamps[-1]

    # Calculate the nearest 20-second intervals for start and end times
    start_time = start_time - np.timedelta64(start_time.astype('datetime64[s]').astype(int) % 20, 's')
    end_time = end_time + np.timedelta64(20 - end_time.astype('datetime64[s]').astype(int) % 20, 's')

    # Generate a list of ticks every 20 seconds
    ticks = np.arange(start_time, end_time + np.timedelta64(1, 's'), np.timedelta64(20, 's'))

    # Set ticks on the x-axis
    axs[i].set_xticks(ticks)

    # Format the ticks as HH:MM:SS
    axs[i].xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))

    axs[i].set_xlabel('Time')
    axs[i].set_ylabel('Value')
    axs[i].set_title(f'Plot for {result} with Timestamps every 20 seconds (starting at 20s)')
    axs[i].grid(True)
    axs[i].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()
