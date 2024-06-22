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
from board import Board, BoardData, Port, Ports, Road, Roads, Settlement, Settlements, Tile, Tiles
from game import associate, parts, GameData
from game.new import create, random
from game.new.random import RandomResourceAndValueMapping


DictList = list[dict]
Game = TypeVar("Game")

def new_game(board_id: int) -> Game:
	# Get board layout.
	board_data: BoardData = board_port_road_settlement_and_tile_dicts(board_id)
	random_resource_and_value_mapping: RandomResourceAndValueMapping = random.resources_and_values(board_data)

	# Create objects.
	game_data: GameData = create.game_ports_roads_robber_settlements_tiles(board_data,
		random_resource_and_value_mapping
	)
	board: Board = parts.instantiate_parts(game_data)
	associate.board_parts(board_id, game_data, board)

	return board


def board_port_road_settlement_and_tile_dicts(board_id: int) -> BoardData:
	name: str = db.boards.get_board(board_id)["name"]  # pylint: disable=no-value-for-parameter
	ports: DictList = db.boards.get_ports(board_id)  # pylint: disable=no-value-for-parameter
	roads: DictList = db.boards.get_roads(board_id)  # pylint: disable=no-value-for-parameter
	settlements: DictList = db.boards.get_settlements(board_id)  # pylint: disable=no-value-for-parameter
	tiles: DictList = db.boards.get_tiles(board_id)  # pylint: disable=no-value-for-parameter

	return BoardData(board_id, name, ports, roads, settlements, tiles)
