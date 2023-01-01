

from typing import Dict, Optional


from Classes import Corner
from Classes import Edge

# TYPES
DESSERT, TREE, BRICK, WHEAT, SHEEP, STONE = ["DESSERT", "TREE", "BRICK", "WHEAT", "SHEEP", "STONE"]

Type = str


class Hexagon:
	"""
	Hexagons relative to edges
	 Edges
	  4  3  2
	   \ | / 
	     ⬣
	   / | \
	  5  0  1

	 Hexagons for edges 0, 3.
	   TOP
	  ——————
	  BOTTOM

	 Hexagons for edges 1, 4.
	  TOP /
	     / BOTTOM

	 Hexagons for edges 2, 5.
	        \ TOP
	  BOTTOM \
	"""
	BOTTOM = 0  # Corner
	TOP = 1  # Corner

	"""
	Hexagons relative to corners
	          ______
	         /      \
	  ______/        \
	 /      \  TOP   /
	/  SIDE  \______/
	\        /      \
	 \______/ BOTTOM \
	        \        /
	         \______/
	  ______
	 /      \
	/        \______
	\   TOP  /      \
	 \______/  SIDE  \
	 /      \        /
	/ BOTTOM \______/
	\        /
	 \______/
	"""
	SIDE = 2  # Edge

	def __init__(self, id: int, type: Type, value: int):
		self._id: int = id
		self._type: Type = type
		self._value: int = value  # the value rolled for this hexagon

		# Corners
		self._corners: list[Optional[Corner]] = [None for _ in range(6)]

		# Edges
		self._edges: list[Optional[Edge]] = [None for _ in range(6)]


def test():
	hexagon = Hexagon(1, DESSERT, 6)


if(__name__ == "__main__"):
	test()
