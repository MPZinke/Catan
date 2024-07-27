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


from typing import Optional


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
	game_dict: Optional[dict] = cursor.fetchone()
	if(game_dict is None):
		return None

	return dict(game_dict)


@connect
def get_board(cursor: psycopg2.extras.RealDictCursor, game_id: int) -> dict:
	query = """
		SELECT *
		FROM "GamesBoards"
		WHERE "Games.id" = %s;
	"""

	cursor.execute(query, (game_id,))
	board_dict: Optional[dict] = cursor.fetchone()
	if(board_dict is None):
		return None

	return dict(board_dict)


@connect
def get_ports(cursor: psycopg2.extras.RealDictCursor, game_id: int) -> list[dict]:
	query = """
		SELECT *
		FROM "GamesPorts"
		WHERE "GamesBoards.id" = %s
		ORDER BY "TemplatesPorts.id" ASC;  -- Ensure that games order is the same as the templates order
	"""

	cursor.execute(query, (game_id,))
	return list(map(dict, cursor))


@connect
def get_roads(cursor: psycopg2.extras.RealDictCursor, game_id: int) -> list[dict]:
	query = """
		SELECT *
		FROM "GamesRoads"
		WHERE "GamesBoards.id" = %s
		ORDER BY "TemplatesRoads.id" ASC;  -- Ensure that games order is the same as the templates order
	"""

	cursor.execute(query, (game_id,))
	return list(map(dict, cursor))


@connect
def get_robber(cursor: psycopg2.extras.RealDictCursor, game_id: int) -> list[dict]:
	query = """
		SELECT *
		FROM "GamesRobbers"
		WHERE "GamesBoards.id" = %s;
	"""

	cursor.execute(query, (game_id,))
	robber_dict: Optional[dict] = cursor.fetchone()
	if(robber_dict is None):
		return None

	return dict(robber_dict)


@connect
def get_settlements(cursor: psycopg2.extras.RealDictCursor, game_id: int) -> list[dict]:
	query = """
		SELECT *
		FROM "GamesSettlements"
		WHERE "GamesBoards.id" = %s
		ORDER BY "TemplatesSettlements.id" ASC;  -- Ensure that games order is the same as the templates order
	"""

	cursor.execute(query, (game_id,))
	return list(map(dict, cursor))


@connect
def get_tiles(cursor: psycopg2.extras.RealDictCursor, game_id: int) -> list[dict]:
	query = """
		SELECT *
		FROM "GamesTiles"
		WHERE "GamesBoards.id" = %s
		ORDER BY "TemplatesTiles.id" ASC;  -- Ensure that games order is the same as the templates order
	"""

	cursor.execute(query, (game_id,))
	return list(map(dict, cursor))
