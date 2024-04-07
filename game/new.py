

from typing import Dict, TypeVar
from random import randint


from database.queries import boards
from database.queries import counts
from database.queries import types


Game = TypeVar("Game")


def random_key_from_dictionary_for_available_items(dictionary: Dict[int, int]) -> int:
	keys = list(dictionary.keys())
	key_index = randint(0, len(keys)-1)  # FROM: https://docs.python.org/3/library/random.html#random.randint
	for increment in range(0, len(keys)):
		if(dictionary[keys[(key_index + increment) % len(keys)]] != 0):
			return keys[(key_index + increment) % len(keys)]

	raise IndexError("There are not available items in the provided dictionary.")


def new_game(board_id: int) -> Game:
	resource_types: list[dict] = types.get_resource_types()
	settlement_types: list[dict] = types.get_settlement_types()

	tile_resources: list[dict] = counts.get_tile_resources(board_id)
	tile_values: list[dict] = counts.get_tile_values(board_id)

	port_dicts: list[dict] = boards.get_ports(board_id)
	road_dicts: list[dict] = boards.get_roads(board_id)
	settlement_dicts: list[dict] = boards.get_settlements(board_id)
	tile_dicts: list[dict] = boards.get_tiles(board_id)
	ports_settlements: list[dict] = boards.get_ports_settlements(board_id)
	roads_settlements: list[dict] = boards.get_roads_settlements(board_id)
	roads_tiles: list[dict] = boards.get_roads_tiles(board_id)
	settlements_tiles: list[dict] = boards.get_settlements_tiles(board_id)


# def create_ports(port_dicts: list[dict]) -> list[Ports]:
# 	ports: list[Port] = []
# 	for port_dict in port_dicts:
# 		Port(port_dict)
