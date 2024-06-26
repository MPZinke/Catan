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
from database.queries.games.new.board import new_port
from database.queries.games.new.board import new_road
from database.queries.games.new.board import new_robber
from database.queries.games.new.board import new_settlement
from database.queries.games.new.board import new_tile
from database.queries.games.new.board import new_ports_settlements
from database.queries.games.new.board import new_roads_settlements
from database.queries.games.new.board import new_roads_tiles
from database.queries.games.new.board import new_settlements_tiles


@connect
def new_game(cursor: psycopg2.extras.RealDictCursor, template_id: int) -> dict:
	query = """
		INSERT INTO "Games" ("Templates.id") VALUES (%s)
		RETURNING *;
	"""

	cursor.execute(query, (template_id,))
	return dict(cursor.fetchone())


def new_player(cursor: psycopg2.extras.RealDictCursor, game_id: int, name: str) -> dict:
	query = """
		INSERT INTO "Games" ("Games.id", "name") VALUES (%s, %s)
		RETURNING *;
	"""

	cursor.execute(query, (game_id, name))
	return dict(cursor.fetchone())
