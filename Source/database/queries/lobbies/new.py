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
