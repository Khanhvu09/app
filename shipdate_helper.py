
import json
import os

METADATA_FILE = 'uploads/ship_dates.json'

def load_metadata():
    if not os.path.exists(METADATA_FILE):
        return {}
    with open(METADATA_FILE, 'r') as f:
        return json.load(f)

def save_metadata(metadata):
    with open(METADATA_FILE, 'w') as f:
        json.dump(metadata, f, indent=4)

def set_ship_date(filename, ship_date):
    data = load_metadata()
    data[filename] = ship_date
    save_metadata(data)

def get_ship_date(filename):
    return load_metadata().get(filename, 'N/A')

def get_all_files_with_ship_dates():
    files = os.listdir('uploads')
    data = load_metadata()
    return [(f, data.get(f, 'N/A')) for f in files if not f.endswith('.json')]
