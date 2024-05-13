import matplotlib.pyplot as plt
import numpy as np
import json
import re

json_files1 = [
    '../data3/cpu/teastore-webui-59f448d7f5-8z9cs.json',
    '../data3/cpu/teastore-registry-69c86867cd-mxccl.json',
    '../data3/cpu/teastore-recommender-6b67599fb9-7g8qv.json',
    '../data3/cpu/teastore-persistence-7d6bcb6b96-jcl4d.json',
    '../data3/cpu/teastore-image-6b9796d7c7-tsq8h.json',
    '../data3/cpu/teastore-db-7685d7b587-bl4vl.json',
    '../data3/cpu/teastore-auth-8877cbcc9-5k2jz.json'
]

json_files2 = [
    '../data2/memory/teastore-webui-59f448d7f5-8z9cs.json',
    '../data2/memory/teastore-registry-69c86867cd-mxccl.json',
    '../data2/memory/teastore-recommender-6b67599fb9-7g8qv.json',
    '../data2/memory/teastore-persistence-7d6bcb6b96-jcl4d.json',
    '../data2/memory/teastore-image-6b9796d7c7-tsq8h.json',
    '../data2/memory/teastore-db-7685d7b587-bl4vl.json',
    '../data2/memory/teastore-auth-8877cbcc9-5k2jz.json'
]

json_files3 = [
    '../data3/cpu/teastore-webui-59f448d7f5-8z9cs.json',
    '../data3/cpu/teastore-registry-69c86867cd-mxccl.json',
    '../data3/cpu/teastore-recommender-6b67599fb9-7g8qv.json',
    '../data3/cpu/teastore-persistence-7d6bcb6b96-jcl4d.json',
    '../data3/cpu/teastore-image-6b9796d7c7-tsq8h.json',
    '../data3/cpu/teastore-db-7685d7b587-bl4vl.json',
    '../data3/cpu/teastore-auth-8877cbcc9-5k2jz.json'
]

def plot_json(file_name, label):
    with open(file_name, 'r') as file:
        json_data = json.load(file)

    datas = json_data['data']['result'][0]['values']

    timestamps = np.array([int(ts) for ts, _ in datas])
    values = [float(value) for _, value in datas]

    # Plot the graph
    plt.plot(timestamps, values, label=label)
    return timestamps

# Initialize the plot
plt.figure(figsize=(10, 16))

# Plot the first set of data
plt.subplot(3, 1, 1)
all_timestamps = []
for file_name in json_files1:
    file_parts = file_name.split("/")
    last_part = (file_parts[-1]).split(".")[0]
    result = re.split(r'-\d+', last_part)[0]
    timestamps = plot_json(file_name, result)
    all_timestamps.append(timestamps)

# Concatenate all timestamps
all_timestamps = np.concatenate(all_timestamps)

# Calculate the start and end times
start_time = min(all_timestamps)
end_time = max(all_timestamps)

# Calculate the nearest 20-second intervals for start and end times
start_time = start_time - (start_time % 20)
end_time = end_time + (20 - end_time % 20)

# Generate a list of ticks every 20 seconds
ticks = np.arange(start_time, end_time + 1, 20)

# Set ticks on the x-axis
ticks_seconds = [((ts - start_time) // 20) * 20 for ts in ticks]
plt.xticks(ticks, ticks_seconds)
plt.xlabel('Time (seconds)')
plt.ylabel('Value')
plt.title('Data Source 1')
plt.grid(True)
plt.xticks(rotation=45)
plt.legend()

# Plot the second set of data
plt.subplot(3, 1, 2)
all_timestamps2 = []
for file_name in json_files2:
    file_parts = file_name.split("/")
    last_part = (file_parts[-1]).split(".")[0]
    result = re.split(r'-\d+', last_part)[0]
    timestamps2 = plot_json(file_name, result)
    all_timestamps2.append(timestamps2)

# Concatenate all timestamps
all_timestamps2 = np.concatenate(all_timestamps2)

# Calculate the start and end times
start_time2 = min(all_timestamps2)
end_time2 = max(all_timestamps2)

# Calculate the nearest 20-second intervals for start and end times
start_time2 = start_time2 - (start_time2 % 20)
end_time2 = end_time2 + (20 - end_time2 % 20)

# Generate a list of ticks every 20 seconds
ticks2 = np.arange(start_time2, end_time2 + 1, 20)

# Set ticks on the x-axis
ticks_seconds2 = [((ts - start_time2) // 20) * 20 for ts in ticks]
plt.xticks(ticks2, ticks_seconds2)
plt.xlabel('Time (seconds)')
plt.ylabel('Value')
plt.title('Data Source 2')
plt.grid(True)
plt.xticks(rotation=45)
plt.legend()

# Plot the third set of data
plt.subplot(3, 1, 3)
all_timestamps3 = []
for file_name in json_files3:
    file_parts = file_name.split("/")
    last_part = (file_parts[-1]).split(".")[0]
    result = re.split(r'-\d+', last_part)[0]
    timestamps3 = plot_json(file_name, result)
    all_timestamps3.append(timestamps3)

# Concatenate all timestamps
all_timestamps3 = np.concatenate(all_timestamps3)

# Calculate the start and end times
start_time3 = min(all_timestamps3)
end_time3 = max(all_timestamps3)

# Calculate the nearest 20-second intervals for start and end times
start_time3 = start_time3 - (start_time3 % 20)
end_time3 = end_time3 + (20 - end_time3 % 20)

# Generate a list of ticks every 20 seconds
ticks3 = np.arange(start_time3, end_time3 + 1, 20)

# Set ticks on the x-axis
ticks_seconds3 = [((ts - start_time3) // 20) * 20 for ts in ticks]
plt.xticks(ticks3, ticks_seconds3)
plt.xlabel('Time (seconds)')
plt.ylabel('Value')
plt.title('Data Source 3')
plt.grid(True)
plt.xticks(rotation=45)
plt.legend()

plt.tight_layout()
plt.show()