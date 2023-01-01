

from typing import Optional


Edge = type('Edge', (object,), {})
Hexagon = type('Hexagon', (object,), {})


class Corner:

	# EvenCorner: BottomLeftCorner, RightCorner, TopLeftCorner
	# OddCorner: BottomRightCorner, LeftCorner, TopRightCorner

	"""
	Corners relative to hexagon
	   4    3
	    \  / 
	 5 — ⬣ — 2
	    /  \
	   0    1
	"""
	BOTTOM_LEFT: int = 0  # BottomLeft corner when referenced by Hexagon
	BOTTOM_RIGHT: int = 1  # BottomRight corner when referenced by Hexagon
	RIGHT: int = 2  # Right corner when referenced by Hexagon
	TOP_RIGHT: int = 3  # TopRight corner when referenced by Hexagon
	TOP_LEFT: int = 4  # TopLeft corner when referenced by Hexagon
	LEFT: int = 5  # Left corner when referenced by Hexagon

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
	LEFT = 0
	RIGHT = 1

	def __init__(self, id: int):
		self._id: int = id
		self._settlement = None
		self._port = None

		self._top_edge: Optional[Edge] = None

		self._bottom_hexagon: Optional[Hexagon] = None
		self._side_hexagon: Optional[Hexagon] = None
		self._top_hexagon: Optional[Hexagon] = None



def test():
	pass


if(__name__ == "__main__"):
	test()
