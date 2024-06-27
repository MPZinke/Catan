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


from game.board import Board, Port, Ports, Road, Roads, Robber, Settlement, Settlements, Tile, Tiles
from game.board.construct.associate import associate_board_parts
from game.board.construct.BoardData import BoardData


def construct_board(board_data: BoardData) -> Board:
	port_objects: Ports = construct_ports(board_data.ports)
	road_objects: Roads = construct_roads(board_data.roads)
	robber_object: Robber = construct_robber(board_data.robber)
	settlement_objects: Settlements = construct_settlements(board_data.settlements)
	tile_objects: Tiles = construct_tiles(board_data.tiles)

	board = Board(port_objects, road_objects, robber_object, settlement_objects, tile_objects)

	associate_board_parts(board_data, board)

	return board


def construct_ports(port_dicts: list[dict]) -> Ports:
	ports_list: list[Port] = []
	for port_dict in port_dicts:
		resource_id = port_dict["ResourceTypes.id"]-1 if(port_dict["ResourceTypes.id"] is not None) else None
		ports_list.append(Port(port_dict["id"], resource_id))

	return ports_list


def construct_roads(road_dicts: list[dict]) -> Roads:
	roads: list[Road] = []
	for road_dict in road_dicts:
		roads.append(Road(road_dict["id"]))

	return roads


def construct_robber(robber_dict: dict) -> Robber:
	robber = Robber(robber_dict["Games.id"], robber_dict["is_friendly"])
	return robber


def construct_settlements(settlement_dicts: list[dict]) -> Settlements:
	settlements: list[Settlement] = []
	for settlement_dict in settlement_dicts:
		settlements.append(Settlement(settlement_dict["id"]))

	return settlements


def construct_tiles(tile_dicts: list[dict]) -> Tiles:
	tiles: list[Tile] = []
	for tile_dict in tile_dicts:
		tiles.append(
			Tile(tile_dict["id"], tile_dict["coordinate"], tile_dict["ResourceTypes.id"]-1, tile_dict["value"])
		)

	return tiles
