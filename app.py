from flask import Flask

# For rendering html templates
from flask import render_template

# For linking files, generates a URL
from flask import url_for

# Import our forms
from forms import LinkForm

# intatiates flask app, configures the application
app = Flask(__name__) 

app.config['SECRET_KEY'] = 'xyz'

@app.route("/")
def main():
    form = LinkForm()
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run()