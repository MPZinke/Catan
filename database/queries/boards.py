

import psycopg2
import psycopg2.extras


from database.connect import connect


@connect
def new_board(cursor: psycopg2.extras.RealDictCursor, name: str) -> int:
	query = """
		INSERT INTO "Boards" ("name") VALUES (%s)
		RETURNING "id";
	"""

	cursor.execute(query, (name,))
	return cursor.fetchone()["id"]


@connect
def get_ports(cursor: psycopg2.extras.RealDictCursor, boards_id: str) -> list[dict]:
	query = """
		SELECT *
		FROM "Ports"
		WHERE "Boards.id" = %s;
	"""

	cursor.execute(query, (boards_id,))
	return list(map(dict, cursor))


@connect
def get_roads(cursor: psycopg2.extras.RealDictCursor, boards_id: str) -> list[dict]:
	query = """
		SELECT *
		FROM "Roads"
		WHERE "Boards.id" = %s;
	"""

	cursor.execute(query, (boards_id,))
	return list(map(dict, cursor))


@connect
def get_settlements(cursor: psycopg2.extras.RealDictCursor, boards_id: str) -> list[dict]:
	query = """
		SELECT *
		FROM "Settlements"
		WHERE "Boards.id" = %s;
	"""

	cursor.execute(query, (boards_id,))
	return list(map(dict, cursor))


@connect
def get_tiles(cursor: psycopg2.extras.RealDictCursor, boards_id: str) -> list[dict]:
	query = """
		SELECT *
		FROM "Tiles"
		WHERE "Boards.id" = %s;
	"""

	cursor.execute(query, (boards_id,))
	return list(map(dict, cursor))


@connect
def get_ports_settlements(cursor: psycopg2.extras.RealDictCursor, boards_id: str) -> list[dict]:
	query = """
		SELECT *
		FROM "PortsSettlements"
		JOIN "Corner's Sides" ON "PortsSettlements"."Corner's Sides.id" = "Corner's Sides"."id"
		JOIN "Side's Corners" ON "PortsSettlements"."Side's Corners.id" = "Side's Corners"."id"
		WHERE "Boards.id" = %s;
	"""

	cursor.execute(query, (boards_id,))
	return list(map(dict, cursor))


@connect
def get_roads_settlements(cursor: psycopg2.extras.RealDictCursor, boards_id: str) -> list[dict]:
	query = """
		SELECT *
		FROM "RoadsSettlements"
		JOIN "Corner's Edges" ON "RoadsSettlements"."Corner's Edges.id" = "Corner's Edges"."id"
		JOIN "Edge's Corners" ON "RoadsSettlements"."Edge's Corners.id" = "Edge's Corners"."id"
		WHERE "Boards.id" = %s;
	"""

	cursor.execute(query, (boards_id,))
	return list(map(dict, cursor))


@connect
def get_roads_tiles(cursor: psycopg2.extras.RealDictCursor, boards_id: str) -> list[dict]:
	query = """
		SELECT *
		FROM "RoadsTiles"
		JOIN "Edge's Sides" ON "RoadsTiles"."Edge's Sides.id" = "Edge's Sides"."id"
		JOIN "Side's Edges" ON "RoadsTiles"."Side's Edges.id" = "Side's Edges"."id"
		WHERE "Boards.id" = %s;
	"""

	cursor.execute(query, (boards_id,))
	return list(map(dict, cursor))


@connect
def get_settlements_tiles(cursor: psycopg2.extras.RealDictCursor, boards_id: str) -> list[dict]:
	query = """
		SELECT *
		FROM "SettlementsTiles"
		JOIN "Corner's Sides" ON "SettlementsTiles"."Corner's Sides.id" = "Corner's Sides"."id"
		JOIN "Side's Corners" ON "SettlementsTiles"."Side's Corners.id" = "Side's Corners"."id"
		WHERE "Boards.id" = %s;
	"""

	cursor.execute(query, (boards_id,))
	return list(map(dict, cursor))
