import os
from pathlib import Path

import dotenv

dotenv.load_dotenv()

APPS_DIR = Path(os.environ['APPS_DIR'])

DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_NAME = os.environ.get('DB_NAME', 'AppsManager')

APP_PORT = int(os.environ.get('APP_PORT', 5001))
GH_TOKEN = os.environ['GH_TOKEN']
