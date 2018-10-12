from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class hug(FlaskForm):
    message = StringField('')
    submit = SubmitField('Sign In', id="send")
