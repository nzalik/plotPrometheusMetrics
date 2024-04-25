import json

import matplotlib.pyplot as plt

# Les données fournies
data = {
    'status': 'success',
    'data': {
        'resultType': 'vector',
        'result': [
            {'metric': {'__name__': 'container_cpu_usage_seconds_total', 'container': 'teastore-auth'}, 'value': [1712925428.169, '74.64022']},
            {'metric': {'__name__': 'container_cpu_usage_seconds_total', 'container': 'teastore-db'}, 'value': [1712925428.169, '8.624465']},
            {'metric': {'__name__': 'container_cpu_usage_seconds_total', 'container': 'teastore-image'}, 'value': [1712925428.169, '60.117853']},
            {'metric': {'__name__': 'container_cpu_usage_seconds_total', 'container': 'teastore-persistence'}, 'value': [1712925428.169, '32.657405']},
            {'metric': {'__name__': 'container_cpu_usage_seconds_total', 'container': 'teastore-recommender'}, 'value': [1712925428.169, '62.560744']},
            {'metric': {'__name__': 'container_cpu_usage_seconds_total', 'container': 'teastore-registry'}, 'value': [1712925428.169, '14.938629']},
            {'metric': {'__name__': 'container_cpu_usage_seconds_total', 'container': 'teastore-webui'}, 'value': [1712925428.169, '102.531033']}
        ]
    }
}

x_values = []
y_values = []
container_names = []

# Extraction des valeurs pour les axes X et Y et les noms des conteneurs
for item in data['data']['result']:
    # Sélectionner les valeurs de temps (axe X) et de valeur (axe Y)
    x_values.append(float(item["value"][0]))  # Valeur en première position
    y_values.append(float(item["value"][1]))  # Valeur en deuxième position
    # Ajouter le nom du conteneur
    container_names.append(item["metric"]["container"])

# Création du tracé en assignant une couleur différente à chaque conteneur
for i in range(len(x_values)):
    plt.plot(x_values[i], y_values[i], marker='o', linestyle='', label=container_names[i])

# Ajout de la légende
plt.legend()

# Définition des étiquettes des axes et du titre
plt.xlabel('Temps')
plt.ylabel('Valeur')
plt.title('Tracé de la valeur en fonction du temps')
plt.grid(True)

# Affichage du tracé
plt.show()