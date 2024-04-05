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
from typing import Tuple


from setup import associate
from setup import create

from board import Board, Road, Settlement, Tile


def from_dictionary(game_data: str) -> Board:
	ports: list[Road] = create.ports(game_data["Board"]["Ports"])
	roads: list[Road] = create.roads(game_data["Board"]["Roads"])
	settlements: list[Settlement] = create.settlements(game_data["Board"]["Settlements"])
	tiles: list[Tile] = create.tiles(game_data["Board"]["Tiles"])

	associate.ports_with_settlements(game_data["Board"]["Ports"], ports, settlements)

	associate.roads_with_settlements(game_data["Board"]["Roads"], roads, settlements)
	associate.roads_with_tiles(game_data["Board"]["Roads"], roads, tiles)

	associate.settlements_with_ports(game_data["Board"]["Settlements"], settlements, ports)
	associate.settlements_with_roads(game_data["Board"]["Settlements"], settlements, roads)
	associate.settlements_with_tiles(game_data["Board"]["Settlements"], settlements, tiles)

	associate.tiles_with_roads(game_data["Board"]["Tiles"], tiles, roads)
	associate.tiles_with_settlements(game_data["Board"]["Tiles"], tiles, settlements)

	return Board(ports, roads, settlements, tiles)


def from_file(filename: str) -> Board:
	with open(filename, "r") as file:
		game_data = json.load(file)

	return from_dictionary(game_data)
