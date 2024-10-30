heroku login
heroku container:login
heroku container:push web -a getaround-dashboard-qg2022
heroku container:release web -a getaround-dashboard-qg2022
heroku open -a getaround-dashboard-qg2022
