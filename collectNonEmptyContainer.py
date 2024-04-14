import requests
import configparser
import json
import matplotlib.pyplot as plt

# Lire le fichier de configuration
config = configparser.ConfigParser()
config.read('config.ini')

prometheus_url = "http://172.16.20.23:32213/api/v1/query?query="

# Créer un dictionnaire pour stocker les réponses
responses = {}

# Obtenir la section 'requetes' du fichier de configuration
requetes_section = config['requetes']

# Parcourir toutes les clés de la section 'requetes' et effectuer les requêtes
for key in requetes_section:
    url = requetes_section[key]
    print("Requête pour :", key)

    # Effectuer la requête GET
    response = requests.get(prometheus_url+url)


    # Vérifier si la requête a réussi (code 200)
    if response.status_code == 200:
        # Ajouter la réponse au dictionnaire avec la clé correspondante
        responses = json.loads(response.text)
        print("La requête a réussi.")
    else:
        # Si la requête a échoué, afficher le code d'erreur
        print("La requête a échoué avec le code :", response.status_code)
    print("\n")  # Ajouter une ligne vide entre les requêtes

print(responses["status"])

# Enregistrer les réponses dans un fichier JSON
# with open('responses.json', 'w') as json_file:
#     json.dump(responses, json_file)


for item in responses['data']['result']:
    print("bonjour")

