import os

import matplotlib.pyplot as plt
import numpy as np
import json
import re
import pandas as pd
import json
from datetime import datetime, timedelta, date

plot_window = 300 # Show by interval of 5 minutes

def smooth(values, w_size=5):
    new_values = []
    for i in range(len(values)):
        window = values[max(0, i - (w_size - 1) // 2):min(i + w_size // 2 + 1, len(values))]
        new_values.append(sum(window) / len(window))
    return new_values


def plot_json(file_name, label):
    with open(file_name, 'r') as file:
        json_data = json.load(file)

    if len(json_data['data']['result']) > 0:
        datas = json_data['data']['result'][0]['values']

        timestamps = np.array([int(ts) for ts, _ in datas])

        given_value = 0.0  # Replace with your desired value
        #given_value = 1716985520.148 # Replace with your desired value

        greater_than_value = timestamps[timestamps > given_value]
        less_than_value = timestamps[timestamps <= given_value]

        values = [float(value) for _, value in datas]

        last_ten_values = values[-(len(greater_than_value)):]

        greater_than_valueReduce = greater_than_value
        last_ten_valuesReduce = last_ten_values

        #lissageValues = smooth(last_ten_valuesReduce)
        lissageValues = last_ten_valuesReduce

        print(file_name)
        print(len(greater_than_valueReduce))
        print(len(lissageValues))

        plt.plot(greater_than_valueReduce, lissageValues, label=label)
        return greater_than_valueReduce
    return []


# Initialize the plot
plt.figure(figsize=(10, 16))

# Plot the first set of data
plt.subplot(6, 1, 1)
all_timestamps = []

today = date.today()
dir_name = today.strftime("%d-%m-%Y")

save_graphics_at = f"../Plots/{dir_name}"  #T
# he directory where you want things to be saved
if not os.path.exists(save_graphics_at):
    os.makedirs(save_graphics_at)

save_path = "../25-06-2024/data_08-26/"

directory = save_path + 'cpu'
for file_name in os.listdir(directory):
    file_path = os.path.join(directory, file_name)
    #for file_name in json_files1:
    file_parts = file_path.split("/")
    last_part = (file_parts[-1]).split(".")[0]
    result = re.split(r'-\d+', last_part)[0]
    timestamps = plot_json(file_path, result)

    if len(timestamps) > 0:
        all_timestamps.append(timestamps)

# Concatenate all timestamps
all_timestamps = np.concatenate(all_timestamps)

# Calculate the start and end times
start_time = min(all_timestamps)
end_time = max(all_timestamps)

# Generate a list of ticks every 20 seconds
ticks = np.arange(start_time, end_time + 1, plot_window)

# Set ticks on the x-axis
ticks_seconds = [((ts - start_time) // plot_window) * plot_window for ts in ticks]

print("max cpu")
print(len(ticks_seconds))

plt.xticks(ticks, ticks_seconds)
plt.xlabel('Time (seconds)')
plt.ylabel('cores per second')
plt.title('CPU usage')
#plt.grid(True)
plt.xticks(rotation=45)
plt.legend()

# Plot the second set of data
plt.subplot(6, 1, 2)
all_timestamps2 = []

directory2 = save_path + 'memory'
for file_name in os.listdir(directory2):
    file_path = os.path.join(directory2, file_name)
    #for file_name in json_files1:
    file_parts = file_path.split("/")
    last_part = (file_parts[-1]).split(".")[0]
    result = re.split(r'-\d+', last_part)[0]
    timestamps2 = plot_json(file_path, result)
    print("taille un element")
    print(len(timestamps2))
    if len(timestamps2) > 0:
        all_timestamps2.append(timestamps2)

# Concatenate all timestamps
all_timestamps2 = np.concatenate(all_timestamps2)

# Calculate the start and end times
start_time2 = min(all_timestamps2)
end_time2 = max(all_timestamps2)


# Generate a list of ticks every 20 seconds
ticks2 = np.arange(start_time2, end_time2 + plot_window, plot_window)

# Set ticks on the x-axis
ticks_seconds2 = [((ts - start_time2) // plot_window) * plot_window for ts in ticks2]


plt.xticks(ticks2, ticks_seconds2)
plt.xlabel('Time (seconds)')
plt.ylabel('Memory (Gbytes)')
plt.title('Memory usage')
#plt.grid(True)
plt.xticks(rotation=45)
plt.legend()

lastEl = ticks_seconds2[-1]

plt.subplot(6, 1, 3)

resultat = ticks_seconds2[3:]

plot_path = "../Load/25-06-2024/"

test = 0

try:
    df = pd.read_csv(plot_path + 'output-3minutes-70requests.csv')
except FileNotFoundError:
    #print(f"Le fichier {file_name} n'a pas été trouvé dans le chemin {plot_path}")
    # Vous pouvez également faire d'autres traitements ici, comme retourner un DataFrame vide
    df = pd.DataFrame()

#df = pd.DataFrame()

nombre_lignes = len(df)

if nombre_lignes > 0:
    test = nombre_lignes

nouvelles_lignes = []

for i in range(test+1, lastEl + 1):
    #for i in range(0, lastEl+1):
    target_time = i + 0.5
    nouvelle_ligne = pd.DataFrame([[target_time, 0, 0, 0, 0, 0, 0]],
                                  columns=['Target Time', 'Load Intensity', 'Successful Transactions',
                                           'Failed Transactions', 'Dropped Transactions', 'Avg Response Time',
                                           'Final Batch Dispatch Time'])
    nouvelles_lignes.append(nouvelle_ligne)

df = pd.concat([df] + nouvelles_lignes, ignore_index=True)

df['Target Time'] = df['Target Time'].astype(int)

# Votre code pour créer le graphique
line1, = plt.plot(df['Target Time'], df['Load Intensity'])
line2, = plt.plot(df['Target Time'], df['Successful Transactions'], color='green')
line3, = plt.plot(df['Target Time'], df['Failed Transactions'], color='red')
# line4, = plt.plot(df['Target Time'], df['Dropped Transactions'])

# Définition des emplacements des marqueurs d'axe personnalisés
interval = plot_window
plt.xticks(np.arange(min(df['Target Time']), max(df['Target Time']) + 1, interval))
plt.xticks(rotation=45)
#plt.legend([line1, line2, line3, line4], ['Load Intensity', 'Successful Transactions', 'Failed Transactions', 'Dropped Transactions'])
plt.legend([line1, line2, line3,], ['Load Intensity', 'Successful Transactions', 'Failed Transactions'])
plt.xlabel('Time (seconds)')
plt.ylabel('Number of requests')

plt.subplot(6, 1, 4)
all_timestamps3 = []
# Read JSON data from a file
directory3 = save_path + 'pod_info/pod_info.json'

with open(directory3, 'r') as file:
    source = json.load(file)

timestamps = []
values = []
tab = []
all_timestamps = []

data_list = source['data']['result']

for json_data in data_list:
    # Convertir la chaîne JSON en un dictionnaire Python
    result = json_data

    # Extraire les valeurs et les timestamps
    timestamps = [float(x[0]) for x in result["values"]]
    values = [float(x[1]) for x in result["values"]]

    all_timestamps.append(timestamps)

    # Récupérer le nom de la métrique et du déploiement
    metric_name = result["metric"]["__name__"]
    deployment_name = result["metric"]["deployment"]

    # Tracer la courbe
    plt.plot(timestamps, values, label=f"{deployment_name}")

all_timestamps = np.concatenate(all_timestamps)

start_time4 = min(timestamps)
end_time4 = max(timestamps)

ticks4 = np.arange(start_time4, end_time4 + 1, plot_window)

ticks_seconds4 = [((ts - start_time4) // plot_window) * plot_window for ts in ticks4]

plt.xticks(ticks4, ticks_seconds4)
plt.xlabel('Time (seconds)')
plt.ylabel('Number of pods')
plt.title('Evolution of pods')
plt.xticks(rotation=45)
plt.legend()

# Plot the second set of data
plt.subplot(6, 1, 5)
directory3 = save_path + 'aggregation/aggregation.json'

with open(directory3, 'r') as file:
    source = json.load(file)

timestamps = []
values = []
tab = []

data_list = source['data']['result']

for json_data in data_list:
    # Convertir la chaîne JSON en un dictionnaire Python
    result = json_data

    # Extraire les valeurs et les timestamps
    timestamps = [float(x[0]) for x in result["values"]]
    values = [float(x[1]) for x in result["values"]]

    # Récupérer le nom de la métrique et du déploiement
    metric_name = result["metric"]["container"]
    deployment_name = result["metric"]["container"]

    # Tracer la courbe
    plt.plot(timestamps, values, label=f"{deployment_name}")

start_time4 = min(timestamps)
end_time4 = max(timestamps)

ticks4 = np.arange(start_time4, end_time4 + 1, plot_window)

ticks_seconds4 = [((ts - start_time4) // plot_window) * plot_window for ts in ticks4]

plt.xticks(ticks4, ticks_seconds4)
plt.xlabel('Time (seconds)')
plt.ylabel('Core per seconds')
plt.title('CPU consumption in aggregate')
plt.xticks(rotation=45)
plt.legend()

plt.subplot(6, 1, 6)
directory3 = save_path + 'aggregation/aggregation_memory.json'

with open(directory3, 'r') as file:
    source = json.load(file)

timestamps = []
values = []
tab = []

data_list = source['data']['result']

for json_data in data_list:
    # Convertir la chaîne JSON en un dictionnaire Python
    result = json_data

    # Extraire les valeurs et les timestamps
    timestamps = [float(x[0]) for x in result["values"]]
    values = [float(x[1]) for x in result["values"]]

    # Récupérer le nom de la métrique et du déploiement
    metric_name = result["metric"]["container"]
    deployment_name = result["metric"]["container"]

    # Tracer la courbe
    plt.plot(timestamps, values, label=f"{deployment_name}")

start_time5 = min(timestamps)
end_time5 = max(timestamps)

ticks5 = np.arange(start_time5, end_time5 + 1, plot_window)

ticks_seconds5 = [((ts - start_time5) // plot_window) * plot_window for ts in ticks5]

plt.xticks(ticks5, ticks_seconds5)
plt.xlabel('Time (seconds)')
plt.ylabel('Memory GB')
plt.title('Memory usage in aggregate')
plt.xticks(rotation=45)
plt.legend()

plt.tight_layout()

files = os.listdir(save_graphics_at)
data_count = sum(1 for f in files if f.startswith("output") and f.endswith(".png"))
my_string = f"{save_graphics_at}/output{str(data_count + 1)}.png"
plt.savefig(my_string)
plt.show()
