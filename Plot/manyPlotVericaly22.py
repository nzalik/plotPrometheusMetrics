import matplotlib.pyplot as plt
import numpy as np
import json
import re

json_files1 = [
    '../data3/cpu/teastore-webui-59f448d7f5-8z9cs.json',
    '../data3/cpu/teastore-registry-69c86867cd-mxccl.json',
    '../data3/cpu/teastore-recommender-6b67599fb9-7g8qv.json',
]

json_files2 = [
    '../data3/cpu/teastore-persistence-7d6bcb6b96-jcl4d.json',
    '../data3/cpu/teastore-image-6b9796d7c7-tsq8h.json',
]

json_files3 = [
    '../data3/cpu/teastore-db-7685d7b587-bl4vl.json',
    '../data3/cpu/teastore-auth-8877cbcc9-5k2jz.json',
]

def plot_json(file_name, label):
    with open(file_name, 'r') as file:
        json_data = json.load(file)

    datas = json_data['data']['result'][0]['values']

    timestamps = np.array([int(ts) for ts, _ in datas])
    values = [float(value) for _, value in datas]

    # Plot the graph
    plt.plot(timestamps, values, label=label)


# Initialize the plot
plt.figure(figsize=(16, 6))

# Plot the first set of data
plt.subplot(1, 3, 1)
for file_name in json_files1:
    file_parts = file_name.split("/")
    last_part = (file_parts[-1]).split(".")[0]
    result = re.split(r'-\d+', last_part)[0]
    plot_json(file_name, result)
plt.xlabel('Time (seconds)')
plt.ylabel('Value')
plt.title('Data Source 1')
plt.grid(True)
plt.xticks(rotation=45)
plt.legend()

# Plot the second set of data
plt.subplot(1, 3, 2)
for file_name in json_files2:
    file_parts = file_name.split("/")
    last_part = (file_parts[-1]).split(".")[0]
    result = re.split(r'-\d+', last_part)[0]
    plot_json(file_name, result)
plt.xlabel('Time (seconds)')
plt.ylabel('Value')
plt.title('Data Source 2')
plt.grid(True)
plt.xticks(rotation=45)
plt.legend()

# Plot the third set of data
plt.subplot(1, 3, 3)
for file_name in json_files3:
    file_parts = file_name.split("/")
    last_part = (file_parts[-1]).split(".")[0]
    result = re.split(r'-\d+', last_part)[0]
    plot_json(file_name, result)
plt.xlabel('Time (seconds)')
plt.ylabel('Value')
plt.title('Data Source 3')
plt.grid(True)
plt.xticks(rotation=45)
plt.legend()

plt.tight_layout()
plt.show()