import json
import matplotlib.pyplot as plt
import datetime
#from datetime import datetime
import re
import matplotlib.dates as mdates

# Définir une fonction pour lire et traiter chaque fichier JSON
def plot_json(file_name):
    with open(file_name, 'r') as file:
        json_data = json.load(file)

    # data = json_data['data']['result'][0]['values']
    #
    # dates = [d[0] for d in data]
    # valeurs = [float(d[1]) for d in data]


    data = json_data['data']['result'][0]['values']



    dates = [datetime.datetime.utcfromtimestamp(d[0]) for d in data]
    #dates = [d[0] for d in data]
    valeurs = [float(d[1]) for d in data]

    print(max(valeurs))
    print(min(dates))
    print(max(dates))
    #print(dates)
    print(len(dates))
    print(len(valeurs))
    return dates, valeurs


# Liste des noms de fichiers JSON à lire et tracer
#json_files = ['container_memory_usage_bytes.json', 'container_memory_usage_bytes2.json']
json_files = [
     '../data/cpu/teastore-webui-59f448d7f5-cmhdv.json',
    '../data/cpu/teastore-registry-69c86867cd-l7c7q.json',
    '../data/cpu/teastore-recommender-6b67599fb9-vqj6x.json',
    '../data/cpu/teastore-persistence-7d6bcb6b96-w9tg4.json',
    '../data/cpu/teastore-image-6b9796d7c7-wlhnt.json',
    '../data/cpu/teastore-db-7685d7b587-6bxzn.json',
    '../data/cpu/teastore-auth-8877cbcc9-rmt4s.json'
]

# Tracer chaque jeu de données JSON
for file_name in json_files:
    file_parts = file_name.split("/")
    last_part = (file_parts[-1]).split(".")[0]
    result = re.split(r'-\d+', last_part)[0]
    dates, valeurs = plot_json(file_name)
    #plt.plot_date(dates, valeurs, linestyle='--', color='b')

    #plt.xlim(datetime(2024, 4, 30, 7, 24))  # Minimum and maximum values for x-axis
    #plt.ylim(0, max(valeurs))  # Minimum and maximum values for y-axis

    plt.plot(dates, valeurs, label=result)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))

# Ajouter des titres et libellés aux axes
#plt.title('Container cpu usage ')
plt.xlabel('Time (s)')
plt.ylabel('Cores')

# Ajouter une légende pour les différentes lignes
plt.legend(bbox_to_anchor=(-.14, 1.02, 1.27, .102), loc='lower left',
           ncols=4, mode="expand", borderaxespad=0.)

# Afficher le graphique
#plt.savefig('cpuwithoutload.png')
plt.show()
