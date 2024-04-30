import json
import matplotlib.pyplot as plt
import datetime
import re


# Définir une fonction pour lire et traiter chaque fichier JSON
def plot_json(file_name):
    with open(file_name, 'r') as file:
        json_data = json.load(file)

    data = json_data['data']['result'][0]['values']

    dates = [datetime.datetime.utcfromtimestamp(d[0]) for d in data]
    valeurs = [float(d[1]) for d in data]

    return dates, valeurs


# Liste des noms de fichiers JSON à lire et tracer
#json_files = ['container_receive_bytes_usage_bytes.json', 'container_receive_bytes_usage_bytes2.json']
json_files = [
    '../data2/network/teastore-webui-59f448d7f5-8z9cs.json',
    '../data2/network/teastore-registry-69c86867cd-mxccl.json',
    '../data2/network/teastore-recommender-6b67599fb9-7g8qv.json',
    '../data2/network/teastore-persistence-7d6bcb6b96-jcl4d.json',
    '../data2/network/teastore-image-6b9796d7c7-tsq8h.json',
    '../data2/network/teastore-db-7685d7b587-bl4vl.json',
    '../data2/network/teastore-auth-8877cbcc9-5k2jz.json'
]

# Tracer chaque jeu de données JSON
for file_name in json_files:
    file_parts = file_name.split("/")
    last_part = (file_parts[-1]).split(".")[0]
    result = re.split(r'-\d+', last_part)[0]
    dates, valeurs = plot_json(file_name)
    plt.plot(dates, valeurs, label=result)

# Ajouter des titres et libellés aux axes
#plt.title('Container receive_bytes usage ')
plt.xlabel('Time(s)')
plt.ylabel('Received bytes')

# Ajouter une légende pour les différentes lignes
plt.legend(bbox_to_anchor=(-.14, 1.02, 1.27, .102), loc='lower left',
           ncols=4, mode="expand", borderaxespad=0.)

# Afficher le graphique
plt.savefig('receivedbyteswithoutload.png')
plt.show()
