

from Edge import Edge

# TYPES
DESSERT, TREE, BRICK, WHEAT, SHEEP, STONE = ["DESSERT", "TREE", "BRICK", "WHEAT", "SHEEP", "STONE"]

Type = str

# CORNERS

# EDGES


class Hexagon:
	def __init__(self, id: int, type: Type,  **kwargs):
		self._id: int = id
		self._type: Type = type

		self._bottom: Edge = kwargs.get("bottom")
		self._bottom_left: Edge = kwargs.get("bottom_left")
		self._bottom_right: Edge = kwargs.get("bottom_right")
		self._top: Edge = kwargs.get("top")
		self._top_left: Edge = kwargs.get("top_left")
		self._top_right: Edge = kwargs.get("top_right")
	
	
def test():
	hexagon = Hexagon(1, DESSERT)
		
		
if(__name__ == "__main__"):
	test()

