import mlflow
from xmlrpc.client import Boolean
import uvicorn
import pandas as pd
from pydantic import BaseModel
from fastapi import FastAPI

# La description apparaîtra dans la documentation
description = """
L'API GetAround vous aide à en savoir plus sur les locations GetAround.

GetAround est une entreprise qui permet aux propriétaires de voitures de louer leurs voitures à des clients. Parfois, un client peut être en retard pour le check-out et le client suivant peut devoir attendre pour le check-in. Cela entraîne des annulations, ayant un impact négatif sur les revenus et l'image de l'entreprise. L'objectif de ce projet est de pouvoir anticiper les retards de check-out, et d'évaluer l'impact de certaines mesures sur les revenus des propriétaires de voitures.
## Aperçu

* `/preview` affiche quelques lignes de votre jeu de données

## Machine Learning

* `/predict` prédit le prix de location par jour pour la ou les voitures données.

Consultez la documentation pour plus d'informations sur chaque endpoint.
"""

# Tags pour trier facilement nos routes
tags_metadata = [
    {
        "name": "Preview",
        "description": "Fonctions directement liées aux données",
    },
    {
        "name": "Machine-Learning",
        "description": "Fonctions liées au Machine Learning"
    },
]

# Initialiser l'objet API
app = FastAPI(
    title="GetAround API",
    description=description,
    version="1.0",
    contact={
        "name": "GetAround API - GitHub Quentin50",
        "url": "https://github.com/Quentin50",
    },
    openapi_tags=tags_metadata
)


# Définir les caractéristiques utilisées en machine learning
class PredictionFeatures(BaseModel):
    model_key: str
    mileage: int
    engine_power: int
    fuel: str
    paint_color: str
    car_type: str
    private_parking_available: Boolean
    has_gps: Boolean
    has_air_conditioning: Boolean
    automatic_car: Boolean
    has_getaround_connect: Boolean
    has_speed_regulator: Boolean
    winter_tires: Boolean


# Prévisualiser quelques lignes du jeu de données
@app.get("/preview", tags=["Preview"])
async def random_car(rows: int = 10):
    """
    Obtenez un échantillon du jeu de données.
    Vous pouvez spécifier le nombre de lignes renvoyées avec `rows`, par défaut c'est `10`.
    """
    print("/preview called")
    df = pd.read_csv("data/get_around_pricing_project.csv")

    # Sélectionner seulement n lignes
    sample = df.sample(rows)
    return sample.to_json()


# Prédire le prix de location pour les voitures données
@app.post("/predict", tags=["Machine-Learning"])
async def predict(predictionFeatures: PredictionFeatures):
    """
    Prédire le prix de location par jour pour une voiture donnée. Retourne un dictionnaire:
    {'prediction': VALEUR_PRÉDITE}
    Toutes les valeurs des colonnes sont nécessaires, en tant que dictionnaire ou données de formulaire.
    """
    print("/predict called")
    # Lire les données
    df = pd.DataFrame(dict(predictionFeatures), index=[0])

    # Charger le modèle depuis mlflow
    logged_model = 'runs:/d72a57cad595407f8d4688a3dd8c897e/car_rental_price'

    # Charger le modèle en tant que PyFuncModel.
    loaded_model = mlflow.pyfunc.load_model(logged_model)
    prediction = loaded_model.predict(df)

    # Formater la réponse
    response = {"prediction": prediction.tolist()[0]}
    return response

# Que faire lorsque le script est exécuté en tant que script principal
if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=4000, reload=True)