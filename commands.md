# Commands for running the app
activate mp2
set FLASK_APP = app.py
set FLASK_DEBUG = 1
set FLASK_ENV=development
flask run

# Commands for setting up requirements

# Commands for heroku
git push heroku master
heroku open