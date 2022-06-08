from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField


class Deploy(FlaskForm):
    repo_url = StringField('Repository URL:', validators=[validators.DataRequired()])
    env_string = StringField('Env vars (";" separated):')
    submit = SubmitField()
