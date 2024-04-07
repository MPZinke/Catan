

from flask import Flask


from database.queries import boards
import setup


app = Flask("Catan")


@app.route("/new/<int:board_id>")
def new(board_id: int):
	port_dicts: list[dict] = boards.get_board_ports(board_id)
	road_dicts: list[dict] = boards.get_board_roads(board_id)
	settlement_dicts: list[dict] = boards.get_board_settlements(board_id)
	tile_dicts: list[dict] = boards.get_board_tiles(board_id)
	boards.get_board_ports_settlements(board_id)
	boards.get_board_roads_settlements(board_id)
	boards.get_board_roads_tiles(board_id)
	boards.get_board_settlements_tiles(board_id)

	ports = setup.create.ports(port_dicts)
	roads = setup.create.roads(road_dicts)
	settlements = setup.create.settlements(settlement_dicts)
	tiles = setup.create.tiles(tile_dicts)
	return "<br/>".join(ports, roads, settlements, tiles)


app.run(host="0.0.0.0", port=80)
