import os
import json


def read_all_json_files(folder_path):
    # Initialize an empty dictionary to store data from JSON files
    all_data = {}

    # List all files in the specified folder
    for filename in os.listdir(folder_path):
        # Check if the file is a JSON file
        if filename.endswith('.json'):
            file_path = os.path.join(folder_path, filename)
            # Open and read the JSON file
            with open(file_path, 'r') as file:
                # Load JSON data into a dictionary
                data = json.load(file)
                # Store data in the dictionary with the filename as the key
                all_data[filename] = data

    return all_data
