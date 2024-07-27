

from datetime import datetime, timedelta
import os
from pathlib import Path
import sys
import traceback
from typing import Any, Optional
import uuid


from flask import redirect, render_template, request, session, Flask


from constants import directions, player_colors, resource_types
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


def build_lobby(lobby_uuid: str) -> Optional[Lobby]:
	lobby_data: Optional[dict] = queries.lobbies.get_valid_lobby_by_uuid(lobby_uuid)  # pylint: disable=no-value-for-parameter
	if(lobby_data is None):
		return None

	lobby = Lobby(**lobby_data)

	players_data: list[dict] = queries.lobbies.get_valid_lobby_players_by_lobby_id(lobby.id)
	for player_data in players_data:
		player_color = next(filter(lambda color: color.id == player_data["PlayerColors.id"], PLAYER_COLORS))

		lobby += LobbyPlayer(
			id=player_data["id"],
			uuid=player_data["uuid"],
			created=player_data["created"],
			updated=player_data["updated"],
			expired=player_data["expired"],
			name=player_data["name"],
			color=player_color
		)

	return lobby


def manage_lobbies(function: callable) -> callable:
	def wrapper(lobby_uuid: str, *args: list, **kwargs: dict) -> Any:
		queries.lobbies.update_expired_lobbies()  # pylint: disable=no-value-for-parameter
		queries.lobbies.update_expired_players()  # pylint: disable=no-value-for-parameter

		lobby: Optional[Lobby] = build_lobby(lobby_uuid)
		if(lobby is not None):
			queries.lobbies.update_lobby_timestamp_by_uuid(lobby_uuid)  # pylint: disable=no-value-for-parameter

		session_lobbies = session.get("session_lobbies", {})
		result: Any = function(lobby, session_lobbies, *args, **kwargs)
		session["session_lobbies"] = session_lobbies
		return result

	wrapper.__annotations__ = function.__annotations__
	wrapper.__name__ = function.__name__

	return wrapper


@app.route("/lobby")
def lobby_GET():
	return render_template("new_lobby.j2")


@app.route("/lobby", methods=["POST"])
def lobby_POST():
	lobby_data: dict = queries.lobbies.new_lobby()  # pylint: disable=no-value-for-parameter
	lobby_uuid = lobby_data["uuid"]

	return redirect(f"/lobby/{lobby_uuid}")


@app.route("/lobby/<string:lobby_uuid>")
@manage_lobbies
def lobby_uuid_GET(lobby: Lobby, session_lobbies: dict):
	if(lobby is None):
		return redirect("/lobby")

	player_uuid = session_lobbies.get(lobby.uuid)
	if(player_uuid is None):
		return render_template("join_lobby.j2", colors=lobby.available_player_colors())

	player: LobbyPlayer = lobby.get(player_uuid)
	if(player is None):
		del session_lobbies[lobby.uuid]
		return render_template("join_lobby.j2", colors=lobby.available_player_colors())

	return render_template("lobby.j2", lobby=lobby, player=player, colors=lobby.available_player_colors())


@app.route("/lobby/<string:lobby_uuid>", methods=["POST"])
@manage_lobbies
def lobby_uuid_POST(lobby: Lobby, session_lobbies: dict):
	if(lobby is None):
		return redirect("/lobby")

	player_uuid: Optional[str] = session_lobbies.get(lobby.uuid)
	if(player_uuid is not None):
		if(player_uuid in lobby):
			return redirect(f"/lobby/{lobby.uuid}")

	# Create Player
	player_name = request.form.get("name")
	player_color_id = request.form.get("color")
	player_data: dict = queries.lobbies.new_lobby_player(player_name, player_color_id, lobby.id)
	player_uuid = player_data["uuid"]
	session_lobbies[lobby.uuid] = player_uuid

	return redirect(f"/lobby/{lobby.uuid}")


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


@app.route("/api/constants")
def api_constants() -> dict:
	return {
		"directions": directions(),
		"player_colors": player_colors(),
		"resource_types": resource_types()
	}


@app.route("/api/lobby/<string:lobby_uuid>")
@manage_lobbies
def api_lobby_GET(lobby: Lobby, session_lobbies: dict) -> None:
	if(lobby is None):
		return "", 400

	player_uuid: Optional[str] = session_lobbies.get(lobby.uuid)
	if(player_uuid is None):
		return "", 400

	player: Optional[LobbyPlayer] = lobby.get(player_uuid)
	if(player is None):
		return "", 400

	return dict(lobby)


@app.route("/api/lobby/<string:lobby_uuid>/player/color", methods=["POST"])
@manage_lobbies
def api_lobby_uuid_player_color_GET(lobby: Lobby, session_lobbies: dict) -> None:
	if(lobby is None):
		return "", 400

	player_uuid: Optional[str] = session_lobbies.get(lobby.uuid)
	if(player_uuid is None):
		return "", 400

	player: Optional[LobbyPlayer] = lobby.get(player_uuid)
	if(player is None):
		return "", 400

	try:
		color_dict: dict = request.json
		color_id = color_dict["id"]
		if(queries.lobbies.update_lobby_player_color(color_id, player_uuid)):
			return """{"success": true}""", 200

		return """{"success": false}""", 500

	except:
		print(traceback.format_exc(), file=sys.stderr)
		return """{"success": false}""", 500


@app.route("/html/lobby/<string:lobby_uuid>")
@manage_lobbies
def html_lobby_GET(lobby: Lobby, session_lobbies: dict) -> None:
	if(lobby is None):
		return "", 400

	return render_template("lobby_status.j2", lobby=lobby)


app.run(host="0.0.0.0", port=80, debug=True)
