

import os
from pathlib import Path


from flask import redirect, render_template, Flask


from database import queries
import game
from game import Game
from routes import api_blueprint, lobby_blueprint


ROOT_DIR = str(Path(__file__).absolute().parent)
TEMPLATE_FOLDER = os.path.join(ROOT_DIR, "Webpage")
STATIC_FOLDER = os.path.join(ROOT_DIR, "Webpage/Static")


app = Flask("Catan", template_folder=TEMPLATE_FOLDER, static_folder=STATIC_FOLDER)
app.secret_key = 'any random string'


@app.route("/new/<int:template_id>")
def new(template_id: int):
	new_game: Game = game.new.new_game(template_id)
	return redirect("/game/{new_game.id}")


@app.route("/game/<int:game_id>")
def ui_game(game_id: int):
	if(queries.games.get_game(game_id) is None):
		return "Game does not exist"
	return render_template("game.j2")


@app.route("/api/game/<int:game_id>")
def api_game(game_id: int) -> dict:
	return dict(game.get_game(game_id))


app.register_blueprint(api_blueprint)
app.register_blueprint(lobby_blueprint)


app.run(host="0.0.0.0", port=80, debug=True)
