from flask import Flask, redirect

# For flashing a  message
from flask import flash

# For rendering html templates
from flask import render_template

# For linking files, generates a URL
from flask import url_for

# Import our forms
from forms import LinkForm

# intatiates flask app, configures the application
app = Flask(__name__) 

app.config['SECRET_KEY'] = 'This is a secret'

@app.route("/",  methods=['GET','POST'])
def main():
    form = LinkForm()
    if form.validate_on_submit():
        flash(f'Correct input!', 'success')
        return redirect(url_for('main'))
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run()