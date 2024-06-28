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
		WHERE "id" = %s;
	"""

	cursor.execute(query, (game_id,))
	return dict(cursor.fetchone())


@connect
def get_ports(cursor: psycopg2.extras.RealDictCursor, game_id: int) -> list[dict]:
	query = """
		SELECT *
		FROM "GamesPorts"
		WHERE "Games.id" = %s
		ORDER BY "TemplatesPorts.id" ASC;  -- Ensure that games order is the same as the templates order
	"""

	cursor.execute(query, (game_id,))
	return list(map(dict, cursor))


@connect
def get_roads(cursor: psycopg2.extras.RealDictCursor, game_id: int) -> list[dict]:
	query = """
		SELECT *
		FROM "GamesRoads"
		WHERE "Games.id" = %s
		ORDER BY "TemplatesRoads.id" ASC;  -- Ensure that games order is the same as the templates order
	"""

	cursor.execute(query, (game_id,))
	return list(map(dict, cursor))


@connect
def get_robber(cursor: psycopg2.extras.RealDictCursor, game_id: int) -> list[dict]:
	query = """
		SELECT *
		FROM "GamesRobbers"
		WHERE "Games.id" = %s;
	"""

	cursor.execute(query, (game_id,))
	return dict(cursor.fetchone())


@connect
def get_settlements(cursor: psycopg2.extras.RealDictCursor, game_id: int) -> list[dict]:
	query = """
		SELECT *
		FROM "GamesSettlements"
		WHERE "Games.id" = %s
		ORDER BY "TemplatesSettlements.id" ASC;  -- Ensure that games order is the same as the templates order
	"""

	cursor.execute(query, (game_id,))
	return list(map(dict, cursor))


@connect
def get_tiles(cursor: psycopg2.extras.RealDictCursor, game_id: int) -> list[dict]:
	query = """
		SELECT *
		FROM "GamesTiles"
		WHERE "Games.id" = %s
		ORDER BY "TemplatesTiles.id" ASC;  -- Ensure that games order is the same as the templates order
	"""

	cursor.execute(query, (game_id,))
	return list(map(dict, cursor))
