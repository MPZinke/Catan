

import math
from PIL import Image, ImageDraw


from HexagonGrid import HexagonGrid


hexagon_grid = HexagonGrid(501, 501, 50)
# FROM: https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.new
#  AND: https://pillow.readthedocs.io/en/stable/handbook/concepts.html#concept-modes
image = Image.new("RGB", [501, 501])
draw = ImageDraw.Draw(image)
for hexagon_row in hexagon_grid.hexagons:
	for hexagon in hexagon_row:
		# FROM: https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html#PIL.ImageDraw.ImageDraw.regular_polygon
		draw.regular_polygon((hexagon.position[0], hexagon.position[1], 2 * hexagon.size / math.sqrt(3)), 6, outline=(255, 255, 255))
		# FROM: https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html#PIL.ImageDraw.ImageDraw.text
		draw.text((hexagon.position[0], hexagon.position[1]), f"[{hexagon.x}, {hexagon.y}]", fill=(255, 255, 255))
image.save("Hello world.jpg")
