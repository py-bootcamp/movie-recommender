import json
import os
from pathlib import Path
from random import choice

from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route

DEBUG = os.environ.get("DEBUG", False)
FOLDER_PATH = Path(__file__).parent

with open(FOLDER_PATH / "movies.json", "r") as f:
    MOVIES = json.loads(f.read())


async def movie_recommender(request):
    return JSONResponse({"movie": choice(MOVIES)})


app = Starlette(
    debug=DEBUG,
    routes=[
        Route("/", movie_recommender),
    ],
)
