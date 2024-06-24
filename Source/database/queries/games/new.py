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
		INSERT INTO "Games" ("Templates.id") VALUES (%s)
		RETURNING *;
	"""

	cursor.execute(query, (board_id,))
	return dict(cursor.fetchone())


@connect
def new_port(cursor: psycopg2.extras.RealDictCursor, game_id: int, port_id: int, resource_type: int) -> dict:
	query = """
		INSERT INTO "GamesPorts" ("Games.id", "TemplatesPorts.id", "ResourceTypes.id") VALUES (%s, %s, %s)
		RETURNING *;
	"""

	cursor.execute(query, (game_id, port_id, resource_type))
	return dict(cursor.fetchone())


@connect
def new_road(cursor: psycopg2.extras.RealDictCursor, game_id: int, road_id: int) -> dict:
	query = """
		INSERT INTO "GamesRoads" ("Games.id", "TemplatesRoads.id") VALUES (%s, %s)
		RETURNING *;
	"""

	cursor.execute(query, (game_id, road_id))
	return dict(cursor.fetchone())


@connect
def new_settlement(cursor: psycopg2.extras.RealDictCursor, game_id: int, settlement_id: int,
	settlement_type_id: Optional[int]=None
) -> dict:
	query = """
		INSERT INTO "GamesSettlements" ("Games.id", "TemplatesSettlements.id", "SettlementTypes.id") VALUES (%s, %s, %s)
		RETURNING *;
	"""

	cursor.execute(query, (game_id, settlement_id, settlement_type_id))
	return dict(cursor.fetchone())


@connect
def new_tile(cursor: psycopg2.extras.RealDictCursor, game_id: int, tile_id: int, resource_type: int, value: int) -> int:
	query = """
		WITH "InsertedGameTile" AS (
			INSERT INTO "GamesTiles" ("Games.id", "TemplatesTiles.id", "ResourceTypes.id", "value")
			VALUES (%s, %s, %s, %s)
			RETURNING *
		)
		SELECT "InsertedGameTile".*, "TemplatesTiles"."coordinate" FROM "InsertedGameTile"
		JOIN "TemplatesTiles" ON "InsertedGameTile"."TemplatesTiles.id" = "TemplatesTiles"."id";
	"""

	print(resource_type)
	cursor.execute(query, (game_id, tile_id, resource_type, value))
	return dict(cursor.fetchone())


@connect
def new_robber(cursor: psycopg2.extras.RealDictCursor, game_id: int, game_tile_id: Optional[int]=None,
	is_friendly: bool=False
) -> dict:
	query = """
		INSERT INTO "GamesRobbers" ("Games.id", "is_friendly", "GamesTiles.id") VALUES (%s, %s, %s)
		RETURNING *;
	"""

	cursor.execute(query, (game_id, is_friendly, game_tile_id))
	return dict(cursor.fetchone())
