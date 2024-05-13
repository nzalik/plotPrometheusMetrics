import matplotlib.pyplot as plt
import numpy as np
import json
import re

# Define your json_files groups
json_files1 = [
    '../data3/cpu/teastore-webui-59f448d7f5-8z9cs.json',
    '../data3/cpu/teastore-registry-69c86867cd-mxccl.json',
    '../data3/cpu/teastore-recommender-6b67599fb9-7g8qv.json'
]

json_files2 = [
    '../data3/cpu/teastore-persistence-7d6bcb6b96-jcl4d.json',
    '../data3/cpu/teastore-image-6b9796d7c7-tsq8h.json',
    '../data3/cpu/teastore-db-7685d7b587-bl4vl.json',
    '../data3/cpu/teastore-auth-8877cbcc9-5k2jz.json'
]

# Define your json_files3 and other groups similarly

# Initialize the plot
fig, axes = plt.subplots(len(json_files1) + len(json_files2), 1, figsize=(10, 6 * (len(json_files1) + len(json_files2))))

def plot_json(ax, file_name, label):
    with open(file_name, 'r') as file:
        json_data = json.load(file)

    datas = json_data['data']['result'][0]['values']

    timestamps = np.array([int(ts) for ts, _ in datas])
    values = [float(value) for _, value in datas]

    # Plot the graph
    ax.plot(timestamps, values, label=label)

# Plot for json_files1
for idx, file_name in enumerate(json_files1):
    ax = axes[idx]
    file_parts = file_name.split("/")
    last_part = (file_parts[-1]).split(".")[0]
    result = re.split(r'-\d+', last_part)[0]
    plot_json(ax, file_name, result)
    ax.set_title(result)

# Plot for json_files2
for idx, file_name in enumerate(json_files2):
    ax = axes[len(json_files1) + idx]
    file_parts = file_name.split("/")
    last_part = (file_parts[-1]).split(".")[0]
    result = re.split(r'-\d+', last_part)[0]
    plot_json(ax, file_name, result)
    ax.set_title(result)

# Set common labels and ticks
for ax in axes:
    ax.set_xlabel('Time (seconds)')
    ax.set_ylabel('Value')
    ax.grid(True)
    ax.legend()
    ax.xaxis.set_tick_params(rotation=45)

plt.tight_layout()
plt.show()
