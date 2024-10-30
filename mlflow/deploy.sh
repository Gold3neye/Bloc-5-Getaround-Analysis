heroku login

heroku container:login

# "getaround-mlflow" should be replaced with your app's name
heroku container:push web -a getaround-mlflow

# "getaround-mlflow" should be replaced with your app's name
heroku container:release web -a getaround-mlflow

# "getaround-mlflow" should be replaced with your app's name
# or https://getaround-mlflow.herokuapp.com/
heroku open -a getaround-mlflow
