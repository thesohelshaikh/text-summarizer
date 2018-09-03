from flask import Flask

# For rendering html templates
from flask import render_template

# For linking files, generates a URL
from flask import url_for

# intatiates flask app, configures the application
app = Flask(__name__) 

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()