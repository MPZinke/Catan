#!/opt/homebrew/bin/python3
# -*- coding: utf-8 -*-
__author__ = "MPZinke"

########################################################################################################################
#                                                                                                                      #
#   created by: MPZinke                                                                                                #
#   on 2024.05.12                                                                                                      #
#                                                                                                                      #
#   DESCRIPTION:                                                                                                       #
#   BUGS:                                                                                                              #
#   FUTURE:                                                                                                            #
#                                                                                                                      #
########################################################################################################################


import psycopg2.extras
from typing import Optional


from database.connect import connect


@connect
def new_game(cursor: psycopg2.extras.RealDictCursor, board_id: int) -> dict:
	query = """
		INSERT INTO "Games" ("Boards.id") VALUES (%s)
		RETURNING *;
	"""

	cursor.execute(query, (board_id,))
	return dict(cursor.fetchone())


@connect
def new_port(cursor: psycopg2.extras.RealDictCursor, game_id: int, port_id: int, resource_type: int) -> dict:
	query = """
		INSERT INTO "GamesPorts" ("Games.id", "Ports.id", "ResourceTypes.id") VALUES (%s, %s, %s)
		RETURNING *;
	"""

	cursor.execute(query, (game_id, port_id, resource_type))
	return dict(cursor.fetchone())


@connect
def new_road(cursor: psycopg2.extras.RealDictCursor, game_id: int, road_id: int) -> dict:
	query = """
		INSERT INTO "GamesRoads" ("Games.id", "Roads.id") VALUES (%s, %s)
		RETURNING *;
	"""

	cursor.execute(query, (game_id, road_id))
	return dict(cursor.fetchone())


@connect
def new_settlement(cursor: psycopg2.extras.RealDictCursor, game_id: int, settlement_id: int,
	settlement_type_id: Optional[int]=None
) -> dict:
	query = """
		INSERT INTO "GamesSettlements" ("Games.id", "Settlements.id", "SettlementTypes.id") VALUES (%s, %s, %s)
		RETURNING *;
	"""

	cursor.execute(query, (game_id, settlement_id, settlement_type_id))
	return dict(cursor.fetchone())


@connect
def new_tile(cursor: psycopg2.extras.RealDictCursor, game_id: int, tile_id: int, resource_type: int, value: int) -> int:
	query = """
		WITH "InsertedGameTile" AS (
			INSERT INTO "GamesTiles" ("Games.id", "Tiles.id", "ResourceTypes.id", "value")
			VALUES (%s, %s, %s, %s)
			RETURNING *
		)
		SELECT * FROM "InsertedGameTile"
		JOIN "Tiles" ON "InsertedGameTile"."Tiles.id" = "Tiles"."id";
	"""

	cursor.execute(query, (game_id, tile_id, resource_type, value))
	return dict(cursor.fetchone())


@connect
def new_robber(cursor: psycopg2.extras.RealDictCursor, game_id: int, game_tile_id: int, is_friendly: bool=False
) -> dict:
	query = """
		INSERT INTO "GamesRobbers" ("Games.id", "is_friendly", "GamesTiles.id") VALUES (%s, %s, %s)
		RETURNING *;
	"""

	cursor.execute(query, (game_id, is_friendly, game_tile_id))
	return dict(cursor.fetchone())
