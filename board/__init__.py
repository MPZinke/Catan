#!/opt/homebrew/bin/python3
# -*- coding: utf-8 -*-
__author__ = "MPZinke"

########################################################################################################################
#                                                                                                                      #
#   created by: MPZinke                                                                                                #
#   on 2024.04.02                                                                                                      #
#                                                                                                                      #
#   DESCRIPTION:                                                                                                       #
#   BUGS:                                                                                                              #
#   FUTURE:                                                                                                            #
#                                                                                                                      #
########################################################################################################################


import json
from random import randint
from typing import Dict


from board.Road import Road
from board.Settlement import Settlement
from board.Tile import Tile
from board.Port import Port
from setup import associate, create
from ResourceType import ResourceType


def random_key_from_dictionary_for_available_items(dictionary: Dict[int, int]) -> int:
	keys = list(dictionary.keys())
	key_index = randint(0, len(keys)-1)
	for increment in range(0, len(keys)):
		if(dictionary[keys[(key_index + increment) % len(keys)]] != 0):
			return keys[(key_index + increment) % len(keys)]

	raise IndexError("There are not available items in the provided dictionary.")


def create_basic_board():
	with open("BasicLayout.json", "r") as file:
		layout = json.load(file)

	port_types = {
		Port.Types.ENUM_KEYS[Port.Types.WHEAT]: 1,
		Port.Types.ENUM_KEYS[Port.Types.WOOD]: 1,
		Port.Types.ENUM_KEYS[Port.Types.SHEEP]: 1,
		Port.Types.ENUM_KEYS[Port.Types.STONE]: 1,
		Port.Types.ENUM_KEYS[Port.Types.BRICK]: 1,
		Port.Types.ENUM_KEYS[Port.Types.ANY]: 4
	}
	tile_types = {
		ResourceType.ENUM_KEYS[ResourceType.DESERT]: 1,
		ResourceType.ENUM_KEYS[ResourceType.WHEAT]: 4,
		ResourceType.ENUM_KEYS[ResourceType.WOOD]: 4,
		ResourceType.ENUM_KEYS[ResourceType.SHEEP]: 4,
		ResourceType.ENUM_KEYS[ResourceType.STONE]: 3,
		ResourceType.ENUM_KEYS[ResourceType.BRICK]: 3
	}
	values = {
		2: 1,
		3: 2,
		4: 2,
		5: 2,
		6: 2,
		7: 2,
		8: 2,
		9: 2,
		10: 2,
		11: 2,
		12: 1,
	}

	for tile_dict in layout["Tiles"]:
		tile_dict["type"] = random_key_from_dictionary_for_available_items(tile_types)
		tile_types[tile_dict["type"]] -= 1

		if(tile_dict["type"] == ResourceType.DESERT):
			tile_dict["value"] = 0
		else:
			tile_dict["value"] = random_key_from_dictionary_for_available_items(values)
			values[tile_dict["value"]] -= 1

	for port_dict in layout["Ports"]:
		port_dict["type"] = random_key_from_dictionary_for_available_items(port_types)
		port_types[port_dict["type"]] -= 1

	ports: list[Road] = create.ports(layout["Ports"])
	roads: list[Road] = create.roads(layout["Roads"])
	settlements: list[Settlement] = create.settlements(layout["Settlements"])
	tiles: list[Tile] = create.tiles(layout["Tiles"])

	associate.ports_with_settlements(layout["Ports"], ports, settlements)

	associate.roads_with_settlements(layout["Roads"], roads, settlements)
	associate.roads_with_tiles(layout["Roads"], roads, tiles)

	associate.settlements_with_ports(layout["Settlements"], settlements, ports)
	associate.settlements_with_roads(layout["Settlements"], settlements, roads)
	associate.settlements_with_tiles(layout["Settlements"], settlements, tiles)

	associate.tiles_with_roads(layout["Tiles"], tiles, roads)
	associate.tiles_with_settlements(layout["Tiles"], tiles, settlements)

	return roads, settlements, tiles
