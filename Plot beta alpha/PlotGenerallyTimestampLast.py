import os

import matplotlib.pyplot as plt
import numpy as np
import json
import re
import pandas as pd
from datetime import datetime
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

    if(len(datas) == 0):
        return []

    timestamps = np.array([int(ts) for ts, _ in datas])

    given_value = 1717733878.849 # Replace with your desired value
    #given_value = 1716985520.148 # Replace with your desired value

    greater_than_value = timestamps[timestamps > given_value]
    less_than_value = timestamps[timestamps <= given_value]

    values = [float(value) for _, value in datas]

    last_ten_values = values[-(len(greater_than_value)):]

    greater_than_valueReduce = greater_than_value
    last_ten_valuesReduce = last_ten_values

    print("la valeur max de la mémoire cest")
    print(max(last_ten_valuesReduce))

    #lissageValues = smooth(last_ten_valuesReduce)
    lissageValues = last_ten_valuesReduce

    plt.plot(greater_than_valueReduce, lissageValues, label=label)
    return greater_than_valueReduce


# Initialize the plot
plt.figure(figsize=(10, 16))

# Plot the first set of data
plt.subplot(4, 1, 1)
all_timestamps = []

save_path = "../1Odata/07-06-24/cpu-variation/data/"

directory = save_path + 'cpu'
for file_name in os.listdir(directory):
    file_path = os.path.join(directory, file_name)
    #for file_name in json_files1:
    file_parts = file_path.split("/")
    last_part = (file_parts[-1]).split(".")[0]
    result = re.split(r'-\d+', last_part)[0]
    print(result)
    timestamps = plot_json(file_path, result)
    all_timestamps.append(timestamps)

# Concatenate all timestamps
all_timestamps = np.concatenate(all_timestamps)

# Calculate the start and end times
start_time = min(all_timestamps)
end_time = max(all_timestamps)

print("time")
print(start_time)
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


directory2 = save_path+'memory'
for file_name in os.listdir(directory2):
    file_path = os.path.join(directory2, file_name)
    #for file_name in json_files1:
    file_parts = file_path.split("/")
    last_part = (file_parts[-1]).split(".")[0]
    result = re.split(r'-\d+', last_part)[0]
    timestamps2 = plot_json(file_path, result)
    all_timestamps2.append(timestamps2)

# Concatenate all timestamps
all_timestamps2 = np.concatenate(all_timestamps2)

# Calculate the start and end times
start_time2 = min(all_timestamps2)
end_time2 = max(all_timestamps2)

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

lastEl = ticks_seconds2[-1]

plt.subplot(4, 1, 3)

resultat = ticks_seconds2[3:]

plot_path="../Load/07-06-24/"

df = pd.read_csv(plot_path+'outputLoadIntensity-with-autoscaler.csv')
#df = pd.DataFrame()

nombre_lignes = len(df)

nouvelles_lignes = []

for i in range(121, lastEl+1):
#for i in range(0, lastEl+1):
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
all_timestamps3 = []
# Read JSON data from a file
directory3 = save_path+'pod_info/pod_info.json'

with open(directory3, 'r') as file:
    data = json.load(file)

timestamps = []
values = []
tab = []

for item in data["data"]["result"]:
    timestamp = item["metric"][0]
    value = float(item["value"][1])
    tab.append(item["value"])

    timestamps.append(timestamp)
    values.append(value)

datas = tab

timestamps3 = np.array([int(ts) for ts, _ in datas])
values3 = [float(value) for _, value in datas]

x_values = [1714666456, 1714666457, 1714666458, 1714666459, 1714666460, 1714666461, 1714666462, 1714666463, 1714666464,
            1714666465]
y_values = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
#
#plt.plot(x_values, y_values)
#
plt.plot(timestamps3, values3, label="pods")
#plt.plot(timestamps3, values3, marker='o', linestyle='-', linewidth=2)
print("the array")
print(tab)
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

plt.xlabel('Time (seconds)')
plt.ylabel('Number of pods')
plt.title('Evolution of pods')

# Set x-axis tick values and labels
tick_values = [i * 20 for i in range(len(x_values))]
tick_labels = [str(i * 20) for i in range(len(x_values))]

plt.xticks(x_values, tick_labels)

plt.tight_layout()

plt.savefig('../Plots/07-06-24/outputLowLoadAutoscalerPodInfo.png')
plt.show()
