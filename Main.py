#!/opt/homebrew/bin/python3
# -*- coding: utf-8 -*-
__author__ = "MPZinke"

########################################################################################################################
#                                                                                                                      #
#   created by: MPZinke                                                                                                #
#   on 2024.04.01                                                                                                      #
#                                                                                                                      #
#   DESCRIPTION:                                                                                                       #
#   BUGS:                                                                                                              #
#   FUTURE:                                                                                                            #
#                                                                                                                      #
########################################################################################################################


import json
from typing import Tuple


import setup
from board import Border
from board import Corner
from board import Tile


def main():
	borders: list[Border]
	corners: list[Corner]
	tiles: list[Tile]
	borders, corners, tiles = setup.from_file("GameData.json")

	for tile in tiles:
		print(str(tile))
		print(dict(tile))


if(__name__ == "__main__"):
	main()
