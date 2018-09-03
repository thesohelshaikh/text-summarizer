# List of important commands

### Commands for running the app
```
activate mp2
set FLASK_APP = app.py
set FLASK_DEBUG = 1
set FLASK_ENV=development
flask run
```

### Command for setting up requirements for heroku
```
pip freeze > requirements.txt 
```

### Commands for heroku deployment
```
git push heroku master
heroku open
```
