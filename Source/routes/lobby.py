

import os
from pathlib import Path
import sys
import traceback
from typing import Any, Optional


from flask import redirect, render_template, request, session, Blueprint


from database import queries
import game
from lobby import Lobby, LobbyPlayer
from PlayerColor import PLAYER_COLORS


ROOT_DIR = str(Path(__file__).absolute().parent.parent)
TEMPLATE_FOLDER = os.path.join(ROOT_DIR, "Webpage")
STATIC_FOLDER = os.path.join(ROOT_DIR, "Webpage/Static")


lobby_blueprint = Blueprint('lobby_blueprint', __name__, template_folder=TEMPLATE_FOLDER, static_folder=STATIC_FOLDER)


def build_lobby(lobby_uuid: str) -> Optional[Lobby]:
	lobby_data: Optional[dict] = queries.lobbies.get_valid_lobby_by_uuid(lobby_uuid)  # pylint: disable=no-value-for-parameter
	if(lobby_data is None):
		return None

	lobby = Lobby(
		id=lobby_data["id"],
		uuid=lobby_data["uuid"],
		created=lobby_data["created"],
		updated=lobby_data["updated"],
		expired=lobby_data["expired"],
		game_id=lobby_data["Games.id"]
	)

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


@lobby_blueprint.route("/lobby")
def lobby_GET():
	return render_template("new_lobby.j2")


@lobby_blueprint.route("/lobby", methods=["POST"])
def lobby_POST():
	lobby_data: dict = queries.lobbies.new_lobby()  # pylint: disable=no-value-for-parameter
	lobby_uuid = lobby_data["uuid"]

	return redirect(f"/lobby/{lobby_uuid}")


@lobby_blueprint.route("/lobby/<string:lobby_uuid>")
@manage_lobbies
def lobby_uuid_GET(lobby: Lobby, session_lobbies: dict):
	if(lobby is None):
		return redirect("/lobby")

	player_uuid = session_lobbies.get(lobby.uuid)
	if(player_uuid is None):
		return render_template("join_lobby.j2", lobby=lobby,)

	player: LobbyPlayer = lobby.get(player_uuid)
	if(player is None):
		del session_lobbies[lobby.uuid]
		return render_template("join_lobby.j2", lobby=lobby,)

	return render_template("lobby.j2", lobby=lobby, player=player)


@lobby_blueprint.route("/lobby/<string:lobby_uuid>", methods=["POST"])
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


@lobby_blueprint.route("/lobby/<string:lobby_uuid>/start")
@manage_lobbies
def lobby_uuid_start_GET(lobby: Lobby, session_lobbies: dict):
	if(lobby is None):
		return redirect("/lobby")

	# If game has already started, redirect player to the game
	if(not lobby.game_id):
		# If (the game does not exists &) player isn't setup, send them to setup (plus, they are naughty for being here)
		player_uuid = session_lobbies.get(lobby.uuid)
		if(player_uuid is None or player_uuid not in lobby):
			return redirect(f"/lobby/{lobby.uuid}")

		# TODO: Setup Game in DB
			# Create game
			# Create players
			# Link Game to Lobby

	return redirect(f"/game/{lobby.game_id}")


@lobby_blueprint.route("/api/lobby/<string:lobby_uuid>")
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


@lobby_blueprint.route("/api/lobby/<string:lobby_uuid>/player/color", methods=["POST"])
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


@lobby_blueprint.route("/lobby/<string:lobby_uuid>/html")
@manage_lobbies
def html_lobby_GET(lobby: Lobby, session_lobbies: dict) -> None:
	if(lobby is None):
		return "", 400

	return render_template("lobby_status.j2", lobby=lobby)
