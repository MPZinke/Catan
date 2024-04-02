

import math
from PIL import Image, ImageDraw


from HexagonGrid import HexagonGrid


hexagon_grid = HexagonGrid(500, 500, 25)
image = Image.new("1", [500, 500])
draw = ImageDraw.Draw(image)
for hexagon_row in hexagon_grid.hexagons:
	for hexagon in hexagon_row:
		# FROM: https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html#PIL.ImageDraw.ImageDraw.regular_polygon
		draw.regular_polygon((hexagon.position[0], hexagon.position[1], 2 * hexagon.size / math.sqrt(3)), 6, outline=(255,))
		draw.text((hexagon.position[0], hexagon.position[1]), f"[{hexagon.x}, {hexagon.y}]", fill=(255,))
image.save("Hello world.jpg")
