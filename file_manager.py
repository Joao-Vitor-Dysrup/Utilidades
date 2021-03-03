import os.path
import json


def get_file(filepath):
    if not file_exists(filepath):
        create_file(filepath)
    return filepath


def create_file(filepath):
    try:
        temp = []
        temp.append({})
        with open(filepath, mode='w') as f:
            f.write(json.dumps(temp, indent=4))
    except Exception:
        pass


def file_exists(filepath):
    return os.path.isfile(filepath)


create_file('activities.json')