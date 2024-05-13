import matplotlib.pyplot as plt
import numpy as np
import json
import re
import pandas as pd
from datetime import datetime

json_files1 = [
    '../data/cpu/teastore-webui-859f4f58dd-tmrx8.json',
    '../data/cpu/teastore-registry-84b85bd645-gv5z9.json',
    '../data/cpu/teastore-recommender-56747d546c-xnr7l.json',
    '../data/cpu/teastore-persistence-545cf59c9b-wknqw.json',
    '../data/cpu/teastore-image-866749dd95-dhk62.json',
    '../data/cpu/teastore-db-7685d7b587-cf85s.json',
    '../data/cpu/teastore-auth-6588c4cd9b-pd2xp.json'
]

json_files2 = [
    '../data/memory/teastore-webui-859f4f58dd-tmrx8.json',
    '../data/memory/teastore-registry-84b85bd645-gv5z9.json',
    '../data/memory/teastore-recommender-56747d546c-xnr7l.json',
    '../data/memory/teastore-persistence-545cf59c9b-wknqw.json',
    '../data/memory/teastore-image-866749dd95-dhk62.json',
    '../data/memory/teastore-db-7685d7b587-cf85s.json',
    '../data/memory/teastore-auth-6588c4cd9b-pd2xp.json'
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

def smooth(values, w_size=5):
    new_values = []
    for i in range(len(values)):
        window = values[max(0, i - (w_size - 1) // 2):min(i + w_size // 2 + 1, len(values))]
        new_values.append(sum(window) / len(window))
    return new_values
def plot_json(file_name, label):
    with open(file_name, 'r') as file:
        json_data = json.load(file)

    datas = json_data['data']['result'][0]['values']

    timestamps = np.array([int(ts) for ts, _ in datas])
    print("non lisser")
    print(len(timestamps))
    print("###########")
    print("lisser")

    given_value = 1714664577.325  # Replace with your desired value

    #timestamps = np.array([int(ts) for ts, _ in datas])

    greater_than_value = timestamps[timestamps > given_value]
    less_than_value = timestamps[timestamps <= given_value]

    values = [float(value) for _, value in datas]

    last_ten_values = values[-(len(greater_than_value)):]

    greater_than_valueReduce = greater_than_value[:20]
    last_ten_valuesReduce = last_ten_values[:20]

    lissageValues = smooth(last_ten_valuesReduce)
    print(len(lissageValues))
    print(lissageValues)
    # Plot the graph
    #plt.plot(timestamps, values, label=label)
    #plt.plot(greater_than_valueReduce, last_ten_valuesReduce, label=label)
    plt.plot(greater_than_valueReduce, lissageValues, label=label)
    return greater_than_valueReduce


# Initialize the plot
plt.figure(figsize=(10, 16))

# Plot the first set of data
plt.subplot(4, 1, 1)
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
plt.ylabel('cores per second')
plt.title('CPU usage')
plt.grid(True)
plt.xticks(rotation=45)
plt.legend()

# Plot the second set of data
plt.subplot(4, 1, 2)
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
plt.ylabel('Memory (Gbytes)')
plt.title('Memory usage')
plt.grid(True)
plt.xticks(rotation=45)
plt.legend()

plt.subplot(4, 1, 3)
print("ticks_seconds2")
print(ticks_seconds2)
resultat = ticks_seconds2[3:]
print("#############")
print("resultat")
print(resultat)

df = pd.read_csv('output020524-22.csv')
nombre_lignes = len(df)
print("nombre_lignes")
print(nombre_lignes)
plt.plot(df['Target Time'], df['Load Intensity'])
plt.xlabel('Time (seconds)')
plt.ylabel('Number of requests')
# Ajouter les valeurs supplémentaires sur l'axe X
x_values = [140, 160, 180]
plt.xticks(x_values + list(df['Target Time']))

# Ajouter la valeur 0 sur l'axe Y
plt.yticks([0] + list(df['Load Intensity']))

plt.subplot(4, 1, 4)
# Read JSON data from a file
with open('../data/pod_info/pod_info.json', 'r') as file:
    data = json.load(file)

timestamps = []
values = []

for item in data["data"]["result"]:
    timestamp = item["value"][0]
    value = float(item["value"][1])

    timestamps.append(timestamp)
    values.append(value)

print("the number of values")
print(timestamps)
# Convert timestamps to time values
times = [datetime.fromtimestamp(ts) for ts in timestamps]

# Transform time values into seconds with interval of 20 seconds
start_time = min(times)
seconds = [(t - start_time).total_seconds() for t in times]
scaled_seconds = [s * 20 for s in seconds]

# Plotting
#plt.figure(figsize=(12, 6))
plt.plot(scaled_seconds, values, marker='o', linestyle='-', linewidth=2)

plt.xlabel('Time (seconds)')
plt.ylabel('Number of pods')
plt.title('Evolution of pods')

# Set x-axis tick values and labels
tick_values = [i * 20 for i in range(len(scaled_seconds))]
tick_labels = [str(i * 20) for i in range(len(scaled_seconds))]
plt.xticks(tick_values, tick_labels)


plt.tight_layout()

plt.savefig('cpuMemoryLoad.png')
plt.show()
