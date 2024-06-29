#!/opt/homebrew/bin/python3
# -*- coding: utf-8 -*-
__author__ = "MPZinke"

########################################################################################################################
#                                                                                                                      #
#   created by: MPZinke                                                                                                #
#   on 2024.06.24                                                                                                      #
#                                                                                                                      #
#   DESCRIPTION:                                                                                                       #
#   BUGS:                                                                                                              #
#   FUTURE:                                                                                                            #
#                                                                                                                      #
########################################################################################################################


from database import queries
import game
from game import Game
from game.board import template, Board
from game.board.construct import construct_board, BoardData
from game.board.new import new_board
from game.board.new.random import random_resources_and_values, ResourceAndValueMapping
from game.board.template import TemplateData


def new_game(template_id: int) -> Game:
	template_data: TemplateData = game.board.template.template_data(template_id)

	game_dict: dict = queries.games.new_game()  # pylint: disable=no-value-for-parameter
	game_id: int = game_dict["id"]

	random_resource_and_value_mapping: ResourceAndValueMapping = random_resources_and_values(template_data)
	board_data: BoardData = new_board(game_id, template_data, random_resource_and_value_mapping)  # pylint: disable=no-value-for-parameter

	board: Board = construct_board(board_data)

	return Game(game_id, board, [], game_dict["started"], game_dict["finished"])
