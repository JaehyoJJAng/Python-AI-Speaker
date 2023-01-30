from typing import Dict
from pathlib import Path
import os
import json

BASE_DIR : str = os.path.dirname(Path(__file__).resolve().parent)
def get_secret(key:str)-> None:
    with open(os.path.join(BASE_DIR,'.secret/.secret.json')) as fp:
        secret : Dict[str,str] = json.loads(fp.read())
    try:
        return secret[key]
    except EnvironmentError:
        raise EnvironmentError(f'Set The {key}')