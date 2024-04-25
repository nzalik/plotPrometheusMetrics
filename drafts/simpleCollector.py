import requests
import configparser

# Lire le fichier de configuration
config = configparser.ConfigParser()
config.read('config.ini')

prometheus_url = "http://172.16.20.23:31436/api/v1/query?query="

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
        # Imprimer le contenu de la réponse
        print(response.text)
    else:
        # Si la requête a échoué, afficher le code d'erreur
        print("La requête a échoué avec le code :", response.status_code)
    print("\n")  # Ajouter une ligne vide entre les requêtes
