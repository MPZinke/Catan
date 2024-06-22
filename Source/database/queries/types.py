

import psycopg2
import psycopg2.extras


from database.connect import connect


@connect
def get_resource_types(cursor: psycopg2.extras.RealDictCursor) -> list[dict]:
	query = """
		SELECT *
		FROM "ResourceTypes";
	"""

	cursor.execute(query)
	return list(map(dict, cursor))


@connect
def get_settlement_types(cursor: psycopg2.extras.RealDictCursor) -> list[dict]:
	query = """
		SELECT *
		FROM "SettlementTypes";
	"""

	cursor.execute(query)
	return list(map(dict, cursor))
