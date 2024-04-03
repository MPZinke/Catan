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
	Tile.Type.DESERT: (189, 160, 106),
	Tile.Type.WHEAT: (246, 215, 99),
	Tile.Type.WOOD: (74, 111, 62),
	Tile.Type.SHEEP: (154, 185, 86),
	Tile.Type.STONE: (163, 150, 140),
	Tile.Type.BRICK: (139, 83, 48)
}


def draw_tiles(tiles: list[Tile]):
	# FROM: https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.new
	#  AND: https://pillow.readthedocs.io/en/stable/handbook/concepts.html#concept-modes
	image = Image.new("RGB", [800, 800], color=(66, 149, 208))
	draw = ImageDraw.Draw(image)

	hexagon_grid = HexagonGrid(700, 700, 70)
	for tile in tiles:
		hexagon = hexagon_grid.hexagons[tile.coordinate[0]][tile.coordinate[1]]
		position = hexagon + [50, 50]

		# FROM: https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html#PIL.ImageDraw.ImageDraw.regular_polygon
		draw.regular_polygon((position[0], position[1], hexagon.radius), 6,
			fill=COLORS[tile.type], outline=(255, 255, 255)
		)
		# FROM: https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html#PIL.ImageDraw.ImageDraw.text
		draw.text((position[0], position[1]), str(tile.value), fill=(220))

		for corner in Tile.Corners.ENUM_VALUES.values():
			position = hexagon.corner_position(corner)
			# FROM: https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html#PIL.ImageDraw.ImageDraw.ellipse
			draw.ellipse((position[0]+40, position[1]+40, position[0]+60, position[1]+60), fill=(200,200,200))

	image.save("Board.jpg")
