import requests
import configparser
import json
import matplotlib.pyplot as plt
import time

while True:
    # Lire le fichier de configuration
    config = configparser.ConfigParser()
    config.read('config.ini')

    prometheus_url = "http://172.16.192.21:32431/api/v1/query?query="

    # Créer un dictionnaire pour stocker les réponses
    responses = {}

    # Obtenir la section 'requetes' du fichier de configuration
    requetes_section = config['requetes']

    # Parcourir toutes les clés de la section 'requetes' et effectuer les requêtes
    for key in requetes_section:
        url = requetes_section[key]
        print("Requête pour :", key)

        # Effectuer la requête GET
        response = requests.get(prometheus_url + url)
        print("request url :", prometheus_url + url)

        # Vérifier si la requête a réussi (code 200)
        if response.status_code == 200:
            # Ajouter la réponse au dictionnaire avec la clé correspondante
            responses[key] = json.loads(response.text)
            print("La requête a réussi.")
        else:
            # Si la requête a échoué, afficher le code d'erreur
            print("La requête a échoué avec le code :", response.status_code)
        print("\n")  # Ajouter une ligne vide entre les requêtes

    x_values = []
    y_values = []
    container_names = []

    data = responses['requete1']

    # Extraction des valeurs pour les axes X et Y et les noms des conteneurs
    for item in data['data']['result']:
        if "metric" in item and "container" in item["metric"]:
            # Sélectionner les valeurs de temps (axe X) et de valeur (axe Y)
            x_values.append(float(item["value"][0]))  # Valeur en première position
            y_values.append(float(item["value"][1]))  # Valeur en deuxième position
            # Ajouter le nom du conteneur
            container_names.append(item["metric"]["container"])

    # Création du tracé en assignant une couleur différente à chaque conteneur
    plt.figure()
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

    # Attendre une seconde avant la prochaine itération
    time.sleep(1)
