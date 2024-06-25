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
from game.board.new.random import ResourceAndValueMapping


def new_board(game_id: int, template_data: TemplateData, random_resource_and_value_mapping: ResourceAndValueMapping
) -> BoardData:
	port_dicts: DictList = new_ports(game_id, template_data.ports,
		random_resource_and_value_mapping.port_resources_dict
	)
	road_dicts: DictList = new_roads(game_id, template_data.roads)
	settlement_dicts: DictList = new_settlements(game_id, template_data.settlements)
	tile_dicts: DictList = new_tiles(game_id, template_data.tiles,
		random_resource_and_value_mapping.tile_dice_values_dict,
		random_resource_and_value_mapping.tile_resources_dict
	)

	ports_settlements_dicts: DictList = new_ports_settlements(template_data, game_id, port_dicts, settlement_dicts)
	roads_settlements_dicts: DictList = new_roads_settlements(template_data, game_id, road_dicts, settlement_dicts)
	roads_tiles_dicts: DictList = new_roads_tiles(template_data, game_id, road_dicts, tile_dicts)
	settlements_tiles_dicts: DictList = new_settlements_tiles(template_data, game_id, settlement_dicts, tile_dicts)

	robber_dict: dict = new_robber(game_id)

	return BoardData(
		id=game_id,
		board_id=template_data.id,
		ports=port_dicts,
		ports_settlements=ports_settlements_dicts,
		roads=road_dicts,
		roads_settlements=roads_settlements_dicts,
		roads_tiles=roads_tiles_dicts,
		robber=robber_dict,
		settlements=settlement_dicts,
		settlements_tiles=settlements_tiles_dicts,
		tiles=tile_dicts,
	)


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


def filter_parts(part_name: str, part_dicts: DictList, mapping: DictList) -> int:
	part_filter: callable = lambda part_dict: part_dict[f"Templates{part_name}.id"] == mapping[f"Templates{part_name}.id"]
	return next(filter(part_filter, part_dicts))["id"]


def new_ports_settlements(template_data: TemplateData, game_id: int, port_dicts: DictList, settlement_dicts: DictList) -> DictList:
	ports_settlements_dicts: DictList = []
	for ports_settlements_mapping in template_data.ports_settlements:
		port_id: dict = filter_parts("Ports", port_dicts, 	ports_settlements_mapping)
		settlement_id: dict = filter_parts("Settlements", settlement_dicts, ports_settlements_mapping)

		ports_settlements_dicts.append(queries.games.new_ports_settlements(game_id, port_id, settlement_id, ports_settlements_mapping["Corner's Sides.id"], ports_settlements_mapping["Side's Corners.id"]))

	return ports_settlements_dicts


def new_roads_settlements(template_data: TemplateData, game_id: int, road_dicts: DictList, settlement_dicts: DictList) -> DictList:
	roads_settlements_dicts: DictList = []
	for roads_settlements_mapping in template_data.roads_settlements:
		road_id: dict = filter_parts("Roads", road_dicts, roads_settlements_mapping)
		settlement_id: dict = filter_parts("Settlements", settlement_dicts, roads_settlements_mapping)

		roads_settlements_dicts.append(queries.games.new_roads_settlements(game_id, road_id, settlement_id, roads_settlements_mapping["Corner's Edges.id"], roads_settlements_mapping["Edge's Corners.id"]))

	return roads_settlements_dicts


def new_roads_tiles(template_data: TemplateData, game_id: int, road_dicts: DictList, tile_dicts: DictList) -> DictList:
	roads_tiles_dicts: DictList = []
	for roads_tiles_mapping in template_data.roads_tiles:
		road_id: dict = filter_parts("Roads", road_dicts, roads_tiles_mapping)
		tile_id: dict = filter_parts("Tiles", tile_dicts, roads_tiles_mapping)

		roads_tiles_dicts.append(queries.games.new_roads_tiles(game_id, road_id, tile_id, roads_tiles_mapping["Edge's Sides.id"], roads_tiles_mapping["Side's Edges.id"]))

	return roads_tiles_dicts


def new_settlements_tiles(template_data: TemplateData, game_id: int, settlement_dicts: DictList, tile_dicts: DictList) -> DictList:
	settlements_tiles_dicts: DictList = []
	for settlements_tiles_mapping in template_data.settlements_tiles:
		settlement_id: dict = filter_parts("Settlements", settlement_dicts, settlements_tiles_mapping)
		tile_id: dict = filter_parts("Tiles", tile_dicts, settlements_tiles_mapping)

		settlements_tiles_dicts.append(queries.games.new_settlements_tiles(game_id, settlement_id, tile_id, settlements_tiles_mapping["Corner's Sides.id"], settlements_tiles_mapping["Side's Corners.id"]))

	return settlements_tiles_dicts
