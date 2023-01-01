

from enum import Enum
from typing import Optional, Union


class Corner:
	"""
	Corners relative to edges
	 Edges
	  4  3  2
	   \ | / 
	     ⬣
	   / | \
	  5  0  1

	 0, 3.
	  LEFT————RIGHT

	 1, 4.
	      RIGHT
	      /
	     /
	  LEFT

	 2, 5.
	  LEFT
	   \
	    \
	    RIGHT
	"""
	LEFT, RIGHT = range(2)


class Hexagon:
	"""
	Hexagon relative to edge
	 Edges
	  4  3  2
	   \ | / 
	     ⬣
	   / | \
	  5  0  1

	 0, 3.
	   TOP
	  ——————
	  BOTTOM

	 1, 4.
	  TOP /
	     / BOTTOM

	 2, 5.
	        \ TOP
	  BOTTOM \
	"""
	BOTTOM, TOP = range(2)


class Edge:
	CORNERS = Corner
	HEXAGONS = Hexagon

	def __init__(self, id: int, *, top: Optional[Hexagon]=None, bottom: Optional[Hexagon]=None):
		self._id: int = id

		self._hexagons: list[Optional[Hexagon]] = [None for _ in range(2)]
		self._corners: list[Optional[Corner]] = [None for _ in range(2)]


	def __xor__(self, right: Hexagon) -> Hexagon:
		return self._hexagons[self._hexagons[0] == right]


	def __rxor__(right: Hexagon, self) -> Hexagon:
		return self ^ right


def test():
	top = "ABC"
	bottom = "DEF"
	edge = Edge(1, top=top, bottom=bottom)
	print(edge ^ top)
	print(edge ^ bottom)
	print()
	print(top ^ edge)
	print(bottom ^ edge)


if(__name__ == "__main__"):
	test()

