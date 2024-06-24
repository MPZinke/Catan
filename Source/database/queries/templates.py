

import psycopg2.extras


from database.connect import connect


@connect
def new_template(cursor: psycopg2.extras.RealDictCursor, name: str) -> int:
	query = """
		INSERT INTO "Templates" ("name") VALUES (%s)
		RETURNING "id";
	"""

	cursor.execute(query, (name,))
	return cursor.fetchone()["id"]


@connect
def get_template(cursor: psycopg2.extras.RealDictCursor, boards_id: str) -> dict:
	query = """
		SELECT *
		FROM "Templates"
		WHERE "id" = %s;
	"""

	cursor.execute(query, (boards_id,))
	return dict(cursor.fetchone())


@connect
def get_ports(cursor: psycopg2.extras.RealDictCursor, boards_id: str) -> list[dict]:
	query = """
		SELECT *
		FROM "TemplatesPorts"
		WHERE "Templates.id" = %s;
	"""

	cursor.execute(query, (boards_id,))
	return list(map(dict, cursor))


@connect
def get_roads(cursor: psycopg2.extras.RealDictCursor, boards_id: str) -> list[dict]:
	query = """
		SELECT *
		FROM "TemplatesRoads"
		WHERE "Templates.id" = %s;
	"""

	cursor.execute(query, (boards_id,))
	return list(map(dict, cursor))


@connect
def get_settlements(cursor: psycopg2.extras.RealDictCursor, boards_id: str) -> list[dict]:
	query = """
		SELECT *
		FROM "TemplatesSettlements"
		WHERE "Templates.id" = %s;
	"""

	cursor.execute(query, (boards_id,))
	return list(map(dict, cursor))


@connect
def get_tiles(cursor: psycopg2.extras.RealDictCursor, boards_id: str) -> list[dict]:
	query = """
		SELECT *
		FROM "TemplatesTiles"
		WHERE "Templates.id" = %s;
	"""

	cursor.execute(query, (boards_id,))
	return list(map(dict, cursor))


@connect
def get_ports_settlements(cursor: psycopg2.extras.RealDictCursor, boards_id: str) -> list[dict]:
	query = """
		SELECT *
		FROM "TemplatesPortsSettlements"
		JOIN "Corner's Sides" ON "TemplatesPortsSettlements"."Corner's Sides.id" = "Corner's Sides"."id"
		JOIN "Side's Corners" ON "TemplatesPortsSettlements"."Side's Corners.id" = "Side's Corners"."id"
		WHERE "Templates.id" = %s;
	"""

	cursor.execute(query, (boards_id,))
	return list(map(dict, cursor))


@connect
def get_roads_settlements(cursor: psycopg2.extras.RealDictCursor, boards_id: str) -> list[dict]:
	query = """
		SELECT *
		FROM "TemplatesRoadsSettlements"
		JOIN "Corner's Edges" ON "TemplatesRoadsSettlements"."Corner's Edges.id" = "Corner's Edges"."id"
		JOIN "Edge's Corners" ON "TemplatesRoadsSettlements"."Edge's Corners.id" = "Edge's Corners"."id"
		WHERE "Templates.id" = %s;
	"""

	cursor.execute(query, (boards_id,))
	return list(map(dict, cursor))


@connect
def get_roads_tiles(cursor: psycopg2.extras.RealDictCursor, boards_id: str) -> list[dict]:
	query = """
		SELECT *
		FROM "TemplatesRoadsTiles"
		JOIN "Edge's Sides" ON "TemplatesRoadsTiles"."Edge's Sides.id" = "Edge's Sides"."id"
		JOIN "Side's Edges" ON "TemplatesRoadsTiles"."Side's Edges.id" = "Side's Edges"."id"
		WHERE "Templates.id" = %s;
	"""

	cursor.execute(query, (boards_id,))
	return list(map(dict, cursor))


@connect
def get_settlements_tiles(cursor: psycopg2.extras.RealDictCursor, boards_id: str) -> list[dict]:
	query = """
		SELECT *
		FROM "TemplatesSettlementsTiles"
		JOIN "Corner's Sides" ON "TemplatesSettlementsTiles"."Corner's Sides.id" = "Corner's Sides"."id"
		JOIN "Side's Corners" ON "TemplatesSettlementsTiles"."Side's Corners.id" = "Side's Corners"."id"
		WHERE "Templates.id" = %s;
	"""

	cursor.execute(query, (boards_id,))
	return list(map(dict, cursor))
