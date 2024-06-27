
import psycopg2
import psycopg2.extras
from typing import Optional


from database.connect import connect


@connect
def get_dice_value_counts(cursor: psycopg2.extras.RealDictCursor, template_id: int) -> list[dict]:
	query = """
		SELECT *
		FROM "TemplatesDiceValuesCounts"
		WHERE "Templates.id" = %s;
	"""

	cursor.execute(query, (template_id,))
	return list(map(dict, cursor))


@connect
def get_ports_resource_types_counts(cursor: psycopg2.extras.RealDictCursor, template_id: int) -> list[dict]:
	query = """
		SELECT *
		FROM "TemplatesPortsResourceTypesCounts"
		LEFT JOIN "ResourceTypes" ON "TemplatesPortsResourceTypesCounts"."ResourceTypes.id" = "ResourceTypes"."id"
		WHERE "Templates.id" = %s;
	"""

	cursor.execute(query, (template_id,))
	return list(map(dict, cursor))


@connect
def get_tiles_resource_types_counts(cursor: psycopg2.extras.RealDictCursor, template_id: int) -> list[dict]:
	query = """
		SELECT *
		FROM "TemplatesTilesResourceTypesCounts"
		LEFT JOIN "ResourceTypes" ON "TemplatesTilesResourceTypesCounts"."ResourceTypes.id" = "ResourceTypes"."id"
		WHERE "Templates.id" = %s;
	"""

	cursor.execute(query, (template_id,))
	return list(map(dict, cursor))
