#!/opt/homebrew/bin/python3
# -*- coding: utf-8 -*-
__author__ = "MPZinke"

########################################################################################################################
#                                                                                                                      #
#   created by: MPZinke                                                                                                #
#   on 2024.07.22                                                                                                      #
#                                                                                                                      #
#   DESCRIPTION:                                                                                                       #
#   BUGS:                                                                                                              #
#   FUTURE:                                                                                                            #
#                                                                                                                      #
########################################################################################################################


from datetime import datetime


import psycopg2
import psycopg2.extras


from database.connect import connect


@connect
def get_lobby_by_uuid(cursor: psycopg2.extras.RealDictCursor, uuid: str) -> list[dict]:
	query = """
		SELECT *
		FROM "Lobbies"
		WHERE "uuid" = %s;
	"""

	cursor.execute(query, (uuid,))
	if((lobby_player := cursor.fetchone()) is None):
		return None

	return dict(lobby_player)


@connect
def get_lobby_player_by_uuid(cursor: psycopg2.extras.RealDictCursor, uuid: str) -> list[dict]:
	query = """
		SELECT *
		FROM "LobbiesPlayers"
		WHERE "uuid" = %s;
	"""

	cursor.execute(query, (uuid,))
	if((lobby_player := cursor.fetchone()) is None):
		return None

	return dict(lobby_player)


@connect
def get_lobby_players_by_lobby_id(cursor: psycopg2.extras.RealDictCursor, lobby_id: int) -> list[dict]:
	query = """
		SELECT *
		FROM "LobbiesPlayers"
		WHERE "Lobbies.id" = %s;
	"""

	cursor.execute(query, (lobby_id,))
	return list(map(dict, cursor))


@connect
def get_valid_lobby_players_by_lobby_id(cursor: psycopg2.extras.RealDictCursor, lobby_id: int) -> list[dict]:
	query = """
		SELECT *
		FROM "LobbiesPlayers"
		WHERE "Lobbies.id" = %s
		  AND "expired" = FALSE;
	"""

	cursor.execute(query, (lobby_id,))
	return list(map(dict, cursor))


@connect
def get_available_lobby_colors(cursor: psycopg2.extras.RealDictCursor, lobby_uuid: str) -> list[dict]:
	query = """
		SELECT *
		FROM "PlayerColors"
		WHERE "id" NOT IN (
			SELECT "PlayerColors.id"
			FROM "LobbiesPlayers"
			JOIN "Lobbies" ON "LobbiesPlayers"."Lobbies.id" = "Lobbies"."id"
			WHERE "Lobbies"."uuid" = %s
		);
	"""

	cursor.execute(query, (lobby_uuid,))
	return list(map(dict, cursor))


@connect
def get_valid_lobby_by_uuid(cursor: psycopg2.extras.RealDictCursor, uuid: str) -> list[dict]:
	query = """
		SELECT *
		FROM "Lobbies"
		WHERE "uuid" = %s
		  AND "expired" = FALSE;
	"""

	cursor.execute(query, (uuid,))
	if((lobby_player := cursor.fetchone()) is None):
		return None

	return dict(lobby_player)


@connect
def get_valid_lobby_player_by_uuid(cursor: psycopg2.extras.RealDictCursor, uuid: str) -> list[dict]:
	query = """
		SELECT *
		FROM "LobbiesPlayers"
		WHERE "uuid" = %s
		  AND "expired" = FALSE;
	"""

	cursor.execute(query, (uuid,))
	if((lobby_player := cursor.fetchone()) is None):
		return None

	return dict(lobby_player)
