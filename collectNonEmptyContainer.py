import requests
import configparser
import json
import matplotlib.pyplot as plt

# Lire le fichier de configuration
config = configparser.ConfigParser()
config.read('config.ini')

prometheus_url = "http://172.16.192.22:32213/api/v1/query?query="

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
        responses[key] = json.loads(response.text)
        print("La requête a réussi.")
    else:
        # Si la requête a échoué, afficher le code d'erreur
        print("La requête a échoué avec le code :", response.status_code)
    print("\n")  # Ajouter une ligne vide entre les requêtes

# Enregistrer les réponses dans un fichier JSON
# with open('responses.json', 'w') as json_file:
#     json.dump(responses, json_file)

# Extraction des valeurs pour les axes X et Y et les noms des conteneurs
for key, response in responses.items():
    x_values = []
    y_values = []
    container_names = []

    for item in response['data']['result']:
        # Sélectionner les valeurs de temps (axe X) et de valeur (axe Y)
        x_values.append(float(item["value"][0]))  # Valeur en première position
        y_values.append(float(item["value"][1]))  # Valeur en deuxième position
        # Ajouter le nom du conteneur
        if "container" in item["metric"]:
            container_names.append(item["metric"]["container"])

    # Création du tracé en assignant une couleur différente à chaque conteneur
    if x_values and y_values and container_names:
        for i in range(len(x_values)):
            plt.plot(x_values[i], y_values[i], marker='o', linestyle='', label=container_names[i])

        # Ajout de la légende
        plt.legend()

        # Définition des étiquettes des axes et du titre
        plt.xlabel('Temps')
        plt.ylabel('Valeur')
        plt.title(f'Tracé de la valeur en fonction du temps ({key})')
        plt.grid(True)

        # Affichage du tracé
        plt.show()
    else:
        print("Aucune donnée disponible pour tracer le graphique.")
