# 🐧 Penguins of Madagascar - Species Classification

This project classifies penguin species based on beak length, flipper length, and body mass. It includes an automated pipeline that fetches new penguin data daily from an API and predicts its species.

## 🚀 Features
- **Feature Selection**: Identifies the most relevant features using Mutual Information, RFE, Random Forest, and Permutation Importance.
- **Model Training**: Uses **Logistic Regression** for species classification.
- **Automated Data Retrieval**: Fetches new penguin data from an API every morning at 07:30 AM.
- **GitHub Actions Integration**: Automates prediction updates.
- **GitHub Pages Deployment**: Displays the latest prediction -->     https://cami9000.github.io/Penguins-of-Madagascar/)

---

## 📂 **Repository Structure**
```bash
Penguins-of-Madagascar/
│── .github/workflows               # Github Actions workflow
│── Features and model.ipynb        # Feature selection and model training
│── New prediction with API.ipynb   # Prediction using API data
│── Prediction.ipynb                # Prediction based on local input
│── README.md                       # Documentation (this file)
│── penguin_classifier.joblib       # Saved model file
│── penguins.db                     # SQL Database
│── prediction.txt                  # Latest prediction result
```


## 📊 **Feature Selection**

To identify the most relevant features, the following methods were used:

Feature	        Mutual Info	  RFE	   Random Forest	Permutation	  Keep/Remove?
bill_length_mm	  ✅	        ✅	      ✅	            ✅	        Keep ✅
flipper_length_mm	✅	        ❌	      ✅	            ❌	        Keep ✅
bill_depth_mm	    ✅	        ✅	      ✅	            ✅	        Keep ✅
body_mass_g	      ❌	        ✅	      ❌	            ❌	        Remove ❌
island_id	        ❌	        ✅	      ❌	            ✅	        Remove ❌

🚀 Final features used in the model:
bill_length_mm, flipper_length_mm, bill_depth_mm


## 🏆 **Model Training**

The model was trained using Logistic Regression, achieving an accuracy of 99% via cross-validation.

Model Performance:
Test Accuracy: 100%
Cross-Validation Accuracy: 99% ± 0.00
**The trained model is saved as:**
    models/penguin_classifier.joblib


## 🔄 **Automated Prediction Pipeline**

🔹 1️⃣ Fetch New Penguin Data
import requests

def fetch_new_penguin():
    url = "http://130.225.39.127:8000/new_penguin/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None
🔹 2️⃣ Make Prediction
from joblib import load
import numpy as np

model = load("models/penguin_classifier.joblib")
penguin = fetch_new_penguin()

if penguin:
    features = np.array([[penguin["bill_length_mm"], penguin["flipper_length_mm"], penguin["bill_depth_mm"]]])
    predicted_class = model.predict(features)[0]
    species_mapping = {0: "Adelie", 1: "Chinstrap", 2: "Gentoo"}
    predicted_species = species_mapping.get(predicted_class, "Unknown")

    with open("prediction.txt", "w") as file:
        file.write(f"Latest Prediction: {predicted_species}\n")
🔹 3️⃣ Automating with GitHub Actions
GitHub Actions runs every day at 07:30 AM and updates prediction.txt:

name: Fetch and Predict Penguin

on:
  schedule:
    - cron: "30 6 * * *"  # Runs daily at 07:30 CET (06:30 UTC)
  workflow_dispatch:

jobs:
  predict:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run prediction script
        run: python predict.py
      - name: Commit and push prediction
        run: |
          git config --global user.name "GitHub Actions"
          git config --global user.email "actions@github.com"
          git add prediction.txt
          git commit -m "Updated prediction"
          git push

## **🛠 Running the Project Locally**

To test the project locally, follow these steps:

1️⃣ Clone the repository:

git clone https://github.com/Cami9000/Penguins-of-Madagascar.git
cd Penguins-of-Madagascar
2️⃣ Install dependencies:

pip install -r requirements.txt
3️⃣ Train the model:

python train_model.py
4️⃣ Run the prediction script:

python predict.py
5️⃣ Check the latest prediction:

cat prediction.txt


#**📌 Technologies Used**

Python (pandas, sklearn, joblib, requests)
SQLite for database storage
GitHub Actions for automation
GitHub Pages for displaying predictions

