echo "Accédez via le navigateur à localhost:4000/docs"

# Exécuter le conteneur localement avec un montage de liaison ;
docker run -it -v "%cd%:/home/app" -p 4000:4000 -e PORT=4000 \
-e MLFLOW_TRACKING_URI=%MLFLOW_TRACKING_URI% \
-e AWS_ACCESS_KEY_ID=%AWS_ACCESS_KEY_ID% \
-e AWS_SECRET_ACCESS_KEY=%AWS_SECRET_ACCESS_KEY% \
-e BACKEND_STORE_URI=%BACKEND_STORE_URI% \
-e ARTIFACT_ROOT=%ARTIFACT_ROOT% getaround-api