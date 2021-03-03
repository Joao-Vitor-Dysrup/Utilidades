import os
import unidecode


def filtrar_string(string, title=True):
    if string is None:
        return None
    filtered = string.strip()
    if title:
        filtered = filtered.title()
    return filtered


def unicode_to_ascii(accented_string):
    return unidecode.unidecode(accented_string).replace('*', '').strip().lower()


def is_directory(path):
    return os.path.isdir(path)


def create_folder(path):
    try:
        os.mkdir(path)
    except Exception:
        print(f'Not possible to create the folder at "{path}"')


def is_folder_empty(folder_path):
    try:
        return not os.listdir(folder_path)
    except Exception:
        print('Folder does not exist.')