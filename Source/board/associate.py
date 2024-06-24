

from typing import Dict


from board import Board, Port, Ports, Road, Roads, Robber, Settlement, Settlements, Tile, Tiles
import database.queries as db
from game import BoardData


BoardPartID = int
DictList = list[dict]
GamePartID = int
BoardPartIDGamePartIDMapping = Dict[BoardPartID, GamePartID]


def find(id: int) -> callable:
	def callback(item: object) -> bool:
		return item.id == id

	return callback


def map_board_part_id_to_game_part_id(part_dicts: DictList, board_part_id_key: str) -> BoardPartIDGamePartIDMapping:
	mapping: BoardPartIDGamePartIDMapping = {game_part[board_part_id_key]: game_part["id"] for game_part in part_dicts}
	return mapping


def board_parts(board_data: BoardData, board: Board) -> None:
	ports_and_settlements(board_data, board)
	roads_and_settlements(board_data, board)
	roads_and_tiles(board_data, board)
	settlements_and_tiles(board_data, board)


def ports_and_settlements(board_data: BoardData, board: Board) -> None:
	port_dicts: DictList = board_data.ports
	settlement_dicts: DictList = board_data.settlements
	ports_settlements: DictList = board_data.ports_settlements

	ports: Ports = board.ports
	settlements: Settlements = board.settlements

	ports_board_game_mapping: BoardPartIDGamePartIDMapping = map_board_part_id_to_game_part_id(port_dicts, "TemplatesPorts.id")
	settlements_board_game_mapping: BoardPartIDGamePartIDMapping = map_board_part_id_to_game_part_id(settlement_dicts,
		"TemplatesSettlements.id"
	)

	for ports_settlement in ports_settlements:
		game_port_id: int = ports_board_game_mapping[ports_settlement["TemplatesPorts.id"]]
		game_settlement_id: int = settlements_board_game_mapping[ports_settlement["TemplatesSettlements.id"]]

		port: Port = next(filter(find(game_port_id), ports))
		settlement: Settlement = next(filter(find(game_settlement_id), settlements))

		port.settlements[ports_settlement["Side's Corners.id"]-1] = settlement
		settlement.ports[ports_settlement["Corner's Sides.id"]-1] = port


def roads_and_settlements(board_data: BoardData, board: Board) -> None:
	road_dicts: DictList = board_data.roads
	settlement_dicts: DictList = board_data.settlements
	roads_settlements: DictList = board_data.roads_settlements

	roads: Ports = board.roads
	settlements: Settlements = board.settlements

	roads_board_game_mapping: BoardPartIDGamePartIDMapping = map_board_part_id_to_game_part_id(road_dicts, "TemplatesRoads.id")
	settlements_board_game_mapping: BoardPartIDGamePartIDMapping = map_board_part_id_to_game_part_id(settlement_dicts,
		"TemplatesSettlements.id"
	)

	for roads_settlement in roads_settlements:
		game_road_id: int = roads_board_game_mapping[roads_settlement["TemplatesRoads.id"]]
		game_settlement_id: int = settlements_board_game_mapping[roads_settlement["TemplatesSettlements.id"]]

		road = next(filter(find(game_road_id), roads))
		settlement = next(filter(find(game_settlement_id), settlements))

		road.settlements[roads_settlement["Edge's Corners.id"]-1] = settlement
		settlement.roads[roads_settlement["Corner's Edges.id"]-1] = road


def roads_and_tiles(board_data: BoardData, board: Board) -> None:
	road_dicts: DictList = board_data.roads
	tile_dicts: DictList = board_data.tiles
	roads_tiles: DictList = board_data.roads_tiles

	roads: Ports = board.roads
	tiles: Settlements = board.tiles

	roads_board_game_mapping: BoardPartIDGamePartIDMapping = map_board_part_id_to_game_part_id(road_dicts, "TemplatesRoads.id")
	tiles_board_game_mapping: BoardPartIDGamePartIDMapping = map_board_part_id_to_game_part_id(tile_dicts, "TemplatesTiles.id")

	for roads_tile in roads_tiles:
		game_road_id: int = roads_board_game_mapping[roads_tile["TemplatesRoads.id"]]
		game_tile_id: int = tiles_board_game_mapping[roads_tile["TemplatesTiles.id"]]

		road: Road = next(filter(find(game_road_id), roads))
		tile: Tile = next(filter(find(game_tile_id), tiles))

		road.tiles[roads_tile["Edge's Sides.id"]-1] = tile
		tile.roads[roads_tile["Side's Edges.id"]-1] = road


def robber_and_tile(robber_dict: dict, robber: Robber, tiles: Tiles) -> None:
	tile: Tile = next(filter(find(robber_dict["TemplatesTiles.id"]), tiles))
	robber.tile = tile


def settlements_and_tiles(board_data: BoardData, board: Board) -> None:
	settlement_dicts: DictList = board_data.settlements
	tile_dicts: DictList = board_data.tiles
	settlements_tiles: DictList = board_data.settlements_tiles

	settlements: Ports = board.settlements
	tiles: Settlements = board.tiles

	settlements_board_game_mapping: BoardPartIDGamePartIDMapping = map_board_part_id_to_game_part_id(settlement_dicts,
		"TemplatesSettlements.id"
	)
	tiles_board_game_mapping: BoardPartIDGamePartIDMapping = map_board_part_id_to_game_part_id(tile_dicts, "TemplatesTiles.id")

	for settlements_tile in settlements_tiles:
		game_settlement_id: int = settlements_board_game_mapping[settlements_tile["TemplatesSettlements.id"]]
		game_tile_id: int = tiles_board_game_mapping[settlements_tile["TemplatesTiles.id"]]

		settlement: Settlement = next(filter(find(game_settlement_id), settlements))
		tile: Tile = next(filter(find(game_tile_id), tiles))

		settlement.tiles[settlements_tile["Corner's Sides.id"]-1] = tile
		tile.settlements[settlements_tile["Side's Corners.id"]-1] = settlement
