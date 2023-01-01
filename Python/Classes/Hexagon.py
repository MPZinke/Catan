

from enum import Enum
from typing import Dict, Optional


Type = str


class Corner:
	"""
	Corners relative to hexagon
	   4    3
	    \  / 
	 5 — ⬣ — 2
	    /  \
	   0    1
	"""
	BOTTOM_LEFT, BOTTOM_RIGHT, RIGHT, TOP_RIGHT, TOP_LEFT, LEFT = range(6)


class Edge:
	"""
	Edges relative to hexagon
	 Edges
	  4  3  2
	   \ | / 
	     ⬣
	   / | \
	  5  0  1
	"""
	BOTTOM, BOTTOM_RIGHT, TOP_RIGHT, TOP, TOP_LEFT, BOTTOM_LEFT = range(6)



class Hexagon:
	DESSERT, TREE, BRICK, WHEAT, SHEEP, STONE = ["DESSERT", "TREE", "BRICK", "WHEAT", "SHEEP", "STONE"]
	CORNERS = Corner
	EDGES = Edge


	def __init__(self, id: int, type: Type, value: int):
		self._id: int = id
		self._type: Type = type
		self._value: int = value  # the value rolled for this hexagon

		# Corners
		self._corners: list[Optional[Corner]] = [None for _ in range(6)]

		# Edges
		self._edges: list[Optional[Edge]] = [None for _ in range(6)]


def test():
	hexagon = Hexagon(1, Hexagon.DESSERT, 6)


if(__name__ == "__main__"):
	test()
