#!/opt/homebrew/bin/python3
# -*- coding: utf-8 -*-
__author__ = "MPZinke"

########################################################################################################################
#                                                                                                                      #
#   created by: MPZinke                                                                                                #
#   on 2024.07.26                                                                                                      #
#                                                                                                                      #
#   DESCRIPTION:                                                                                                       #
#   BUGS:                                                                                                              #
#   FUTURE:                                                                                                            #
#                                                                                                                      #
########################################################################################################################


from database import queries


def directions() -> dict:
	corner_edges: dict = queries.directions.get_corner_edges()  # pylint: disable=no-value-for-parameter
	corner_sides: dict = queries.directions.get_corner_sides()  # pylint: disable=no-value-for-parameter
	edge_corners: dict = queries.directions.get_edge_corners()  # pylint: disable=no-value-for-parameter
	edge_sides: dict = queries.directions.get_edge_sides()  # pylint: disable=no-value-for-parameter
	side_corners: dict = queries.directions.get_side_corners()  # pylint: disable=no-value-for-parameter
	side_edges: dict = queries.directions.get_side_edges()  # pylint: disable=no-value-for-parameter
	return {
		"Corner's Edges": {direction["label"]: direction["id"]-1 for direction in corner_edges},
		"Corner's Sides": {direction["label"]: direction["id"]-1 for direction in corner_sides},
		"Edge's Corners": {direction["label"]: direction["id"]-1 for direction in edge_corners},
		"Edge's Sides": {direction["label"]: direction["id"]-1 for direction in edge_sides},
		"Side's Corners": {direction["label"]: direction["id"]-1 for direction in side_corners},
		"Side's Edges": {direction["label"]: direction["id"]-1 for direction in side_edges},
	}


def player_colors() -> list[dict]:
	return queries.player_colors.get_player_colors()  # pylint: disable=no-value-for-parameter


def resource_types() -> dict:
	return {type["label"]: type["id"]-1 for type in queries.types.get_resource_types()}  # pylint: disable=no-value-for-parameter
