#!/opt/homebrew/bin/python3
# -*- coding: utf-8 -*-
__author__ = "MPZinke"

########################################################################################################################
#                                                                                                                      #
#   created by: MPZinke                                                                                                #
#   on 2024.04.27                                                                                                      #
#                                                                                                                      #
#   DESCRIPTION:                                                                                                       #
#   BUGS:                                                                                                              #
#   FUTURE:                                                                                                            #
#                                                                                                                      #
########################################################################################################################


from database import queries
from game import new
from game.Game import Game
from game.board import get_board, Board
from game.board.construct import construct_board, BoardData
from game.player.Player import Player, Players


def get_game(game_id: int) -> Game:
	board: Board = get_board(game_id)

	game_dict: dict = queries.games.get_game(game_id)  # pylint: disable=no-value-for-parameter
	game = Game(game_dict["id"], board, [], game_dict["started"], game_dict["finished"])

	return game
