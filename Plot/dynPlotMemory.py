import glob
import json
import matplotlib.pyplot as plt
import datetime

# Définir une fonction pour lire et traiter chaque fichier JSON
def plot_json(file_name):
    with open(file_name, 'r') as file:
        json_data = json.load(file)

    data = json_data['data']['result'][0]['values']

    dates = [datetime.datetime.utcfromtimestamp(d[0]) for d in data]
    valeurs = [float(d[1]) for d in data]

    return dates, valeurs

# Chemin du dossier contenant les fichiers JSON
folder_path = '../data/memory'

# Obtenir la liste des fichiers JSON dans le dossier
json_files = glob.glob(folder_path + '*.json')

# Tracer chaque jeu de données JSON
for file_name in json_files:
    dates, valeurs = plot_json(file_name)
    plt.plot(dates, valeurs, label=file_name)

# Ajouter des titres et libellés aux axes
plt.title('Container memory usage')
plt.xlabel('Date')
plt.ylabel('cores')

# Ajouter une légende pour les différentes lignes
#plt.legend()

# Afficher le graphique
plt.show()