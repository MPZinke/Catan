

from flask import Flask


from game.new import new_game
from game import Game


app = Flask("Catan")


@app.route("/new/<int:template_id>")
def new(template_id: int):
	game: Game = new_game(game_id)
	return game.id


app.run(host="0.0.0.0", port=80)
