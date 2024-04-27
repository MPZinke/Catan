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
from typing import Optional, Tuple


from database.connect import connect


@connect
def new_game(cursor, board_id: int) -> int:
	query = """
		INSERT INTO "Games" ("Boards.id") VALUES (%s)
		RETURNING *;
	"""

	cursor.execute(query, (board_id,))
	return dict(cursor.fetchone())


@connect
def new_port(cursor, game_id: int, port_id: int, resource_type: int) -> int:
	query = """
		INSERT INTO "GamesPorts" ("Games.id", "Ports.id", "ResourceTypes.id") VALUES (%s, %s, %s)
		RETURNING *;
	"""

	cursor.execute(query, (game_id, port_id, resource_type))
	return dict(cursor.fetchone())


@connect
def new_road(cursor, game_id: int, road_id: int) -> int:
	query = """
		INSERT INTO "GamesRoads" ("Games.id", "Roads.id") VALUES (%s, %s)
		RETURNING *;
	"""

	cursor.execute(query, (game_id, road_id))
	return dict(cursor.fetchone())


@connect
def new_settlement(cursor, game_id: int, settlement_id: int, settlement_type_id: Optional[int]=None) -> int:
	query = """
		INSERT INTO "GamesSettlements" ("Games.id", "Settlements.id", "SettlementTypes.id") VALUES (%s, %s, %s)
		RETURNING *;
	"""

	cursor.execute(query, (game_id, settlement_id, settlement_type_id))
	return dict(cursor.fetchone())


@connect
def new_tile(cursor, game_id: int, tile_id: int, resource_type: int, value: int) -> int:
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
def get_ports(cursor, game_id: int) -> dict:
	query = """
		SELECT *
		FROM "GamesPorts"
		JOIN "Ports" ON "GamesPorts"."Ports.id" = "Ports"."id"
		WHERE "Games.id" = %s
	"""

	cursor.execute(query, (game_id,))
	return list(map(dict, cursor))


@connect
def get_roads(cursor, game_id: int) -> dict:
	query = """
		SELECT *
		FROM "GamesRoads"
		JOIN "Roads" ON "GamesRoads"."Roads.id" = "Roads"."id"
		WHERE "Games.id" = %s
	"""

	cursor.execute(query, (game_id,))
	return list(map(dict, cursor))


@connect
def get_settlements(cursor, game_id: int) -> dict:
	query = """
		SELECT *
		FROM "GamesSettlements"
		JOIN "Settlements" ON "GamesSettlements"."Settlements.id" = "Settlements"."id"
		WHERE "Games.id" = %s
	"""

	cursor.execute(query, (game_id,))
	return list(map(dict, cursor))


@connect
def get_tiles(cursor, game_id: int) -> dict:
	query = """
		SELECT *
		FROM "GamesTiles"
		JOIN "Tiles" ON "GamesTiles"."Tiles.id" = "Tiles"."id"
		WHERE "Games.id" = %s
	"""

	cursor.execute(query, (game_id,))
	return list(map(dict, cursor))
