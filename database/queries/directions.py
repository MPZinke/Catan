

import psycopg2
import psycopg2.extras


from database.connect import connect


@connect
def get_corner_edges(cursor: psycopg2.extras.RealDictCursor) -> list[dict]:
	query = """
		SELECT *
		FROM "Corner's Edges";
	"""

	cursor.execute(query)
	return list(map(dict, cursor))


@connect
def get_corner_sides(cursor: psycopg2.extras.RealDictCursor) -> list[dict]:
	query = """
		SELECT *
		FROM "Corner's Sides";
	"""

	cursor.execute(query)
	return list(map(dict, cursor))


@connect
def get_edge_corners(cursor: psycopg2.extras.RealDictCursor) -> list[dict]:
	query = """
		SELECT *
		FROM "Edge's Corners";
	"""

	cursor.execute(query)
	return list(map(dict, cursor))


@connect
def get_edge_sides(cursor: psycopg2.extras.RealDictCursor) -> list[dict]:
	query = """
		SELECT *
		FROM "Edge's Sides";
	"""

	cursor.execute(query)
	return list(map(dict, cursor))


@connect
def get_side_corners(cursor: psycopg2.extras.RealDictCursor) -> list[dict]:
	query = """
		SELECT *
		FROM "Side's Corners";
	"""

	cursor.execute(query)
	return list(map(dict, cursor))


@connect
def get_side_edges(cursor: psycopg2.extras.RealDictCursor) -> list[dict]:
	query = """
		SELECT *
		FROM "Side's Edges";
	"""

	cursor.execute(query)
	return list(map(dict, cursor))
