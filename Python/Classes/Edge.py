

from typing import Optional, Union


Corner = type('Corner', (object,), {})
Hexagon = type('Hexagon', (object,), {})


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
	BOTTOM = 0
	TOP = 1
	SIDE = 2
	"""
	Edges relative to hexagon
	 Edges
	  4  3  2
	   \ | / 
	     ⬣
	   / | \
	  5  0  1

	"""
	def __init__(self, id: int, *, top: Optional[Hexagon]=None, bottom: Optional[Hexagon]=None):
		self._id: int = id

		self._hexagons: list[Optional[Hexagon]] = [None for _ in range(2)]
		self._corners: list[Optional[Corner]] = [None for _ in range(3)]


	def __xor__(self, right: Hexagon) -> Hexagon:
		return self._hexagons[self._top == right]


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

