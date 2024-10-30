# Utiliser l'image de base Miniconda pour tirer parti de Conda pour la gestion des environnements
FROM continuumio/miniconda3

# Définir le répertoire de travail comme /api
WORKDIR /api

# Mettre à jour le gestionnaire de paquets et installer des utilitaires nécessaires comme nano, unzip, python3 et curl
RUN apt update
RUN apt install -y nano unzip python3 curl

# Installer l'outil de ligne de commande Deta pour le déploiement
RUN curl -fsSL https://get.deta.dev/cli.sh | sh

# Copier le fichier requirements.txt dans le dossier des dépendances sur l'image Docker
COPY requirements.txt /dependencies/requirements.txt
# Installer les dépendances Python listées dans le requirements.txt
RUN pip install -r /dependencies/requirements.txt

# Copier le fichier app.py dans le répertoire /api sur l'image Docker
# COPY app.py /api

# Définir la commande pour démarrer le serveur avec Gunicorn en utilisant Uvicorn pour gérer les workers, avec un timeout de 120 secondes
CMD gunicorn app:app  --bind 0.0.0.0:$PORT --worker-class uvicorn.workers.UvicornWorker --timeout 120