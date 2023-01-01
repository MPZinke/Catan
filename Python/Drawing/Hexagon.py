#!/opt/homebrew/bin/python3
# -*- coding: utf-8 -*-
__author__ = "MPZinke"

########################################################################################################################
#                                                                                                                      #
#   created by: MPZinke                                                                                                #
#   on 2023.01.01                                                                                                      #
#                                                                                                                      #
#   DESCRIPTION:                                                                                                       #
#   BUGS:                                                                                                              #
#   FUTURE:                                                                                                            #
#                                                                                                                      #
########################################################################################################################


import math


class Hexagon:
	DEFAULT_RADIUS = 60
	DEG_TO_RADIANS = math.pi / 180.

	def __init__(self, hexagon, canvas, position):
		position = (position[0] + canvas.size[0] / 2, position[1] + canvas.size[1] / 2)
		x_pos_60_degrees = math.cos(60 * math.pi / 180.0) * self.DEFAULT_RADIUS
		y_pos_60_degrees = math.sin(60 * math.pi / 180.0) * self.DEFAULT_RADIUS

		point0_XY = (-x_pos_60_degrees + position[0], -y_pos_60_degrees + position[1])
		point1_XY = (x_pos_60_degrees + position[0], -y_pos_60_degrees + position[1])
		point2_XY = (self.DEFAULT_RADIUS + position[0], position[1])
		point3_XY = (x_pos_60_degrees + position[0], y_pos_60_degrees + position[1])
		point4_XY = (-x_pos_60_degrees + position[0], y_pos_60_degrees + position[1])
		point5_XY = (-self.DEFAULT_RADIUS + position[0], position[1])

		canvas.polygon((point0_XY, point1_XY, point2_XY, point3_XY, point4_XY, point5_XY))
