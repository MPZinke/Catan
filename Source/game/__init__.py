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
from game.Game import Game
from game.board import Board
from game.board.construct import construct_board, BoardData
from game.player.Player import Player, Players


def game(game_id: int) -> Game:
	game_dict: dict = queries.games.get_game(game_id)  # pylint: disable=no-value-for-parameter

	port_dicts: list[dict] = queries.games.get_ports(game_id)  # pylint: disable=no-value-for-parameter
	roads_dicts: list[dict] = queries.games.get_roads(game_id)  # pylint: disable=no-value-for-parameter
	settlements_dicts: list[dict] = queries.games.get_settlements(game_id)  # pylint: disable=no-value-for-parameter
	tiles_dicts: list[dict] = queries.games.get_tiles(game_id)  # pylint: disable=no-value-for-parameter
	robber_dict: dict = queries.games.get_robber(game_id)  # pylint: disable=no-value-for-parameter

	# players: list[dict] = queries.games.get_players(game_id)

	board_data = BoardData(
		ports=port_dicts,
		roads=roads_dicts,
		robber=robber_dict,
		settlements=settlements_dicts,
		tiles=tiles_dicts,
	)

	board: Board = construct_board(board_data)
	game = Game(game_dict["id"], board, [])

	return game
