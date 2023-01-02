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


import Classes


class Hexagon:
	DEFAULT_RADIUS = 60

	COS_60_DEG = math.cos(60 * math.pi / 180.0)
	SIN_60_DEG = math.sin(60 * math.pi / 180.0)

	COLORS = {
		Classes.Hexagon.DESSERT: (220, 170, 120),  # DCAA78
		Classes.Hexagon.TREE: (109, 126, 75),  # 6D6A4B
		Classes.Hexagon.BRICK: (140, 50, 30),  # 8C321E
		Classes.Hexagon.WHEAT: (220, 190, 100),  # DCBE64
		Classes.Hexagon.SHEEP: (185, 190, 105),  # B9BE69
		Classes.Hexagon.STONE: (220, 220, 220)    # DDDDDD
	}

	def __init__(self, hexagon, canvas, position):
		# position = (position[0] + canvas.size[0] / 2, canvas.size[1] / 2 - position[1])
		position = (position[0], canvas.size[1]-position[1])
		x_60_degree_difference = self.COS_60_DEG * self.DEFAULT_RADIUS
		y_60_degree_difference = self.SIN_60_DEG * self.DEFAULT_RADIUS

		point0_XY = (-x_60_degree_difference + position[0], -y_60_degree_difference + position[1])
		point1_XY = (x_60_degree_difference + position[0], -y_60_degree_difference + position[1])
		point2_XY = (self.DEFAULT_RADIUS + position[0], position[1])
		point3_XY = (x_60_degree_difference + position[0], y_60_degree_difference + position[1])
		point4_XY = (-x_60_degree_difference + position[0], y_60_degree_difference + position[1])
		point5_XY = (-self.DEFAULT_RADIUS + position[0], position[1])

		color = self.COLORS[hexagon._type]

		canvas.polygon((point0_XY, point1_XY, point2_XY, point3_XY, point4_XY, point5_XY), fill=color)
