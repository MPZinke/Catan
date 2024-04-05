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

from board import Road, Settlement, Tile


def from_file(filename: str) -> Tuple[list[Road], list[Settlement], list[Tile]]:
	with open(filename, "r") as file:
		game_data = json.load(file)

	ports: list[Road] = create.ports(game_data["Ports"])
	roads: list[Road] = create.roads(game_data["Roads"])
	settlements: list[Settlement] = create.settlements(game_data["Settlements"])
	tiles: list[Tile] = create.tiles(game_data["Tiles"])

	associate.ports_with_settlements(game_data["Ports"], ports, settlements)

	associate.roads_with_settlements(game_data["Roads"], roads, settlements)
	associate.roads_with_tiles(game_data["Roads"], roads, tiles)

	associate.settlements_with_ports(game_data["Settlements"], settlements, ports)
	associate.settlements_with_roads(game_data["Settlements"], settlements, roads)
	associate.settlements_with_tiles(game_data["Settlements"], settlements, tiles)

	associate.tiles_with_roads(game_data["Tiles"], tiles, roads)
	associate.tiles_with_settlements(game_data["Tiles"], tiles, settlements)

	return roads, settlements, tiles
