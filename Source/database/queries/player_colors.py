#!/opt/homebrew/bin/python3
# -*- coding: utf-8 -*-
__author__ = "MPZinke"

########################################################################################################################
#                                                                                                                      #
#   created by: MPZinke                                                                                                #
#   on 2024.07.23                                                                                                      #
#                                                                                                                      #
#   DESCRIPTION:                                                                                                       #
#   BUGS:                                                                                                              #
#   FUTURE:                                                                                                            #
#                                                                                                                      #
########################################################################################################################


import psycopg2
import psycopg2.extras


from database.connect import connect


@connect
def get_player_colors(cursor: psycopg2.extras.RealDictCursor) -> list[dict]:
	query = """
		SELECT *
		FROM "PlayerColors";
	"""

	cursor.execute(query)
	return list(map(dict, cursor))
