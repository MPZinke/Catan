
import psycopg2
import psycopg2.extras
from typing import Optional


from database.connect import connect


@connect
def get_dice_value_counts(cursor: psycopg2.extras.RealDictCursor, board_id: int) -> list[dict]:
	query = """
		SELECT *
		FROM "DiceValuesCounts"
		WHERE "Boards.id" = %s;
	"""

	cursor.execute(query, (board_id))
	return list(cursor)


@connect
def get_ports_resource_types_counts(cursor: psycopg2.extras.RealDictCursor, board_id: int) -> list[dict]:
	query = """
		SELECT *
		FROM "PortsResourceTypesCounts"
		JOIN "ResourceTypes" ON "TilesResources"."ResourceTypes.id" = "ResourceTypes"."id"
		WHERE "Boards.id" = %s;
	"""

	cursor.execute(query, (board_id))
	return list(cursor)


@connect
def get_tiles_resource_types_counts(cursor: psycopg2.extras.RealDictCursor, board_id: int) -> list[dict]:
	query = """
		SELECT *
		FROM "TilesResourceTypesCounts"
		JOIN "ResourceTypes" ON "TilesResources"."ResourceTypes.id" = "ResourceTypes"."id"
		WHERE "Boards.id" = %s;
	"""

	cursor.execute(query, (board_id))
	return list(cursor)
