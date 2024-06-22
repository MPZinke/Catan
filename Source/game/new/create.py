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
from board import Board, BoardData, DictList, Tile
from game import GameData
from game.new.random import RandomResourceAndValueMapping


def game(board_id: int) -> dict:
	game_dict: dict = db.games.new_game(board_id)  # pylint: disable=no-value-for-parameter
	return game_dict


def game_ports(game_id: int, port_dicts: list[dict]) -> list[dict]:
	game_port_dicts = []

	for port_dict in port_dicts:
		game_port_dict = db.games.new_port(game_id, port_dict["id"],  # pylint: disable=no-value-for-parameter
			port_dict["ResourceTypes.id"]
		)
		game_port_dicts.append(game_port_dict)

	return game_port_dicts


def game_roads(game_id: int, road_dicts: list[dict]) -> list[dict]:
	game_road_dicts = []

	for road_dict in road_dicts:
		game_road_dict = db.games.new_road(game_id, road_dict["id"])  # pylint: disable=no-value-for-parameter
		game_road_dicts.append(game_road_dict)

	return game_road_dicts


def game_robber(game_id: int, game_tile_id: int) -> dict:
	robber_dict: dict = db.games.new_robber(game_id, game_tile_id)  # pylint: disable=no-value-for-parameter
	return robber_dict


def game_settlements(game_id: int, settlement_dicts: list[dict]) -> list[dict]:
	game_settlement_dicts = []

	for settlement_dict in settlement_dicts:
		game_settlement_dict = db.games.new_settlement(game_id,  # pylint: disable=no-value-for-parameter
			settlement_dict["id"]
		)
		game_settlement_dicts.append(game_settlement_dict)

	return game_settlement_dicts

def game_tiles(game_id: int, tile_dicts: list[dict]) -> list[dict]:
	game_tile_dicts = []

	for tile_dict in tile_dicts:
		game_tile_dict = db.games.new_tile(game_id, tile_dict["id"],  # pylint: disable=no-value-for-parameter
			tile_dict["ResourceTypes.id"], tile_dict["value"]
		)
		game_tile_dicts.append(game_tile_dict)

	return game_tile_dicts


def game_ports_roads_robber_settlements_tiles(board_data: BoardData,
	random_resource_and_value_mapping: RandomResourceAndValueMapping
) -> GameData:
	# Create game-board instances.
	game_dict: dict = game(board_data.id)
	game_id = game_dict["id"]

	port_dicts: DictList = game_ports(game_id, board_data.port)
	road_dicts: DictList = game_roads(game_id, board_data.road)
	settlement_dicts: DictList = game_settlements(game_id, board_data.settlement)
	tile_dicts: DictList = game_tiles(game_id, board_data.tile)

	robber_tile_id = next(filter(lambda tile: tile.type == Tile.ResourceTypes.DESERT, tile_dicts))["id"]
	robber_dict: dict = game_robber(game_id, robber_tile_id)

	return GameData(game_dict["id"], game_dict["name"], port_dicts, road_dicts, robber_dict, settlement_dicts,
		tile_dicts
	)
