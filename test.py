import dj_database_url
import os, json, dotenv
from pathlib import Path

json_file = os.path.join(Path(__file__).resolve().parent, "databases.json")
if os.path.isfile(json_file):
    with open(json_file) as f:
        DATABASES = json.load(f)

print(DATABASES)