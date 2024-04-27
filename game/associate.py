

from board import Port, Ports, Road, Roads, Settlement, Settlements, Tile, Tiles
import database.queries as db


DictList = list[dict]


def find(id: int) -> callable:
	def callback(item: object) -> bool:
		return item.id == id

	return callback


def ports_and_settlements(board_id: int, port_dicts: DictList, ports: Ports, settlement_dicts: DictList,
	settlements: Settlements
) -> None:
	ports_settlements: DictList = db.boards.get_ports_settlements(board_id)

	print(port_dicts)
	ports_board_game_mapping = {port["Ports.id"]: port["id"] for port in port_dicts}
	settlements_board_game_mapping = {settlement["Settlements.id"]: settlement["id"] for settlement in settlement_dicts}

	for ports_settlement in ports_settlements:
		game_port_id: int = ports_board_game_mapping[ports_settlement["Ports.id"]]
		game_settlement_id: int = settlements_board_game_mapping[ports_settlement["Settlements.id"]]

		port = next(filter(find(game_port_id), ports))
		settlement = next(filter(find(game_settlement_id), settlements))

		port.settlements[ports_settlement["Side's Corners.id"]-1] = settlement
		settlement.ports[ports_settlement["Corner's Sides.id"]-1] = port


def roads_and_settlements(board_id: int, road_dicts: DictList, roads: Roads, settlement_dicts: DictList,
	settlements: Settlements
) -> None:
	roads_settlements: DictList = db.boards.get_roads_settlements(board_id)

	roads_board_game_mapping = {road["Roads.id"]: road["id"] for road in road_dicts}
	settlements_board_game_mapping = {settlement["Settlements.id"]: settlement["id"] for settlement in settlement_dicts}

	for roads_settlement in roads_settlements:
		game_road_id: int = roads_board_game_mapping[roads_settlement["Roads.id"]]
		game_settlement_id: int = settlements_board_game_mapping[roads_settlement["Settlements.id"]]

		road = next(filter(find(game_road_id), roads))
		settlement = next(filter(find(game_settlement_id), settlements))

		road.settlements[roads_settlement["Edge's Corners.id"]-1] = settlement
		settlement.roads[roads_settlement["Corner's Edges.id"]-1] = road


def roads_and_tiles(board_id: int, road_dicts: DictList, roads: Roads, tile_dicts: DictList, tiles: Tiles) -> None:
	roads_tiles: DictList = db.boards.get_roads_tiles(board_id)

	roads_board_game_mapping = {road["Roads.id"]: road["id"] for road in road_dicts}
	tiles_board_game_mapping = {tile["Tiles.id"]: tile["id"] for tile in tile_dicts}

	for roads_tile in roads_tiles:
		game_road_id: int = roads_board_game_mapping[roads_tile["Roads.id"]]
		game_tile_id: int = tiles_board_game_mapping[roads_tile["Tiles.id"]]

		road = next(filter(find(game_road_id), roads))
		tile = next(filter(find(game_tile_id), tiles))

		road.tiles[roads_tile["Edge's Sides.id"]-1] = tile
		tile.roads[roads_tile["Side's Edges.id"]-1] = road


def settlements_and_tiles(board_id: int, settlement_dicts: DictList, settlements: Settlements, tile_dicts: DictList,
	tiles: Tiles
) -> None:
	settlements_tiles: DictList = db.boards.get_settlements_tiles(board_id)

	settlements_board_game_mapping = {settlement["Settlements.id"]: settlement["id"] for settlement in settlement_dicts}
	tiles_board_game_mapping = {tile["Tiles.id"]: tile["id"] for tile in tile_dicts}

	for settlements_tile in settlements_tiles:
		game_settlement_id: int = settlements_board_game_mapping[settlements_tile["Settlements.id"]]
		game_tile_id: int = tiles_board_game_mapping[settlements_tile["Tiles.id"]]

		settlement = next(filter(find(game_settlement_id), settlements))
		tile = next(filter(find(game_tile_id), tiles))

		settlement.tiles[settlements_tile["Corner's Sides.id"]-1] = tile
		tile.settlements[settlements_tile["Side's Corners.id"]-1] = settlement
