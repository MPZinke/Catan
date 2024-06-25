#!/opt/homebrew/bin/python3
# -*- coding: utf-8 -*-
__author__ = "MPZinke"

########################################################################################################################
#                                                                                                                      #
#   created by: MPZinke                                                                                                #
#   on 2024.04.26                                                                                                      #
#                                                                                                                      #
#   DESCRIPTION:                                                                                                       #
#   BUGS:                                                                                                              #
#   FUTURE:                                                                                                            #
#                                                                                                                      #
########################################################################################################################


from typing import Any, Dict, Tuple, TypeVar
from random import randint


import database.queries as db
from board import Board, Port, Ports, Road, Roads, Settlement, Settlements, Tile, Tiles
from board.template_data import template_data, TemplateData
from board.construct import BoardData, board
from game.new import board, random
from game.new.random import ResourceAndValueMapping


DictList = list[dict]
Game = TypeVar("Game")


def new_game(template_id: int) -> Game:
	# Get board layout.
	board_template_data: TemplateData = template_data(template_id)
	random_resource_and_value_mappings: ResourceAndValueMapping = random.resources_and_values(board_template_data)

	# Create objects.
	board_data: BoardData = board.new_board(board_template_data, random_resource_and_value_mappings)
	board: Board = construct.board(board_data)

	return board



def _new_game(template_id: int) -> dict:
	game_dict: dict = db.games.new_game(template_id)  # pylint: disable=no-value-for-parameter
	return game_dict
