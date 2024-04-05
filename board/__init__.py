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


from board.Board import Board
from board.Port import Port
from board.Road import Road
from board.Settlement import Settlement
from board.Tile import Tile
import setup
from ResourceType import ResourceType


def random_key_from_dictionary_for_available_items(dictionary: Dict[int, int]) -> int:
	keys = list(dictionary.keys())
	key_index = randint(0, len(keys)-1)  # FROM: https://docs.python.org/3/library/random.html#random.randint
	for increment in range(0, len(keys)):
		if(dictionary[keys[(key_index + increment) % len(keys)]] != 0):
			return keys[(key_index + increment) % len(keys)]

	raise IndexError("There are not available items in the provided dictionary.")


def create_basic_board() -> Board:
	with open("BasicLayout.json", "r") as file:
		game_data = json.load(file)

	tile_resources: Dict[str, int] = {key: value["Tiles"] for key, value in game_data["Board"]["Resources"].items()}
	tile_values: Dict[str, int] = game_data["Board"]["values"]
	for tile_dict in game_data["Board"]["Tiles"]:
		tile_dict["type"] = random_key_from_dictionary_for_available_items(tile_resources)
		tile_resources[tile_dict["type"]] -= 1

		if(tile_dict["type"] == ResourceType.DESERT):
			tile_dict["value"] = 0
		else:
			tile_dict["value"] = random_key_from_dictionary_for_available_items(tile_values)
			tile_values[tile_dict["value"]] -= 1

	port_resources: Dict[str, int] = {key: value["Ports"] for key, value in game_data["Board"]["Resources"].items()}
	for port_dict in game_data["Board"]["Ports"]:
		port_dict["type"] = random_key_from_dictionary_for_available_items(port_resources)
		port_resources[port_dict["type"]] -= 1

	return setup.from_dictionary(game_data)
