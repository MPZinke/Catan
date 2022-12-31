

class Corner:
	def __init__(self, id: int):
		self._id: int = id
		self._settlement = None
		self._port = None
		
		
class EvenCorner(Corner):  # BottomLeftCorner, RightCorner, TopLeftCorner
	def __init__(self, id: int):
		Corner.__init__(self, id)
		self._left_hexagon = None
		self._top_right_hexagon = None
		self._bottom_right_hexagon = None
	
		self._right_edge = None
		self._bottom_left_edge = None
		self._top_left_edge = None
		

BottomLeftCorner = RightCorner = TopLeftCorner = EvenCorner


class OddCorner(Corner):  # BottomRightCorner, LeftCorner, TopRightCorner
	def __init__(self, id: int):
		Corner.__init__(self, id)
		self._right_hexagon = None
		self._top_left_hexagon = None
		self._bottom_left_hexagon = None
	
		self._left_edge = None
		self._bottom_right_edge = None
		self._top_right_edge = None
		
		
BottomRightCorner = LeftCorner = TopRightCorner = OddCorner


def test():
	left_corner = LeftCorner(1)
	print(type(left_corner))
	
	
if(__name__ == "__main__"):
	test()

