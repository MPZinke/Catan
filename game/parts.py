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



from board import Port, Road, Settlement, Tile


def ports(port_dicts: list[dict]) -> list[Port]:
	ports_list: list[Port] = []
	for port_dict in port_dicts:
		resource_id = port_dict["ResourceTypes.id"]-1 if(port_dict["ResourceTypes.id"] is not None) else None
		ports_list.append(Port(port_dict["id"], resource_id))

	return ports_list


def roads(road_dicts: list[dict]) -> list[Road]:
	roads: list[Road] = []
	for road_dict in road_dicts:
		roads.append(Road(road_dict["id"]))

	return roads


def settlements(settlement_dicts: list[dict]) -> list[Settlement]:
	settlements: list[Settlement] = []
	for settlement_dict in settlement_dicts:
		settlements.append(Settlement(settlement_dict["id"]))

	return settlements


def tiles(tile_dicts: list[dict]) -> list[Tile]:
	tiles: list[Tile] = []
	for tile_dict in tile_dicts:
		tiles.append(Tile(tile_dict["id"], tile_dict["coordinate"], tile_dict["ResourceTypes.id"]-1, tile_dict["value"]))

	return tiles
