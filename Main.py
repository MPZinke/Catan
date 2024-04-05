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


import gui
import setup
import board
from board import Road
from board import Settlement
from board import Tile
from board.Port import Port


def main():
	roads: list[Road]
	settlements: list[Settlement]
	tiles: list[Tile]
	roads, settlements, tiles = board.create_basic_board()
	gui.draw_tiles(tiles)

	print(Port.Type.items())
	# for tile in tiles:
	# 	print(str(tile))
	# 	print(dict(tile))


if(__name__ == "__main__"):
	main()
