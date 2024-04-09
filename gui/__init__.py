#!/opt/homebrew/bin/python3
# -*- coding: utf-8 -*-
__author__ = "MPZinke"

########################################################################################################################
#                                                                                                                      #
#   created by: MPZinke                                                                                                #
#   on 2024.04.03                                                                                                      #
#                                                                                                                      #
#   DESCRIPTION:                                                                                                       #
#   BUGS:                                                                                                              #
#   FUTURE:                                                                                                            #
#                                                                                                                      #
########################################################################################################################


import math
from PIL import Image, ImageDraw


from board import Tile
from gui.Hexagon import Hexagon
from gui.HexagonGrid import HexagonGrid


COLORS = {
	Tile.Types.DESERT: (189, 160, 106),
	Tile.Types.WHEAT: (246, 215, 99),
	Tile.Types.WOOD: (74, 111, 62),
	Tile.Types.SHEEP: (154, 185, 86),
	Tile.Types.STONE: (163, 150, 140),
	Tile.Types.BRICK: (139, 83, 48)
}


def draw_tiles(tiles: list[Tile]):
	# FROM: https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.new
	#  AND: https://pillow.readthedocs.io/en/stable/handbook/concepts.html#concept-modes
	image = Image.new("RGB", [700, 700], color=(66, 149, 208))
	draw = ImageDraw.Draw(image)

	hexagon_grid = HexagonGrid(600, 600, 60)
	for tile in tiles:
		hexagon = hexagon_grid.hexagons[tile.coordinate[0]][tile.coordinate[1]]
		position = hexagon + [50, 50]

		# FROM: https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html#PIL.ImageDraw.ImageDraw.regular_polygon
		draw.regular_polygon((position[0], position[1], hexagon.radius), 6, fill=COLORS[tile.type],
			outline=(255, 255, 255)
		)
		# FROM: https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html#PIL.ImageDraw.ImageDraw.text
		draw.text((position[0], position[1]-10), str(tile.id), fill=(220))
		draw.text((position[0], position[1]+10), str(tile.value), fill=(220))

		for direction in Tile.Settlements.values():
			settlement = tile.settlements[direction]
			position = hexagon.settlement_position(direction)
			# FROM: https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html#PIL.ImageDraw.ImageDraw.ellipse
			draw.ellipse((position[0]+40, position[1]+40, position[0]+60, position[1]+60), fill=(200,200,200))
			draw.text((position[0]+45, position[1]+45), str(settlement.id), fill=220)

		for direction in Tile.Roads.values():
			road = tile.roads[direction]
			position = hexagon.road_position(direction)
			draw.text((position[0]+45, position[1]+45), str(road.id), fill=220)

	image.save("Board.jpg")
