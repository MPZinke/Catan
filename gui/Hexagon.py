

import math
from typing import Tuple


from board import Tile


Coordinate = Tuple[float, float]


class Hexagon:
	SQUAREROOT_3 = math.sqrt(3)
	RADIAN = math.pi / 180.0
	COS_60 = math.cos(RADIAN * 60)
	SIN_60 = math.sin(RADIAN * 60)

	def __init__(self, position: Coordinate, size: int):
		self.position: Coordinate = position
		self.size: int = size  # Distance from centerpoint to a side.
		self.radius: float = 2 * size / math.sqrt(3)  # Distance from centerpoint to a settlement.


	def __repr__(self) -> str:
		return str(self)


	def __str__(self) -> str:
		return f"""<Hexagon position=[{self.position[0]}, {self.position[1]}] size={self.size}>"""


	def __add__(self, right: Tuple[int, int]) -> Tuple[int, int]:
		return tuple(left_value+right_value for left_value, right_value in zip(self.position, right))


	def __iter__(self) -> Tuple[int, int, float]:
		self._iter_values = [self.position[0], self.position[1], self.radius]
		return self


	def __next__(self) -> int|float:
		yield from self._iter_values


	def settlement_position(self, settlement: int) -> Tuple[int, int]:
		match(settlement):
			case(Tile.Settlements.TOP_LEFT):
				return self + [-self.COS_60*self.radius, self.SIN_60*self.radius]
			case(Tile.Settlements.TOP_RIGHT):
				return self + [self.COS_60*self.radius, self.SIN_60*self.radius]
			case(Tile.Settlements.RIGHT):
				return self + [self.radius, 0]
			case(Tile.Settlements.BOTTOM_RIGHT):
				return self + [self.COS_60*self.radius, -self.SIN_60*self.radius]
			case(Tile.Settlements.BOTTOM_LEFT):
				return self + [-self.COS_60*self.radius, -self.SIN_60*self.radius]
			case(Tile.Settlements.LEFT):
				return self + [-self.radius, 0]
			case _:
				raise ValueError(f"Unknown settlement '{settlement}'")
