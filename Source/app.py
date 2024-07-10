

import os
from pathlib import Path


from flask import render_template, Flask

from database import queries
import game
from game import Game


ROOT_DIR = str(Path(__file__).absolute().parent)
TEMPLATE_FOLDER = os.path.join(ROOT_DIR, "Webpage")
STATIC_FOLDER = os.path.join(ROOT_DIR, "Webpage/Static")



app = Flask("Catan", template_folder=TEMPLATE_FOLDER, static_folder=STATIC_FOLDER)


@app.route("/new/<int:template_id>")
def new(template_id: int):
	new_game: Game = game.new.new_game(template_id)
	return new_game.id


@app.route("/game/<int:game_id>")
def ui_game(game_id: int):
	return render_template("game.j2")


@app.route("/api/game/<int:game_id>")
def api_game(game_id: int) -> dict:
	return dict(game.get_game(game_id))


@app.route("/api/resource_types")
def api_resource_types() -> dict:
	return {type["label"]: type["id"]-1 for type in queries.types.get_resource_types()}  # pylint: disable=no-value-for-parameter


@app.route("/api/directions")
def api_directions() -> dict:
	corner_edges: dict = queries.directions.get_corner_edges()  # pylint: disable=no-value-for-parameter
	corner_sides: dict = queries.directions.get_corner_sides()  # pylint: disable=no-value-for-parameter
	edge_corners: dict = queries.directions.get_edge_corners()  # pylint: disable=no-value-for-parameter
	edge_sides: dict = queries.directions.get_edge_sides()  # pylint: disable=no-value-for-parameter
	side_corners: dict = queries.directions.get_side_corners()  # pylint: disable=no-value-for-parameter
	side_edges: dict = queries.directions.get_side_edges()  # pylint: disable=no-value-for-parameter
	return {
		"Corner's Edges": {direction["label"]: direction["id"]-1 for direction in corner_edges},
		"Corner's Sides": {direction["label"]: direction["id"]-1 for direction in corner_sides},
		"Edge's Corners": {direction["label"]: direction["id"]-1 for direction in edge_corners},
		"Edge's Sides": {direction["label"]: direction["id"]-1 for direction in edge_sides},
		"Side's Corners": {direction["label"]: direction["id"]-1 for direction in side_corners},
		"Side's Edges": {direction["label"]: direction["id"]-1 for direction in side_edges},
	}


app.run(host="0.0.0.0", port=80, debug=True)
