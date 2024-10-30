import requests
import json
import pandas as pd


# Test du endpoint de prédiction localement avec un échantillon aléatoire
def test_prediction_2():
    """
    Teste le point de terminaison de prédiction en local en utilisant un échantillon aléatoire du dataset.
    """

    # Importer les données
    df = pd.read_csv("https://full-stack-assets.s3.eu-west-3.amazonaws.com/Deployment/get_around_pricing_project.csv",
                     index_col=0)
    df = df.sample(1)  # Sélectionne un échantillon aléatoire d'une ligne
    values = []

    # Créer le dictionnaire de l'échantillon
    for element in df.iloc[0, :].values.tolist():
        if type(element) != str:
            values.append(element.item())
        else:
            values.append(element)
    df_dict = {key: value for key, value in zip(df.columns, values)}

    # Poster localement
    response = requests.post(
        "http://localhost:4000/predict",  # Remplacer par une url pour tester l'API en ligne
        data=json.dumps(df_dict)
    )

    print(f"post: {df_dict}")
    print(f"   response: {response.json()}")


# Appeler la fonction pour tester la prédiction
test_prediction_2()