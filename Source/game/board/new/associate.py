#!/opt/homebrew/bin/python3
# -*- coding: utf-8 -*-
__author__ = "MPZinke"

########################################################################################################################
#                                                                                                                      #
#   created by: MPZinke                                                                                                #
#   on 2024.06.25                                                                                                      #
#                                                                                                                      #
#   DESCRIPTION:                                                                                                       #
#   BUGS:                                                                                                              #
#   FUTURE:                                                                                                            #
#                                                                                                                      #
########################################################################################################################


from game.board.construct import BoardData
from game.board.template import TemplateData


class TemplateGameMapping:
	def __init__(self, board_data: BoardData, template_data: TemplateData):
		self.ports = {t_port["id"]: g_port["id"] for g_port, t_port in zip(board_data.ports, template_data.ports)}
		self.roads = {t_road["id"]: g_road["id"] for g_road, t_road in zip(board_data.roads, template_data.roads)}
		self.settlements = {t_settlement["id"]: g_settlement["id"] for g_settlement, t_settlement in zip(board_data.settlements, template_data.settlements)}
		self.tiles = {t_tile["id"]: g_tile["id"] for g_tile, t_tile in zip(board_data.tiles, template_data.tiles)}


def associate_board_data(board_data: BoardData, template_data: TemplateData) -> None:
	template_game_mappings = TemplateGameMapping(board_data, template_data)
	associate_ports(board_data, template_data, template_game_mappings)
	associate_roads(board_data, template_data, template_game_mappings)
	associate_settlements(board_data, template_data, template_game_mappings)
	associate_tiles(board_data, template_data, template_game_mappings)


def associate_ports(board_data: BoardData, template_data: TemplateData, template_game_mappings: dict) -> None:
	for template_port_dict, game_port_dict in zip(template_data.ports, board_data.ports):
		for x, template_settlement_id in enumerate(template_port_dict["TemplatesSettlements.ids"]):
			if(template_settlement_id is not None):
				game_port_dict["GamesSettlements.ids"][x] = template_game_mappings.settlements[template_settlement_id]


def associate_roads(board_data: BoardData, template_data: TemplateData, template_game_mappings: dict) -> None:
	for template_road_dict, game_road_dict in zip(template_data.roads, board_data.roads):
		for x, template_settlement_id in enumerate(template_road_dict["TemplatesSettlements.ids"]):
			if(template_settlement_id is not None):
				game_road_dict["GamesSettlements.ids"][x] = template_game_mappings.settlements[template_settlement_id]

		for x, template_tile_id in enumerate(template_road_dict["TemplatesTiles.ids"]):
			if(template_tile_id is not None):
				game_road_dict["GamesTiles.ids"][x] = template_game_mappings.tiles[template_tile_id]


def associate_settlements(board_data: BoardData, template_data: TemplateData, template_game_mappings: dict) -> None:
	for template_settlement_dict, game_settlement_dict in zip(template_data.settlements, board_data.settlements):
		for x, template_port_id in enumerate(template_settlement_dict["TemplatesPorts.ids"]):
			if(template_port_id is not None):
				game_settlement_dict["GamesPorts.ids"][x] = template_game_mappings.ports[template_port_id]

		for x, template_road_id in enumerate(template_settlement_dict["TemplatesRoads.ids"]):
			if(template_road_id is not None):
				game_settlement_dict["GamesRoads.ids"][x] = template_game_mappings.roads[template_road_id]

		for x, template_tile_id in enumerate(template_settlement_dict["TemplatesTiles.ids"]):
			if(template_tile_id is not None):
				game_settlement_dict["GamesTiles.ids"][x] = template_game_mappings.tiles[template_tile_id]


def associate_tiles(board_data: BoardData, template_data: TemplateData, template_game_mappings: dict) -> None:
	for template_tile_dict, game_tile_dict in zip(template_data.tiles, board_data.tiles):
		for x, template_road_id in enumerate(template_tile_dict["TemplatesRoads.ids"]):
			if(template_road_id is not None):
				game_tile_dict["GamesRoads.ids"][x] = template_game_mappings.roads[template_road_id]

		for x, template_settlement_id in enumerate(template_tile_dict["TemplatesSettlements.ids"]):
			if(template_settlement_id is not None):
				game_tile_dict["GamesSettlements.ids"][x] = template_game_mappings.settlements[template_settlement_id]
