

from typing import Dict


from game.board import Board, Port, Ports, Road, Roads, Robber, Settlement, Settlements, Tile, Tiles
from game.board.construct import BoardData


BoardPartID = int
DictList = list[dict]
GamePartID = int
BoardPartIDGamePartIDMapping = Dict[BoardPartID, GamePartID]


def find(id: int, parts: list[object]) -> object:
	return next(filter(lambda part: part.id == id, parts))


def map_board_part_id_to_game_part_id(part_dicts: DictList, board_part_id_key: str) -> BoardPartIDGamePartIDMapping:
	mapping: BoardPartIDGamePartIDMapping = {game_part[board_part_id_key]: game_part["id"] for game_part in part_dicts}
	return mapping


def board_parts(board_data: BoardData, board: Board) -> None:
	ports_and_settlements(board_data, board)
	roads_and_settlements(board_data, board)
	roads_and_tiles(board_data, board)
	settlements_and_tiles(board_data, board)


def ports_and_settlements(board_data: BoardData, board: Board) -> None:
	ports: Ports = board.ports
	settlements: Settlements = board.settlements

	for ports_settlement in board_data.ports_settlements:
		port: Port = find(ports_settlement["GamesPorts.id"], ports)
		settlement: Settlement = find(ports_settlement["GamesSettlements.id"], settlements)

		port.settlements[ports_settlement["Side's Corners.id"]-1] = settlement
		settlement.ports[ports_settlement["Corner's Sides.id"]-1] = port


def roads_and_settlements(board_data: BoardData, board: Board) -> None:
	roads: Roads = board.roads
	settlements: Settlements = board.settlements

	for roads_settlement in board_data.roads_settlements:
		road: Road = find(roads_settlement["GamesRoads.id"], roads)
		settlement: Settlement = find(roads_settlement["GamesSettlements.id"], settlements)

		road.settlements[roads_settlement["Edge's Corners.id"]-1] = settlement
		settlement.roads[roads_settlement["Corner's Edges.id"]-1] = road


def roads_and_tiles(board_data: BoardData, board: Board) -> None:
	roads: Roads = board.roads
	tiles: Settlements = board.tiles

	for roads_tile in board_data.roads_tiles:
		road: Road = find(roads_tile["GamesRoads.id"], roads)
		tile: Tile = find(roads_tile["GamesTiles.id"], tiles)

		road.tiles[roads_tile["Edge's Sides.id"]-1] = tile
		tile.roads[roads_tile["Side's Edges.id"]-1] = road


def robber_and_tile(robber_dict: dict, robber: Robber, tiles: Tiles) -> None:
	tile: Tile = find(robber_dict["TemplatesTiles.id"], tiles)
	robber.tile = tile


def settlements_and_tiles(board_data: BoardData, board: Board) -> None:
	settlements: Ports = board.settlements
	tiles: Settlements = board.tiles

	for settlements_tile in board_data.settlements_tiles:
		settlement: Settlement = find(settlements_tile["GamesSettlements.id"], settlements)
		tile: Tile = find(settlements_tile["GamesTiles.id"], tiles)

		settlement.tiles[settlements_tile["Corner's Sides.id"]-1] = tile
		tile.settlements[settlements_tile["Side's Corners.id"]-1] = settlement
