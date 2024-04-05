#!/opt/homebrew/bin/python3
# -*- coding: utf-8 -*-
__author__ = "MPZinke"

########################################################################################################################
#                                                                                                                      #
#   created by: MPZinke                                                                                                #
#   on 2024.04.05                                                                                                      #
#                                                                                                                      #
#   DESCRIPTION:                                                                                                       #
#   BUGS:                                                                                                              #
#   FUTURE:                                                                                                            #
#                                                                                                                      #
########################################################################################################################



import psycopg2
from typing import Optional


from database.connect import connect


@connect
def new_game(cursor, board_id: int) -> int:
	print(type(cursor))
	query = """
		INSERT INTO "Games" ("Board.id") VALUES (%s)
		RETURNING "id";
	"""

	cursor.execute(query, (board_id,))
	return cursor.fetchone()["id"]


@connect
def new_port(cursor, game_id: int, resource_type: int) -> int:
	print(type(cursor))
	query = """
		INSERT INTO "Ports" ("Games.id", "ResourceTypes.id") VALUES (%s, %s)
		RETURNING "id";
	"""

	cursor.execute(query, (game_id, resource_type))
	return cursor.fetchone()["id"]


@connect
def new_road(cursor, game_id: int) -> int:
	print(type(cursor))
	query = """
		INSERT INTO "Roads" ("Games.id") VALUES (%s, %s)
		RETURNING "id";
	"""

	cursor.execute(query, (game_id))
	return cursor.fetchone()["id"]


@connect
def new_settlement(cursor, game_id: int, settlement_type: int) -> int:
	print(type(cursor))
	query = """
		INSERT INTO "Settlements" ("Games.id", , "SettlementTypes.id") VALUES (%s, %s)
		RETURNING "id";
	"""

	cursor.execute(query, (game_id, resource_type))
	return cursor.fetchone()["id"]


@connect
def new_tile(cursor, game_id: int, coordinate: Tuple[int, int], resource_type: int, value: int) -> int:
	print(type(cursor))
	query = """
		INSERT INTO "Tiles" ("Games.id", "coordinate", "ResourceTypes.id", "value") VALUES (%s, %s, %s, %s)
		RETURNING "id";
	"""

	cursor.execute(query, (game_id, coordinate, resource_type, value))
	return cursor.fetchone()["id"]
