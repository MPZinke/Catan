

from typing import Union


Hexagon = object


class Edge:
	def __init__(self, *, top: Hexagon=None, bottom: Hexagon=None):
		self._top = top
		self._bottom = bottom
		
		
	def __xor__(self, right: Hexagon) -> Hexagon:
		return [self._top, self._bottom][self._top == right]
		
		
	def __rxor__(right: Hexagon, self) -> Hexagon:
		return self ^ right


def test():
	top = "ABC"
	bottom = "DEF"
	edge = Edge(top=top, bottom=bottom)
	print(edge ^ top)
	print(edge ^ bottom)
	print()
	print(top ^ edge)
	print(bottom ^ edge)
	
	
if(__name__ == "__main__"):
	test()

