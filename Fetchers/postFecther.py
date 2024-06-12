import requests
import configparser
import json
from datetime import datetime, timedelta, date
import os
import matplotlib.pyplot as plt
import time

file_path = '../teastore.json'


def read_parameters_from_json(file_path):
    with open(file_path, 'r') as file:
        parameters = json.load(file)
    return parameters


parameters = read_parameters_from_json(file_path)

load = parameters['DURATION']

window = 6
window2 = 10

#os.makedirs("../data", exist_ok=True)

today = date.today()
dir_name = today.strftime("%d-%m-%Y")

save_path = f"../{dir_name + '/data' + parameters['WORKLOAD']}/"  #The directory where you want things to be saved
#save_path = "../data/"  #The directory where you want things to be saved

if os.path.exists(save_path):
    # Récupérer la liste des fichiers dans le répertoire "data"
    files = os.listdir(save_path)

    # Trouver le nombre de fichiers "data" existants
    #data_count = sum(1 for f in files if f.startswith("data"))

    # Construire le nouveau nom de répertoire
    new_dir_name = f"data_{datetime.now().strftime('%H-%M-%S')}"
    #new_dir_name = f"data{data_count + 1}_{datetime.now().strftime('%H-%M')}"
    save_path = f"../{dir_name}/{new_dir_name}"

    # Créer le nouveau répertoire
    #os.makedirs(save_path, exist_ok=True)
    #print(f"Nouveau répertoire créé : {save_path}")

prom_url = parameters['PROMETHEUS_URL']


def query_prometheus(query):
    my_url = prom_url + '/api/v1/' + query
    #print("Querying " + url)
    res = None

    print(my_url)

    try:
        res = requests.get(my_url).json()
    # print("Query successful")
    #print(res)
    except Exception as e:
        print(e)

    if res != None and 'error' in res:
        res = None

    return res


def query_svc_names(namespace='default'):
    query_str = '/label/pod/values?match[]=kube_pod_container_info{namespace="' + namespace + '"}'
    res = query_prometheus(query_str)
    svc_names = []
    services = res['data']
    print(services)
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

    return services


def _init_metric_metadata(metric, interval):
    #for metric in names:

    query_str = 'metadata?metric=' + metric
    url = prom_url + '/api/v1/' + query_str
    metric_obj = {}
    res = None

    try:
        res = requests.get(url).json()
    except Exception as e:
        print(e)

    if res != None and 'error' in res:
        print(res["error"])
        res = None
    elif res != None and res['data']:
        metadata = res['data'][metric][0]

        if (metadata['type'] == "gauge"):
            return f"{metric}{{pod=\"{container_name}\", container!=\"\" }}"
        elif (metadata['type'] == "counter"):
            return f"irate({metric}{{pod=\"{container_name}\", container!=\"\"}}[{interval}])"
        else:
            return f"{metric}{{namespace=\"default\"}}"


def read_ini_file(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)
    return config


all_services = query_svc_names()

file_path = '../config.ini'
config = read_ini_file(file_path)

prometheus_url = prom_url + "/api/v1/query?query="

# Créer un dictionnaire pour stocker les réponses
responses = {}

# Obtenir la section 'requetes' du fichier de configuration
requetes_section = config['requetes']

# Parcourir toutes les clés de la section 'requetes' et effectuer les requêtes

for section_name in config.sections():

    for key, value in config.items(section_name):
        for svc in all_services:

            current_timestamp = datetime.now().timestamp()

            current_time = datetime.now()
            valueTime = parameters['DURATION']
            unit = parameters['DURATION_UNIT']
            # Subtract 10 minutes
            if unit == "hours":
                new_time = current_time - timedelta(hours=int(valueTime))
                interval = valueTime + "h"
            else:
                new_time = current_time - timedelta(minutes=int(valueTime))
                interval = valueTime + "m"

            #new_time = current_time - timedelta(minutes=window2)

            # Convert the result to a timestamp
            new_timestamp = new_time.timestamp()

            step = parameters['STEP']
            container_name = svc

            query_str = _init_metric_metadata(value, interval)

            payload = {'query': query_str, 'start': new_timestamp, 'end': current_timestamp, 'step': step}

            url = prom_url + '/api/v1/query_range?'

            #print("Querying " + url + " with payload " + str(payload))

            res = None
            directory = save_path + "/" + key
            filename = svc + '.json'
            query_str_file = os.path.join(directory, filename)
            #query_str_file = "nom_du_fichier.json"
            os.makedirs(directory, exist_ok=True)
            # Query Prometheus
            try:
                res = requests.post(url, headers={'Content-Type': 'application/x-www-form-urlencoded'},
                                    data=payload).json()
                #print("la reponse")
                #print(res)
                with open(query_str_file, 'a') as f:
                    json.dump(res, f, ensure_ascii=False)

            except Exception as e:
                print(e)
                print("...Fail at Prometheus request.")

current_timestamp = datetime.now().timestamp()

current_time = datetime.now()

valueTime = parameters['DURATION']
unit = parameters['DURATION_UNIT']
# Subtract 10 minutes
if unit == "hours":
    new_time = current_time - timedelta(hours=int(valueTime))
else:
    new_time = current_time - timedelta(minutes=int(valueTime))

# Subtract 10 minutes
#new_time = current_time - timedelta(hours=1)

# Convert the result to a timestamp
new_timestamp = new_time.timestamp()

step = parameters['STEP']
container_name = "pod_info"

query_str = "kube_deployment_status_replicas{namespace=\"default\"}"

url = prom_url + '/api/v1/query_range?'

payload = {'query': query_str, 'start': new_timestamp, 'end': current_timestamp, 'step': step}

res = None

directory = save_path + "/pod_info"
filename = container_name + '.json'
query_str_file = os.path.join(directory, filename)
#query_str_file = "nom_du_fichier.json"
os.makedirs(directory, exist_ok=True)
# Query Prometheus
try:
    #res = requests.get(url, headers={'Content-Type': 'application/x-www-form-urlencoded'}).json()
    res = requests.post(url, headers={'Content-Type': 'application/x-www-form-urlencoded'},
                        data=payload).json()
    #print("la reponse pour les pods")
    #print(res)
    with open(query_str_file, 'a') as f:
        json.dump(res, f, ensure_ascii=False)

except Exception as e:
    print(e)
    print("...Fail at Prometheus request.")
