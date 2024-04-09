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


import gui
from game.new import new_game


def main():
	board_id = 1
	ports, roads, settlements, tiles = new_game(board_id)
	ports_strings = list(map(str, ports))
	roads_strings = list(map(str, roads))
	settlements_strings = list(map(str, settlements))
	tiles_strings = list(map(str, tiles))

	print(
		"\n".join(ports_strings),
		"\n".join(roads_strings),
		"\n".join(settlements_strings),
		"\n".join(tiles_strings)
	)

	gui.draw_tiles(tiles)


if(__name__ == "__main__"):
	main()
