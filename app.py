

from flask import Flask


from database.queries import boards


app = Flask("Catan")


@app.route("/new/<int:board_id>")
def new(board_id: int):
	print(boards.get_board_ports(board_id))
	print(boards.get_board_roads(board_id))
	print(boards.get_board_settlements(board_id))
	print(boards.get_board_tiles(board_id))
	print(boards.get_board_ports_settlements(board_id))
	print(boards.get_board_roads_settlements(board_id))
	print(boards.get_board_roads_tiles(board_id))
	print(boards.get_board_settlements_tiles(board_id))
	return ""


app.run(host="0.0.0.0", port=80)
