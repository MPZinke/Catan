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
def new_ports(cursor: psycopg2.extras.RealDictCursor, game_id: int, resource_types: dict) -> dict:
	query = """
		INSERT INTO "GamesPorts" ("Games.id", "TemplatesPorts.id", "ResourceTypes.id")
		SELECT %s, "TemplatesPorts"."id", "ResourceTypes"."id"
		FROM "TemplatesPorts"
		JOIN UNNEST(
			%s,
			%s
		) AS "ResourceTypes" ("TemplatesPorts.id", "id") ON "TemplatesPorts"."id" = "ResourceTypes"."TemplatesPorts.id"
		RETURNING *;
	"""

	resource_type_template_tile_ids = list(resource_types.keys())
	resource_type_ids = list(resource_types.values())

	cursor.execute(query, (game_id, resource_type_template_tile_ids, resource_type_ids))
	return list(map(dict, cursor))


@connect
def new_road(cursor: psycopg2.extras.RealDictCursor, game_id: int, road_id: int) -> dict:
	query = """
		INSERT INTO "GamesRoads" ("Games.id", "TemplatesRoads.id") VALUES (%s, %s)
		RETURNING *;
	"""

	cursor.execute(query, (game_id, road_id))
	return dict(cursor.fetchone())


@connect
def new_roads(cursor: psycopg2.extras.RealDictCursor, game_id: int) -> dict:
	query = """
		INSERT INTO "GamesRoads" ("Games.id", "TemplatesRoads.id")
		SELECT %s, "TemplatesRoads"."id"
		FROM "TemplatesRoads"
		RETURNING *;
	"""

	cursor.execute(query, (game_id,))
	return list(map(dict, cursor))


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
def new_settlements(cursor: psycopg2.extras.RealDictCursor, game_id: int) -> dict:
	query = """
		INSERT INTO "GamesSettlements" ("Games.id", "TemplatesSettlements.id")
		SELECT %s, "TemplatesSettlements"."id"
		FROM "TemplatesSettlements"
		RETURNING *;
	"""

	cursor.execute(query, (game_id,))
	return list(map(dict, cursor))


@connect
def new_tile(cursor: psycopg2.extras.RealDictCursor, game_id: int, tile_id: int, resource_type: int, value: int) -> int:
	query = """
		INSERT INTO "GamesTiles" ("Games.id", "TemplatesTiles.id", "ResourceTypes.id", "value")
		VALUES (%s, %s, %s, %s)
		RETURNING *;
	"""

	cursor.execute(query, (game_id, tile_id, resource_type, value))
	return dict(cursor.fetchone())


@connect
def new_tiles(cursor: psycopg2.extras.RealDictCursor, game_id: int, resource_types: dict, values: dict) -> int:
	query = """
		INSERT INTO "GamesTiles" ("Games.id", "TemplatesTiles.id", "coordinate", "ResourceTypes.id", "value")
		SELECT %s, "TemplatesTiles"."id", "TemplatesTiles"."coordinate", "ResourceTypes"."id", "DiceValues"."value"
		FROM "TemplatesTiles"
		JOIN UNNEST(
			%s,
			%s
		) AS "ResourceTypes" ("TemplatesTiles.id", "id") ON "TemplatesTiles"."id" = "ResourceTypes"."TemplatesTiles.id"
		JOIN UNNEST(
			%s,
			%s
		) AS "DiceValues" ("TemplatesTiles.id", "value") ON "TemplatesTiles"."id" = "DiceValues"."TemplatesTiles.id"
		RETURNING *;
	"""

	resource_type_template_tile_ids = list(resource_types.keys())
	resource_type_ids = list(resource_types.values())
	value_template_tile_ids = list(values.keys())
	value_ids = list(values.values())

	cursor.execute(query,
		(game_id, resource_type_template_tile_ids, resource_type_ids, value_template_tile_ids, value_ids)
	)
	return list(map(dict, cursor))
