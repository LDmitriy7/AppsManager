import os
from pathlib import Path

import dotenv

dotenv.load_dotenv()

APPS_DIR = os.environ['APPS_DIR']
APPS_DIR = Path(APPS_DIR)
DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_NAME = os.environ.get('DB_NAME', 'AppsManager')
