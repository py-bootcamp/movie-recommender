import json
import os
from pathlib import Path
from random import choice

from flask import jsonify

DEBUG = os.environ.get("DEBUG", False)
FOLDER_PATH = Path(__file__).parent

with open(FOLDER_PATH / "movies.json", "r") as f:
    MOVIES = json.loads(f.read())


def recommend_movie(request):
    return jsonify(movie=choice(MOVIES))
