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


import psycopg2.extras


from database.connect import connect


@connect
def get_ports(cursor: psycopg2.extras.RealDictCursor, game_id: int) -> dict:
	query = """
		SELECT *
		FROM "GamesPorts"
		JOIN "Ports" ON "GamesPorts"."Ports.id" = "Ports"."id"
		WHERE "Games.id" = %s
	"""

	cursor.execute(query, (game_id,))
	return list(map(dict, cursor))


@connect
def get_roads(cursor: psycopg2.extras.RealDictCursor, game_id: int) -> dict:
	query = """
		SELECT *
		FROM "GamesRoads"
		JOIN "Roads" ON "GamesRoads"."Roads.id" = "Roads"."id"
		WHERE "Games.id" = %s
	"""

	cursor.execute(query, (game_id,))
	return list(map(dict, cursor))


@connect
def get_settlements(cursor: psycopg2.extras.RealDictCursor, game_id: int) -> dict:
	query = """
		SELECT *
		FROM "GamesSettlements"
		JOIN "Settlements" ON "GamesSettlements"."Settlements.id" = "Settlements"."id"
		WHERE "Games.id" = %s
	"""

	cursor.execute(query, (game_id,))
	return list(map(dict, cursor))


@connect
def get_tiles(cursor: psycopg2.extras.RealDictCursor, game_id: int) -> dict:
	query = """
		SELECT *
		FROM "GamesTiles"
		JOIN "Tiles" ON "GamesTiles"."Tiles.id" = "Tiles"."id"
		WHERE "Games.id" = %s
	"""

	cursor.execute(query, (game_id,))
	return list(map(dict, cursor))
