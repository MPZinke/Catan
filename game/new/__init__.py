#!/opt/homebrew/bin/python3
# -*- coding: utf-8 -*-
__author__ = "MPZinke"

########################################################################################################################
#                                                                                                                      #
#   created by: MPZinke                                                                                                #
#   on 2024.04.26                                                                                                      #
#                                                                                                                      #
#   DESCRIPTION:                                                                                                       #
#   BUGS:                                                                                                              #
#   FUTURE:                                                                                                            #
#                                                                                                                      #
########################################################################################################################


from typing import Any, Dict, Tuple, TypeVar
from random import randint


import database.queries as db
from board import Board, Port, Ports, Road, Roads, Settlement, Settlements, Tile, Tiles
from game import associate, parts
from game.new import create


DictList = list[dict]
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
	port_dicts: DictList = db.boards.get_ports(board_id)
	road_dicts: DictList = db.boards.get_roads(board_id)
	settlement_dicts: DictList = db.boards.get_settlements(board_id)
	tile_dicts: DictList = db.boards.get_tiles(board_id)

	assign_port_dicts_random_resources(board_id, port_dicts)
	assign_tile_dicts_random_resources_and_dice_values(board_id, tile_dicts)

	game_dict: dict = create.game(board_id)
	game_id = game_dict["id"]

	game_port_dicts: DictList = create.game_ports(game_id, port_dicts)
	game_road_dicts: DictList = create.game_roads(game_id, road_dicts)
	game_settlement_dicts: DictList = create.game_settlements(game_id, settlement_dicts)
	game_tile_dicts: DictList = create.game_tiles(game_id, tile_dicts)

	ports: Ports = parts.ports(game_port_dicts)
	roads: Roads = parts.roads(game_road_dicts)
	settlements: Settlements = parts.settlements(game_settlement_dicts)
	tiles: Tiles = parts.tiles(game_tile_dicts)

	associate.ports_and_settlements(board_id, game_port_dicts, ports, game_settlement_dicts, settlements)
	associate.roads_and_settlements(board_id, game_road_dicts, roads, game_settlement_dicts, settlements)
	associate.roads_and_tiles(board_id, game_road_dicts, roads, game_tile_dicts, tiles)
	associate.settlements_and_tiles(board_id, game_settlement_dicts, settlements, game_tile_dicts, tiles)

	return Board(ports, roads, settlements, tiles)


def assign_port_dicts_random_resources(board_id: int, port_dicts: DictList) -> None:
	ports_resource_types_counts_list: DictList = db.counts.get_ports_resource_types_counts(board_id)
	ports_resource_types_counts = {dictionary["ResourceTypes.id"]: dictionary["count"]
		for dictionary in ports_resource_types_counts_list
	}
	print(ports_resource_types_counts)
	for port_dict in port_dicts:
		port_dict["ResourceTypes.id"] = random_key_from_dictionary_for_available_items(ports_resource_types_counts)


def assign_tile_dicts_random_resources_and_dice_values(board_id: int, tile_dicts: DictList) -> None:
	dice_value_counts_list: DictList = db.counts.get_dice_value_counts(board_id)
	tiles_resource_types_counts_list: DictList = db.counts.get_tiles_resource_types_counts(board_id)

	dice_value_counts = {dictionary["value"]: dictionary["count"] for dictionary in dice_value_counts_list}
	tiles_resource_types_counts = {dictionary["ResourceTypes.id"]: dictionary["count"]
		for dictionary in tiles_resource_types_counts_list
	}

	for tile_dict in tile_dicts:
		tile_dict["ResourceTypes.id"] = random_key_from_dictionary_for_available_items(tiles_resource_types_counts)
		tile_dict["value"] = random_key_from_dictionary_for_available_items(dice_value_counts)
