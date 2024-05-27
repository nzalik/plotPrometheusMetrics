import matplotlib.pyplot as plt
import numpy as np
import json
import re
import pandas as pd
from datetime import datetime

json_files1 = [
    '../data/cpu/teastore-webui-8665fbfd74-dcw7r.json',
    '../data/cpu/teastore-registry-f6dcdf97c-lr26h.json',
    '../data/cpu/teastore-recommender-79c58f6556-88jb8.json',
    '../data/cpu/teastore-persistence-668667c675-jh6dz.json',
    '../data/cpu/teastore-image-84cc4fd468-mlrmk.json',
    '../data/cpu/teastore-db-5847859bf8-r52pb.json',
    '../data/cpu/teastore-auth-5767dbc6b-7h4z7.json'
]

json_files2 = [
    '../data/memory/teastore-webui-8665fbfd74-dcw7r.json',
    '../data/memory/teastore-registry-f6dcdf97c-lr26h.json',
    '../data/memory/teastore-recommender-79c58f6556-88jb8.json',
    '../data/memory/teastore-persistence-668667c675-jh6dz.json',
    '../data/memory/teastore-image-84cc4fd468-mlrmk.json',
    '../data/memory/teastore-db-5847859bf8-r52pb.json',
    '../data/memory/teastore-auth-5767dbc6b-7h4z7.json'
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

    #given_value = 1716457765.096  # Replace with your desired value
    #given_value = 1716462610.14867  # Replace with your desired value
    #given_value = 1716515990.615 # Replace with your desired value
    given_value = 1716782470.186 # Replace with your desired value

    #timestamps = np.array([int(ts) for ts, _ in datas])

    greater_than_value = timestamps[timestamps > given_value]
    less_than_value = timestamps[timestamps <= given_value]

    values = [float(value) for _, value in datas]

    last_ten_values = values[-(len(greater_than_value)):]

    greater_than_valueReduce = greater_than_value
    last_ten_valuesReduce = last_ten_values

    #lissageValues = smooth(last_ten_valuesReduce)
    lissageValues = last_ten_valuesReduce

    # Plot the graph
    #plt.plot(timestamps, values, label=label)
    #plt.plot(greater_than_valueReduce, last_ten_valuesReduce, label=label)
    print("le max")
    print(file_name)
    print(max(lissageValues))
    print(len(lissageValues))
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
#start_time = start_time - (start_time % 20)
#end_time = end_time + (20 - end_time % 20)

# Generate a list of ticks every 20 seconds
ticks = np.arange(start_time, end_time + 1, 20)

# Set ticks on the x-axis
ticks_seconds = [((ts - start_time) // 20) * 20 for ts in ticks]

plt.xticks(ticks, ticks_seconds)
plt.xlabel('Time (seconds)')
plt.ylabel('cores per second')
plt.title('CPU usage')
#plt.grid(True)
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
#start_time2 = start_time2 - (start_time2 % 20)
#end_time2 = end_time2 + (20 - end_time2 % 20)

# Generate a list of ticks every 20 seconds
ticks2 = np.arange(start_time2, end_time2 + 1, 20)

# Set ticks on the x-axis
ticks_seconds2 = [((ts - start_time2) // 20) * 20 for ts in ticks2]
plt.xticks(ticks2, ticks_seconds2)
plt.xlabel('Time (seconds)')
plt.ylabel('Memory (Gbytes)')
plt.title('Memory usage')
#plt.grid(True)
plt.xticks(rotation=45)
plt.legend()

plt.subplot(4, 1, 3)

resultat = ticks_seconds2[3:]

df = pd.read_csv('output020524-22.csv')
nombre_lignes = len(df)

nouvelles_lignes = []

for i in range(121, 1421):
    target_time = i + 0.5
    nouvelle_ligne = pd.DataFrame([[target_time, 0, 0, 0, 0, 0, 0]],
                                  columns=['Target Time', 'Load Intensity', 'Successful Transactions',
                                           'Failed Transactions', 'Dropped Transactions', 'Avg Response Time',
                                           'Final Batch Dispatch Time'])
    nouvelles_lignes.append(nouvelle_ligne)

df = pd.concat([df] + nouvelles_lignes, ignore_index=True)

#df = df.append(nouvelles_lignes, ignore_index=True)
nombre_lignes2 = len(df)

df['Target Time'] = df['Target Time'].astype(int)

# Votre code pour créer le graphique
plt.plot(df['Target Time'], df['Load Intensity'])

# Définition des emplacements des marqueurs d'axe personnalisés
interval = 20
plt.xticks(np.arange(min(df['Target Time']), max(df['Target Time']) + 1, interval))
plt.xticks(rotation=45)
plt.xlabel('Time (seconds)')
plt.ylabel('Number of requests')

plt.subplot(4, 1, 4)
# Read JSON data from a file
with open('../data/pod_info/pod_info.json', 'r') as file:
    data = json.load(file)

timestamps = []
values = []
tab = []

for item in data["data"]["result"]:
    timestamp = item["value"][0]
    value = float(item["value"][1])
    tab.append(item["value"])

    timestamps.append(timestamp)
    values.append(value)

datas = tab

print(tab)

timestamps3 = np.array([int(ts) for ts, _ in datas])
values3 = [float(value) for _, value in datas]

print("le timestam")
print(timestamps3)
print(values3)

x_values = [1714666456, 1714666457, 1714666458, 1714666459, 1714666460, 1714666461, 1714666462, 1714666463, 1714666464,
            1714666465]
y_values = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
#
plt.plot(x_values, y_values)
#
# plt.plot(timestamps3, values3, label="pods")
# plt.plot(timestamps3, values3, marker='o', linestyle='-', linewidth=2)
# print("the array")
# print(tab)
# Convert timestamps to time values
times = [datetime.fromtimestamp(ts) for ts in timestamps]

# Transform time values into seconds with interval of 20 seconds
start_time = min(times)
seconds = [(t - start_time).total_seconds() for t in times]
#scaled_seconds = [s * 20 for s in seconds]
scaled_seconds = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

# Plotting
#plt.figure(figsize=(12, 6))
#plt.plot(scaled_seconds, values, marker='o', linestyle='-', linewidth=2)

print("the array")
print(scaled_seconds)
print(values)

plt.xlabel('Time (seconds)')
plt.ylabel('Number of pods')
plt.title('Evolution of pods')

# Set x-axis tick values and labels
tick_values = [i * 20 for i in range(len(x_values))]
tick_labels = [str(i * 20) for i in range(len(x_values))]

print("les vleurs")
print(tick_values)
print("les labels")
print(tick_labels)
plt.xticks(x_values, tick_labels)

plt.tight_layout()

# now = datetime.datetime.now()
# date_time_str = now.strftime("%Y-%m-%d_%H-%M-%S")
# file_name = f"cpuMemoryLoadGenerate_{date_time_str}.png"
# plt.savefig(file_name)

plt.savefig('cpuMemoryLoadGenerate27.png')
plt.show()
