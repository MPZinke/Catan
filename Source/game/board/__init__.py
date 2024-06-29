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




from game.board.Board import Board
from game.board.Port import Port, Ports
from game.board.Road import Road, Roads
from game.board.Robber import Robber
from game.board.Settlement import Settlement, Settlements
from game.board.Tile import Tile, Tiles


def get_board(game_id: int) -> Board:
	from database import queries
	from game.board.construct import construct_board, BoardData

	board_dict: dict = queries.games.get_board(game_id)  # pylint: disable=no-value-for-parameter
	board_id: int = board_dict["id"]

	port_dicts: list[dict] = queries.games.get_ports(board_id)  # pylint: disable=no-value-for-parameter
	roads_dicts: list[dict] = queries.games.get_roads(board_id)  # pylint: disable=no-value-for-parameter
	settlements_dicts: list[dict] = queries.games.get_settlements(board_id)  # pylint: disable=no-value-for-parameter
	tiles_dicts: list[dict] = queries.games.get_tiles(board_id)  # pylint: disable=no-value-for-parameter
	robber_dict: dict = queries.games.get_robber(board_id)  # pylint: disable=no-value-for-parameter

	board_data = BoardData(
		id=board_dict["id"],
		size=board_dict["size"],
		game_id=board_dict["Games.id"],
		template_id=board_dict["Templates.id"],
		ports=port_dicts,
		roads=roads_dicts,
		robber=robber_dict,
		settlements=settlements_dicts,
		tiles=tiles_dicts,
	)

	board: Board = construct_board(board_data)

	return board
