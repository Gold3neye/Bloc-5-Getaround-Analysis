import argparse
import pandas as pd
import time
import mlflow
from mlflow.models.signature import infer_signature
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline

if __name__ == "__main__":
    ### Configuration de l'expérimentation MLFLOW
    experiment_name = "car_rental_price"  # Nom de l'expérience MLflow
    mlflow.set_experiment(experiment_name)  # Définir l'expérience
    experiment = mlflow.get_experiment_by_name(experiment_name)  # Obtenir l'expérience par nom

    client = mlflow.tracking.MlflowClient()  # Créer un client de suivi MLflow
    run = client.create_run(experiment.experiment_id)  # Créer une nouvelle exécution dans l'expérience

    print("Start training model")

    # Mesurer le temps d'exécution
    start_time = time.time()

    # Activer la journalisation automatique de MLFlow pour sklearn mais sans enregistrer les modèles immédiatement
    mlflow.sklearn.autolog(log_models=False)

    # Analyser les arguments passés via le shell script
    parser = argparse.ArgumentParser()
    parser.add_argument("--n_estimators")  # Nombre d'estimateurs pour le RandomForest
    parser.add_argument("--min_samples_split")  # Nombre minimum d'échantillons pour diviser un noeud
    args = parser.parse_args()

    # Importer le jeu de données
    df = pd.read_csv("https://full-stack-assets.s3.eu-west-3.amazonaws.com/Deployment/get_around_pricing_project.csv",
                     index_col=0)

    # Séparation des données en variables X et cible y
    X = df.iloc[:, 0:-1]
    y = df.iloc[:, -1]

    # Séparation des données en ensembles d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Prétraitement des données
    categorical_features = [
        "model_key",
        "fuel",
        "paint_color",
        "car_type",
        "private_parking_available",
        "has_gps",
        "has_air_conditioning",
        "automatic_car",
        "has_getaround_connect",
        "has_speed_regulator",
        "winter_tires"
    ]  # Colonnes contenant des chaînes ou des booléens
    categorical_transformer = OneHotEncoder(drop='first', handle_unknown='error', sparse_output=False)

    # Prétraitement des features numériques
    numerical_feature_mask = X_train.columns.isin(["mileage", "engine_power"])  # Colonnes contenant des entiers
    numerical_features = X_train.columns[numerical_feature_mask]
    numerical_transformer = StandardScaler()

    # Création du préprocesseur final
    feature_preprocessor = ColumnTransformer(
        transformers=[
            ("categorical_transformer", categorical_transformer, categorical_features),
            ("numerical_transformer", numerical_transformer, numerical_features)
        ]
    )

    # Importer les hyperparamètres à partir des arguments passés
    n_estimators = int(args.n_estimators)
    min_samples_split = int(args.min_samples_split)

    # Créer le modèle à partir du préprocesseur et du RandomForestClassifier
    model = Pipeline(steps=[
        ('features_preprocessing', feature_preprocessor),
        ("Regressor", RandomForestClassifier(n_estimators=n_estimators, min_samples_split=min_samples_split))
    ])

    # Journaliser l'expérimentation avec MLflow
    with mlflow.start_run(run_id=run.info.run_id) as run:
        model.fit(X_train, y_train)  # Entraîner le modèle
        predictions = model.predict(X_train)  # Prédire sur l'ensemble d'entraînement

        # Journaliser le modèle séparément pour plus de flexibilité dans la configuration
        mlflow.sklearn.log_model(
            sk_model=model,
            artifact_path=experiment_name,
            registered_model_name=f"Random_Forest_{experiment_name}",
            signature=infer_signature(X_train, predictions)
        )

    print(f"Training completed in {time.time() - start_time}")  # Afficher le temps total d'entraînement