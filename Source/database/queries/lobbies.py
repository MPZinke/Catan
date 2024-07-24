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
def new_lobby(cursor: psycopg2.extras.RealDictCursor) -> list[dict]:
	query = """
		INSERT INTO "Lobbies" ("created") VALUES
		(%s)
		RETURNING *;
	"""

	cursor.execute(query, (datetime.now(),))
	return dict(cursor.fetchone())


@connect
def new_lobby_player(cursor: psycopg2.extras.RealDictCursor, name: str, player_color_id: int, lobby_id: str
) -> list[dict]:
	query = """
		INSERT INTO "LobbiesPlayers" ("name", "PlayerColors.id", "Lobbies.id") VALUES
		(%s, %s, %s)
		RETURNING *;
	"""

	cursor.execute(query, (name, player_color_id, lobby_id))
	return dict(cursor.fetchone())


@connect
def update_lobby_player_by_uuid(cursor: psycopg2.extras.RealDictCursor, uuid: str) -> list[dict]:
	query = """
		UPDATE "LobbiesPlayers"
		SET "updates" = CURRENT_TIMESTAMP
		WHERE "uuid" = %s;
	"""

	cursor.execute(query, (uuid,))


@connect
def update_lobby_player_by_uuid(cursor: psycopg2.extras.RealDictCursor, uuid: str) -> list[dict]:
	query = """
		UPDATE "LobbiesPlayers"
		SET "updated" = CURRENT_TIMESTAMP
		WHERE "uuid" = %s
		  AND INTERVAL '30 minutes' <= CURRENT_TIMESTAMP - "updated";
	"""

	cursor.execute(query, (uuid,))


@connect
def update_expired_players(cursor: psycopg2.extras.RealDictCursor, uuid: str) -> list[dict]:
	query = """
		UPDATE "LobbiesPlayers"
		SET "expired" = TRUE
		JOIN "Lobbies" ON "LobbiesPlayers"."Lobbies.id" = "Lobbies"."id"
		WHERE "Lobbies"."uuid" = %s
		  AND INTERVAL '30 minutes' <= CURRENT_TIMESTAMP - "LobbiesPlayers"."updated";
	"""

	cursor.execute(query, (uuid,))


