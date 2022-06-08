import subprocess
from pathlib import Path

import git
from flask import render_template, Markup, get_flashed_messages, flash
from flask_wtf import FlaskForm

import config


def make_form(form: FlaskForm) -> Markup:
    fields = getattr(form, '_fields').values()
    text = render_template('form.html', fields=fields)
    return Markup(text)


def make_flashes() -> Markup:
    messages = get_flashed_messages()
    text = render_template('flashes.html', messages=messages)
    return Markup(text)


def clone_repo(from_url: str, name: str = None) -> Path:
    """Return path of cloned repo"""
    repo_name = from_url.split('/')[-1].split('.')[0]
    to_path = config.APPS_DIR / (name or repo_name)

    try:
        git.Repo.clone_from(from_url, to_path)
    except git.GitCommandError as e:
        _desc: bytes = e.args[2]
        desc = _desc.decode('utf-8').lower()

        if 'already exists' in desc:
            flash('[info] App already exists')
        elif 'does not exist' in desc or 'repository not found' in desc:
            raise ValueError('Repository not found')
        else:
            raise ValueError('Unknown error')

    return to_path


def deploy_app(app_dir: str | Path, compose_file='docker-compose.yml'):
    cmd = f'docker compose -f {compose_file} build && docker compose -f {compose_file} up &'
    subprocess.run(cmd, shell=True, cwd=app_dir)
