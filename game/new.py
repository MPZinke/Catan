

from typing import Any, Dict, Tuple, TypeVar
from random import randint


from database.queries import boards
from database.queries import counts
from database.queries import types
from board import Port, Road, Settlement, Tile
from game import associate


Game = TypeVar("Game")


def random_key_from_dictionary_for_available_items(dictionary: Dict[Any, int]) -> int:
	keys = list(dictionary.keys())
	key_index = randint(0, len(keys)-1)  # FROM: https://docs.python.org/3/library/random.html#random.randint
	for increment in range(0, len(keys)):
		key = keys[(key_index + increment) % len(keys)]
		if(dictionary[key] != 0):
			dictionary[key] -= 1
			return key

	raise IndexError("There are not available items in the provided dictionary.")


def new_game(board_id: int) -> Game:
	port_dicts, road_dicts, settlement_dicts, tile_dicts = get_board_parts(board_id)

	ports: list[Port] = create_ports(board_id, port_dicts)
	roads: list[Road] = create_roads(road_dicts)
	settlements: list[Settlement] = create_settlements(settlement_dicts)
	tiles: list[Tile] = create_tiles(board_id, tile_dicts)

	associate_parts(board_id, ports, roads, settlements, tiles)

	return ports, roads, settlements, tiles

	# ports_settlements: list[dict] = boards.get_ports_settlements(board_id)
	# roads_settlements: list[dict] = boards.get_roads_settlements(board_id)
	# roads_tiles: list[dict] = boards.get_roads_tiles(board_id)
	# settlements_tiles: list[dict] = boards.get_settlements_tiles(board_id)


def get_board_parts(board_id: int):
	port_dicts: list[dict] = boards.get_ports(board_id)
	road_dicts: list[dict] = boards.get_roads(board_id)
	settlement_dicts: list[dict] = boards.get_settlements(board_id)
	tile_dicts: list[dict] = boards.get_tiles(board_id)

	return port_dicts, road_dicts, settlement_dicts, tile_dicts


def associate_parts(board_id: int, ports: list[Port], roads: list[Road], settlements: list[Settlement],
	tiles: list[Tile]
) -> None:
	ports_settlements: list[dict] = boards.get_ports_settlements(board_id)
	roads_settlements: list[dict] = boards.get_roads_settlements(board_id)
	roads_tiles: list[dict] = boards.get_roads_tiles(board_id)
	settlements_tiles: list[dict] = boards.get_settlements_tiles(board_id)

	associate.ports_and_settlements(ports_settlements, ports, settlements)
	associate.roads_and_settlements(roads_settlements, roads, settlements)
	associate.roads_and_tiles(roads_tiles, roads, tiles)
	associate.settlements_and_tiles(settlements_tiles, settlements, tiles)


def create_ports(board_id: int, port_dicts: list[dict]) -> list[Port]:
	ports_resource_types_counts_list: list[dict] = counts.get_ports_resource_types_counts(board_id)
	ports_resource_types_counts = {dictionary["ResourceTypes.id"]: dictionary["count"] for dictionary in ports_resource_types_counts_list}
	ports: list[Port] = []
	for port_dict in port_dicts:
		type = random_key_from_dictionary_for_available_items(ports_resource_types_counts)
		ports.append(Port(port_dict["id"], type))

	return ports


def create_roads(road_dicts: list[dict]) -> list[Road]:
	roads: list[Road] = []
	for road_dict in road_dicts:
		roads.append(Road(road_dict["id"]))

	return roads


def create_settlements(settlement_dicts: list[dict]) -> list[Settlement]:
	settlements: list[Settlement] = []
	for settlement_dict in settlement_dicts:
		settlements.append(Settlement(settlement_dict["id"]))

	return settlements


def create_tiles(board_id: int, tile_dicts: list[dict]) -> list[Tile]:
	dice_value_counts_list: list[dict] = counts.get_dice_value_counts(board_id)
	tiles_resource_types_counts_list: list[dict] = counts.get_tiles_resource_types_counts(board_id)

	dice_value_counts = {dictionary["value"]: dictionary["count"] for dictionary in dice_value_counts_list}
	tiles_resource_types_counts = {dictionary["ResourceTypes.id"]: dictionary["count"] for dictionary in tiles_resource_types_counts_list}
	print(tiles_resource_types_counts)
	tiles: list[Tile] = []
	for tile_dict in tile_dicts:
		type = random_key_from_dictionary_for_available_items(tiles_resource_types_counts)
		value = random_key_from_dictionary_for_available_items(dice_value_counts)
		tiles.append(Tile(tile_dict["id"], tile_dict["coordinate"], type-1, value))

	return tiles
