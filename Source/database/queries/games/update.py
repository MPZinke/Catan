#!/opt/homebrew/bin/python3
# -*- coding: utf-8 -*-
__author__ = "MPZinke"

########################################################################################################################
#                                                                                                                      #
#   created by: MPZinke                                                                                                #
#   on 2024.06.26                                                                                                      #
#                                                                                                                      #
#   DESCRIPTION:                                                                                                       #
#   BUGS:                                                                                                              #
#   FUTURE:                                                                                                            #
#                                                                                                                      #
########################################################################################################################


import psycopg2.extras


from database.connect import connect


@connect
def update_port_settlements(cursor: psycopg2.extras.RealDictCursor, port_id: int, settlement_ids: list[int]) -> dict:
	query = """
		UPDATE "GamesPorts" SET "GamesSettlements.ids" = ARRAY[%s, %s, %s, %s, %s, %s]::INT[6]
		WHERE "id" = %s
		RETURNING *;
	"""

	cursor.execute(query, (*(id for id in settlement_ids), port_id))
	return dict(cursor.fetchone())


@connect
def update_road_settlements_and_tiles(cursor: psycopg2.extras.RealDictCursor, road_id: int, settlement_ids: list[int],
	tile_ids: list[int]
) -> dict:
	query = """
		UPDATE "GamesRoads"
		SET "GamesSettlements.ids" = ARRAY[%s, %s]::INT[2],
		    "GamesTiles.ids" = ARRAY[%s, %s]::INT[2]
		WHERE "id" = %s
		RETURNING *;
	"""

	cursor.execute(query, (*(id for id in settlement_ids), *(id for id in tile_ids), road_id))
	return dict(cursor.fetchone())


@connect
def update_settlement_ports_roads_and_tiles(cursor: psycopg2.extras.RealDictCursor, settlement_id: int, port_ids: list[int],
	road_ids: list[int], tile_ids: list[int]
) -> dict:
	query = """
		UPDATE "GamesSettlements"
		SET "GamesPorts.ids" = ARRAY[%s, %s, %s]::INT[3],
			"GamesRoads.ids" = ARRAY[%s, %s, %s]::INT[3],
			"GamesTiles.ids" = ARRAY[%s, %s, %s]::INT[3]
		WHERE "id" = %s
		RETURNING *;
	"""

	values = (*(id for id in port_ids), *(id for id in road_ids), *(id for id in tile_ids), settlement_id)
	cursor.execute(query, values)
	return dict(cursor.fetchone())


@connect
def update_tile_roads_and_settlements(cursor: psycopg2.extras.RealDictCursor, tile_id: int, road_ids: list[int],
	settlement_ids: list[int]
) -> dict:
	query = """
		UPDATE "GamesTiles"
		SET "GamesRoads.ids" = ARRAY[%s, %s, %s, %s, %s, %s]::INT[6],
		    "GamesSettlements.ids" = ARRAY[%s, %s, %s, %s, %s, %s]::INT[6]
		WHERE "id" = %s
		RETURNING *;
	"""

	cursor.execute(query, (*(id for id in road_ids), *(id for id in settlement_ids), tile_id))
	return dict(cursor.fetchone())
