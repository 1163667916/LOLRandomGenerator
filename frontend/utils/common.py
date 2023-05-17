import hashlib
import os
from frontend.settings import BASE_DIR


def hash_name(name: str):
    hash = hashlib.md5()
    hash.update(name.encode('utf-8'))
    return hash


def store_static_path(path):
    return os.path.join(BASE_DIR, 'statics', path)
