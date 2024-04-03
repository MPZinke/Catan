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
from gui.HexagonGrid import HexagonGrid


COLORS = {
	Tile.Type.ENUM_KEYS[Tile.Type.DESERT]: (189, 160, 106),
	Tile.Type.ENUM_KEYS[Tile.Type.WHEAT]: (246, 215, 99),
	Tile.Type.ENUM_KEYS[Tile.Type.WOOD]: (74, 111, 62),
	Tile.Type.ENUM_KEYS[Tile.Type.SHEEP]: (154, 185, 86),
	Tile.Type.ENUM_KEYS[Tile.Type.STONE]: (163, 150, 140),
	Tile.Type.ENUM_KEYS[Tile.Type.BRICK]: (139, 83, 48)
}


def draw_tiles(game_data: dict, tiles: list[Tile]):
	# FROM: https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.new
	#  AND: https://pillow.readthedocs.io/en/stable/handbook/concepts.html#concept-modes
	image = Image.new("RGB", [701, 701], color=(66, 149, 208))
	draw = ImageDraw.Draw(image)

	hexagon_grid = HexagonGrid(701, 701, 70)
	for tile in tiles:
		tile_data = next(filter(lambda tile_dict: tile_dict["id"] == tile.id, game_data["Tiles"]))
		coordinate = tile_data["coordinate"]
		value = str(tile_data["value"])
		type = tile_data["type"]
		hexagon = hexagon_grid.hexagons[coordinate[0]][coordinate[1]]

		# FROM: https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html#PIL.ImageDraw.ImageDraw.regular_polygon
		draw.regular_polygon((hexagon.position[0], hexagon.position[1], 2 * hexagon.size / math.sqrt(3)), 6,
			fill=COLORS[type], outline=(255, 255, 255)
		)
		# FROM: https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html#PIL.ImageDraw.ImageDraw.text
		draw.text((hexagon.position[0], hexagon.position[1]), value, fill=(220))

	image.save("Hello world.jpg")
