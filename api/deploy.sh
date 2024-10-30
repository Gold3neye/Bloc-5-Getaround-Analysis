# Connexion à Heroku
heroku login
heroku container:login

# "getaround-api-qg2022" doit être remplacé par le nom de votre application
heroku container:push web -a getaround-api-qg2022

# "getaround-api-qg2022" doit être remplacé par le nom de votre application
heroku container:release web -a getaround-api-qg2022

# Vous devez maintenant ajouter des paramètres à l'application Heroku sur le site web
# Les identifiants MLFlow sont nécessaires pour utiliser la route de machine learning

# "getaround-api-qg2022" doit être remplacé par le nom de votre application
# Accès à la documentation : https://getaround-api-qg2022.herokuapp.com/docs
heroku open -a getaround-api-qg2022