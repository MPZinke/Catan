

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
		WHERE "Templates.id" = %s
		ORDER BY "TemplatesPorts"."id" ASC;
	"""

	cursor.execute(query, (boards_id,))
	return list(map(dict, cursor))


@connect
def get_roads(cursor: psycopg2.extras.RealDictCursor, boards_id: str) -> list[dict]:
	query = """
		SELECT *
		FROM "TemplatesRoads"
		WHERE "Templates.id" = %s
		ORDER BY "TemplatesRoads"."id" ASC;
	"""

	cursor.execute(query, (boards_id,))
	return list(map(dict, cursor))


@connect
def get_settlements(cursor: psycopg2.extras.RealDictCursor, boards_id: str) -> list[dict]:
	query = """
		SELECT *
		FROM "TemplatesSettlements"
		WHERE "Templates.id" = %s
		ORDER BY "TemplatesSettlements"."id" ASC;
	"""

	cursor.execute(query, (boards_id,))
	return list(map(dict, cursor))


@connect
def get_tiles(cursor: psycopg2.extras.RealDictCursor, boards_id: str) -> list[dict]:
	query = """
		SELECT *
		FROM "TemplatesTiles"
		WHERE "Templates.id" = %s
		ORDER BY "TemplatesTiles"."id" ASC;
	"""

	cursor.execute(query, (boards_id,))
	return list(map(dict, cursor))
