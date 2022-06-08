from flask import render_template, flash, url_for, redirect

import api
import forms
from loader import app


@app.route('/', methods=['GET', 'POST'])
def index():
    form = forms.Deploy()

    if form.validate_on_submit():
        try:
            app_dir = api.download_repo(form.repo_url.data)
        except ValueError as e:
            flash(f'[error] {e}')
        else:
            api.make_env(app_dir, form.env_string.data)
            api.deploy_app(app_dir)
            flash(f'[info] Deploying in progress...')

        return redirect(url_for('index'))

    return render_template('index.html', form=api.make_form(form), flashes=api.make_flashes())


def setup():
    pass
