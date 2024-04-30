import requests
import configparser
import json
from datetime import datetime, timedelta
import os
import matplotlib.pyplot as plt
import time


def read_parameters_from_json(file_path):
    with open(file_path, 'r') as file:
        parameters = json.load(file)
    return parameters


file_path = '../teastore.json'
parameters = read_parameters_from_json(file_path)
print(parameters)

prom_url = parameters['PROMETHEUS_URL']


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


def _init_metric_metadata(metric):
    #for metric in names:
    print("#########################")
    print(metric)
    query_str = 'metadata?metric=' + metric
    url = prom_url + '/api/v1/' + query_str
    print("Querying metadata at " + url)
    metric_obj = {}
    res = None

    try:
        res = requests.get(url).json()
    except Exception as e:
        print(e)
        print("...Fail at Prometheus request.")

    if res != None and 'error' in res:
        print(res["error"])
        res = None
    elif res != None and res['data']:
        metadata = res['data'][metric][0]
        print("#########################")
        print(metadata)

        if (metadata['type'] == "gauge"):
            return f"sum({metric}{{pod=\"{container_name}\"}})/1"
        else:
            return f"sum(irate({metric}{{pod=\"{container_name}\"}}[10m]))/1"


def read_ini_file(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)
    return config


all_services = query_svc_names()

print("voici les services")
print(all_services)

file_path = '../config.ini'
config = read_ini_file(file_path)

prometheus_url = prom_url + "/api/v1/query?query="

# Créer un dictionnaire pour stocker les réponses
responses = {}

# Obtenir la section 'requetes' du fichier de configuration
requetes_section = config['requetes']

# Parcourir toutes les clés de la section 'requetes' et effectuer les requêtes

for section_name in config.sections():
    print("Section:", section_name)
    for key, value in config.items(section_name):
        for svc in all_services:

            current_timestamp = datetime.now().timestamp()

            current_time = datetime.now()

            # Subtract 10 minutes
            new_time = current_time - timedelta(minutes=10)

            # Convert the result to a timestamp
            new_timestamp = new_time.timestamp()

            step = parameters['STEP']
            container_name = svc

            query_str = _init_metric_metadata(value)

            payload = {'query': query_str, 'start': new_timestamp, 'end': current_timestamp, 'step': step}

            url = prom_url + '/api/v1/query_range?'

            print("Querying " + url + " with payload " + str(payload))

            res = None
            directory = "../data/"+key
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
