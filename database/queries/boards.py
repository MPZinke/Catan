

import psycopg2
from typing import Optional


from database.connect import connect


@connect
def new_board(cursor, name: str) -> int:
	print(type(cursor))
	query = """
		INSERT INTO "Boards" ("name") VALUES (%s)
		RETURNING "id";
	"""

	cursor.execute(query, (name,))
	return cursor.fetchone()["id"]


@connect
def get_board_ports(cursor, boards_id: str) -> list[dict]:
	print(type(cursor))
	query = """
		SELECT *
		FROM "BoardsPorts"
		WHERE "Boards.id" = %s;
	"""

	cursor.execute(query, (boards_id,))
	return list(cursor)


@connect
def get_board_roads(cursor, boards_id: str) -> list[dict]:
	print(type(cursor))
	query = """
		SELECT *
		FROM "BoardsSettlements"
		WHERE "Boards.id" = %s;
	"""

	cursor.execute(query, (boards_id,))
	return list(cursor)


@connect
def get_board_settlements(cursor, boards_id: str) -> list[dict]:
	print(type(cursor))
	query = """
		SELECT *
		FROM "BoardsSettlements"
		WHERE "Boards.id" = %s;
	"""

	cursor.execute(query, (boards_id,))
	return list(cursor)


@connect
def get_board_tiles(cursor, boards_id: str) -> list[dict]:
	print(type(cursor))
	query = """
		SELECT *
		FROM "BoardsTiles"
		WHERE "Boards.id" = %s;
	"""

	cursor.execute(query, (boards_id,))
	return list(cursor)


@connect
def get_board_ports_settlements(cursor, boards_id: str) -> list[dict]:
	print(type(cursor))
	query = """
		SELECT *
		FROM "BoardsPortsSettlements"
		JOIN "Corner's Sides" ON "BoardsPortsSettlements"."Corner's Sides.id" = "Corner's Sides"."id"
		JOIN "Side's Corners" ON "BoardsPortsSettlements"."Side's Corners.id" = "Side's Corners"."id"
		WHERE "Boards.id" = %s;
	"""

	cursor.execute(query, (boards_id,))
	return list(cursor)


@connect
def get_board_roads_settlements(cursor, boards_id: str) -> list[dict]:
	print(type(cursor))
	query = """
		SELECT *
		FROM "BoardsRoadsSettlements"
		JOIN "Corner's Edges" ON "BoardsRoadsSettlements"."Corner's Edges.id" = "Corner's Edges"."id"
		JOIN "Edge's Corners" ON "BoardsRoadsSettlements"."Edge's Corners.id" = "Edge's Corners"."id"
		WHERE "Boards.id" = %s;
	"""

	cursor.execute(query, (boards_id,))
	return list(cursor)


@connect
def get_board_roads_tiles(cursor, boards_id: str) -> list[dict]:
	print(type(cursor))
	query = """
		SELECT *
		FROM "BoardsRoadsTiles"
		JOIN "Edge's Sides" ON "BoardsRoadsTiles"."Edge's Sides.id" = "Edge's Sides"."id"
		JOIN "Side's Edges" ON "BoardsRoadsTiles"."Side's Edges.id" = "Side's Edges"."id"
		WHERE "Boards.id" = %s;
	"""

	cursor.execute(query, (boards_id,))
	return list(cursor)


@connect
def get_board_settlements_tiles(cursor, boards_id: str) -> list[dict]:
	print(type(cursor))
	query = """
		SELECT *
		FROM "BoardsSettlementsTiles"
		JOIN "Corner's Sides" ON "BoardsSettlementsTiles"."Corner's Sides.id" = "Corner's Sides"."id"
		JOIN "Side's Corners" ON "BoardsSettlementsTiles"."Side's Corners.id" = "Side's Corners"."id"
		WHERE "Boards.id" = %s;
	"""

	cursor.execute(query, (boards_id,))
	return list(cursor)
