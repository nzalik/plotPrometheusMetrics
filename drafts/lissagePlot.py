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
    '../data3/cpu/teastore-db-7685d7b587-bl4vl.json',
]

json_files3 = [
    '../data3/cpu/teastore-auth-8877cbcc9-5k2jz.json',
]

# Initialize the plot
fig, axs = plt.subplots(9, 1, figsize=(10, 18))

def plot_json(file_name, label, ax):
    with open(file_name, 'r') as file:
        json_data = json.load(file)

    datas = json_data['data']['result'][0]['values']

    timestamps = np.array([int(ts) for ts, _ in datas])
    values = [float(value) for _, value in datas]

    # Plot the graph
    ax.plot(timestamps, values, label=label)

# Loop over the JSON files and plot the data
for i, file_name in enumerate(json_files1):
    file_parts = file_name.split("/")
    last_part = (file_parts[-1]).split(".")[0]
    result = re.split(r'-\d+', last_part)[0]

    ax = axs[i]
    plot_json(file_name, result, ax)

    # Set labels, title, grid, and legend
    ax.set_xlabel('Time (seconds)')
    ax.set_ylabel('Value')
    ax.set_title(f'Plot for {result}')
    ax.grid(True)
    ax.legend()

# Loop over the JSON files and plot the data
for i, file_name in enumerate(json_files2):
    file_parts = file_name.split("/")
    last_part = (file_parts[-1]).split(".")[0]
    result = re.split(r'-\d+', last_part)[0]

    ax = axs[i+3]
    plot_json(file_name, result, ax)

    # Set labels, title, grid, and legend
    ax.set_xlabel('Time (seconds)')
    ax.set_ylabel('Value')
    ax.set_title(f'Plot for {result}')
    ax.grid(True)
    ax.legend()

# Loop over the JSON files and plot the data
for i, file_name in enumerate(json_files3):
    file_parts = file_name.split("/")
    last_part = (file_parts[-1]).split(".")[0]
    result = re.split(r'-\d+', last_part)[0]

    ax = axs[i+6]
    plot_json(file_name, result, ax)

    # Set labels, title, grid, and legend
    ax.set_xlabel('Time (seconds)')
    ax.set_ylabel('Value')
    ax.set_title(f'Plot for {result}')
    ax.grid(True)
    ax.legend()

# Remove unused subplots
for i in range(len(json_files1) + len(json_files2) + len(json_files3), len(axs)):
    axs[i].remove()

plt.tight_layout()
plt.show()