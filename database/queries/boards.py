
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
def new_board_port(cursor, boards_id: str, top_left_settlement: int, top_right_settlement: int, right_settlement: int,
	bottom_right_settlement: int, bottom_left_settlement: int, left_settlement: int
) -> int:
	print(type(cursor))
	query = """
		INSERT INTO "BoardsPorts" ("Boards.id", "Settlements::TOP_LEFT", "Settlements::TOP_RIGHT", "Settlements::RIGHT",
			"Settlements::BOTTOM_RIGHT", "Settlements::BOTTOM_LEFT", "Settlements::LEFT")
		VALUES (%s, %s, %s, %s, %s, %s, %s)
		RETURNING "id";
	"""

	cursor.execute(query,
		(boards_id, top_left_settlement, top_right_settlement, right_settlement, bottom_right_settlement,
			bottom_left_settlement, left_settlement
		)	
	)
	return cursor.fetchone()["id"]
