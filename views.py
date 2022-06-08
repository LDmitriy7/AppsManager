from flask import render_template, flash, url_for, redirect

import api
import forms
from loader import app


@app.route('/', methods=['GET', 'POST'])
def index():
    form = forms.Deploy()

    if form.validate_on_submit():
        repo_url = form.repo_url.data

        try:
            app_dir = api.clone_repo(repo_url)
        except ValueError as e:
            flash(f'[error] {e.args[0]}')
        else:
            api.deploy_app(app_dir)
            flash(f'[info] Deploying in progress...')

        return redirect(url_for('index'))

    return render_template('index.html', form=api.make_form(form), flashes=api.make_flashes())


def setup():
    pass
