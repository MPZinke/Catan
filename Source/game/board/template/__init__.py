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


from database import queries


from game.board.template.TemplateData import TemplateData


DictList = list[dict]


def template_data(template_id: int) -> TemplateData:
	name: str = queries.templates.get_template(template_id)["name"]  # pylint: disable=no-value-for-parameter
	ports: DictList = queries.templates.get_ports(template_id)  # pylint: disable=no-value-for-parameter
	roads: DictList = queries.templates.get_roads(template_id)  # pylint: disable=no-value-for-parameter
	settlements: DictList = queries.templates.get_settlements(template_id)  # pylint: disable=no-value-for-parameter
	tiles: DictList = queries.templates.get_tiles(template_id)  # pylint: disable=no-value-for-parameter

	return TemplateData(
		id=template_id,
		name=name,
		ports=ports,
		roads=roads,
		settlements=settlements,
		tiles=tiles
	)
