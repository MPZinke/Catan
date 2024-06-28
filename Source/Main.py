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
import game
from game.new import new_game


def main():
	template_id = 1
	game = new_game(template_id)
	board = game.board
	ports, roads, settlements, tiles = board.ports, board.roads, board.settlements, board.tiles
	ports_strings = list(map(str, ports))
	roads_strings = list(map(str, roads))
	settlements_strings = list(map(str, settlements))
	tiles_strings = list(map(str, tiles))
	print(tiles[0].settlements[tiles[0].Settlements.TOP_LEFT])
	print(
		"\n".join(ports_strings),
		"\n".join(roads_strings),
		"\n".join(settlements_strings),
		"\n".join(tiles_strings)
	)

	gui.draw_tiles(tiles)
# def main():
# 	current_game: Game = game.game(1)
# 	board = current_game.board
# 	print(dir(board))
# 	ports, roads, settlements, tiles = board.ports, board.roads, board.settlements, board.tiles
# 	ports_strings = list(map(str, ports))
# 	roads_strings = list(map(str, roads))
# 	settlements_strings = list(map(str, settlements))
# 	tiles_strings = list(map(str, tiles))
# 	print(tiles[0].settlements[tiles[0].Settlements.TOP_LEFT])
# 	print(
# 		"\n".join(ports_strings),
# 		"\n".join(roads_strings),
# 		"\n".join(settlements_strings),
# 		"\n".join(tiles_strings)
# 	)


if(__name__ == "__main__"):
	main()
