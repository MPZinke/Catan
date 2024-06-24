#!/opt/homebrew/bin/python3
# -*- coding: utf-8 -*-
__author__ = "MPZinke"

########################################################################################################################
#                                                                                                                      #
#   created by: MPZinke                                                                                                #
#   on 2024.04.26                                                                                                      #
#                                                                                                                      #
#   DESCRIPTION: Creates new game items, hence the "create nomenclature".                                              #
#   BUGS:                                                                                                              #
#   FUTURE:                                                                                                            #
#                                                                                                                      #
########################################################################################################################


import database.queries as db
from board import Board, BoardTemplateData, DictList, Tile
from game import BoardData
from game.new.random import ResourceAndValueMapping


def game(board_id: int) -> dict:
	game_dict: dict = db.games.new_game(board_id)  # pylint: disable=no-value-for-parameter
	return game_dict


def game_ports(game_id: int, port_dicts: DictList, port_resources_dict: dict) -> DictList:
	game_port_dicts = []

	for port_dict in port_dicts:
		resource_type_id: int = port_resources_dict[port_dict["id"]]
		game_port_dict = db.games.new_port(game_id, port_dict["id"], resource_type_id)  # pylint: disable=no-value-for-parameter
		game_port_dicts.append(game_port_dict)

	return game_port_dicts


def game_roads(game_id: int, road_dicts: DictList) -> DictList:
	game_road_dicts = []

	for road_dict in road_dicts:
		game_road_dict = db.games.new_road(game_id, road_dict["id"])  # pylint: disable=no-value-for-parameter
		game_road_dicts.append(game_road_dict)

	return game_road_dicts


def game_robber(game_id: int) -> dict:
	robber_dict: dict = db.games.new_robber(game_id)  # pylint: disable=no-value-for-parameter
	return robber_dict


def game_settlements(game_id: int, settlement_dicts: DictList) -> DictList:
	game_settlement_dicts = []

	for settlement_dict in settlement_dicts:
		game_settlement_dict = db.games.new_settlement(game_id,  # pylint: disable=no-value-for-parameter
			settlement_dict["id"]
		)
		game_settlement_dicts.append(game_settlement_dict)

	return game_settlement_dicts

def game_tiles(game_id: int, tile_dicts: DictList, tile_dice_values_dict: dict, tile_resources_dict: dict) -> DictList:
	game_tile_dicts = []

	for tile_dict in tile_dicts:
		tile_id: int = tile_dict["id"]
		dice_value: int = tile_dice_values_dict[tile_id]
		resource_type_id: int = tile_resources_dict[tile_id]
		game_tile_dict = db.games.new_tile(game_id, tile_id, resource_type_id, dice_value)  # pylint: disable=no-value-for-parameter

		game_tile_dicts.append(game_tile_dict)

	return game_tile_dicts


def game_ports_roads_robber_settlements_tiles(board_template_data: BoardTemplateData,
	random_resource_and_value_mapping: ResourceAndValueMapping
) -> BoardData:
	# Create game-board instances.
	game_dict: dict = game(board_template_data.id)
	game_id = game_dict["id"]

	port_dicts: DictList = game_ports(game_id, board_template_data.ports,
		random_resource_and_value_mapping.port_resources_dict
	)
	road_dicts: DictList = game_roads(game_id, board_template_data.roads)
	settlement_dicts: DictList = game_settlements(game_id, board_template_data.settlements)
	tile_dicts: DictList = game_tiles(game_id, board_template_data.tiles,
		random_resource_and_value_mapping.tile_dice_values_dict,
		random_resource_and_value_mapping.tile_resources_dict
	)

	ports_settlements: DictList = db.templates.get_ports_settlements(board_template_data.id)  # pylint: disable=no-value-for-parameter
	roads_settlements: DictList = db.templates.get_roads_settlements(board_template_data.id)  # pylint: disable=no-value-for-parameter
	roads_tiles: DictList = db.templates.get_roads_tiles(board_template_data.id)  # pylint: disable=no-value-for-parameter
	settlements_tiles: DictList = db.templates.get_settlements_tiles(board_template_data.id)  # pylint: disable=no-value-for-parameter

	robber_dict: dict = game_robber(game_id)

	return BoardData(
		id=game_dict["id"],
		board_id=board_template_data.id,
		ports=port_dicts,
		ports_settlements=ports_settlements,
		roads=road_dicts,
		roads_settlements=roads_settlements,
		roads_tiles=roads_tiles,
		robber=robber_dict,
		settlements=settlement_dicts,
		settlements_tiles=settlements_tiles,
		tiles=tile_dicts,
	)
