

from datetime import datetime, timedelta
import os
from pathlib import Path
from typing import Optional
import uuid


from flask import redirect, render_template, request, session, Flask


from database import queries
import game
from game import Game
from Lobbies import LobbyPlayer, Lobby, Lobbies


ROOT_DIR = str(Path(__file__).absolute().parent)
TEMPLATE_FOLDER = os.path.join(ROOT_DIR, "Webpage")
STATIC_FOLDER = os.path.join(ROOT_DIR, "Webpage/Static")


LOBBIES = Lobbies()


app = Flask("Catan", template_folder=TEMPLATE_FOLDER, static_folder=STATIC_FOLDER)
app.secret_key = 'any random string'


def manage_lobbies(function: callable) -> callable:
	def wrapper(*args: list, **kwargs: dict):
		now = datetime.now()
		# Clear inactive lobbies
		for lobby_index in range(len(LOBBIES)-1, -1, -1):
			lobby: Lobby = LOBBIES.lobbies[lobby_index]
			if(lobby.last_updated + timedelta(minutes=30) < now):
				del LOBBIES[lobby]
			else:
				# Clear inactive players
				for player_index in range(len(lobby)-1, -1, -1):
					player: LobbyPlayer = lobby.players[player_index]
					if(lobby.last_updated + timedelta(minutes=30) < now):
						del lobby[player]

		param_names: list[str] = list(function.__annotations__)
		lobby_id_param_index: int = param_names.index("lobby_id") if("lobby_id" in param_names) else None
		if(lobby_id_param_index is not None):
			lobby_id = kwargs.get("lobby_id") or args[lobby_id_param_index]
			lobby: Optional[Lobby] = LOBBIES.get(lobby_id)
			if(lobby is not None):
				lobby.update()

		return function(*args, **kwargs)

	wrapper.__annotations__ = function.__annotations__
	wrapper.__name__ = function.__name__

	return wrapper


@app.route("/lobby")
@manage_lobbies
def lobby_GET():
	return render_template("new_lobby.j2")


@app.route("/lobby", methods=["POST"])
@manage_lobbies
def lobby_POST():
	lobby_id: str = str(uuid.uuid4())
	LOBBIES.append(Lobby(lobby_id))

	return redirect(f"/lobby/{lobby_id}")


@app.route("/lobby/<string:lobby_id>")
@manage_lobbies
def lobby_id_GET(lobby_id: int):
	print(session)
	lobby: Lobby = LOBBIES.get(lobby_id)
	if(lobby is None):
		return redirect("/lobby")

	session_lobbies = session.get("lobbies")
	if(session_lobbies is None):
		session_lobbies = {}
		session["lobbies"] = session_lobbies

	player_id = session_lobbies.get(lobby_id)
	if(player_id is None):
		return render_template("join_lobby.j2", colors=LobbyPlayer.COLORS)

	player: Optional[LobbyPlayer] = lobby.get(player_id)
	if(player is None):
		return render_template("join_lobby.j2", colors=LobbyPlayer.COLORS)

	return render_template("lobby.j2", player=player)


@app.route("/lobby/<string:lobby_id>", methods=["POST"])
@manage_lobbies
def lobby_id_POST(lobby_id: int):
	session_lobbies = session.get("lobbies")
	if(session_lobbies is None):
		session_lobbies = {}
		session["lobbies"] = session_lobbies

	lobby: Optional[Lobby] = LOBBIES.get(lobby_id)
	if(lobby is None):
		return redirect("/lobby")

	player_id: Optional[str] = session_lobbies.get(lobby_id)
	if(player_id is not None):
		return redirect(f"/lobby/{lobby_id}")

	# Create Player
	player_id = str(uuid.uuid4())
	player_name = request.form.get("name")
	player_color = request.form.get("color")
	player = LobbyPlayer(player_id, player_name, player_color)
	lobby += player

	session_lobbies[lobby_id] = player_id
	print(session_lobbies)
	print(session)
	session["lobbies"] = session_lobbies

	return redirect(f"/lobby/{lobby_id}")


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


@app.route("/api/lobby/active/<string:lobby_id>")
def api_lobby_active_GET(lobby_id: str) -> None:
	lobbies = session.get("lobbies")
	if(lobbies is None):
		lobbies = {}
		session["lobbies"] = lobbies

	player_id: Optional[str] = lobbies.get(lobby_id)
	if(player_id is None):
		return """{"error": {"type": "lobby", "message": "Lobby not found in session"}}""", 400

	lobby: Lobby = LOBBIES.get(lobby_id)
	if(lobby is None):
		return """{"error": {"type": "lobby", "message": "Lobby not found"}}""", 404
	lobby.update()

	player: Optional[LobbyPlayer] = lobby.get(player_id)
	if(player is None):
		return """{"error": {"type": "player", "message": "Player not found"}}""", 400
	player.update()

	return """{"updated": ["lobby", "player"]}""", 200




app.run(host="0.0.0.0", port=80, debug=True)
