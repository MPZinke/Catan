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


import database.queries as db


def game(board_id: int) -> dict:
	game_dict: dict = db.games.new_game(board_id)
	return game_dict


def game_ports(game_id: int, port_dicts: list[dict]) -> list[dict]:
	game_port_dicts = []

	for port_dict in port_dicts:
		game_port_dict = db.games.new_port(game_id, port_dict["id"], port_dict["ResourceTypes.id"])
		game_port_dicts.append(game_port_dict)

	return game_port_dicts

def game_roads(game_id: int, road_dicts: list[dict]) -> list[dict]:
	game_road_dicts = []

	for road_dict in road_dicts:
		game_road_dict = db.games.new_road(game_id, road_dict["id"])
		game_road_dicts.append(game_road_dict)

	return game_road_dicts

def game_settlements(game_id: int, settlement_dicts: list[dict]) -> list[dict]:
	game_settlement_dicts = []

	for settlement_dict in settlement_dicts:
		game_settlement_dict = db.games.new_settlement(game_id, settlement_dict["id"])
		game_settlement_dicts.append(game_settlement_dict)

	return game_settlement_dicts

def game_tiles(game_id: int, tile_dicts: list[dict]) -> list[dict]:
	game_tile_dicts = []

	for tile_dict in tile_dicts:
		game_tile_dict = db.games.new_tile(game_id, tile_dict["id"], tile_dict["ResourceTypes.id"],
			tile_dict["value"]
		)
		game_tile_dicts.append(game_tile_dict)

	return game_tile_dicts

