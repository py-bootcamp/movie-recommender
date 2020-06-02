import os
import json
from pathlib import Path
from random import choice
import cherrypy

PORT = os.environ.get('PORT', 8888)

FOLDER_PATH = Path(__file__).parent

with open(FOLDER_PATH / "movies.json", "r") as f:
    MOVIES = json.loads(f.read())

class Movie:
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self):
        return {"movie": choice(MOVIES)}

cherrypy.quickstart(
    Movie(), config=cherrypy.config.update({
        'server.socket_host': '0.0.0.0',
        'server.socket_port': PORT,
        }))
