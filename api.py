import re
import shutil
import subprocess
import tarfile
from pathlib import Path

import requests
from flask import render_template, Markup, get_flashed_messages
from flask_wtf import FlaskForm
from github import Github
from github.GithubException import GithubException

import config


def make_form(form: FlaskForm) -> Markup:
    fields = getattr(form, '_fields').values()
    text = render_template('form.html', fields=fields)
    return Markup(text)


def make_flashes() -> Markup:
    messages = get_flashed_messages()
    text = render_template('flashes.html', messages=messages)
    return Markup(text)


def _get_repo_download_url(repo_url: str):
    match = re.search(r'/[\w-]+/[\w-]+', repo_url)
    fullname = match.group(0).strip('/')
    return Github(config.GH_TOKEN).get_repo(fullname).get_archive_link('tarball')


def download_repo(repo_url: str, to_path: str = None):
    """Return app dir of cloned repo"""
    to_path = to_path or repo_url.split('/')[-1].removesuffix('.git')

    try:
        download_url = _get_repo_download_url(repo_url)
    except (GithubException, AttributeError):
        raise ValueError('Repository not found')

    response = requests.get(download_url)
    temp_name = 'temp.tar.gz'

    with open(temp_name, 'wb') as file:
        file.write(response.content)

    with tarfile.open(temp_name) as file:
        file.extractall(config.APPS_DIR)

        old_dir = config.APPS_DIR / file.getnames()[0]
        new_dir = config.APPS_DIR / to_path

    shutil.rmtree(new_dir, ignore_errors=True)
    shutil.move(old_dir, new_dir)

    return new_dir


def deploy_app(app_dir: str | Path, compose_file='docker-compose.yml'):
    cmd = f'docker compose -f {compose_file} build && docker compose -f {compose_file} up &'
    subprocess.run(cmd, shell=True, cwd=app_dir)
