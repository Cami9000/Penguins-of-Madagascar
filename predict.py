from joblib import load
import numpy as np
import requests
from datetime import datetime

# Load the trained model
model = load("penguin_classifier.joblib")

# Fetch a new penguin from the API
def fetch_new_penguin():
    url = "http://130.225.39.127:8000/new_penguin/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

penguin = fetch_new_penguin()

if penguin:
    features = np.array([[penguin["bill_length_mm"], penguin["flipper_length_mm"], penguin["bill_depth_mm"]]])
    predicted_class = model.predict(features)[0]

    # Convert prediction to species name
    species_mapping = {0: "Adelie", 1: "Chinstrap", 2: "Gentoo"}
    predicted_species = species_mapping.get(predicted_class, "Unknown")

    # Get timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Save latest and previous predictions in the same file
    with open("prediction.txt", "a") as file:  # 'a' = append (tilføj uden at slette det gamle)
        file.write(f"{timestamp}: {predicted_species}\n")
