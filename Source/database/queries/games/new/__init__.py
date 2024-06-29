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
def new_game(cursor: psycopg2.extras.RealDictCursor) -> dict:
	query = """
		INSERT INTO "Games" ("started")
		VALUES
		(CURRENT_TIMESTAMP)
		RETURNING *;
	"""

	cursor.execute(query)
	return dict(cursor.fetchone())


def new_player(cursor: psycopg2.extras.RealDictCursor, game_id: int, name: str) -> dict:
	query = """
		INSERT INTO "Games" ("Games.id", "name") VALUES (%s, %s)
		RETURNING *;
	"""

	cursor.execute(query, (game_id, name))
	return dict(cursor.fetchone())
