import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import numpy as np
import json
import re

json_files = [
    '../data/cpu/teastore-webui-59f448d7f5-cmhdv.json',
    '../data/cpu/teastore-registry-69c86867cd-l7c7q.json',
    '../data/cpu/teastore-recommender-6b67599fb9-vqj6x.json',
    '../data/cpu/teastore-persistence-7d6bcb6b96-w9tg4.json',
    '../data/cpu/teastore-image-6b9796d7c7-wlhnt.json',
    '../data/cpu/teastore-db-7685d7b587-6bxzn.json',
    '../data/cpu/teastore-auth-8877cbcc9-rmt4s.json'
]

# Initialize the plot
plt.figure(figsize=(10, 6))

def plot_json(file_name, label):
    with open(file_name, 'r') as file:
        json_data = json.load(file)

    datas = json_data['data']['result'][0]['values']

    threshold_timestamp = np.datetime64("2024-05-02T10:30:30.635000")
    timestamps = np.array([np.datetime64(datetime.fromtimestamp(ts)) for ts, _ in datas])
    greater_than_threshold = timestamps[timestamps > threshold_timestamp]
    less_than_threshold = timestamps[timestamps <= threshold_timestamp]

    values = [float(value) for _, value in datas]

    print(file_name)
    print(len(timestamps))
    print(len(greater_than_threshold))
    print(len(less_than_threshold))
    print("################################")

    # Take the last ten elements of the values array
    last_ten_values = values[-(len(greater_than_threshold)):]

    # Plot the graph
    plt.plot(greater_than_threshold, last_ten_values, label=label)

    return greater_than_threshold

# Initialize variables to store timestamps from all files
all_timestamps = []

for file_name in json_files:
    file_parts = file_name.split("/")
    last_part = (file_parts[-1]).split(".")[0]
    result = re.split(r'-\d+', last_part)[0]

    timestamps = plot_json(file_name, result)
    all_timestamps.append(timestamps)

# Concatenate all timestamps
all_timestamps = np.concatenate(all_timestamps)

print("33333333333333333333333333333333")
print(all_timestamps)
# Calculate the start and end times
start_time = min(all_timestamps)
end_time = max(all_timestamps)

# Calculate the nearest 20-second intervals for start and end times
start_time = start_time - np.timedelta64(start_time.astype('datetime64[s]').astype(int) % 20, 's')
end_time = end_time + np.timedelta64(20 - end_time.astype('datetime64[s]').astype(int) % 20, 's')

# Generate a list of ticks every 20 seconds
ticks = np.arange(start_time, end_time + np.timedelta64(1, 's'), np.timedelta64(20, 's'))

# Set ticks on the x-axis
plt.xticks(ticks)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))

plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Plot with Timestamps every 20 seconds (starting at 20s)')
plt.grid(True)
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

plt.show()
