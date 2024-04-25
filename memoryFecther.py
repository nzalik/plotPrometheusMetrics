import requests
import configparser
import json
from datetime import datetime, timedelta
import os
import matplotlib.pyplot as plt
import time
prom_url = "http://172.16.192.8:30959"

def query_prometheus(query):
    url = prom_url + '/api/v1/' + query
    print("Querying " + url)
    res = None

    try:
        res = requests.get(url).json()
        print("Query successful")
        print(res)
    except Exception as e:
        print(e)
        print("...Fail at Prometheus.")

    if res != None and 'error' in res:
        print(res["error"])
        res = None

    return res

def query_svc_names(namespace='default'):
    query_str = '/label/pod/values?match[]=kube_pod_container_info{namespace="' + namespace + '"}'
    print("Querying existing services by " + query_str)
    res = query_prometheus(query_str)
    svc_names = []
    services = res['data']
    # if res != None:
    #     svc_names = res['data']
    #     for name in svc_names:
    #         query_str = '/query?query=container_last_seen{namespace="' + namespace + '", pod="' + name + '"}'
    #         res = query_prometheus(query_str)
    #         if res != None and len(res['data']['result']) > 0:
    #             instance = res['data']['result'][0]['metric']['instance'].split(':')[0]
    #             node = res['data']['result'][0]['metric']['node']
    #             service_obj = {'pod': name, 'instance': instance, 'node': node}
    #             services.append(service_obj)

    # print("...Services found at namespace " + namespace + ': ' + str(services))
    print("voici les services")
    print(services)
    return services


all_services = query_svc_names()
print("voici les services")
print(all_services)

# Lire le fichier de configuration
config = configparser.ConfigParser()
config.read('config.ini')

prometheus_url = "http://172.16.192.8:30959/api/v1/query?query="

# Créer un dictionnaire pour stocker les réponses
responses = {}

# Obtenir la section 'requetes' du fichier de configuration
requetes_section = config['requetes']

# Parcourir toutes les clés de la section 'requetes' et effectuer les requêtes
# for key in requetes_section:
#     url1 = requetes_section[key]
#     print("Requête pour :", key)
for svc in all_services:

    print("voici le services")
    print(svc)

    # Effectuer la requête GET
    #response = requests.get(prometheus_url + url)
    #print("request url :", prometheus_url + url)

    #query_str = self._query_str(svc)

    #svc = "teastore-webui-59f448d7f5-jqx57"

    # Spécifier les valeurs de début et de fin de l'expérimentation
    debut_exp = datetime(year=2024, month=4, day=24, hour=14, minute=44)
    fin_exp = datetime(year=2024, month=4, day=24, hour=14, minute=46)

    # Convertir les valeurs de début et de fin en timestamps Unix
    debut_exp_timestamp = debut_exp.timestamp()
    fin_exp_timestamp = fin_exp.timestamp()
    current_timestamp = datetime.now().timestamp()

    current_time = datetime.now()

    # Subtract 10 minutes
    new_time = current_time - timedelta(minutes=10)

    # Convert the result to a timestamp
    new_timestamp = new_time.timestamp()

    print("Début de l'expérimentation (timestamp) :", debut_exp_timestamp)
    print("Fin de l'expérimentation (timestamp) :", fin_exp_timestamp)

    step = "1s"
    container_name = svc
    start_at = "1713929399.433031"
    end_at = '1713929699.433031'
    #container_name = "teastore-webui-59f448d7f5-jqx57"

    query_str = f"sum(container_memory_working_set_bytes{{pod=\"{container_name}\"}})/1"

    #query_str = "sum(irate(container_cpu_usage_seconds_total{pod=\"teastore-webui-59f448d7f5-jqx57\"}[5m]))/1"

    payload = {'query': query_str, 'start': new_timestamp, 'end': current_timestamp, 'step': step}
    #payload = {'query': query_str, 'start': start_dt.timestamp(), 'end': end_dt.timestamp(), 'step': step + 's'}
    #payload = {'query': query_str, 'step': step}

    url = prom_url + '/api/v1/query_range?'

    print("Querying " + url + " with payload " + str(payload))

    res = None
    directory = "./data/memory"
    filename = svc + '.json'
    query_str_file = os.path.join(directory, filename)
    #query_str_file = "nom_du_fichier.json"
    os.makedirs(directory, exist_ok=True)
    # Query Prometheus
    try:
        res = requests.post(url, headers={'Content-Type': 'application/x-www-form-urlencoded'}, data=payload).json()
        print("la reponse")
        print(res)
        with open(query_str_file, 'a') as f:
            json.dump(res, f, ensure_ascii=False)

    except Exception as e:
        print(e)
        print("...Fail at Prometheus request.")

    # Vérifier si la requête a réussi (code 200)
        # Ajouter la réponse au dictionnaire avec la clé correspondante
        #responses[key] = json.loads(res.text)
        #print("La requête a réussi.")

 # Ajouter une ligne vide entre les requêtes

# x_values = []
# y_values = []
# container_names = []
#
# data = responses['requete1']
#
# # Extraction des valeurs pour les axes X et Y et les noms des conteneurs
# for item in data['data']['result']:
#     if "metric" in item and "container" in item["metric"]:
#         # Sélectionner les valeurs de temps (axe X) et de valeur (axe Y)
#         x_values.append(float(item["value"][0]))  # Valeur en première position
#         y_values.append(float(item["value"][1]))  # Valeur en deuxième position
#         # Ajouter le nom du conteneur
#         container_names.append(item["metric"]["container"])
#
# # Création du tracé en assignant une couleur différente à chaque conteneur
# plt.figure()
# for i in range(len(x_values)):
#     plt.plot(x_values[i], y_values[i], marker='o', linestyle='', label=container_names[i])
#
# # Ajout de la légende
# plt.legend()
#
# # Définition des étiquettes des axes et du titre
# plt.xlabel('Temps')
# plt.ylabel('Valeur')
# plt.title('Tracé de la valeur en fonction du temps')
# plt.grid(True)
#
# # Affichage du tracé
# plt.show()

# Attendre une seconde avant la prochaine itération
# time.sleep(1)
