import requests

def fetch_new_penguin():
    url = "http://130.225.39.127:8000/new_penguin/"
    response = requests.get(url)

    if response.status_code == 200:
        new_penguin = response.json()
        print("✅ New penguin picked up:", new_penguin)
        return new_penguin
    else:
        print("Error retrieving penguin:", response.status_code)
        return None

import numpy as np
from joblib import load
import warnings
warnings.filterwarnings('ignore')


# Load the saved model
model = load("penguin_classifier.joblib")

# Get a new pinguin from API
new_penguin = fetch_new_penguin()

if new_penguin:
    # Only relevant features
    feature_values = np.array([[new_penguin["bill_length_mm"], 
                                new_penguin["flipper_length_mm"], 
                                new_penguin["bill_depth_mm"]]])
    
    # Predict the pinguin
    predicted_class = model.predict(feature_values)[0]

    # Convert numbers back to species name
    species_mapping = {0: "Adelie", 1: "Chinstrap", 2: "Gentoo"}
    predicted_species = species_mapping.get(predicted_class, "Unknown")

    print(f"Prediction: The penguin is a {predicted_species}!")
    
    # Save the result to a file so we can display it on GitHub Pages
    with open("prediction.txt", "w") as file:
        file.write(f"Latest prediction: {predicted_species}\n")
