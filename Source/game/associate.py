

from typing import Dict


from board import Board, Port, Ports, Road, Roads, Robber, Settlement, Settlements, Tile, Tiles
import database.queries as db
from game import GameData


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


def board_parts(board_id: int, game_data: GameData, board: Board) -> None:
	ports_and_settlements(board_id, game_data.ports, board.ports, game_data.settlements, board.settlements)
	roads_and_settlements(board_id, game_data.roads, board.roads, game_data.settlements, board.settlements)
	roads_and_tiles(board_id, game_data.roads, board.roads, game_data.tiles, board.tiles)
	settlements_and_tiles(board_id, game_data.settlements, board.settlements, game_data.tiles, board.tiles)


def ports_and_settlements(board_id: int, port_dicts: DictList, ports: Ports, settlement_dicts: DictList,
	settlements: Settlements
) -> None:
	ports_settlements: DictList = db.boards.get_ports_settlements(board_id)  # pylint: disable=no-value-for-parameter

	ports_board_game_mapping: BoardPartIDGamePartIDMapping = map_board_part_id_to_game_part_id(port_dicts, "Ports.id")
	settlements_board_game_mapping: BoardPartIDGamePartIDMapping = map_board_part_id_to_game_part_id(settlement_dicts,
		"Settlements.id"
	)

	for ports_settlement in ports_settlements:
		game_port_id: int = ports_board_game_mapping[ports_settlement["Ports.id"]]
		game_settlement_id: int = settlements_board_game_mapping[ports_settlement["Settlements.id"]]

		port: Port = next(filter(find(game_port_id), ports))
		settlement: Settlement = next(filter(find(game_settlement_id), settlements))

		port.settlements[ports_settlement["Side's Corners.id"]-1] = settlement
		settlement.ports[ports_settlement["Corner's Sides.id"]-1] = port


def roads_and_settlements(board_id: int, road_dicts: DictList, roads: Roads, settlement_dicts: DictList,
	settlements: Settlements
) -> None:
	roads_settlements: DictList = db.boards.get_roads_settlements(board_id)  # pylint: disable=no-value-for-parameter

	roads_board_game_mapping: BoardPartIDGamePartIDMapping = map_board_part_id_to_game_part_id(road_dicts, "Roads.id")
	settlements_board_game_mapping: BoardPartIDGamePartIDMapping = map_board_part_id_to_game_part_id(settlement_dicts,
		"Settlements.id"
	)

	for roads_settlement in roads_settlements:
		game_road_id: int = roads_board_game_mapping[roads_settlement["Roads.id"]]
		game_settlement_id: int = settlements_board_game_mapping[roads_settlement["Settlements.id"]]

		road = next(filter(find(game_road_id), roads))
		settlement = next(filter(find(game_settlement_id), settlements))

		road.settlements[roads_settlement["Edge's Corners.id"]-1] = settlement
		settlement.roads[roads_settlement["Corner's Edges.id"]-1] = road


def roads_and_tiles(board_id: int, road_dicts: DictList, roads: Roads, tile_dicts: DictList, tiles: Tiles) -> None:
	roads_tiles: DictList = db.boards.get_roads_tiles(board_id)  # pylint: disable=no-value-for-parameter

	roads_board_game_mapping: BoardPartIDGamePartIDMapping = map_board_part_id_to_game_part_id(road_dicts, "Roads.id")
	tiles_board_game_mapping: BoardPartIDGamePartIDMapping = map_board_part_id_to_game_part_id(tile_dicts, "Tiles.id")

	for roads_tile in roads_tiles:
		game_road_id: int = roads_board_game_mapping[roads_tile["Roads.id"]]
		game_tile_id: int = tiles_board_game_mapping[roads_tile["Tiles.id"]]

		road: Road = next(filter(find(game_road_id), roads))
		tile: Tile = next(filter(find(game_tile_id), tiles))

		road.tiles[roads_tile["Edge's Sides.id"]-1] = tile
		tile.roads[roads_tile["Side's Edges.id"]-1] = road


def robber_and_tile(robber_dict: dict, robber: Robber, tiles: Tiles) -> None:
	tile: Tile = next(filter(find(robber_dict["Tiles.id"]), tiles))
	robber.tile = tile


def settlements_and_tiles(board_id: int, settlement_dicts: DictList, settlements: Settlements, tile_dicts: DictList,
	tiles: Tiles
) -> None:
	settlements_tiles: DictList = db.boards.get_settlements_tiles(board_id)  # pylint: disable=no-value-for-parameter

	settlements_board_game_mapping: BoardPartIDGamePartIDMapping = map_board_part_id_to_game_part_id(settlement_dicts,
		"Settlements.id"
	)
	tiles_board_game_mapping: BoardPartIDGamePartIDMapping = map_board_part_id_to_game_part_id(tile_dicts, "Tiles.id")

	for settlements_tile in settlements_tiles:
		game_settlement_id: int = settlements_board_game_mapping[settlements_tile["Settlements.id"]]
		game_tile_id: int = tiles_board_game_mapping[settlements_tile["Tiles.id"]]

		settlement: Settlement = next(filter(find(game_settlement_id), settlements))
		tile: Tile = next(filter(find(game_tile_id), tiles))

		settlement.tiles[settlements_tile["Corner's Sides.id"]-1] = tile
		tile.settlements[settlements_tile["Side's Corners.id"]-1] = settlement
