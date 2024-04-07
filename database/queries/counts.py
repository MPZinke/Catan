
import psycopg2
import psycopg2.extras
from typing import Optional


from database.connect import connect


@connect
def get_tile_resources(cursor: psycopg2.extras.RealDictCursor, board_id: int) -> list[dict]:
	query = """
		SELECT *
		FROM "ResourceTypesCounts"
		JOIN "ResourceTypes" ON "TilesResources"."ResourceTypes.id" = "ResourceTypes"."id"
		WHERE "Boards.id" = %s;
	"""

	cursor.execute(query, (board_id))
	return list(cursor)


@connect
def get_tile_values(cursor: psycopg2.extras.RealDictCursor, board_id: int) -> list[dict]:
	query = """
		SELECT *
		FROM "TilesValues"
		WHERE "Boards.id" = %s;
	"""

	cursor.execute(query, (board_id))
	return list(cursor)
