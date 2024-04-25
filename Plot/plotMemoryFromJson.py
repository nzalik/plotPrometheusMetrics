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

# Liste des noms de fichiers JSON à lire et tracer
#json_files = ['container_memory_usage_bytes.json', 'container_memory_usage_bytes2.json']
json_files = [
              #   './memory/container_memory_max_usage_bytes_li1_teaauth.json',
              # './memory/container_memory_max_usage_bytes_li1_teadb.json',
              # './memory/container_memory_max_usage_bytes_li1_teaimg.json',
              #'./memory/container_memory_max_usage_bytes_li1_tearecom.json',
              # './memory/container_memory_max_usage_bytes_li1_teaui.json',
               '../data/memory/teastore-recommender-6b67599fb9-gsr8s.json',
               '../data/memory/teastore-persistence-7d6bcb6b96-ltlf8.json',
               '../data/memory/teastore-webui-59f448d7f5-kvj5z.json',
               '../data/memory/teastore-registry-69c86867cd-qrd98.json',
               '../data/memory/teastore-image-6b9796d7c7-pqvvq.json',
               '../data/memory/teastore-db-7685d7b587-xc96b.json',
               '../data/memory/teastore-auth-8877cbcc9-287j7.json',
              ]

# Tracer chaque jeu de données JSON
for file_name in json_files:
    dates, valeurs = plot_json(file_name)
    plt.plot(dates, valeurs, label=file_name)

# Ajouter des titres et libellés aux axes
plt.title('Container memory usage ')
plt.xlabel('Date')
plt.ylabel('cores')

# Ajouter une légende pour les différentes lignes
#plt.legend()

# Afficher le graphique
plt.show()