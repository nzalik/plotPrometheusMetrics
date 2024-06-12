import matplotlib.pyplot as plt
import json

save_path = "../data/cpu-variation/data/"
directory3 = save_path+'pod_info/pod_info.json'

with open(directory3, 'r') as file:
    source = json.load(file)


# Vos données JSON
#data_list = source['data']['result']
data_list = source['data']['result']

plt.figure(figsize=(12, 6))

for json_data in data_list:
    # Convertir la chaîne JSON en un dictionnaire Python
    result = json_data

    # Extraire les valeurs et les timestamps
    timestamps = [float(x[0]) for x in result["values"]]
    values = [float(x[1]) for x in result["values"]]

    print(max)
    print(max(values))

    # Récupérer le nom de la métrique et du déploiement
    metric_name = result["metric"]["__name__"]
    deployment_name = result["metric"]["deployment"]

    # Tracer la courbe
    plt.plot(timestamps, values, label=f"{metric_name} - {deployment_name}")

plt.legend()
plt.title("Déploiements Kubernetes")
plt.xlabel("Timestamp")
plt.ylabel("Valeur")
plt.grid()
plt.show()

