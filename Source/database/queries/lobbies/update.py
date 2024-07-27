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


import psycopg2
import psycopg2.extras


from database.connect import connect


@connect
def update_expired_lobbies(cursor: psycopg2.extras.RealDictCursor) -> list[dict]:
	query = """
		UPDATE "Lobbies"
		SET "expired" = TRUE
		WHERE "expired" = FALSE  -- Prevent recalculation of time interval
		  AND INTERVAL '30 minutes' < CURRENT_TIMESTAMP - "updated";
	"""

	cursor.execute(query)


@connect
def update_expired_players(cursor: psycopg2.extras.RealDictCursor) -> list[dict]:
	query = """
		UPDATE "LobbiesPlayers"
		SET "expired" = TRUE
		WHERE "expired" = FALSE  -- Prevent recalculation of time interval
		  AND INTERVAL '30 minutes' < CURRENT_TIMESTAMP - "updated";
	"""

	cursor.execute(query)


@connect
def update_lobby_timestamp_by_uuid(cursor: psycopg2.extras.RealDictCursor, uuid: str) -> list[dict]:
	query = """
		UPDATE "Lobbies"
		SET "updated" = CURRENT_TIMESTAMP
		WHERE "uuid" = %s;
	"""

	cursor.execute(query, (uuid,))


@connect
def update_lobby_player_color(cursor: psycopg2.extras.RealDictCursor, color_id: int, uuid: str) -> int:
	query = """
		UPDATE "LobbiesPlayers"
		SET "updated" = CURRENT_TIMESTAMP,
		    "PlayerColors.id" = %s
		WHERE "uuid" = %s;
	"""

	cursor.execute(query, (color_id, uuid))
	return bool(cursor.rowcount)


@connect
def update_lobby_player_timestamp_by_uuid(cursor: psycopg2.extras.RealDictCursor, uuid: str) -> list[dict]:
	query = """
		UPDATE "LobbiesPlayers"
		SET "updated" = CURRENT_TIMESTAMP
		WHERE "uuid" = %s;
	"""

	cursor.execute(query, (uuid,))
