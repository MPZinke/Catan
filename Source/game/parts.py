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



from board import Board, Port, Ports, Road, Roads, Robber, Settlement, Settlements, Tile, Tiles
from game import GameData


def ports(port_dicts: list[dict]) -> Ports:
	ports_list: list[Port] = []
	for port_dict in port_dicts:
		resource_id = port_dict["ResourceTypes.id"]-1 if(port_dict["ResourceTypes.id"] is not None) else None
		ports_list.append(Port(port_dict["id"], resource_id))

	return ports_list


def roads(road_dicts: list[dict]) -> Roads:
	roads: list[Road] = []
	for road_dict in road_dicts:
		roads.append(Road(road_dict["id"]))

	return roads


def robber(robber_dict: dict) -> Robber:
	robber = Robber(robber_dict["Games.id"], robber_dict["is_friendly"])
	return robber


def settlements(settlement_dicts: list[dict]) -> Settlements:
	settlements: list[Settlement] = []
	for settlement_dict in settlement_dicts:
		settlements.append(Settlement(settlement_dict["id"]))

	return settlements


def tiles(tile_dicts: list[dict]) -> Tiles:
	tiles: list[Tile] = []
	for tile_dict in tile_dicts:
		tiles.append(Tile(tile_dict["id"], tile_dict["coordinate"], tile_dict["ResourceTypes.id"]-1, tile_dict["value"]))

	return tiles


def instantiate_parts(game_data: GameData) -> Board:
	ports: Ports = ports(game_data.ports)
	roads: Roads = roads(game_data.roads)
	robber: Robber = robber(game_data.robber)
	settlements: Settlements = settlements(game_data.settlements)
	tiles: Tiles = tiles(game_data.tiles)

	return Board(ports, roads, robber, settlements, tiles)
