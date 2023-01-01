

from typing import Optional
from enum import Enum


class Edge:
	"""
	Edges relative to corner
	 TOP
	   \__ SIDE
	   /
	 BOTTOM

	        TOP
	 SIDE __/
	        \
	        BOTTOM
	"""
	BOTTOM, TOP, SIDE = range(3)



class Hexagon:
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
	BOTTOM, TOP, SIDE = range(3)


class Corner:
	EDGES = Edge
	HEXAGONS = Hexagon

	def __init__(self, id: int):
		self._id: int = id
		self._settlement = None
		self._port = None

		self._edges: list[Optional[Edge]] = [None for _ in range(3)]
		self._hexagons: list[Optional[Hexagon]] = [None for _ in range(3)]


def test():
	pass


if(__name__ == "__main__"):
	test()
