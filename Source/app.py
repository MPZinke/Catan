

from datetime import datetime, timedelta
import os
from pathlib import Path
from typing import Any, Optional
import uuid


from flask import redirect, render_template, request, session, Flask


from database import queries
import game
from game import Game
from lobby import Lobby, LobbyPlayer
from PlayerColor import PlayerColor, PLAYER_COLORS


ROOT_DIR = str(Path(__file__).absolute().parent)
TEMPLATE_FOLDER = os.path.join(ROOT_DIR, "Webpage")
STATIC_FOLDER = os.path.join(ROOT_DIR, "Webpage/Static")


app = Flask("Catan", template_folder=TEMPLATE_FOLDER, static_folder=STATIC_FOLDER)
app.secret_key = 'any random string'


def manage_lobbies(function: callable) -> callable:
	def wrapper(*args: list, **kwargs: dict):
		now = datetime.now()
		# Clear inactive lobbies
		# for lobby_index in range(len(LOBBIES)-1, -1, -1):
		# 	lobby: Lobby = LOBBIES.lobbies[lobby_index]
		# 	if(lobby.last_updated + timedelta(minutes=30) < now):
		# 		del LOBBIES[lobby]
		# 	else:
		# 		# Clear inactive players
		# 		for player_index in range(len(lobby)-1, -1, -1):
		# 			player: LobbyPlayer = lobby.players[player_index]
		# 			if(lobby.last_updated + timedelta(minutes=30) < now):
		# 				del lobby[player]

		# param_names: list[str] = list(function.__annotations__)
		# lobby_uuid_param_index: int = param_names.index("lobby_uuid") if("lobby_uuid" in param_names) else None
		# if(lobby_uuid_param_index is not None):
		# 	lobby_uuid = kwargs.get("lobby_uuid") or args[lobby_uuid_param_index]

		return function(*args, **kwargs)

	wrapper.__annotations__ = function.__annotations__
	wrapper.__name__ = function.__name__

	return wrapper


@app.route("/lobby")
def lobby_GET():
	return render_template("new_lobby.j2")


@app.route("/lobby", methods=["POST"])
def lobby_POST():
	lobby_data: dict = queries.lobbies.new_lobby()
	lobby_uuid = lobby_data["uuid"]

	return redirect(f"/lobby/{lobby_uuid}")


@app.route("/lobby/<string:lobby_uuid>")
# @manage_lobbies
def lobby_uuid_GET(lobby_uuid: int):
	lobby_data: Optional[dict] = queries.lobbies.get_lobby_by_uuid(lobby_uuid)
	if(lobby_data is None):
		return redirect("/lobby")

	lobby = Lobby(**lobby_data)

	session_lobbies: dict = session.get("lobbies", {})
	player_uuid = session_lobbies.get(lobby_uuid)
	print("player_uuid", player_uuid)
	if(player_uuid is None):
		return render_template("join_lobby.j2", colors=PLAYER_COLORS)

	player_data: Optional[dict] = queries.lobbies.get_lobby_player_by_uuid(player_uuid)
	if(player_data is None):
		return render_template("join_lobby.j2", colors=PLAYER_COLORS)

	player_color = next(filter(lambda color: color.id == player_data["PlayerColors.id"], PLAYER_COLORS))
	del player_data["PlayerColors.id"]
	del player_data["Lobbies.id"]
	player = LobbyPlayer(**player_data, color=player_color)

	session["lobbies"] = session_lobbies
	return render_template("lobby.j2", player=player)


@app.route("/lobby/<string:lobby_uuid>", methods=["POST"])
# @manage_lobbies
def lobby_uuid_POST(lobby_uuid: int):
	lobby_data: Optional[dict] = queries.lobbies.get_lobby_by_uuid(lobby_uuid)
	if(lobby_data is None):
		return redirect("/lobby")

	lobby_primary_key: int = lobby_data["id"]

	session_lobbies: dict = session.get("lobbies", {})
	player_uuid: Optional[str] = session_lobbies.get(lobby_uuid)
	if(player_uuid is not None):
		if(queries.lobbies.get_lobby_player_by_uuid(player_uuid) is not None):
			return redirect(f"/lobby/{lobby_uuid}")

	# Create Player
	player_name = request.form.get("name")
	player_color_id = request.form.get("color")
	player_data: dict = queries.lobbies.new_lobby_player(player_name, player_color_id, lobby_primary_key)
	player_uuid = player_data["uuid"]

	session_lobbies[lobby_uuid] = player_uuid
	session["lobbies"] = session_lobbies
	return redirect(f"/lobby/{lobby_uuid}")


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


@app.route("/api/lobby/active/<string:lobby_uuid>")
def api_lobby_active_GET(lobby_uuid: str) -> None:
	lobbies = session.get("lobbies")
	if(lobbies is None):
		lobbies = {}
		session["lobbies"] = lobbies

	player_uuid: Optional[str] = lobbies.get(lobby_uuid)
	if(player_uuid is None):
		return """{"error": {"type": "lobby", "message": "Lobby not found in session"}}""", 400

	lobby: Lobby = LOBBIES.get(lobby_uuid)
	if(lobby is None):
		return """{"error": {"type": "lobby", "message": "Lobby not found"}}""", 404
	lobby.update()

	player: Optional[LobbyPlayer] = lobby.get(player_uuid)
	if(player is None):
		return """{"error": {"type": "player", "message": "Player not found"}}""", 400
	player.update()

	return """{"updated": ["lobby", "player"]}""", 200




app.run(host="0.0.0.0", port=80, debug=True)
