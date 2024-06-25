import csv
from datetime import date

def generate_linear_profile(duration, step_size, start_value, end_value):
    """
    Génère un profil de charge linéaire avec la progression donnée.

    Args:
        duration (float): Durée totale du profil de charge (en secondes).
        step_size (float): Taille de chaque étape de la progression.
        start_value (float): Valeur de départ.
        end_value (float): Valeur finale.

    Returns:
        None
    """

    today = date.today()
    dir_name = today.strftime("%d-%m-%Y")

    dtm = int(duration/60)

    file_name = f"intensity_profile-five-{dir_name}-{dtm}min-{end_value}requests.csv"
    with open(file_name, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['timestamp', 'requests'])

        for t in range(0, int(duration + step_size), int(step_size)):
            value = start_value + (end_value - start_value) * t / duration
            if t % 5 == 0:  # Injecter le même nombre de requêtes pendant 5 secondes consécutives
                value = value // 1  # Arrondir la valeur au nombre entier le plus proche
            writer.writerow([t+0.5, value])

        print(f"Profil de charge linéaire généré: {file_name}")

# Paramètres de configuration
DURATION = 180.5  # Durée totale du profil de charge (en secondes)
STEP_SIZE = 1.0  # Taille de chaque étape de la progression
START_VALUE = 0.5  # Valeur de départ
END_VALUE = 100.0  # Valeur finale

generate_linear_profile(DURATION, STEP_SIZE, START_VALUE, END_VALUE)