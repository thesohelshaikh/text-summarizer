from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class LinkForm(FlaskForm):
    link = StringField('Link', validators=[DataRequired()])

    submit = SubmitField('Summarize')