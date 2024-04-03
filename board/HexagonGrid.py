

import math
from typing import Optional, Tuple


Coordinate = Tuple[float, float]


class Hexagon:
	def __init__(self, index: Tuple[int, int], position: Coordinate, size: int):
		x, y = index
		self.x: int = x
		self.y: int = y
		self.position: Coordinate = position
		self.size: int = size


	def __repr__(self) -> str:
		return str(self)


	def __str__(self) -> str:
		return f"""<Hexagon x={self.x} y={self.y} position=[{self.position[0]}, {self.position[1]}] size={self.size}>"""



class HexagonGrid:
	SQUAREROOT_3 = math.sqrt(3)

	def __init__(self, width: int, height: int, hexagon_size: int):
		self.width: int = width
		self.height: int = height
		self.hexagon_size: int = hexagon_size

		self.hexagons: Optional[list[list[Hexagon]]] = None

		self._current_index: Optional[Tuple[int, int]] = None  # The "Hexagon Grid"'s last index.
		self._current_position: Optional[Coordinate] = None  # The cartesean coordinates of the center of the last placed hexagon.

		for _ in self:
			pass



	def __iter__(self) -> object:
		position_x: float = 2 * self.hexagon_size / self.SQUAREROOT_3
		position_y: float = self.hexagon_size

		self._current_index = [0, 0]
		self._current_position = [position_x, position_y]
		self.hexagons = [[Hexagon(list(self._current_index), list(self._current_position), self.hexagon_size)]]

		return self


	def __next__(self) -> Optional[Coordinate]:
		current_position_x, current_position_y = self._current_position

		y_offset: float = self.hexagon_size * 2
		next_position_y: float = current_position_y + y_offset
		next_boundary_y: float = next_position_y + self.hexagon_size

		if(next_boundary_y <= self.height):
			next_position_x: float = current_position_x
			self._current_index = [self._current_index[0], self._current_index[1] + 1]
			self._current_position = [next_position_x, next_position_y]

		else:
			x_offset: float = self.SQUAREROOT_3 * self.hexagon_size
			next_position_x: float = current_position_x + x_offset
			next_boundary_x: float = next_position_x + (x_offset / 2)
			if(next_boundary_x > self.width):
				raise StopIteration

			next_position_y: float = self.hexagon_size if(self._current_index[0] & 0b1) else self.hexagon_size * 2
			self._current_index = [self._current_index[0] + 1, 0]
			self._current_position = [next_position_x, next_position_y]

		self.hexagons[-1].append(Hexagon(list(self._current_index), list(self._current_position), self.hexagon_size))

		print(self.hexagons)
