from flask import render_template, Markup, get_flashed_messages
from flask_wtf import FlaskForm


def make_form(form: FlaskForm) -> Markup:
    fields = getattr(form, '_fields').values()
    text = render_template('form.html', fields=fields)
    return Markup(text)


def make_flashes() -> Markup:
    messages = get_flashed_messages()
    text = render_template('flashes.html', messages=messages)
    return Markup(text)
