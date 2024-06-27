

from typing import Dict, Tuple


from game.board import Board, Port, Ports, Road, Roads, Robber, Settlement, Settlements, Tile, Tiles
from game.board.construct import BoardData


BoardPartID = int
DictList = list[dict]
GamePartID = int
BoardPartIDGamePartIDMapping = Dict[BoardPartID, GamePartID]


def find(id: int, parts: list[object]) -> object:
	for part in parts:
		if(part.id == id):
			return part


def find_index(sought_value: int, values: list[int]) -> int:
	for index, value in enumerate(values):
		if(sought_value == value):
			return index


def find_part_dict_and_part(id: int, part_dicts: DictList, parts: list[object]) -> Tuple[dict, object]:
	for part_dict, part in zip(part_dicts, parts):
		if(part.id == id):
			return part_dict, part


def map_board_part_id_to_game_part_id(part_dicts: DictList, board_part_id_key: str) -> BoardPartIDGamePartIDMapping:
	mapping: BoardPartIDGamePartIDMapping = {game_part[board_part_id_key]: game_part["id"] for game_part in part_dicts}
	return mapping


def associate_board_parts(board_data: BoardData, board: Board) -> None:
	associate_ports_and_settlements(board_data, board)
	associate_roads_and_settlements(board_data, board)
	associate_roads_and_tiles(board_data, board)
	associate_robber_and_tile(board_data.robber, board.robber, board.tiles)
	associate_settlements_and_tiles(board_data, board)


def associate_ports_and_settlements(board_data: BoardData, board: Board) -> None:
	ports: Ports = board.ports
	settlements: Settlements = board.settlements

	for port_dict, port in zip(board_data.ports, ports):
		for settlement_index, settlement_id in enumerate(port_dict["GamesSettlements.ids"]):
			if(settlement_id is not None):
				settlement_dict, settlement = find_part_dict_and_part(settlement_id, board_data.settlements, settlements)

				port.settlements[settlement_index] = settlement
				port_index: int = find_index(port.id, settlement_dict["GamesPorts.ids"])
				settlement.ports[port_index] = port


def associate_roads_and_settlements(board_data: BoardData, board: Board) -> None:
	roads: Roads = board.roads
	settlements: Settlements = board.settlements

	for road_dict, road in zip(board_data.roads, roads):
		for settlement_index, settlement_id in enumerate(road_dict["GamesSettlements.ids"]):
			if(settlement_id is not None):
				settlement_dict, settlement = find_part_dict_and_part(settlement_id, board_data.settlements, settlements)

				road.settlements[settlement_index] = settlement
				road_index: int = find_index(road.id, settlement_dict["GamesRoads.ids"])
				settlement.roads[road_index] = road


def associate_roads_and_tiles(board_data: BoardData, board: Board) -> None:
	roads: Roads = board.roads
	tiles: Tiles = board.tiles

	for road_dict, road in zip(board_data.roads, roads):
		for tile_index, tile_id in enumerate(road_dict["GamesTiles.ids"]):
			if(tile_id is not None):
				tile_dict, tile = find_part_dict_and_part(tile_id, board_data.tiles, tiles)

				road.tiles[tile_index] = tile
				road_index: int = find_index(road.id, tile_dict["GamesRoads.ids"])
				tile.roads[road_index] = road


def associate_robber_and_tile(robber_dict: dict, robber: Robber, tiles: Tiles) -> None:
	tile: Tile = find(robber_dict["GamesTiles.id"], tiles)
	robber.tile = tile


def associate_settlements_and_tiles(board_data: BoardData, board: Board) -> None:
	settlements: Settlements = board.settlements
	tiles: Tiles = board.tiles

	for settlement_dict, settlement in zip(board_data.settlements, settlements):
		for tile_index, tile_id in enumerate(settlement_dict["GamesTiles.ids"]):
			if(tile_id is not None):
				tile_dict, tile = find_part_dict_and_part(tile_id, board_data.tiles, tiles)

				settlement.tiles[tile_index] = tile
				settlement_index: int = find_index(settlement.id, tile_dict["GamesSettlements.ids"])
				tile.settlements[settlement_index] = settlement
