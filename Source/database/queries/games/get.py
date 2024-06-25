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
def get_game(cursor: psycopg2.extras.RealDictCursor, game_id: int) -> dict:
	query = """
		SELECT *
		FROM "Games"
		WHERE "Games.id" = %s
	"""

	cursor.execute(query, (game_id,))
	return dict(cursor.fetchone())


@connect
def get_ports(cursor: psycopg2.extras.RealDictCursor, game_id: int) -> list[dict]:
	query = """
		SELECT *
		FROM "GamesPorts"
		JOIN "TemplatesPorts" ON "GamesPorts"."TemplatesPorts.id" = "TemplatesPorts"."id"
		WHERE "Games.id" = %s
	"""

	cursor.execute(query, (game_id,))
	return list(map(dict, cursor))


@connect
def get_roads(cursor: psycopg2.extras.RealDictCursor, game_id: int) -> list[dict]:
	query = """
		SELECT *
		FROM "GamesRoads"
		JOIN "TemplatesRoads" ON "GamesRoads"."TemplatesRoads.id" = "TemplatesRoads"."id"
		WHERE "Games.id" = %s
	"""

	cursor.execute(query, (game_id,))
	return list(map(dict, cursor))


@connect
def get_settlements(cursor: psycopg2.extras.RealDictCursor, game_id: int) -> list[dict]:
	query = """
		SELECT *
		FROM "GamesSettlements"
		JOIN "TemplatesSettlements" ON "GamesSettlements"."TemplatesSettlements.id" = "TemplatesSettlements"."id"
		WHERE "Games.id" = %s
	"""

	cursor.execute(query, (game_id,))
	return list(map(dict, cursor))


@connect
def get_tiles(cursor: psycopg2.extras.RealDictCursor, game_id: int) -> list[dict]:
	query = """
		SELECT *
		FROM "GamesTiles"
		JOIN "TemplatesTiles" ON "GamesTiles"."TemplatesTiles.id" = "TemplatesTiles"."id"
		WHERE "Games.id" = %s
	"""

	cursor.execute(query, (game_id,))
	return list(map(dict, cursor))
