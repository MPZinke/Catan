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
from board import Board, BoardTemplateData, Port, Ports, Road, Roads, Settlement, Settlements, Tile, Tiles
from board import construct
from game import BoardData
from game.new import create, random
from game.new.random import ResourceAndValueMapping


DictList = list[dict]
Game = TypeVar("Game")


def new_game(board_template_id: int) -> Game:
	# Get board layout.
	board_template_data: BoardTemplateData = board_port_road_settlement_and_tile_dicts(board_template_id)
	random_resource_and_value_mappings: ResourceAndValueMapping = random.resources_and_values(board_template_data)

	# Create objects.
	board_data: BoardData = create.game_ports_roads_robber_settlements_tiles(board_template_data,
		random_resource_and_value_mappings
	)
	board: Board = construct.board(board_data)

	return board


def board_port_road_settlement_and_tile_dicts(board_id: int) -> BoardTemplateData:
	name: str = db.templates.get_template(board_id)["name"]  # pylint: disable=no-value-for-parameter
	ports: DictList = db.templates.get_ports(board_id)  # pylint: disable=no-value-for-parameter
	roads: DictList = db.templates.get_roads(board_id)  # pylint: disable=no-value-for-parameter
	settlements: DictList = db.templates.get_settlements(board_id)  # pylint: disable=no-value-for-parameter
	tiles: DictList = db.templates.get_tiles(board_id)  # pylint: disable=no-value-for-parameter

	return BoardTemplateData(board_id, name, ports, roads, settlements, tiles)
