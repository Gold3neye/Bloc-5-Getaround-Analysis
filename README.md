# Getaround project with Jedha

Please be careful with secrets.bat file, never push your credentials to a repository. I use this file localy and the one in this repo is only a sample you can use.

## Presentation video
[Presentation video on vidyard](https://share.vidyard.com/watch/U9YaiBRCXcdPKYRnz44RE8?)

## Objective
GetAround is a company that allows car owners to rent their cars to customers. Sometimes a customer might be late to checkout and the next customer might have to wait to checkin. It leads to cancellations, have a negative impact on the company revenues and image. The goal of this project is to be able to anticipate late checkouts, and evaluate the impact of some measures on car owners revenues. 

The technical goal of this project is to deploy multiple tools related to data science:
- a web dashbord acessible anywhere
- a web MLFlow server to exchange with peer data scientists
- an web API exposing a machine learning prediction route

## Deliverables

[GetAround Dashboard](https://getaround-dashboard-qg2022.herokuapp.com/)

[My MLFlow server](https://getaround-mlflow.herokuapp.com/)

[API docs](https://getaround-api-qg2022.herokuapp.com/docs)

I am using the free Heroku version so allow up to one minute to get the first response if the app is sleeping. Furthermore, I won't support it in the future so it may not be working anymore after December 2022 due to Heroku or Python libraries updates.

## Dataset
* [Delay Analysis](https://full-stack-assets.s3.eu-west-3.amazonaws.com/Deployment/get_around_delay_analysis.xlsx) 👈 Data Analysis 
* [Pricing Optimization](https://full-stack-assets.s3.eu-west-3.amazonaws.com/Deployment/get_around_pricing_project.csv) 👈 Machine Learning: place it in api/data

## Prerequisites
### Dependencies
- The source code is written in Python 3.
- Docker is necessary to build and run localy the docker images
- Heroku CLI is necessary to upload images to Heroku 

## Usage
### Dashboard
Build the docker image with build.bat and run the docker image localy with run.bat. Or upload image to heroku with heroku CLI.

### MLFlow
Create a S3 bucket and a posgres database, then use secrets.bat file to store credentials as env var. Build the docker image with build.bat and run the docker image localy with run.bat. Or upload image to heroku with heroku CLI, you need to add the previous credentials on the website. Once your MLFlow server is set up, use train.py to train your ML algorithm.Use run_train.bat file to do so as credentials are also needed. 

### API
You must have a MLFlow server and its URI ready at this point. All previous credentials and the server URI must be available in env vars. Build the docker image with build.bat and run the docker image localy with run.bat. Or upload image to heroku with heroku CLI, you need to add the previous credentials on the website for the ML route to work. You can use run_test.bat to test, or access the doc to try it out.

## Team contributors
Axelle Gottafray

## References

