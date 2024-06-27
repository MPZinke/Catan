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


from database import queries
from game.board import Board
from game.board.template import TemplateData, DictList
from game.board.construct import BoardData
from game.board.new.associate import associate_board_data
from game.board.new.random import ResourceAndValueMapping


def new_board(game_id: int, template_data: TemplateData, resource_and_value_mapping: ResourceAndValueMapping
) -> BoardData:
	port_dicts: DictList = queries.games.new_ports(game_id, resource_and_value_mapping.port_resources_dict)
	road_dicts: DictList = queries.games.new_roads(game_id)
	settlement_dicts: DictList = queries.games.new_settlements(game_id)
	tile_dicts: DictList = queries.games.new_tiles(game_id, resource_and_value_mapping.tile_resources_dict, resource_and_value_mapping.tile_dice_values_dict)

	robber_dict: dict = new_robber(game_id)

	board_data = BoardData(
		id=game_id,
		template_id=template_data.id,
		ports=port_dicts,
		roads=road_dicts,
		robber=robber_dict,
		settlements=settlement_dicts,
		tiles=tile_dicts,
	)

	associate_board_data(board_data, template_data)
	update_board(board_data)

	return board_data


def new_ports(game_id: int, port_dicts: DictList, port_resources_dict: dict) -> DictList:
	game_port_dicts = []

	for port_dict in port_dicts:
		resource_type_id: int = port_resources_dict[port_dict["id"]]
		game_port_dict = queries.games.new_port(game_id, port_dict["id"], resource_type_id)  # pylint: disable=no-value-for-parameter
		game_port_dicts.append(game_port_dict)

	return game_port_dicts


def new_roads(game_id: int, road_dicts: DictList) -> DictList:
	game_road_dicts = []

	for road_dict in road_dicts:
		game_road_dict = queries.games.new_road(game_id, road_dict["id"])  # pylint: disable=no-value-for-parameter
		game_road_dicts.append(game_road_dict)

	return game_road_dicts


def new_robber(game_id: int) -> dict:
	robber_dict: dict = queries.games.new_robber(game_id)  # pylint: disable=no-value-for-parameter
	return robber_dict


def new_settlements(game_id: int, settlement_dicts: DictList) -> DictList:
	game_settlement_dicts = []

	for settlement_dict in settlement_dicts:
		game_settlement_dict = queries.games.new_settlement(game_id, settlement_dict["id"])  # pylint: disable=no-value-for-parameter
		game_settlement_dicts.append(game_settlement_dict)

	return game_settlement_dicts

def new_tiles(game_id: int, tile_dicts: DictList, tile_dice_values_dict: dict, tile_resources_dict: dict) -> DictList:
	game_tile_dicts = []

	for tile_dict in tile_dicts:
		tile_id: int = tile_dict["id"]
		dice_value: int = tile_dice_values_dict[tile_id]
		resource_type_id: int = tile_resources_dict[tile_id]
		game_tile_dict = queries.games.new_tile(game_id, tile_id, resource_type_id, dice_value)  # pylint: disable=no-value-for-parameter

		game_tile_dicts.append(game_tile_dict)

	return game_tile_dicts


def update_board(board_data: BoardData) -> None:
	for port in board_data.ports:
		queries.games.update.update_port_settlements(port["id"], port["GamesSettlements.ids"])

	for road in board_data.roads:
		queries.games.update.update_road_settlements_and_tiles(road["id"], road["GamesSettlements.ids"], road["GamesTiles.ids"])

	for settlement in board_data.settlements:
		queries.games.update.update_settlement_ports_roads_and_tiles(settlement["id"], settlement["GamesPorts.ids"], settlement["GamesRoads.ids"], settlement["GamesTiles.ids"])

	for tile in board_data.tiles:
		queries.games.update.update_tile_roads_and_settlements(tile["id"], tile["GamesRoads.ids"], tile["GamesSettlements.ids"])
