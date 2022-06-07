from flask import render_template, flash, url_for, redirect

import api
import forms
from loader import app


@app.route('/', methods=['GET', 'POST'])
def index():
    form = forms.Deploy()

    if form.validate_on_submit():
        repo_url = form.repo_url.data
        flash(f'[info] Deploying in progress...')
        return redirect(url_for('index'))

    return render_template('index.html', form=api.make_form(form), flashes=api.make_flashes())


def setup():
    pass
