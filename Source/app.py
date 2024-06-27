

import os
from pathlib import Path


from flask import render_template, Flask


import game
from game import Game


ROOT_DIR = str(Path(__file__).absolute().parent)
TEMPLATE_FOLDER = os.path.join(ROOT_DIR, "webpage")
STATIC_FOLDER = os.path.join(ROOT_DIR, "Frontend/Static")



app = Flask("Catan", template_folder=TEMPLATE_FOLDER)


@app.route("/new/<int:template_id>")
def new(template_id: int):
	new_game: Game = game.new.new_game(template_id)
	return new_game.id


@app.route("/game/<int:game_id>")
def game(game_id: int):
	return render_template("game.j2")



app.run(host="0.0.0.0", port=80, debug=True)
