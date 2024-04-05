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
from typing import Optional


from database.connect import connect


@connect
def new_game(cursor, boards_id: Optional[int]) -> int:
	print(type(cursor))
	query = """
		INSERT INTO "Games" ("Boards.id") VALUES (%s)
		RETURNING "id";
	"""

	cursor.execute(query, (boards_id,))
	return cursor.fetchone()["id"]
