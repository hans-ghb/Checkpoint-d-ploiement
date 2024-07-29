import os

import pandas as pd

import requests

from dotenv import load_dotenv 

from PIL import Image

import io

from io import BytesIO


# Recuperation des variables dans le fichier .env qui contient l'API_Key

load_dotenv()

# Recuperation de la Clé de l'API depuis le fichier .env

api_key = os.getenv('API_KEY')

# L'url de la requête

api_url = 'https://api.nasa.gov/planetary/apod'

# Les paramêtres de la requête 

param = ({
    'api_key': api_key,
    'date': '2024-07-29'

})

# Récuperation de l'image du jour

response = requests.get(api_url, params= param)

# Afficher la reponse 

print(response.json())

# Afficher le code de la reponse

print(response.status_code)

# Afficher l'image 

images = response.json()

image_url = 'https://apod.nasa.gov/apod/image/2407/UluruMilkyWay_Inwood_1350.jpg'
image_response = requests.get(image_url)
image = Image.open(BytesIO(image_response.content))

image.show()

image.save('Images_du_jour.jpg')

# Stockage de la requête dans un dataframe

df = pd.DataFrame([images])
print(df)

print(df.head())

# Enregistrer le dataframe dans un fichier CSV
df.to_csv('df_nasa.csv')

# Afficher un message de confirmation
print("Les données ont été enregistrées dans 'env'")
