from flask import Flask

# For rendering html templates
from flask import render_template

# intatiates flask app, configures the application
app = Flask(__name__) 

@app.route("/")
def hello():
    return render_template('index.html')