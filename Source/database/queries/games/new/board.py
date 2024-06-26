#!/opt/homebrew/bin/python3
# -*- coding: utf-8 -*-
__author__ = "MPZinke"

########################################################################################################################
#                                                                                                                      #
#   created by: MPZinke                                                                                                #
#   on 2024.06.25                                                                                                      #
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
def new_robber(cursor: psycopg2.extras.RealDictCursor, game_id: int, game_tile_id: Optional[int]=None,
	is_friendly: bool=False
) -> dict:
	query = """
		INSERT INTO "GamesRobbers" ("Games.id", "is_friendly", "GamesTiles.id") VALUES (%s, %s, %s)
		RETURNING *;
	"""

	cursor.execute(query, (game_id, is_friendly, game_tile_id))
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
def new_ports_settlements(cursor: psycopg2.extras.RealDictCursor, game_id: int, ports_id: int, settlements_id: int,
	corners_sides_id: int, sides_corners_id: int
) -> dict:
	query = """
		INSERT INTO "GamesPortsGamesSettlements" 
		("Games.id", "GamesPorts.id", "GamesSettlements.id", "Corner's Sides.id", "Side's Corners.id")
		VALUES (%s, %s, %s, %s, %s)
		RETURNING *;
	"""

	cursor.execute(query, (game_id, ports_id, settlements_id, corners_sides_id, sides_corners_id))
	return dict(cursor.fetchone())


@connect
def new_roads_settlements(cursor: psycopg2.extras.RealDictCursor, game_id: int, roads_id: int, settlements_id: int,
	corners_edges_id: int, edges_corners_id: int
) -> dict:
	query = """
		INSERT INTO "GamesRoadsGamesSettlements" 
		("Games.id", "GamesRoads.id", "GamesSettlements.id", "Corner's Edges.id", "Edge's Corners.id")
		VALUES (%s, %s, %s, %s, %s)
		RETURNING *;
	"""

	cursor.execute(query, (game_id, roads_id, settlements_id, corners_edges_id, edges_corners_id))
	return dict(cursor.fetchone())


@connect
def new_roads_tiles(cursor: psycopg2.extras.RealDictCursor, game_id: int, roads_id: int, tiles_id: int,
	edges_sides_id: int, sides_edges_id: int
) -> dict:
	query = """
		INSERT INTO "GamesRoadsGamesTiles" 
		("Games.id", "GamesRoads.id", "GamesTiles.id", "Edge's Sides.id", "Side's Edges.id")
		VALUES (%s, %s, %s, %s, %s)
		RETURNING *;
	"""

	cursor.execute(query, (game_id, roads_id, tiles_id, edges_sides_id, sides_edges_id))
	return dict(cursor.fetchone())


@connect
def new_settlements_tiles(cursor: psycopg2.extras.RealDictCursor, game_id: int, settlements_id: int, tiles_id: int,
	corners_sides_id: int, sides_corners_id: int
) -> dict:
	query = """
		INSERT INTO "GamesSettlementsGamesTiles" 
		("Games.id", "GamesSettlements.id", "GamesTiles.id", "Corner's Sides.id", "Side's Corners.id")
		VALUES (%s, %s, %s, %s, %s)
		RETURNING *;
	"""

	cursor.execute(query, (game_id, settlements_id, tiles_id, corners_sides_id, sides_corners_id))
	return dict(cursor.fetchone())
