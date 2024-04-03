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

from board import Border, Corner, Tile


def from_file(filename: str) -> Tuple[list[Border], list[Corner], list[Tile]]:
	with open(filename, "r") as file:
		game_data = json.load(file)

	borders: list[Border] = create.borders(game_data["Borders"])
	corners: list[Corner] = create.corners(game_data["Corners"])
	tiles: list[Tile] = create.tiles(game_data["Tiles"])

	associate.borders_with_corners(game_data["Borders"], borders, corners)
	associate.borders_with_tiles(game_data["Borders"], borders, tiles)

	associate.corners_with_borders(game_data["Corners"], corners, borders)
	associate.corners_with_tiles(game_data["Corners"], corners, tiles)

	associate.tiles_with_borders(game_data["Tiles"], tiles, borders)
	associate.tiles_with_corners(game_data["Tiles"], tiles, corners)

	return borders, corners, tiles
