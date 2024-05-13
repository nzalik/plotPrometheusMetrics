import json
import re
import numpy as np
import matplotlib.pyplot as plt

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
    # Add your second set of JSON files here
]

json_files3 = [
    # Add your third set of JSON files here
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

# Plot the first set of JSON files
plt.figure(figsize=(10, 6))
plt.subplot(311)
for file_name in json_files1:
    file_parts = file_name.split("/")
    last_part = (file_parts[-1]).split(".")[0]
    result = re.split(r'-\d+', last_part)[0]

    timestamps = plot_json(file_name, result)

plt.xlabel('Time (seconds)')
plt.ylabel('Value')
plt.title('Plot for json_files1')
plt.grid(True)
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

# Plot the second set of JSON files
plt.figure(figsize=(10, 6))
plt.subplot(312)
for file_name in json_files2:
    file_parts = file_name.split("/")
    last_part = (file_parts[-1]).split(".")[0]
    result = re.split(r'-\d+', last_part)[0]

    timestamps = plot_json(file_name, result)

plt.xlabel('Time (seconds)')
plt.ylabel('Value')
plt.title('Plot for json_files2')
plt.grid(True)
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

# Plot the third set of JSON files
plt.figure(figsize=(10, 6))
plt.subplot(313)
for file_name in json_files3:
    file_parts = file_name.split("/")
    last_part = (file_parts[-1]).split(".")[0]
    result = re.split(r'-\d+', last_part)[0]

    timestamps = plot_json(file_name, result)

plt.xlabel('Time (seconds)')
plt.ylabel('Value')
plt.title('Plot for json_files3')
plt.grid(True)
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

plt.show()