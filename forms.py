from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField


class Deploy(FlaskForm):
    repo_url = StringField('Repository URL:', validators=[validators.DataRequired()])
    submit = SubmitField()
