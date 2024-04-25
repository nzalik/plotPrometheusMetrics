import json

# Lire le fichier JSON
with open('cpu.json', 'r') as json_file:
    data = json.load(json_file)

# Filtrer les éléments ayant la clé "container" avec leurs valeurs
filtered_data = [result for result in data["data"]["result"] if "container" in result["metric"]]

# Afficher les données filtrées
print(filtered_data)